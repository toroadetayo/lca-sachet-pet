Scripts README

Files created
- `brightway_prepare.py`: scans installed Brightway2 databases for matching background processes using `openlca_premap.csv` search strings and writes `brightway_premap_results.csv` with top matches.
- `run_lcia.py`: creates foreground processes from `inventory_template.csv` and runs deterministic LCIA for `Sachet_fu` and `PET_fu`. It expects `brightway_premap_results.csv` to be completed with chosen process IDs.
- `montecarlo.py`: samples input parameters within uncertainty bounds and writes sampled parameter tables for Monte Carlo runs.

Usage overview
1. Install python and dependencies:
```
python -m pip install -r requirements.txt
```
2. Ensure Brightway2 background databases (ELCD/USLCI or similar) are installed and available to Brightway2.
3. Run `brightway_prepare.py` to search for candidate background processes and produce `brightway_premap_results.csv`.
4. Review `brightway_premap_results.csv` and edit the file to select the preferred `(db_name, process name, process code)` for each flow. Add an explicit `nexus_process_id` or ensure the `top_match` is the correct one.
5. Run `run_lcia.py` to build foreground processes and run the LCIA. If needed, adapt `run_lcia.py` to accept a custom inventory file for Monte Carlo.

Notes & limitations
- These scripts are designed to be a reproducible starting point. They do not fully automate every mapping decision — you must review and confirm background matches, and ensure appropriate LCIA methods are installed in Brightway2 (e.g., ReCiPe or ELCD methods).
- If you prefer a fully-GUI OpenLCA workflow instead of Brightway2, use `openlca_import_template.csv` and `openlca_premap.csv` plus `openlca_mapping.md` which contain guidance for import.
