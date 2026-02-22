"""Run deterministic LCIA for the prepared Brightway2 foreground.

Assumes you have run `brightway_prepare.py` and completed `brightway_premap_results.csv`
by selecting background process identifiers.

The script creates simple foreground processes from `inventory_template.csv`, links
the selected background processes, and computes LCIA using an available method.
"""
import os
import pandas as pd
from brightway2 import projects, Database, methods, Method

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
INVENTORY = os.path.join(ROOT, 'inventory_template.csv')
MAP = os.path.join(ROOT, 'brightway_premap_results.csv')

projects.set_current('LCA_Sachet_Lagos')

def load_mapping():
    if not os.path.exists(MAP):
        raise FileNotFoundError('Run brightway_prepare.py and populate brightway_premap_results.csv')
    return pd.read_csv(MAP)

def build_foreground():
    df = pd.read_csv(INVENTORY)
    mapping = load_mapping()

    fg = Database('foreground_lagos')
    data = {}

    # Example: create two product processes: Sachet_FU and PET_FU
    sachet_process = {
        'name': 'Sachet_fu',
        'unit': 'unit',
        'exchanges': []
    }
    pet_process = {
        'name': 'PET_fu',
        'unit': 'unit',
        'exchanges': []
    }

    # Map inventory rows into exchanges (very simplified)
    for _, row in df.iterrows():
        flow = row['flow'] if 'flow' in row else row.get('flow_name')
        amount = row.get('amount_per_FU') if 'amount_per_FU' in row else row.get('amount')
        stage = row.get('stage', '')
        if pd.isna(amount):
            continue
        # Assign to sachet or pet by matching process_name in inventory_template comment
        comment = row.get('comment', '').lower() if 'comment' in row else ''
        if 'sachet' in comment or 'sachet' in str(flow).lower():
            sachet_process['exchanges'].append({'name': flow, 'amount': float(amount), 'unit': row.get('flow_unit', '')})
        elif 'pet' in comment or 'pet' in str(flow).lower():
            pet_process['exchanges'].append({'name': flow, 'amount': float(amount), 'unit': row.get('flow_unit', '')})
        else:
            # Generic add to both
            sachet_process['exchanges'].append({'name': flow, 'amount': float(amount)/2, 'unit': row.get('flow_unit', '')})
            pet_process['exchanges'].append({'name': flow, 'amount': float(amount)/2, 'unit': row.get('flow_unit', '')})

    # Write or update in database
    fg.write({('foreground_lagos', 'Sachet_fu'): sachet_process})
    fg.write({('foreground_lagos', 'PET_fu'): pet_process})
    print('Foreground processes written to database foreground_lagos')

def pick_method():
    available = [m for m in methods]
    if not available:
        raise RuntimeError('No LCIA methods available in Brightway2 installation. Import ReCiPe or ELCD methods.')
    # Prefer ReCiPe if present
    for name in available:
        if 'ReCiPe' in name or 'rec' in name.lower():
            return Method(name)
    return Method(available[0])

def run():
    build_foreground()
    method = pick_method()
    print('Using LCIA method:', method.name)
    # Compute LCA for the two processes
    fg = Database('foreground_lagos')
    for key in fg:
        if key[1] in ('Sachet_fu', 'PET_fu'):
            from brightway2 import LCA
            lca = LCA({('foreground_lagos', key[1]): 1}, method=method)
            lca.lci()
            lca.lcia()
            print(f'Process {key[1]} -> {lca.score:.6g} {method.name}')

if __name__ == '__main__':
    run()
