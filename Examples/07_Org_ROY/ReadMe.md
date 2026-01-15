# Example 7 - ROY, using well-established methods, with a state of the art monomer correction at the final ranking stage

## Summary

In this example, we show a description of a published CSP workflow: <https://doi.org/10.1039/D1SC06074K> which uses established methods, with a state-of-the-art monomer correction

---

## Input

The datablock (in file `csp_input.cif`) starts by introducing three identifiers of the target compound:

- The (human-readable) chemical name `ROY`
- A unique identifier that can be used for an internal storage or database (`Beran_ROY`)
- A datablock unique ID (``).

Only the latter will be used to link output structures to the input datablock.

The input then describes the molecules (smiles, atoms and bonds, and stoichiometries)

---

## Structure Generation Methods

In the file `structure_generation_methods.cif` we describe a random sampling method using the Sobol algorithm.

The 59 most popular spacegroups for organic crystals are used.

---

## Structure Ranking Methods

In the same way as structure generation methods, in the file `structure_ranking_methods.cif`, each datablock describe a
single method while the links between them are shown in the `csp_workflow.cif` file.

The first three consists of geometry optimisations with energy methods of increasing computational cost: CrystalPredictor, using a 

---

## Output structure

In file `structures.cif` we show an example of the evolution of a single structure through the different ranking
stages.

In the initial part of the datablocks (one for each stage), links to the input, generation method, ranking stage and
workflow datablocks are shown to correctly identify the origin and stage of the structure.
Please note that only the unique ID is mandatory for this purpose, the description is made to help readability for
humans.
For free energy calculations, also reference temperature and pressure must be specified.
As different files have been used to describe the input and workflow, the path to this is added with the data field
`_csp.data_block_additional_files`.
This would not be needed if methodology and output structures are all in a single file.

Next, we find structure properties such as energy and rank.

Finally, cell and atomic coordinates are shown in the standard CIF format. Except for the first step, this section has
been omitted in the other datablocks to focus on the new data fields introduced with the CSP Dictionary.