# Example 2 - Multi-Stage generation and ranking approaches

![img.jpg](img.jpg)

## Summary
In this example, we show a description of a hypothetical CSP method for the cannabinol:tetramethylpyrazine (CBN:TMP) cocrystal with the current CSP Dictionary.
Three stoichiometries are researched (1:1, 2:1, 1:2) and multistep generation and ranking methods are implemented.
Input molecules, output structures, workflows, generation and ranking methods are organised in separate files but this is not mandatory. As all these items are organised in separated datablocks, they could be merged into a single file.

## Input
The datablock starts by introducing three identifiers of the target compound: 
 - The (human-readable) chemical name `cannabinol_tetramethylpyrazine` 
 - A unique identifier that can be used for an internal database (being target XXX of the 7th Blind Test, we used `BT-XXX`)
 - A datablock unique ID (`2a2611e3-2021-4b03-a7c6-0ef71239008f`). 

Only the latter will be used to link output structures to the input datablock.


The input then describe the two molecules (smiles, atoms and bonds) and finally defines the three stoichiometries analysed in the search.
As stoichiometries are not variables in the optimisation (the `_csp.input_composition_calculation` is set to `"fixed"`), this is equivalent to have three different input files each one with a single stoichiometry.


