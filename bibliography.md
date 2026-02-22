Short bibliography — open-access numeric sources used for Lagos defaults

1. OpenLCA Nexus (ELCD and other open datasets)
- What: Background LCI processes for polymer production, energy, transport, and common materials.
- Use for: plastic production emission factors, electricity mixes, transport unit processes.
- Link: https://nexus.openlca.org/datasets

2. US EPA — US Life Cycle Inventory (USLCI) Database
- What: Open LCI inventory data for chemicals, fuels, packaging, and processes.
- Use for: alternative background processes where ELCD entries are missing.
- Link: https://www.epa.gov/lca/us-life-cycle-inventory-database

3. World Bank — "What a Waste 2.0" (2018) and Nigeria country profile
- What: Waste generation, management, and mismanagement fractions by country/region.
- Use for: baseline waste fate shares and municipal solid waste context for Lagos.
- Link: https://openknowledge.worldbank.org/handle/10986/30317

4. UNEP — "Single-Use Plastics: A Roadmap for Sustainability" (2018)
- What: Global synthesis on single-use plastics, waste fate, and management options.
- Use for: open-burning emission factors, mismanaged plastic definitions, policy context.
- Link: https://wedocs.unep.org/handle/20.500.11822/25496

5. UNEP — "Global Waste Management Outlook" (2015)
- What: Regional summaries and best-practice waste-management data applicable to West Africa.
- Link: https://www.unep.org/resources/report/global-waste-management-outlook

6. FAO AQUASTAT
- What: Country water withdrawal and resource availability statistics.
- Use for: contextual water depletion and abstraction data for Nigeria.
- Link: https://www.fao.org/aquastat

7. Lagos Waste Management Authority (LAWMA)
- What: Local waste management practice descriptions, reports, and public data for Lagos.
- Use for: regional waste-management practices and collection/recycling infrastructure.
- Link: https://lawma.gov.ng/

8. OpenLCA / OpenLCA documentation
- What: Guidance for importing CSV/process data and mapping to Nexus datasets.
- Use for: OpenLCA build and reproducibility instructions.
- Link: https://www.openlca.org/documentation/

9. IPCC Assessment Reports (for GWP factors)
- What: Global Warming Potentials (AR5/AR6) and methodology for GWP100 references.
- Use for: converting greenhouse gas emissions to CO2-eq.
- Link: https://www.ipcc.ch/reports/

10. Supplementary literature & targeted searches (open access)
- What: Peer-reviewed open-access studies measuring sachet and PET packaging mass, filling energy, and local transport distances in Nigeria/West Africa.
- How to find: Google Scholar searches such as "sachet water Nigeria", "sachet water Lagos waste", "packaging mass PET bottle 500 mL"; examples and PDFs are often available via institutional repositories and ResearchGate.
- Google Scholar search example: https://scholar.google.com/scholar?q=sachet+water+nigeria

Notes
- I used the above open datasets and reports to set the default numeric values in `inventory_template.csv`. Where local primary data are unavailable, I prioritized ELCD/USLCI processes and contextualized waste fractions using World Bank and LAWMA reports. I will record exact process IDs and page-level sources when I map these flows into OpenLCA.
