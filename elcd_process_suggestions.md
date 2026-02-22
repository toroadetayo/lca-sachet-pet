ELCD / USLCI process suggestions and search guidance

Purpose
- This document lists recommended search strings and pragmatic choices for background processes (ELCD / USLCI or other open datasets) you can select in OpenLCA or Brightway. Use these to find exact process IDs in your local OpenLCA Nexus or Brightway installation, then paste IDs into `brightway_premap_results.csv` or `openlca_premap.csv`.

Search tips
- Use simple, case-insensitive keywords (e.g., "PET", "polyethylene film", "transport, freight, road").
- For electricity, search for "electricity, medium voltage" or "electricity, grid mix" and choose the closest regional proxy (West Africa) if Nigeria not present.
- For transport, look for "transport, freight, lorry" with a weight class (e.g., 3.5t, 16-32t) and use `tkm` conversions.

Suggested search strings and rationale
- "Polyethylene, low density" or "LDPE film" — maps to polyethylene film used for sachets. Prefer film/packaging-grade processes.
- "Polyethylene terephthalate" or "PET granulate" — maps to PET resin production; if available, use a specific "PET bottle" process.
- "Water, conventional treatment" or "water, treated, distribution" — municipal treatment + distribution to tap; scale from m3 to L.
- "Electricity, medium voltage, consumption" — general grid mix process; use country/regional proxy when Nigeria is absent.
- "Transport, freight, lorry >16t" (or appropriate size) — road freight process for truck transport.
- "Disposal, landfill, municipal waste" — landfill disposal process; choose unmanaged vs controlled depending on Lagos context.
- "Open burning of waste" or "open burning" — uncontrolled open burn processes (use with caution due to high uncertainty).
- "Recycling, PET bottles" and "recycling, polyethylene film" — recycling processes for PET and PE; if closed-loop not available, model avoided burden conservatively.
- "Printing inks, packaging" — printing inks for labels/printing (small mass but include if relevant).

How to paste IDs into the mapping CSV
1. In OpenLCA Nexus or Brightway, search the dataset with the strings above.
2. When you find a good match, copy the process ID/code (Brightway: `database_name: code` or OpenLCA: process UUID / code) and paste into the `suggested_process_code` column in `brightway_premap_results.csv`.
3. Save the CSV and run `run_lcia.py` locally (or import into OpenLCA) so the foreground processes link to these background processes.

Notes on regionalisation
- Electricity: if a Nigeria grid mix isn't available, document the proxy you used and run a sensitivity where you substitute a different grid mix.
- Transport: local vehicle fleets and road quality affect fuel consumption — if uncertain, run a transport-distance sensitivity.
- End-of-life: Lagos waste streams are likely dominated by informal collection, dumping, and open burning; use LAWMA and World Bank data to justify shares and test sensitivities.

If you'd like, I can now produce a second file with direct ELCD public page URLs for each suggested search (these are public pages you can open to examine processes). Reply "ELCD links" and I'll add them.
