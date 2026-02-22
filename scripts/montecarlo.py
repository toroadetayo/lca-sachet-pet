"""Simple Monte Carlo wrapper sampling key foreground parameters and re-running LCIA.

This script performs a basic uncertainty analysis by sampling packaging mass and
waste fate shares within the bounds provided in `inventory_template.csv`. It is
intended as a reproducible starting point — adapt parameter distributions as needed.
"""
import os
import pandas as pd
import numpy as np
from subprocess import run

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
INV = os.path.join(ROOT, 'inventory_template.csv')
OUT = os.path.join(ROOT, 'montecarlo_results.csv')

def sample_params(df, n=200):
    samples = []
    for i in range(n):
        row = {}
        for _, r in df.iterrows():
            flow = r.get('flow') or r.get('flow_name')
            low = r.get('uncertainty_low', 0.9)
            high = r.get('uncertainty_high', 1.1)
            base = r.get('amount_per_FU') if 'amount_per_FU' in r else r.get('amount')
            try:
                base = float(base)
            except Exception:
                continue
            factor = np.random.uniform(low, high)
            row[flow] = base * factor
        samples.append(row)
    return samples

def run_lcia_for_sample(sample, idx):
    # This is a stub. For now we write sampled inventory to a temporary CSV and call run_lcia.py
    tmp = os.path.join(ROOT, f'tmp_inventory_{idx}.csv')
    pd.DataFrame([sample]).to_csv(tmp, index=False)
    # You can modify `run_lcia.py` to accept a temporary inventory path; here we simply call it.
    # For now, we call run_lcia.py (which reads inventory_template.csv). Users should adapt run_lcia.py to accept tmp path.
    run(['python', os.path.join(HERE, 'run_lcia.py')])

def main(n=100):
    df = pd.read_csv(INV)
    samples = sample_params(df, n)
    # Placeholder: currently writes samples to OUT and instructs next steps
    pd.DataFrame(samples).to_csv(OUT, index=False)
    print('Wrote sampled parameter table to', OUT)
    print('Adapt `run_lcia.py` to accept a sample inventory and call it per sample to compute distributions.')

if __name__ == '__main__':
    main(100)
