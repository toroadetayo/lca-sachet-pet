LCA Protocol — Sachet vs PET bottled water (Lagos case study)

1. Goal and scope
- Goal: Quantify and compare cradle-to-grave environmental impacts of sachet water and PET bottled water for Lagos, Nigeria; identify hotspots and improvement opportunities, and provide policy-relevant recommendations.
- Audience: Researchers, policymakers, NGOs, and the project owner.

2. Functional unit
- 1 L of potable drinking water consumed at point of use.

3. System boundaries
- Cradle-to-grave: raw water abstraction, treatment (if any), packaging material production, transportation to filling site, filling & bottling/sachet operations, retail distribution, consumption, and end-of-life management of packaging (collection, recycling, landfill, open burning, leakage).

4. Alternatives compared
- Sachet water (single-use polyethylene/polyethylene blend sachets).
- PET bottled water (single-use PET bottles), including typical bottle sizes.

5. Allocation
- Where multi-output processes occur (e.g., polymer production producing multiple co-products), use mass allocation as primary approach; test energy allocation sensitivity.

6. Data quality requirements
- Preferred hierarchy: (1) Local primary data, (2) peer-reviewed literature & government/NGO reports for Nigeria, (3) open LCI database processes (ELCD, USLCI) adjusted to local context.

7. Life-cycle inventory (LCI)
- Key flows to collect per FU: packaging mass (g), polymer type, printing/inks mass, filling water volume (L), process energy (kWh) for treatment/filling, chemicals used, transport distances and vehicle types, distribution distances, consumer storage/cooling assumptions, waste-management fate shares.
- Use `inventory_template.csv` to record each flow with source and uncertainty bounds.

8. Impact categories & LCIA method
- Core: Global Warming Potential (GWP100, kg CO2-eq), Water depletion/use (m3), Cumulative energy demand (MJ).
- End-of-life: plastic leakage mass (kg), emissions from open burning (kg PM/CO2), landfill methane (if applicable).
- Additional optional: human toxicity, ecotoxicity, particulate matter formation.
- LCIA method: ReCiPe (if available in OpenLCA setup) or ELCD-compatible methods from OpenLCA Nexus. Document method selection in results.

9. Scenarios and sensitivity analysis
- Baseline (best-available data for Lagos).
- Sensitivities: waste-management shares (high informal recycling vs high littering), transport distances (local vs regional), recycled content in packaging, sachet mass variability, bottle reuse/return rates.
- Uncertainty: Monte Carlo on key inventory parameters (packaging mass, transport distances, waste fate shares, energy intensity).

10. Allocation of end-of-life
- Model explicit waste flows and fate shares. Where recycling occurs, apply closed-loop or open-loop allocation consistently and test effect of different recycling credits.

11. Reporting
- Provide transparency table listing all data sources, assumptions, and adjustments.
- Provide hotspot analysis (contribution analysis per life-cycle stage) and scenario comparison tables and plots.

12. Reproducibility
- Deliver OpenLCA project files (or export) plus the filled `inventory_template.csv` and a JSON/CSV of scenario parameters.

13. Ethics & limitations
- List limitations related to data gaps, regionalization of LCI data, and uncertainty. Recommend data collection to reduce major uncertainties.
