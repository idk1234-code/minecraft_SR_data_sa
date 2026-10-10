from pathlib import Path
import json
import numpy as np
from scipy.stats import binomtest
ROOT=Path(__file__).resolve().parents[1]
with np.load(ROOT/'data/validation_b_arrays.npz') as d:first=d['first']
targets=['巨型针叶林','蘑菇岛','丛林','恶地'];result=[]
for k,target in enumerate(targets):
    a=np.isfinite(first[:,2+k,k])
    for j,label in [(0,'随机直飞'),(1,'覆盖优先')]:
        b=np.isfinite(first[:,j,k]);diff=a.astype(np.int8)-b.astype(np.int8);rng=np.random.default_rng(202610113100+k*2+j);boot=[]
        for _ in range(100):boot.extend(diff[rng.integers(0,5000,size=(100,5000),dtype=np.int32)].mean(axis=1))
        aa=int((diff==1).sum());bb=int((diff==-1).sum())
        result.append(dict(target=target,reference=label,seeds=5000,fixed_expert_rate=float(a.mean()),reference_rate=float(b.mean()),difference=float(diff.mean()),difference_ci95=np.quantile(boot,[.025,.975]).tolist(),expert_only=aa,reference_only=bb,paired_exact_p=float(binomtest(aa,aa+bb,.5).pvalue) if aa+bb else 1.))
order=np.argsort([r['paired_exact_p'] for r in result]);last=0.
for rank,i in enumerate(order):last=max(last,min(1.,(8-rank)*result[i]['paired_exact_p']));result[i]['holm_p_across8']=last
expected=json.loads((ROOT/'data/validation_b_fixed_expert_review.json').read_text(encoding='utf-8'))['comparisons'];assert result==expected
print('Eight fixed-expert comparisons reproduce exactly.')
