# Theoretical Crystallography Open Database (TCOD)

Theoretical Crystallography Open Database (TCOD, https://www.crystallography.net/tcod/) is an open-access collection of theoretically calculated or refined crystal structures of organic, inorganic, metal-organic compounds and minerals, excluding biopolymers (Merkys *et. al*, 2017).

Crystal structure data in TCOD is recorded using the CIF framework (CIF 1.1 files, DDL1 dictionaries).
Data names used in TCOD CIF files come from three main sources:
- IUCr dictionaries that were originally created to record experimental crystallographic data (e.g. `cif_core.dic`).
- The `cif_dft.dic` dictionary which contains data items used to record parameters and results of DFT computations.
- The `cif_tcod.dic` dictionary which contains data items used to record computational provenance of theoretical experiments.

See the following resources for a more in-depth description of the data items defined by these dictionaries:
- IUCr dictionaries: https://www.iucr.org/resources/cif/dictionaries/
- `cif_dft.dic`: https://wiki.crystallography.net/cif/dictionaries/ddl1/cif_dft/
- `cif_tcod.dic`: https://wiki.crystallography.net/cif/dictionaries/ddl1/cif_tcod/

The plain-text DDL1/DDLm versions of the `cif_dft.dic` and `cif_tcod.dic` dictionary files can be retrieved from the TCOD website (https://www.crystallography.net/tcod/cif/dictionaries/).
Note, that the DDLm versions of the dictionaries were generated using an automated converter and should thus be treated as work-in-progress.

## Bibliographic references

- Merkys, A., Mounet, N., Cepellotti, A., Marzari, N., Gražulis, S. & Pizzi, G. (2017). A posteriori metadata from automated provenance tracking: Integration of AiiDA and TCOD. *Journal of Cheminformatics*, 9. https://doi.org/10.1186/s13321-017-0242-y
