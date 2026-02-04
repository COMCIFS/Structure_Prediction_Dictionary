# Example 2 - Multi-Stage Generation and Ranking Approaches

![Example_1_diagram.jpg](Example_1_diagram.jpg)

## Summary

In this example, we show a description of a hypothetical CSP workflow for the methyl 2-aminobenzoate that uses a Monte
Carlo Parallel Tempering approach to generate structures.
Output structures are initially evaluated with a Multipole approach and subsequently with a DFT method.
Input molecules, output structures, workflows, generation and ranking methods are organised in separate files. This
is not mandatory, and they could be merged into a single file (as all these items are organised in separated
datablocks).

---

## Input

The datablock (in file `csp_input.cif`) starts by introducing three identifiers of the target compound:

- The (human-readable) chemical name `"methyl 2-aminobenzoate"` of the compound
- A unique identifier that can be used for an internal storage or database (being target XXIX of the 7th Blind Test, we
  used `BT-XXX`)
- A datablock unique ID (`0d430939-34a3-4fc1-bf49-d04e39580fbc`).

Only the latter will be used to link output structures to the input datablock.

The input then describe the molecule with details on atoms and bonds.

---

## Structure Generation Methods

In the file `structure_generation_methods.cif` we describe Monte Carlo Parallel Tempering (MCPT).
This includes parameters specific to the MCPT method (for example the number of replicas), constraints in the search (
for example the number spacegroups used) and stopping criteria for ending the generation of structures.

---

## Structure Ranking Methods

In the file `structure_ranking_methods.cif`, the two datablocks describe the Multipoles and pDFT approaches while the
links between them are shown in the `csp_workflow.cif` file.
Two criteria are set for structures to pass the first stage (Multipoles) to the second and final stage (pDFT), an energy
cutoff and a maximum number of structures (as
shown in `csp_workflow.cif`).

---

## Output structure

In file `structure_1.cif` we show an example of a single structure at the two ranking stages.

In the initial part of the datablocks (one for each stage), links to the input, generation method, ranking stage and
workflow datablocks are shown to correctly identify the origin and stage of the structure.
Please note that only the unique ID is mandatory for this purpose, the description is made to help readability for
humans.
As different files have been used to describe the input and workflow, the path to this is added with the data field
`_csp.data_block_additional_files`.
This would not be needed if methodology and output structures are all in a single file.

Next, we find structure properties such as energy and rank.

Finally, cell and atomic coordinates are shown in the standard CIF format.