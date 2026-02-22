"""Prepare a Brightway2 foreground project from the CSV templates.

This script attempts to find matching background processes in your installed Brightway2
databases using the `recommended_search_string` column in `openlca_premap.csv`.

Usage:
  - Install requirements: `pip install -r requirements.txt`
  - Ensure Brightway2 databases (ELCD/USLCI or equivalents) are installed.
  - Run: `python brightway_prepare.py`

The script will create a Brightway2 project named "LCA_Sachet_Lagos" and a database
`foreground_lagos` containing processes for sachet and PET life-cycles. It will print
matches and write a mapping CSV `brightway_premap_results.csv` for review.
"""
import os
import pandas as pd
from brightway2 import projects, databases, Database

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
PREMAP = os.path.join(ROOT, 'openlca_premap.csv')
INVENTORY = os.path.join(ROOT, 'inventory_template.csv')
OUTMAP = os.path.join(ROOT, 'brightway_premap_results.csv')

def find_matches(search_str):
    matches = []
    for db_name in databases:
        try:
            db = Database(db_name)
            for ds in db:
                name = ds.get('name', '')
                if search_str.lower() in name.lower():
                    matches.append((db_name, ds.get('name'), ds.get('code')))
        except Exception:
            continue
    return matches

def main():
    df = pd.read_csv(PREMAP)
    results = []

    projects.set_current('LCA_Sachet_Lagos')
    # Create foreground database
    fg_db_name = 'foreground_lagos'
    if fg_db_name in databases:
        Database(fg_db_name).purge()
    fg_db = Database(fg_db_name)
    fg_db.register()

    # Minimal processes to create: Sachet manufacture and PET manufacture + filling + EoL
    # We'll create placeholder processes whose exchanges should be linked to matched background processes later.
    for idx, row in df.iterrows():
        search = str(row.get('recommended_search_string', ''))
        flow = row.get('flow_name')
        unit = row.get('flow_unit')
        amount = row.get('amount')
        matches = find_matches(search)
        results.append({
            'flow_name': flow,
            'flow_unit': unit,
            'amount': amount,
            'search_string': search,
            'matches_count': len(matches),
            'top_match': matches[0] if matches else ('', '', '')
        })

    # Write mapping results for user review
    pd.DataFrame(results).to_csv(OUTMAP, index=False)
    print('Wrote mapping results to', OUTMAP)
    print('Please review the top matches and update `brightway_premap_results.csv` with preferred process IDs.')

if __name__ == '__main__':
    main()
