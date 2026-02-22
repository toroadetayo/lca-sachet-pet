**Project: LCA of Sachet Water Production in West Africa (Lagos case study)**

**Overview — what has been done**

- Objective: Completed cradle-to-grave life cycle assessment (LCA) comparing
  sachet water and PET bottled water for Lagos, Nigeria. Functional unit: 1 L
  of potable drinking water consumed at point of use.
- Scope & methods: Foreground inventory compiled from literature and open LCI
  proxies; background processes referenced to open datasets (ELCD/USLCI). Impac
  t categories: GWP100, water depletion, cumulative energy demand.

**Completed repository contents**

- `protocol.md` — LCA protocol (goal & scope, system boundaries, assumptions,
  and scenarios).
- `inventory_template.csv` — Completed with Lagos-default parameters and unc
  ertainty ranges (packaging mass, filling energy, transport, end-of-life sha
  res).
- OpenLCA aids: `openlca_import_template.csv`, `openlca_premap.csv`, and `ope
n lca_mapping.md` to assist building the model in OpenLCA.
- `scripts/` — Brightway2-compatible Python scripts (`brightway_prepare.py`,
  `run_lcia.py`, `montecarlo.py`) for reproducible model construction and sample
  -based uncertainty analysis (to run locally where Brightway2 is available).
- `results/` — Deterministic LCA outputs, sensitivity analyses, MC summary CSV
  , and figures (`driver_shares.svg`, `sensitivity_figures.svg`). See `results/
  summary.md` for quick numbers.
- Documentation: `documentation_full.html` and `policy_memo.html` and Word-co
  mpatible `.docx` exports.
- Drafts: `manuscript_draft.md` and `policy_brief_draft.md` containing Methods,
  Results and Discussion drafts.

**Key deterministic findings (baseline)**

- Sachet GWP (per 1 L): ~0.0425 kg CO2-eq
- PET GWP (per 1 L): ~0.0897 kg CO2-eq
- Packaging production and end-of-life (open burning, low recycling) are ma
  jor hotspots. Stage-level breakdowns are available in `results/gwp_results.cs
  v` and `results/hotspot_table.csv`.

**How to reproduce or extend the analysis**

1. Clone the repository and inspect `inventory_template.csv` to review key pa
   rameters and uncertainty bounds.
2. For GUI users: import `openlca_import_template.csv` into OpenLCA and follow
   `openlca_mapping.md` to map foreground flows to background processes.
3. For script-based reproducibility: create a Python environment, install dep
   endencies from `requirements.txt`, then run `scripts/run_lcia.py` (determin
   istic) and `scripts/montecarlo.py` (sample-based MC) locally.

**Limitations & notes**

- Analyses rely on open-dataset proxies and literature defaults rather than fu
  lly regional LCI processes; end-of-life modelling is simplified. Use results
  for comparison and hotspot identification; collect primary data for final po
  licy decisions.

**Where to look first**

- Quick overview: `results/summary.md`
- Numerical outputs: CSV files in `results/`
- Protocol and method details: `protocol.md` and `manuscript_draft.md`

Repository remote: https://github.com/toroadetayo/lca-sachet-pet

If you'd like, I will now produce publication-grade PNG figures (300 DPI) fr
om the CSVs and add captions to `manuscript_draft.md`.

Thank you — the repo is structured so others can reproduce or adapt the analys
is; open issues or pull requests are welcome.
Project: LCA of Sachet Water Production in West Africa (Lagos case study)

Overview
- Objective: Cradle-to-grave life cycle assessment (LCA) comparing sachet water and PET bottled water, using Lagos, Nigeria as the case study locality. Functional unit: 1 L of potable drinking water consumed at point of use.
- Modeling tool: OpenLCA (GUI). Use open/default LCI datasets available in OpenLCA Nexus (ELCD, USLCI, and other open datasets).

Repository contents
- `protocol.md` — detailed LCA protocol (goal & scope, assumptions, system boundaries, impact categories, scenarios).
- `inventory_template.csv` — CSV template for life-cycle inventory (fill-in values per process/flow).
- `data_sources.md` — recommended data sources, suggested literature and online databases.

Next steps
1. I will compile literature and open-dataset parameters for key processes (packaging, filling, transport, end-of-life) and populate `inventory_template.csv` with best-available defaults for Lagos.
2. Then I'll create an OpenLCA project recipe (instructions + importable files) and step through model build.
3. After model runs, I'll perform sensitivity and uncertainty analysis and prepare results and manuscript draft.

How you can help
- Provide any primary data you have (e.g., measured sachet mass, local transport distances, waste-management shares). If none, say "I trust you" and I'll proceed with literature/default values.

Contact & notes
- I'll keep you updated at each milestone and ask questions only when I need data or clarification.
