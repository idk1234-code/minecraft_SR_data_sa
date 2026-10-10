from pathlib import Path
import json,hashlib,re,csv
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
for name,h in manifest.items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,name
a={json.loads(s)['seed_u64'] for s in (ROOT/'data/validation_a_seeds.jsonl').read_text().splitlines()};b={json.loads(s)['seed_u64'] for s in (ROOT/'data/validation_b_seeds.jsonl').read_text().splitlines()};t={json.loads(s)['seed_u64'] for s in (ROOT/'data/training_seeds.jsonl').read_text().splitlines()};assert len(a)==len(b)==5000 and len(t)==8000 and not a&b and not t&(a|b)
for p in ROOT.rglob('*.md'):
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if '://' not in link and not link.startswith('#'):assert (p.parent/link.split('#')[0]).exists(),(p,link)
req=json.loads((ROOT/'data/advancement_1.16.1_requirements.json').read_text(encoding='utf-8'));assert req['criteria_count']==42 and sum(len(v) for v in req['required_biomes'].values())==42
v=json.loads((ROOT/'data/validation_b_longhaul_results.json').read_text(encoding='utf-8'))
assert [r['methods'][3]['successes'] for r in v['table']]==[1916,1199,2108,1339]
m=next(r for r in v['comparisons'] if r['cohort']=='all5000' and r['target']=='蘑菇岛' and r['reference']=='当前搜索器');assert m['new_successes']-m['reference_successes']==27 and m['difference_ci95'][0]<0<m['difference_ci95'][1]
assert all(json.loads((ROOT/f'data/longhaul_{name}.json').read_text(encoding='utf-8'))['passed'] for name in ['training_audit','route_audit','independent_distance_audit','delivery_check'])
print(f'PASS: {len(manifest)} hashed files, document links, two disjoint validation cohorts,42 biome requirements and frozen numerical claims.')
