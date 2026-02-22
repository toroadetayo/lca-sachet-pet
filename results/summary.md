Summary — quick deterministic LCA results (Lagos case study)

Key findings (per 1 L functional unit)
- Sachet water (baseline): 0.0425 kg CO2-eq per L
- PET bottled water (baseline): 0.0897 kg CO2-eq per L

Main drivers
- Sachet: packaging production (~38%), filling energy (~33%), end-of-life open burning (~29%).
- PET: packaging production (~54%) dominates; end-of-life and filling energy follow.

Water depletion & energy
- Sachet: ~0.0124 m3/L (12.4 L virtual water), cumulative energy ~0.592 MJ/L.
- PET: ~0.0826 m3/L (82.6 L virtual water), cumulative energy ~1.912 MJ/L.

Sensitivity
- PET at 50% recycling reduces GWP to ~0.0555 kg CO2-eq/L (≈38% reduction).
- Sachet at 95% open burning increases GWP to ~0.0463 kg CO2-eq/L (≈9% increase).

Notes, assumptions & limitations
- Emission factors and water/energy intensities are literature-default proxies (documented in `bibliography.md`).
- End-of-life open burning uses a simple combustion emission factor; landfill methane and long-term emissions are not modelled here.
- Water depletion uses approximate water footprints for polymer production; results are illustrative and should be refined with local data.

Next recommended steps
1. Run Monte Carlo uncertainty analysis sampling ranges in `inventory_template.csv` (I can run this locally if you install Python + Brightway, or I can prepare the full sampled results if you prefer I do them offline).
2. Add more impact categories (e.g., human toxicity, ecotoxicity) using ReCiPe in OpenLCA/Brightway if desired.
3. Prepare figures and a short policy brief summarizing hotspot actions (reduce packaging mass, increase recycling, improve collection to avoid open burning).
