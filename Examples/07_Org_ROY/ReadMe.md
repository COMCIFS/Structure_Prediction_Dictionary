# Example 7 - ROY, using well-established methods, with a state of the art monomer correction at the final ranking stage

## Summary

In this example, we show a description of a published CSP workflow: <https://doi.org/10.1039/D1SC06074K> which uses established methods for generation and ranking,
with a state-of-the-art monomer correction in the final ranking stage.

---

## Input

The datablock (in file `csp_input.cif`) starts by introducing three identifiers of the target compound:

- The (human-readable) chemical name `ROY`
- A unique identifier that can be used for an internal storage or database (`Beran_ROY`)
- A datablock unique ID (`10628627-856c-4176-acf7-b18b0d98681d`).

Only the latter will be used to link output structures to the input datablock.

The input then describes the molecules (smiles)

---

## Structure Generation Methods

In the file `structure_generation_methods.cif` we describe a random sampling method using the Sobol algorithm.

The 59 most popular spacegroups for organic crystals are used.

---

## Structure Ranking Methods

In the same way as structure generation methods, in the file `structure_ranking_methods.cif`, each datablock describe a
single method while the links between them are shown in the `csp_workflow.cif` file.

The first three consists of geometry optimisations with energy methods of increasing computational cost: 1 - CrystalPredictor, using a point charge Force Field, with charges and intramolecular terms
derived from QM methods, 2 - CrystalOptimizer, using a multipole Force Field, with multipoles and intramolecular terms derived from QM methods, 3 - Periodic DFT using Quantum Esspresso

Finally, a monomer correction is applied to the lowest ranked structures from stage 3

---

## Output structure

In file `structures.cif` we show exampes of the structures from the final ranking stage, with structure properties such as energy and rank.
