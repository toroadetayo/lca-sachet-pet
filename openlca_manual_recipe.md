OpenLCA manual import recipe (CSV) — import & map without scripts

Goal
- Guide to import `openlca_import_template.csv` into OpenLCA, map each flow to ELCD/USLCI background processes, and run LCIA — everything you can do inside OpenLCA GUI (no local Python required).

Step 1 — OpenLCA setup
- Ensure OpenLCA is installed. Connect to OpenLCA Nexus (Menu: File → Preferences → Nexus) and add ELCD/USLCI datasets from the Nexus browser.

Step 2 — Import foreground CSV
- Menu: File → Import → CSV → Processes and exchanges.
- Select `openlca_import_template.csv` from the project folder.
- Map columns: `process_name` → Process name, `flow_name` → Flow name, `flow_unit` → Unit, `amount` → Amount, `exchange_type` → Exchange type.
- Complete import; OpenLCA will create foreground processes with unlinked flows.

Step 3 — Link background processes
- For each unlinked flow (e.g., polyethylene film, electricity, truck transport):
  - In the process view, click the exchange → click "Choose" to select a flow from a dataset.
  - Use the search box in Nexus: paste a recommended search string from `elcd_process_suggestions.md` (e.g., "LDPE film", "PET granulate").
  - Inspect candidate processes, check their metadata, and choose the best match. Click OK.
  - Document the selected dataset and process code by adding the code to `brightway_premap_results.csv` or a local notes file.

Step 4 — Units & conversions
- Ensure units match — most background processes use kg, m3, kWh, or tkm. Convert grams to kg (1 g = 0.001 kg) or use OpenLCA's unit conversion when creating exchanges.

Step 5 — Model end-of-life scenarios
- Duplicate the product system/process and edit the end-of-life exchange shares to create scenario variants (baseline, high recycling, high mismanagement).

Step 6 — LCIA methods and running results
- Under Methods, enable ReCiPe or an ELCD-compatible method.
- Create a product system or directly run impact assessment on a process: Right-click process → Calculate LCIA → choose method → run.

Step 7 — Export and provenance
- Export the project or the product system (File → Export → Project) for reproducibility.
- Save a CSV of input flows and the selected process codes (use the `brightway_premap_results.csv` format) for record-keeping.

Troubleshooting
- If a matching background process is not available in ELCD, try USLCI or a generic process (e.g., "polymer production, generic") and document the substitution.
- For electricity, document the proxy and run a sensitivity with an alternate grid mix.

If you'd like, I can now create a sheet (`final_mapping_instructions.csv`) listing each foreground flow with a short recommended search string and the exact UI steps to link it (I can add that next). Reply "add mapping sheet" to have it created.
