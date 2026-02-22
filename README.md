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
