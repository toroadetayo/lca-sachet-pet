OpenLCA import & mapping guidance

What this is
- `openlca_import_template.csv` contains sample process rows and exchanges you can import into OpenLCA as processes and link to background flows.

Recommended columns and meanings
- `process_name`: name of the foreground process in OpenLCA.
- `process_type`: optional descriptor (e.g., "process").
- `flow_name`: name of the flow or input (e.g., "polyethylene film", "electricity").
- `flow_unit`: unit (g, kg, L, kWh, tkm).
- `amount`: amount per functional unit (FU = 1 L consumed).
- `exchange_type`: typically "input" for foreground-consuming exchanges.
- `linked_process_id`: optional field where you can paste an OpenLCA/Nexus process ID after you find the matching background process.
- `reference`: source or note for the number.
- `uncertainty_low` / `uncertainty_high`: multiplicative bounds for sensitivity/Monte Carlo.

Step-by-step import & mapping (GUI + mapping guidance)
1. Install OpenLCA and ensure access to OpenLCA Nexus datasets (ELCD/USLCI). Create a new local database.
2. Prepare foreground processes: In OpenLCA, create a new process group (e.g., "Sachet vs PET Lagos").
3. Import CSV: OpenLCA can import processes/exchanges from CSV using the CSV import tool (Menu: File → Import → CSV). Use the template and map columns accordingly.
4. Link background flows: After import, each flow (e.g., "polyethylene film", "electricity", "truck transport") must be linked to a background process from Nexus (ELCD) or USLCI.
   - Search Nexus for processes: e.g., "polyethylene, granulate" or "polyethylene film production"; for electricity choose the nearest grid mix available (use country-level proxy if Nigeria not available).
   - For transport, choose a truck transport unit process (e.g., "transport, freight, road, lorry 16-32t"), then convert to `tkm` by multiplying mass by distance (see CSV example using tkm units).
5. Units & conversions: Ensure units match (OpenLCA may require kg instead of g). Convert grams to kg where needed or set consistent units in CSV.
6. Waste flows and end-of-life: Model explicit waste flows (recycled, landfill, open burn) as separate processes. Link landfill to an appropriate disposal process (e.g., "disposal, landfill"), and for open burning, choose an open-burning or open-incineration process and document limitations.
7. LCIA methods: Import or enable ReCiPe or ELCD-compatible LCIA method in OpenLCA. Run the LCIA on the assembled product system.

Tips for Lagos regionalization
- Electricity: if country-level Nigerian grid mix is not available in Nexus, use a regional proxy (e.g., West Africa or Ghana) and document the substitution.
- Transport distances: use the `transport_km` row and convert to `tkm` by multiplying freight mass (kg→t) by km; CSV approach uses tkm to avoid creating many trip processes.
- End-of-life: model separate scenarios (baseline, high recycling, high mismanagement) by editing the mass shares for the end-of-life exchanges.

Recording provenance
- After you link each `flow_name` to an OpenLCA/Nexus process, paste the process identifier into `linked_process_id` in the CSV and save a copy. This ensures reproducibility.

Next steps I can do for you
- Create a pre-mapped CSV where I select Nexus ELCD/USLCI process IDs for plastics, electricity proxies, and transport (requires listing available Nexus dataset IDs; I can prepare a mapping file you can import directly).
- Or I can walk through the OpenLCA GUI import and linking interactively if you want to run OpenLCA locally.
