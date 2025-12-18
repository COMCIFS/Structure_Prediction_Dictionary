# Example 2 - Multi-Stage Generation and Ranking Approaches

![img.jpg](img.jpg)

## Summary

In this example, we show a description of a hypothetical CSP method for the cannabinol:tetramethylpyrazine (CBN:TMP)
cocrystal that intentionally uses many different methods.
Three stoichiometries are researched (1:1, 2:1, 1:2) and multistep generation and ranking methods are implemented.
Input molecules, output structures, workflows, generation and ranking methods are organised in separate files but this
is not mandatory. As all these items are organised in separated datablocks, they could be merged into a single file.

---

## Input

The datablock (in file `csp_input.cif`) starts by introducing three identifiers of the target compound:

- The (human-readable) chemical name `cannabinol_tetramethylpyrazine` of the two compounds
- A unique identifier that can be used for an internal database (being target XXX of the 7th Blind Test, we used
  `BT-XXX`)
- A datablock unique ID (`2a2611e3-2021-4b03-a7c6-0ef71239008f`).

Only the latter will be used to link output structures to the input datablock.

The input then describe the two molecules (smiles, atoms and bonds) and finally defines the three stoichiometries
analysed in the search.
As stoichiometries are not variables in the optimisation (the `_csp.input_composition_calculation` is set to `"fixed"`),
this is equivalent to have three different input files each one with a single stoichiometry.

---

## Structure Generation Methods

In the file `structure_generation_methods.cif` we describe an approach using multiple methods.
While this could add complexity to the search, the combined strengths of these different methods can help identify
relevant states.
The four structure generation methods here described are: a random sampling method using the Sobol algorithm, a Monte
Carlo parallel tempering approach, an evolutionary algorithm and a particle swarm optimisation.

In all these methods, the 10 most popular spacegroups for organic crystals are used.
The random sampling generates 7500 structures which are then used by the other three methods as inputs to generated at
most 100,000 structures each. Relationships between methods are instead described in the `csp_workflow.cif` file

---

## Structure Ranking Methods

In the same way as structure generation methods, in the file `structure_ranking_methods.cif`, each datablock describe a
single method while the links between them are shown in the `csp_workflow.cif` file.

The first three consists of geometry optimisations with energy methods of increasing computational cost: a classical
forcefield (GAFF) with point charges generated from a gas-phase quantum mechanical method, a semi-empirical method (
DFTB) and a dispersion-corrected DFT method (PBE-MBD).
Two criteria are set for structures to pass to next stage, an energy cutoff and a maximum number of structures (as
shown in `csp_workflow.cif`).

Energies of PBE-optimised structures are then recalculated using hybrid and meta DFT functionals (PBE0-MBD, PBE0-XDM,
R2SCAN-D4) and the MP2 wavefunction approach.
The DFT method with the best agreement to MP2 is then selected to re-optimise structures.

Finally, the free-energy of the top 50 structures are calculated at temperature 100, 200 and 300 K using the
quasi-harmonic approximation.

---

## Output structure

In file `structure_A1B1_1.cif` we show an example of the evolution of a single structure through the different ranking
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
been omitted in the othe datablocks.