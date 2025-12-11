# Examples

## Summary 
This directory provides a curated set of configuration examples demonstrating the usage of the CSP Data Dictionary across various domains and methodologies.

The goal of these examples is to illustrate:
1. **Input Handling:** Defining fixed vs. variable chemical stoichiometry.
2. **Structure Generation:** Describe and combine structure generation techniques.
3. **Structure Ranking:** Describe and combine structure ranking techniques.

---

## Index

The table below summarizes the core concept, domain, and specific dictionary fields highlighted in each self-contained example folder.

| Folder Name                                           | Primary Domain | Input Description                        | Key Input/Methodology                                                               | Core Concepts & Dictionary Fields Highlighted                                                                                                             |
|:------------------------------------------------------|:---------------|------------------------------------------|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`01_Org_MCPT_Minimal`**                             | Organic CSP    | XXXI?                                    | Fixed Stoichiometry / Single generation and ranking methods / MC Parallel Tempering | High level description of a CSP method for molecular crystals.                                                                                            |
| **`02_Org_Multi_Stoich`**                             | Organic CSP    | cannabinol:tetramethylpyrazine cocrystal | Multiple Fixed Stoichiometries / Multi-Stage generation and ranking approaches      | In detail description of multiple structure generation and ranking methods. Highlights the sequential use and links between  different stages of the CSP. |
| **`03_Inorg_Random_Search_Fixed_stoich`**             | Inorganic      |                                          | Fixed Stoichiometry / Random Search                                                 | Shows a random numbers based approach to inorganic CSP.                                                                                                   |
| **`04_Inorg_Evolutionary_Algorithm_Variable_Stoich`** | Inorganic      |                                          | Variable Composition / Evolutionary Algorithm                                       | Highlights how to specify variable composition inputs and the use of Evolutionary Algorithms methods for structure generation.                            |
| **`05_Inorg_Particle_Swarm_Opt_Variable_Stoich`**     | Inorganic      |                                          | Variable Composition / Particle Swarm Optimization                                  | Highlights how to specify variable composition inputs and the use of Particle Swarm Optimisation methods for structure generation.                        |
| **`06_MOFs_input`**                                   | MOF CSP        |                                          | MOFs Input                                                                          | Shows how to describe a the inputs for a MOFs CSP search.                                                                                                 |
