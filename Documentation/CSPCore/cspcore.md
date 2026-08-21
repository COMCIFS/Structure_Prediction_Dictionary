# CSP Core Dictionary

## Introduction

### Summary

This is the CSP dictionary for describing predicted crystal structures and the methods, parameters and workflows used to
calculate these.

### Table of contents

* **1. Datablocks Identifiers and File Cross-Referencing** describing the links between methods, workflows and output
  structures.
* **2. Input Chemical System** describing the input atoms or molecular entities for CSP.
* **3. Structure Generation Methods** describing the methods used to generate theoretical crystal structures.
* **4. Structure Ranking Methods** describing the energy evaluation models used to optimise and rank the structures.
* **5. Output Structure Properties** describing the properties of each output structure, such as their energy or
  density, and the general output of a CSP run, such as the computational cost and global minima at each step.
* **6. Intermediate Step** describing additional steps made in selecting structures or inputs.
* **7. Conventions** specifying guidelines to avoid multiple labels for the same term.
* **8. Future Developments** describing what is missing from the current dictionary and possible new developments.

## 1. Data blocks identifiers and file cross-referencing

Category `_csp_data_block.[]`: This section specifies the class type of the data block and assigns a unique identifier
to it.

| Group             | Data Field         | Type       | Definition                                                                                                                 | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Units | Example                                                            |
|-------------------|--------------------|------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|--------------------------------------------------------------------|
| `_csp_data_block` | `class`            | char       | Class type of the data block.                                                                                              | - "Input": Describes the input atoms or molecular entities for CSP. <br/>- "Generation Method": Describes the method used to generate theoretical crystal structures. <br/>- "Ranking Method": Describes the energy evaluation models used to optimise and rank the structures. <br/>- "Workflow": Describe how generation, ranking and intermediate steps are linked together to create the CSP Workflow. <br/>- "Theoretical Structure": Describes the properties and 3D coordinates of output structures. <br/>- "Output": Describes the general outputs of a CSP run, such as the computational cost and global minima of each step. <br/>- "Step": Describes possible intermediate steps, such as clustering to remove duplicates on conformer generation for CSP of molecular crystals. |       | "Input"                                                            |
| `_csp_data_block` | `id`               | char       | Unique identifier of the data block. This will be used to link the different datablocks in a workflow or output structure. | It is recommended a unique identifiers generation protocol is used, such as UUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |       | "`dd55207f-9649-435b-9708-c8154c33fc03`"                           |
| `_csp_data_block` | `description`      | char       | Text identifier of a datablock for human readability.                                                                      | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |       | "Molecule 1"                                                       |
| `_csp_data_block` | `additional_files` | list[char] | If datablocks are specified in different files, add the position of these files.                                           | `List[str]`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |       | `["generation_methods.cif" "ranking_methods.cif" "workflows.cif"]` |

Single inputs systems, generation methods and ranking methods must be described in separate datablocks and a unique
identifier should be assigned to them. We recommend the use of Universally Unique Identifiers (UUIDs), described
in [here](https://www.rfc-editor.org/rfc/rfc9562) and naturally implemented in most programming languages. The Workflow
datablock is meant to connect different generation and ranking methods in multistep approaches. Finally, the output
theoretical structures will have a link to the specific stage in the workflow and the previous structure. Examples of
each one of these data blocks are available below.

Datablocks can be stored in different files or in multiple files depending on the user. In the former case, the
`_csp_data_block.additional_files` field should be used. In practice, one can have a set of default settings for the
generation, ranking methods and workflows, with the different landscapes differing only in the input and output
structure's data blocks.

## 2. Input Chemical System

Category `_csp_input.[]`, `_csp_input_molecular_entity.[]`, `_csp_input_atom.[]`: These categories specify the atomic
species used in inorganic CSP or the input molecular entities for organic or organometallic crystal generation.

| Group                         | Data Field                     | Type       | Definition                                                                                                                                                              | Constraints                                                                                                                                                         | Units | Example                                                     |
|-------------------------------|--------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------------------------------------------|
| `_csp_input`                  | `name`                         | char       | See name_common and name_systematic from Core CIF dictionary.                                                                                                           | Free Text                                                                                                                                                           |       | "urea hydrate"                                              |
| `_csp_input`                  | `identifier`                   | char       | An input identifier used for internal databases or classification.                                                                                                      | Free Text                                                                                                                                                           |       | "UREAXXH2O"                                                 |
| `_csp_input`                  | `composition_calculation`      | char       | "fixed" or "variable" composition calculation.                                                                                                                          | - "Fixed": The composition is not a variable in the search/generation of new structures. <br/>- "Variable": The composition is allowed to change during the search. |       | "Fixed"                                                     |
| `_csp_input`                  | `composition_coefficients`     | list[numb] | List of possible compositions for fixed-composition calculations or extremes for variable-composition simulations.                                                      | `List[PositiveInt]`                                                                                                                                                 |       | - `[1 1]`<br/>- `[2 1]`                                     |
| `_csp_input`                  | `maximum_number_of_components` | numb       | The maximum number of components (atoms or molecular entities) in the unit cell.                                                                                        | \>1                                                                                                                                                                 |       | 4                                                           |
| `_csp_input`                  | `minimum_number_of_components` | numb       | The minimum number of components (atoms or molecular entities) in the unit cell.                                                                                        | \>1                                                                                                                                                                 |       | 2                                                           |
| `_csp_input`                  | `atom_types`                   | list[char] | List of atomic species defining the composition. This simplifies the input definition in inorganic CSP, avoiding defining a separate molecular entity for each species. | `List[str]` or `List[PositiveInt]`                                                                                                                                  |       | - `[Mg O]` (Atomic symbols)<br/>- `[12 8]` (Atomic numbers) |
| `_csp_input_molecular_entity` | `number`                       | numb       | Molecular entity component index.                                                                                                                                       | \>1                                                                                                                                                                 |       | 1                                                           |
| `_csp_input_molecular_entity` | `identifier`                   | char       | Label used to identify the molecular entity.                                                                                                                            | Free Text                                                                                                                                                           |       | - "urea"<br/>- "water"                                      |
| `_csp_input_molecular_entity` | `smiles`                       | char       | SMILES of the component.                                                                                                                                                | Free Text                                                                                                                                                           |       | "C(=O)(N)N"                                                 |
| `_csp_input_atom`             | `molecular_entity_number`      | numb       | In a loop describing the atoms in a molecular entity, the molecular entity component index of which the atom belongs.                                                   | \>1                                                                                                                                                                 |       | 1                                                           |
| `_csp_input_atom`             | `molecular_entity_identifier`  | char       | In a loop describing the atoms in a molecular entity, the label of the molecular entity of which the atom belongs.                                                      | Free Text                                                                                                                                                           |       | - "urea"<br/>- "water"                                      |
| `_csp_input_atom`             | `label`                        | char       | In a loop describing the atoms in a molecular entity, the label of the atom in the molecular entity.                                                                    | Free Text                                                                                                                                                           |       | C1                                                          |

Additional details on atoms in molecule ad their connectivity can be specified through the CIF Chemical dictionary,
available at: https://www.iucr.org/__data/iucr/cifdic_html/1/cif_core.dic/index.html

The term "Molecular Entity" is used to describe any separately distinguishable entity as described in the IUPAC
Compendium of Chemical Terminology at: https://doi.org/10.1351/goldbook.M03986. Data fields in this category can be used
to describe both metals and ligands in a MOF.

### Examples

Inorganic CSP input with fixed stoichiometry:

```text
data_ferrosilite
# Datablock Details
_csp_data_block.class               "Input"
_csp_data_block.id                  1ac303d1-ea55-439a-8f3d-d9bd462b3b25
_csp_data_block.description         Ferrosilite

# Input Details
_csp_input.name                     Ferrosilite
_csp_input.atom_types               [ Fe Si O ] 
_csp_input.composition_calculation  fixed
_csp_input.composition_coefficients [ 1 1 3 ]
```

Inorganic CSP input with variable stoichiometry:

```text
data_input2
# Datablock Details
_csp_data_block.class                   "Input"
_csp_data_block.id                      d5c894e9-561c-490a-89b0-877bbc516b14
_csp_data_block.description             Hypersthene

# Input Details
_csp_input.name                         Hypersthene 
_csp_input.atom_types                   [ Fe Mg Si O ]
_csp_input.composition_calculation      variable
_csp_input.composition_coefficients     [[1 0 1 3] [0 1 1 3]]
_csp_input.minimum_number_of_components 2
_csp_input.maximum_number_of_components 10
```

This implies that resulting structures will have formula *x*(FeSiO3)+ *y*(MgSiO3) with *2<x+y<10*. Worth noticing that
the string following `data_` is not used in the linking of datablocks.

Multi-component molecular crystal CSP with fixed stoichiometry:

```text
data_molecule
# Datablock Details
_csp_data_block.class       "Input"
_csp_data_block.id          2a2611e3-2021-4b03-a7c6-0ef71239008f
_csp_data_block.description input1

_csp_input.name             Urea_Hydrate

# Molecules
loop_
    _csp_input_molecular_entity.number
    _csp_input_molecular_entity.identifier
    _csp_input_molecular_entity.smiles
    _chemical.name_common
    1 WAT O      water
    2 URE OCN(N) urea

# Atoms in molecules
loop_
    _csp_input_atom.molecular_entity_number     
    _csp_input_atom.molecular_entity_identifier
    _csp_input_atom.label
    _chemical.conn_atom_number
    _chemical.conn_atom_type_symbol
    _chemical.conn_atom_charge
    1 WAT O1 1  O -0.800000
    1 WAT H1 2  H  0.400000
    1 WAT H1 3  H  0.400000
    2 URE O1 4  O -0.613359
    2 URE C1 5  C  0.880229
    2 URE N1 6  N -0.923545
    2 URE N2 7  N -0.923545
    2 URE H1 8  H  0.395055
    2 URE H2 9  H  0.395055
    2 URE H3 10 H  0.395055
    2 URE H4 11 H  0.395055

# Bonds
loop_
    _chemical.conn_bond_atom_1
    _chemical.conn_bond_atom_2
    _chemical.conn_bond_type
    1 2  sing
    1 3  sing
    4 5  doub
    5 6  sing
    5 7  sing
    6 8  sing
    6 9  sing
    7 10 sing
    8 11 sing

_csp_input.composition_calculation  "fixed"
_csp_input.composition_coefficients [ 2 1 ] # Indexes from molecule section (2 water molecules and one urea)
```

`composition_coefficients` here refers to the molecular entity number. Worthy of note the use of the `Chemical`
dictionary in defining the molecules.

Variable stoichiometry search can be specified in the same way as for inorganic systems:

```text
...
_csp_input.composition_calculation      "variable"
_csp_input.composition_coefficients     [[1 0] [0 1]]
_csp_input.maximum_number_of_components 4
_csp_input.minimum_number_of_components 2
```

For metal-organic systems, the `_csp.input_molecular_entity` and `Chemical` dictionaries can be used specifying metallic
atoms and ligands:

```text
data_mo
# Datablock Details
_csp_data_block.class       "Input"
_csp_data_block.id          fbbe2b09-da53-4505-ba9c-d4952a096dbb
_csp_data_block.description input1

_csp.input_name "(mi-tricyanomethanide)-silver"

# Molecules
loop_
    _csp_input_molecular_entity.number
    _csp_input_molecular_entity.identifier
    _chemical.name_common
    1 Metal Silver
    2 c4n3  tricyanomethanide

# Atoms in molecules
loop_
    _csp_input_atom.molecular_entity_number
    _csp_input_atom.molecular_entity_identifier
    _csp_input_atom.label
    _chemical.conn_atom_number
    _chemical.conn_atom_type_symbol
    1 Metal Ag1 1  Ag
    2 c4n3  C1  2  C 
    2 c4n3  C2  3  C 
    2 c4n3  C3  4  C 
    2 c4n3  C4  5  C 
    2 c4n3  N1  6  N 
    2 c4n3  N2  7  N 
    2 c4n3  N3  8  N 

# Bonds
loop_
    _chemical.conn_bond_atom_1
    _chemical.conn_bond_atom_2
    _chemical.conn_bond_type
    1 6  sing
    1 7  sing
    1 8  sing
    2 3  doub
    2 4  sing
    2 5  sing
    3 6  doub
    4 7  trip
    5 8  trip

_csp_input.composition_calculation   "fixed"
_csp_input.composition_coefficients  [1 1]
```

## 3. Structure Generation Methods

This section helps delineate the space search range and specify the parameters used for different methods.

### 3.1 General Fields

Category `_csp.structure_generation_[]`: Category for structure generation methods.

| Group                                         | Data Field                                     | Type       | Definition                                                                                                                                                                                                                                                                           | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Units               | Example                                                                |
|-----------------------------------------------|------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------------------------------------------------------|
| `_csp`                                        | `structure_generation_space_group_number_list` | List[numb] | Space group selection: a subset (list) specifying which space group numbers were used.                                                                                                                                                                                               | 1-230                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                     | `[14 2 15 61 19 4 33 29 5 1]`                                          |
| `_csp`                                        | `structure_generation_space_group_list`        | List[char] | Space group selection: it could be "all" or a subset (list) specifying which space groups were used.                                                                                                                                                                                 | Either "all" or list of sg labels                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                     | `["P1" "P-1" "P21" "P21/c" "P21212" "P212121" "Pna21" "Pca21" "Pbca"]` |
| `_csp`                                        | `structure_generation_method`                  | char       | Structure generation method.                                                                                                                                                                                                                                                         | - "Evolutionary Algorithm" (Sec. 3.2): Search methods based on Evolutionary Algorithms. <br>- "Particle Swarm Optimisation" (Sec. 3.3): Search methods based on Particle Swarm Optimisation.  <br>- "Simulated Annealing" (Sec. 3.4): Search methods based on Monte Carlo Simulated Annealing optimisations. <br>- "Monte Carlo Parallel Tempering" (Sec. 3.5): Search methods based on Monte Carlo Parallel Tempering optimisations. <br>- "Random Search" (Sec. 3.6): Search methods based on random sampling. <br>- "Analogue Templates": Search methods based on templating structures from similar systems. <br>- Other: Any other structure generation methods. |                     | "Simulated Annealing"                                                  |
| `_csp`                                        | `structure_generation_method_description`      | char       | Short description of the method used.                                                                                                                                                                                                                                                | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                     |                                                                        |
| `_csp`                                        | `structure_generation_method_other`            | char       | If `_csp.structure_generation_method` is "Other", it specifies the label of the method used.                                                                                                                                                                                         | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                     |                                                                        |
| `_csp`                                        | `structure_generation_software`                | char       | Name of the software used for structure generation.                                                                                                                                                                                                                                  | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                     |                                                                        |
| `_csp`                                        | `structure_generation_software_citation`       | char       | Details of the software used for structure generation. Either URL to webpage or DOI of the related publication.                                                                                                                                                                      | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                     |                                                                        |
| `_csp`                                        | `structure_generation_software_version`        | char       | Version of software used for structure generation.                                                                                                                                                                                                                                   | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                     |                                                                        |
| `_csp`                                        | `structure_generation_density_lower_limit`     | numb       | Minimum Cell Density.                                                                                                                                                                                                                                                                | \>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | kg m<sup>-3</sup>   | 800.0                                                                  |
| `_csp`                                        | `structure_generation_density_upper_limit`     | numb       | Maximum Cell Density.                                                                                                                                                                                                                                                                | \>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | kg m<sup>-3</sup>   | 1400.0                                                                 |
| `_csp`                                        | `structure_generation_reference_temperature`   | numb       | Reference temperature for finite-temperature simulations.                                                                                                                                                                                                                            | \>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | K                   | 0.0                                                                    |
| `_csp`                                        | `structure_generation_reference_pressure`      | numb       | Reference pressure for variable cell calculations.                                                                                                                                                                                                                                   | \>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Pa                  | 100000.0                                                               |
| `_csp_structure_generation_stopping_criteria` | `description`                                  | List[char] | List of rules for stopping the generation of new structures. This can be a single field or a list of criteria. Additional datafields are present for two popular approaches (max structures and no new low-energy structures added).                                                 | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                     | `["Max Structures" "Low-Energy Structures Unchanged"]`                 |
| `_csp_structure_generation_stopping_criteria` | `max_structures_evaluated`                     | numb       | The maximum total number of unique crystal structures that will be generated and evaluated during the search. If it relates to a list of spacegroups in `stopping_criteria_space_group_number_list`, the value applies to all spacegroups in total (see the Examples section below). | \>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                     | 10000                                                                  |
| `_csp_structure_generation_stopping_criteria` | `iterations_without_improvement`               | numb       | The maximum number of consecutive iterations (generations, MC steps, etc.) where the global minimum (or the lowest few structures) does not change.                                                                                                                                  | \>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                     | 50                                                                     |
| `_csp_structure_generation_stopping_criteria` | `energy_range`                                 | numb       | An energy threshold for the selection of low-energy structures to be considered in the convergence criteria.                                                                                                                                                                         | \>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | kJ mol<sup>-1</sup> | 5.0                                                                    |
| `_csp_structure_generation_stopping_criteria` | `structures_range`                             | numb       | The number of low-energy structures to be considered in the convergence criteria.                                                                                                                                                                                                    | \>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                     | 1000                                                                   |
| `_csp_structure_generation_search_space`      | `space_group_number_list`                      | List[numb] | If different stopping criteria are used for each space group, it allows a user to specify a single space group or a subset of space groups numbers in a loop.                                                                                                                        | 1-230                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                     |                                                                        |
| `_csp_structure_generation_search_space`      | `space_group_list`                             | List[char] | If different stopping criteria are used for each space group, it allows a user to specify a single space group or a subset of space groups names in a loop.                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                     |                                                                        |
| `_csp_structure_generation_search_space`      | `z_prime`                                      | List[numb] | If different stopping criteria are used for each value of Z', it allows a user to specify it in a loop.                                                                                                                                                                              | \>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                     |                                                                        |
| `_csp_structure_generation`                   | `stage`                                        | numb       | To be used in the "Workflow" datablock, specifying the stage number of the generation method.                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                     |                                                                        |
| `_csp_structure_generation`                   | `preceding_stage`                              | numb       | To be used in the "Workflow" datablock, specifying the stage number of the previous generation method.                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                     |                                                                        |
| `_csp_structure_generation`                   | `data_block_id`                                | char       | To be used in the "Workflow" datablock, specifying the identifier of the datablock in which the structure generation method is described.                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                     |                                                                        |
| `_csp_structure_generation`                   | `data_block_label`                             | char       | To be used in the "Workflow" datablock, it is a short, human-readable label of the generation method.                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                     | "ea"                                                                   |
| `_csp_structure_generation`                   | `data_block_description`                       | char       | To be used in the "Workflow" datablock, it is a short, human-readable description of the generation method.                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                     | "Evolutionary Algorithm"                                               |

### 3.2 Evolutionary Algorithms

Category `_csp.evolutionary_algorithm_[]`: Subgroup for CSP Structure Generation methods that use Evolutionary
Algorithms. For these fields to be used, the `_csp.structure_generation_method` must include "Evolutionary Algorithm".

| Group                          | Data Field                    | Type | Definition                                                                                                                                                     | Constraints | Units | Example |
|--------------------------------|:------------------------------|:-----|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:------|:--------|
| `_csp_evolutionary_algorithms` | `population_size`             | numb | The number of candidate structures in each generation.                                                                                                         | \>0         |       | 100     |
| `_csp_evolutionary_algorithms` | `initial_population_size`     | numb | The number of candidate structures in the first generation.                                                                                                    | \>0         |       | 50      |
| `_csp_evolutionary_algorithms` | `number_of_generations`       | numb | The maximum number of evolutionary cycles the algorithm will run before termination (unless other stopping criteria are met).                                  | \>0         |       | 50      |
| `_csp_evolutionary_algorithms` | `parents_structure_fraction`  | numb | The fraction of individuals in the current population that is used to generate structures in the next cycle.                                                   | 0.-1.       |       | 0.75    |
| `_csp_evolutionary_algorithms` | `nextgen_structure_selection` | numb | The number of individuals that survives (are kept) in the next generation.                                                                                     | \>1         |       | 5       |
| `_csp_evolutionary_algorithms` | `mutation_fraction`           | numb | The fraction of individuals in the population that will undergo mutation in each generation.                                                                   | 0.-1.       |       | 0.2     |
| `_csp_evolutionary_algorithms` | `heredity_fraction`           | numb | The fraction of individuals in the population that will be generated through heredity (crossover/recombination) operations between two or more parents.        | 0.-1.       |       | 0.6     |
| `_csp_evolutionary_algorithms` | `permutation_fraction`        | numb | The fraction of individuals in the population that will undergo a permutation operation (e.g., swapping atom positions within a structure) in each generation. | 0.-1.       |       | 0.1     |

### 3.3 Particle Swarm Optimisation Algorithms

Category `_csp.particle_swarm_optimisation_[]`: Subgroup for CSP Structure Generation methods that use Particle Swarm
Optimisation. For these fields to be used, the `_csp.structure_generation_method` must include "Particle Swarm
Optimisation".

| Group                              | Data Field              | Type | Definition                                                                                                                                        | Constraints | Units | Example |
|------------------------------------|:------------------------|:-----|:--------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:------|:--------|
| `_csp_particle_swarm_optimisation` | `population_size`       | numb | The number of candidate crystal structures (particles) in the swarm.                                                                              | \>0         |       | 50      |
| `_csp_particle_swarm_optimisation` | `number_of_generations` | numb | The maximum number of optimisation cycles (generations or iterations) the PSO algorithm will run.                                                 | \>0         |       | 100     |
| `_csp_particle_swarm_optimisation` | `inertia_weight`        | numb | A parameter controlling the contribution of the previous velocity of the particle to its current velocity.                                        | 0.-1.       |       | 0.7     |
| `_csp_particle_swarm_optimisation` | `max_inertia_weight`    | numb | If the inertia weight changes with each iteration, this parameter specifies the maximum value it can have.                                        | 0.-1.       |       | 0.9     |
| `_csp_particle_swarm_optimisation` | `min_inertia_weight`    | numb | If the inertia weight changes with each iteration, this parameter specifies the minimum value it can have.                                        | 0.-1.       |       | 0.4     |
| `_csp_particle_swarm_optimisation` | `cognitive_coefficient` | numb | A parameter (also called self-confidence factor) controlling the influence of the particle's own best position found so far on its movement.      | \>=0.       |       | 2       |
| `_csp_particle_swarm_optimisation` | `social_coefficient`    | numb | A parameter (also called swarm confidence factor) controlling the influence of the swarm's best position found so far on the particle's movement. | \>=0.       |       | 2       |
| `_csp_particle_swarm_optimisation` | `velocity_clamp_max`    | numb | The maximum allowed velocity for each dimension if velocity clamping is enabled.                                                                  | \>0.        |       | 0.2     |

### 3.4 Simulated Annealing

Category `_csp.simulated_annealing_[]`: Subgroup for CSP Structure Generation methods that use Simulated Annealing. For
these fields to be used, the `_csp.structure_generation_method` must include "Simulated Annealing".

| Group                      | Data Field            | Type | Definition                                                                                        | Constraints | Units | Example |
|----------------------------|:----------------------|:-----|:--------------------------------------------------------------------------------------------------|:------------|:------|:--------|
| `_csp_simulated_annealing` | `initial_temperature` | numb | The starting temperature of the simulated annealing process.                                      | \>0.        | K     | 500.    |
| `_csp_simulated_annealing` | `cooling_rate`        | numb | The parameter that determines how the temperature is decreased over the course of the simulation. | 0.-1.       |       | 0.95    |
| `_csp_simulated_annealing` | `number_of_steps`     | numb | The number of attempted structure generation and acceptance steps performed at each temperature.  | \>0         |       | 10      |

### 3.5 Monte Carlo Parallel Tempering

Category `_csp_monte_carlo_parallel_tempering.[]`: Subgroup for CSP Structure Generation methods that use Monte Carlo
Parallel tempering. For these fields to be used, the `_csp.structure_generation_method` must be set to "Monte Carlo
Parallel Tempering".

| Group                                 | Data Field           | Type       | Definition                                                                                                              | Constraints | Units | Example          |
|---------------------------------------|:---------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------|:------------|:------|:-----------------|
| `_csp_monte_carlo_parallel_tempering` | `number_of_replicas` | numb       | The number of independent Monte Carlo simulations (replicas) running in parallel at different temperatures.             | \>1         |       | 3                |
| `_csp_monte_carlo_parallel_tempering` | `temperatures_list`  | list[numb] | The list of temperatures at which the replicas are run.                                                                 | \>=0.       | K     | `[0. 300. 600.]` |
| `_csp_monte_carlo_parallel_tempering` | `number_of_steps`    | numb       | The number of Monte Carlo steps performed by each replica at its assigned temperature in each parallel tempering cycle. | \>0         |       | 100              |

### 3.6 Random Search

Category `_csp_random_search.[]`: Subgroup for CSP Structure Generation methods that use Random algorithms. For these
fields to be used, the `_csp.structure_generation_method` should be set to "Random Search".

| Group                | Data Field       | Type | Definition                                                            | Constraints                                                                                                                                                                                                                                        | Units | Example        |
|----------------------|:-----------------|:-----|:----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|:---------------|
| `_csp_random_search` | `algorithm_type` | char | Specifies the type of algorithm used to generate random numbers.      | - "Pseudorandom": Random number generation algorithms that aim at mimicking true random numbers. <br>- "Quasirandom": Random number generation algorithms that aim at distributing points evenly across the space. <br>- "Other": Any other method |       | "Pseudorandom" |
| `_csp_random_search` | `algorithm`      | char | Specifies the label of the algorithm used to generate random numbers. | Free Text                                                                                                                                                                                                                                          |       | "Sobol"        |

### Examples

Search in all space groups until 10000 structures are generated with an evolutionary algorithm:

```text
data_ea
# Datablock Details
_csp_data_block.class                                                "Generation Method"
_csp_data_block.id                                                   af534fed-8153-4af2-bd9f-29b0fef8d805
_csp_data_block.description                                          "ea"

# Method Details
_csp.structure_generation_method                                     "Evolutionary Algorithm"
_csp.structure_generation_density_lower_limit                        750
_csp.structure_generation_density_upper_limit                        1600
_csp.structure_generation_space_group_number_list                    "all"
_csp.structure_generation_stopping_criteria_description              "Max Structures"
_csp.structure_generation_stopping_criteria_max_structures_evaluated 10000
```

Combination of different structure generation methods, search limited on most popular space groups for organic crystals.

```text
# Random Search 1
data_rs
    _csp_data_block.class                                                "Generation Method"
    _csp_data_block.description                                          rs
    _csp_data_block.id                                                   8e0147be-0k54-44a1-a3bb-de7df26ddeer
    
    _csp.structure_generation_method                                     "Random Search"
    _csp_random_search.algorithm_type                                    "Quasirandom"
    _csp_random_search.algorithm                                         "Sobol"
    
    _csp.structure_generation_space_group_number_list                    [14 2 15 61 19 4 33 29 5 1]
    _csp_structure_generation_stopping_criteria.description              "Max Structures"
    loop_
        _csp_structure_generation_search_space.z_prime
        _csp_structure_generation_search_space.space_group_number_list                         
        _csp_structure_generation_stopping_criteria.max_structures_evaluated  
        1   14   1000  # 1000 structures for the top 5 spacegroup in organic structures
        1   2    1000
        1   15   1000
        1   61   1000
        1   19   1000
        1   4     500  # 500 structures for the next 5 spacegroup in organic structures
        1   33    500
        1   29    500
        1   5     500
        1   1     500
        2   14    500  # 500 structures for the top 5 spacegroup in organic structres and Z'=2                 
        2   2     500                                                         
        2   15    500                                                         
        2   61    500                                                               
        2   19    500                                                         

# Random Search 2
data_rs2
    _csp_data_block.class                                                "Generation Method"
    _csp_data_block.description                                          rs2
    _csp_data_block.id                                                   6e0147be-0454-44a1-a3bb-de7b326dde1b
    
    _csp.structure_generation_method                                     "Random Search"
    _csp_random_search.algorithm_type                                    "Quasirandom"
    _csp_random_search.algorithm                                         "Sobol"
    
    _csp.structure_generation_space_group_number_list                    [14 2 15 61 19 4 33 29 5 1]
    _csp_structure_generation_stopping_criteria.description              "Max Structures"
    loop_
        _csp_structure_generation_search_space.space_group_number_list                      
        _csp_structure_generation_stopping_criteria.max_structures_evaluated  
        [14 2 15 61 19]  5000 # 5000 structures in total, not necessarily equally distributed
        [4 33 29 5 1]    2500    
       

# Simulated Annealing
data_sa
    _csp_data_block.class                                                "Generation Method"
    _csp_data_block.description                                          sa
    _csp_data_block.id                                                   95f28b3c-d029-4840-a69a-3ced34219c28
    
    _csp.structure_generation_method                                     "Simulated Annealing"
    _csp.structure_generation_space_group_number_list                    [14 2 15 61 19 4 33 29 5 1]
    
    _csp_structure_generation_stopping_criteria.description              "Max Structures"
    _csp_structure_generation_stopping_criteria.max_structures_evaluated 2000000  
    
    _csp_simulated_annealing.initial_temperature                         400
    _csp_simulated_annealing.cooling_rate                                0.95
    _csp_simulated_annealing.number_of_steps                             100
    

# Relations between methods
data_workflow
    _csp_data_block.class                                                Workflow
    _csp_data_block.description                                          wf
    _csp_data_block.id                                                   29ba6f2f-0a56-47be-bc90-9c8adc7760e9

    # Structure Generation Methods
    loop_
        _csp_structure_generation.stage
        _csp_structure_generation.preceding_stage
        _csp_structure_generation.data_block_description
        _csp_structure_generation.method
        _csp_structure_generation.data_block_id
        0 . "rs" "Random Search"     6e0147be-0454-44a1-a3bb-de7b326dde1b
        1 0 "sa" "Simulated Annealing" 95f28b3c-d029-4840-a69a-3ced34219c28

    # Structure Ranking Methods
    ...
```

For the last section, the mandatory data fields to identify and link the different datablocks are
`_csp_structure_generation.stage`, `_csp_structure_generation.preceding_stage` and
`_csp_structure_generation.data_block_id`. Other data fields are included to make the file more human-readable.

The data field `_csp_structure_generation_stopping_criteria.max_structures_evaluated` indicates the _total_ number of
structures generated across the different space groups specified into the
`_csp_structure_generation_space_group_number_list` or
`_csp_structure_generation_stopping_criteria.space_group_number_list`. In the three `Generation Method` datablocks, we
show the use of
`_csp_structure_generation_stopping_criteria.max_structures_evaluated` data fields:

1. In the first `Random Search` approach (Datablock 1), for the space groups **14, 2, 15, 61 and 19**, the criterion is
   set to 1000 structures each, while for **4, 33, 29, 5 and 1**, it is set to 500 structures each, resulting in a total
   of 7500 structures for the `Z'=1` calculations.
2. In the second `Random Search` approach (Datablock 2), 5000 and 2500 structures are generated in total for subsets
   [14, 2, 15, 61, 19] and [4, 33, 29, 5, 1], respectively, for a total of 7500 structures. Contrary to the previous
   example, these are not necessarily equally distributed among the spacegroups of the subset.
3. In the `Simulated Annealing` approach (Datablock 3), the value represents the maximum total number of structures
   evaluated across all space groups combined. The search stops when this limit is reached regardless of how many
   structures were evaluated in any specific space group.

## 4. Structure Ranking Methods

Within this section, you can define the workflow used to rank the different crystals and give _high-level_ details of
the methods used. To allow compatibility with other dictionaries and possible future works on computational chemistry
calculations, single methods data fields don't have the `_csp` prefix.

### 4.1 General Fields

Categories:

* `_csp_structure_ranking.[]`: Category to define structure ranking stages in multistep approaches.
* `_compchem.[]` : Details on calculation types and software citation.
* `_compchem_geometry_optimisation.[]`: Geometry optimisation details.

| Group                             | Data Field                | Type       | Definition                                                                                                                                                                                                                                | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Units                               | Example                         |
|-----------------------------------|:--------------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|:--------------------------------|
| `_csp_structure_ranking`          | `stage`                   | numb       | To be used in the "Workflow" datablock, it specifies the stage number of the ranking method.                                                                                                                                              | \>=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                     | 0                               |
| `_csp_structure_ranking`          | `preceding_stage`         | numb       | To be used in the "Workflow" datablock, it specifies the stage number of the previous ranking method.                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                     |                                 |
| `_csp_structure_ranking`          | `data_block_label`        | char       | To be used in the "Workflow" datablock, it specifies the text identifier of the datablock in which the structure ranking method is described.                                                                                             | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     | - "FF"<br/>- "PBE"<br/>- "PBE0" |
| `_csp_structure_ranking`          | `data_block_description`  | char       | To be used in the "Workflow" datablock, it shortly describes the ranking stage.                                                                                                                                                           | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     | - "FF"<br/>- "PBE"<br/>- "PBE0" |
| `_csp_structure_ranking`          | `data_block_id`           | char       | To be used in the "Workflow" datablock, it is a short, human-readable description of the ranking method.                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                     |                                 |
| `_csp_structure_ranking`          | `relative_energy_cutoff`  | numb       | To be used in the "Workflow" datablock, in case of multi-step ranking of structures, it specifies the structures that will be used in the next step by selecting those below a certain relative energy difference from the global minima. | \>=0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | kJ mol<sup>-1</sup>                 | 10.0                            |
| `_csp_structure_ranking`          | `max_structures_retained` | numb       | To be used in the "Workflow" datablock, in case of multi-step ranking of structures, it specifies the structures that will be used in the next step by selecting the top N structures in the ranking.                                     | \>=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                     | 250                             |
| `_compchem`                       | `method`                  | char       | The energy or scoring model used to rank structures.                                                                                                                                                                                      | - "pDFT" (Sec. 4.2): Ranking methods based on periodic Density Functional Theory methods. <br>- "Forcefield" (Sec. 4.3): Ranking methods based on classical forcefield. <br>- "Semi Empirical" (Sec. 4.4): Ranking methods based on semi empirical approaches, <br>- "Wavefunction" (Sec. 4.5): Ranking methods based on wavefunction approaches. <br>- "ML Potentials" (Sec. 4.6): Ranking methods based on Ml potentials. Forcefields parameterised with ML, should be under the "Forcefield" category. <br>- Other: Any other method. |                                     | "Forcefield"                    |
| `_compchem`                       | `method_description`      | char       | Short description of the energy or scoring model used to rank structures.                                                                                                                                                                 | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     |                                 |
| `_compchem`                       | `method_other`            | char       | If `compchem.method` is "Other", specify the label of the method used.                                                                                                                                                                    | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     |                                 |
| `_compchem`                       | `calculation_type`        | char       | Indicates how atomic positions are changed.                                                                                                                                                                                               | - "Optimisation": Geometry is optimised to minimise the energy. <br>- "Dynamic Ensemble": Include any calculation of a thermodynamic ensemble (e.g. microstates from MD simulations or an ensemble of phonons from lattice dynamics). <br>- "Single point": No change in atomic coordinates or cell parameters.                                                                                                                                                                                                                          |                                     | "Single point"                  |
| `_compchem`                       | `software`                | char       | Name of the software used for structure ranking.                                                                                                                                                                                          | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     |                                 |
| `_compchem`                       | `software_citation`       | char       | Details of the software used for structure ranking.                                                                                                                                                                                       | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     |                                 |
| `_compchem`                       | `software_version`        | char       | Version of software used for structure ranking.                                                                                                                                                                                           | Free Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     |                                 |
| `_compchem_geometry_optimisation` | `algorithm`               | char       | Geometry optimisation algorithm.                                                                                                                                                                                                          | - "BFGS": Broyden Fletcher Goldfarb Shanno Quasi Newton algorithm. <br>- "LBFGS": the limited memory version of BFGS. <br>- "FIRE": Fast Inertial Relaxation Engine algorithm. <br>- "Steepest Descent": Gradient Descent algorithm. <br>- "Conjugate Gradient": Conjugate Gradient Method. <br>- Other: Any other method.                                                                                                                                                                                                               |                                     |                                 |
| `_compchem_geometry_optimisation` | `algorithm_other`         | char       | If `_compchem_geometry_optimisation.algorithm` is "Other", specify the algorithm used.                                                                                                                                                    | Free text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                     |                                 |
| `_compchem_geometry_optimisation` | `cell`                    | char       | It can be "fixed" for no cell optimisation, "isotropic" or "anisotropic" for cell relaxation calculations.                                                                                                                                | - "fixed": no cell optimisation<br/>- "isotropic": Isotropic cell relaxation.<br/>- "anisotropic": Anisotropic cell relaxation                                                                                                                                                                                                                                                                                                                                                                                                           |                                     |                                 |
| `_compchem_geometry_optimisation` | `atoms`                   | char       | It can be "fixed", "all", "intermolecular only", "hydrogens" or "non hydrogens"                                                                                                                                                           | - "fixed": no atoms' position optimisation (only cell dimesions are optimised) <br/>- "all": an all atoms geometry optimisation. <br/>- "intermolecular only": molecules are kept rigid and only optimise their position and orientation. <br/>- "hydrogens": optimisation of only H atoms <br/>- "non hydrogens": non H atoms are optimised while H atoms are kept at fixed positions/orientation from the bonded atom.                                                                                                                 |                                     | "all"                           |
| `_compchem_geometry_optimisation` | `atoms_list`              | list[numb] | A list of atoms for custom relaxation of a subset of atoms.                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                     | `[1 2 3 4]`                     |
| `_compchem_geometry_optimisation` | `relax_force_convergence` | numb       | Convergence criteria for stopping the geometry optimisation. Present in the TCOD DFT Dictionary as `_dft_atom_relax_force_conv`.                                                                                                          | \>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | kJ mol<sup>-1</sup> nm<sup>-1</sup> | 0.1                             |
| `_compchem_geometry_optimisation` | `max_steps`               | numb       | Maximum number of steps in the geometry optimisation.                                                                                                                                                                                     | \>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                     |                                 |
| `_compchem_geometry_optimisation` | `constrained_symmetry`    | bool       | Preserve (True) or not (False) the spacegroup symmetry during optimisation                                                                                                                                                                | bool                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                     | True                            |

### 4.2 Periodic Density Functional Theory

Category `_dft.[]`:  Subgroup for Computational Chemistry methods that use pDFT methods. The *p* of *pDFT* is removed in
`_dft` for consistency with the TCOD DFT Dictionary (https://wiki.crystallography.net/cif/dictionaries/ddl1/cif_dft/).
For these fields to be used, the `_compchem.method` should be set to "pDFT".

| Group  | Data Field                                   | Type | Definition                                                                           | Constraints                                                                                                                                                                                                                                                                       | Units | Example                                                                                                                                                             |
|:-------|:---------------------------------------------|:-----|:-------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_dft` | `exchange_correlation_functional_type`       | char | Specifies the type of exchange-correlation functional used.                          | - "LDA": Local Density Approximation<br/>- "GGA": Generalized Gradient Approximation. <br/>- "metaGGA": Meta GGA Approximation. <br/>- "Hybrid": Mix of exact exchange from Hartree Fock with GGA or metaGGA. <br/>- Other: Any other type of exchange correlation approximation. |       | "GGA"                                                                                                                                                               |
| `_dft` | `exchange_correlation_functional_type_other` | char | Specifies the type of exchange-correlation functional used if not in the given list. | Free text                                                                                                                                                                                                                                                                         |       |                                                                                                                                                                     |
| `_dft` | `exchange_correlation_functional_name`       | char | Specifies the name of exchange-correlation functional used.                          | Free Text                                                                                                                                                                                                                                                                         |       | - "PBE"<br/>- "PBE0"<br/>- "SCAN"                                                                                                                                   |
| `_dft` | `pseudopotential_type`                       | char | Defines the type of pseudopotentials used.                                           | Free Text                                                                                                                                                                                                                                                                         |       | - "Plane-waves"<br/>- "PAW"<br/>- "Norm-conserving"<br/>- "Ultrasoft"                                                                                               |
| `_dft` | `dispersion_correction`                      | char | The van der Waals correction used.                                                   | Free Text                                                                                                                                                                                                                                                                         |       | - "Grimme-D2"<br/>- "Grimme-D3"<br/>- "Tkatchenko-Scheffler"<br/>- "Many-body dispersion"<br/>- "Non-local many-body dispersion"<br/>- "Neumann-Perrin"<br/>- "XDM" |

### 4.3 Forcefields

Category `_forcefield.[]`:  Subgroup for Computational Chemistry methods that use forcefield or mixed inter/intra
molecular methods. For these fields to be used, the `_compchem.method` should be set to "Forcefield".

| Group                          | Data Field                  | Type | Definition                                                                                                                                                                                                                                                                                                                                                                                                           | Constraints                                                                                                                                                                                                                                                                                                     | Units | Example                                                                                                          |
|--------------------------------|:----------------------------|:-----|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|:-----------------------------------------------------------------------------------------------------------------|
| `_forcefield`                  | `name`                      | char | Name of the force field.                                                                                                                                                                                                                                                                                                                                                                                             | Free Text                                                                                                                                                                                                                                                                                                       |       | - "OPLS"<br/>- "GAFF"<br/>- "Dreiding II"<br/>- "CLP"                                                            |
| `_forcefield`                  | `intramolecular_term`       | char | The energy evaluation method for intramolecular interactions.                                                                                                                                                                                                                                                                                                                                                        | - "Bonded Parameters": Set of parameters defining bond stretching, angles bending and dihedrals potentials. <br/>- "Isolated Molecule Energy": The energy of the molecule in the gas phase. <br/>- "None": Only intermolecular interactions are calculated. <br/>- "Other": Any other method.                   |       |                                                                                                                  |
| `_forcefield`                  | `intramolecular_term_other` | char | If `_forcefield.intramolecular_term` is "Other", the energy evaluation method for intramolecular interactions.                                                                                                                                                                                                                                                                                                       | Free text                                                                                                                                                                                                                                                                                                       |       |                                                                                                                  |
| `_forcefield`                  | `electrostatic_term`        | char | Functional form of electrostatic interactions.                                                                                                                                                                                                                                                                                                                                                                       | - "Point Charges": Fixed charge located at the atom centre. <br/>- "Multipoles": Inclusion of higher order moments to better represent the charge distribution. <br/>- "Other": Any other method.                                                                                                               |       |                                                                                                                  |
| `_forcefield`                  | `electrostatic_term_other`  | char | If `_forcefield.electrostatic_term` is "Other", the functional form of electrostatic interactions.                                                                                                                                                                                                                                                                                                                   | Free text                                                                                                                                                                                                                                                                                                       |       |                                                                                                                  |
| `_forcefield`                  | `vdw_term`                  | char | Functional form of van der Waals interactions.                                                                                                                                                                                                                                                                                                                                                                       | Free Text                                                                                                                                                                                                                                                                                                       |       | - "LJ(C6-C12)"<br/>- "LJ(epsilon-sigma)"<br/>- "Buckingham"<br/>- "ReaxFF Morse-Potential"<br/>- "14-7 function" |
| `_forcefield_parameterisation` | `term`                      | char | In a loop, describe which term is parameterised with which approach. It can be "intramolecular", "electrostatic" or "vdw".                                                                                                                                                                                                                                                                                           | - "intramolecular": used to describe the parameterisation of the intramolecular term in a forcefield. <br/>- "electrostatic": used to describe the parameterisation of the electrostatic term in a forcefield. <br/>- "vdw": : used to describe the parameterisation of the van der Waals term in a forcefield. |       | "electrostatic"                                                                                                  |
| `_forcefield_parameterisation` | `description`               | char | Briefly describes the primary method used to derive the intramolecular, electrostatic, dispersion/repulsion force field parameters.                                                                                                                                                                                                                                                                                  | Free Text                                                                                                                                                                                                                                                                                                       |       | - "Fitting to gas-phase QM data"<br/>- "Transferable parameters based on atom types"                             |
| `_forcefield_parameterisation` | `method`                    | char | The parameterisation method used (for example the exchange-correlation functional and basis set used in the gas-phase quantum mechanical calculations when fitting force field parameters) or database from which parameters are taken if no calculation is performed. As a rule of thumb, quantum mechanical methods should be described as <Functional>-<dispersion correction>/<basis set> (e.g. PBE-D3/cc-pvtz). | Free Text                                                                                                                                                                                                                                                                                                       |       | - "MP2/6-31G(d,p)"<br/>- "B3LYP/aug-cc-pVTZ"<br/>- "PBE-D3/cc-pvtz"                                              |

### 4.4 Semi-Empirical

Category `_semiempirical.[]`:  Subgroup for Computational Chemistry methods that use Semi-Empirical methods. For these
fields to be used, the `_compchem.method` should be set to "Semi Empirical".

| Group            | Data Field                 | Type | Definition                                                                                                     | Constraints                                                                                                                                                                                                                                                                                            | Units | Example                                                                                   |
|:-----------------|:---------------------------|:-----|:---------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|:------------------------------------------------------------------------------------------|
| `_semiempirical` | `type`                     | char | Type of semi-empirical method.                                                                                 | - "Tight Binding": Methods using the tight binding approximation. <br/>- "Self Consistent Tight Binding": Methods using a self consistent tight binding formalism. <br/> - "NDDO": Mathods based on the Neglect of Differential Diatomic Overlap integral approximation. <br/>- Other: Any other type. |       |                                                                                           |
| `_semiempirical` | `method`                   | char | Specifies the name of the Semi-Empirical method used.                                                          | Free Text                                                                                                                                                                                                                                                                                              |       | - "AM1"<br/>- "PM3"<br/>- "PM6"<br/>- "xTB"                                               |
| `_semiempirical` | `electronic_parameters`    | char | The Slater-Koster tables or equivalent defining the atomic orbitals and pairwise element-element interactions. | Free Text                                                                                                                                                                                                                                                                                              |       | - "mio"<br/>- "3ob"                                                                       |
| `_semiempirical` | `repulsive_potential`      | char | When not included in the SK files, the repulsive potential term used.                                          | Free Text                                                                                                                                                                                                                                                                                              |       |                                                                                           |
| `_semiempirical` | `dispersion_correction`    | char | Dispersion corrections for semi-empirical methods.                                                             | Free Text                                                                                                                                                                                                                                                                                              |       | - "Grimme-D2"<br/>- "Grimme-D3"<br/>- "Tkatchenko-Scheffler"<br/>- "Many-body dispersion" |
| `_semiempirical` | `hydrogen_bond_correction` | char | H-bond corrections for semi-empirical methods.                                                                 | Free Text                                                                                                                                                                                                                                                                                              |       | - "H+"<br/>- "H4"                                                                         |
| `_semiempirical` | `halogen_bond_correction`  | char | Correction term for halogen bonds interactions.                                                                | Free Text                                                                                                                                                                                                                                                                                              |       | "X"                                                                                       |

### 4.5 Wavefunction

Category `_wavefunction.[]`:  Subgroup for Computational Chemistry methods that use wavefunction methods. For these
fields to be used, the `_compchem.method` should be set to "Wavefunction".

| Group           | Data Field                        | Type | Definition                             | Constraints | Units | Example                                 |
|:----------------|:----------------------------------|:-----|:---------------------------------------|:------------|:------|:----------------------------------------|
| `_wavefunction` | `exchange_correlation_functional` | char | Specifies the name of functional used. | Free Text   |       | - "HF"<br/>- "MP2"<br/>- "CC"<br/>- ... |
| `_wavefunction` | `basis_set_type`                  | char | Defines the type of basis used.        | Free Text   |       | - "GTH"<br/>- "NAO"<br/>- ...           |

### 4.6 ML Potentials

Category `_ml_potential.[]`:  Subgroup for Computational Chemistry methods that use machine learning potentials methods.
For these fields to be used, the `_compchem.method` should be set to "ML Potentials".

| Group           | Data Field             | Type | Definition                                                                                                                                       | Constraints | Units | Example                            |
|:----------------|:-----------------------|:-----|:-------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:------|:-----------------------------------|
| `_ml_potential` | `method`               | char | Specifies the name of the ML Potential used. In the case of ML parameterisation of classical forcefields, refer to the Forcefields dictionaries. |             |       | - "ANI"<br/>- "MACE"<br/>- "UMA"   |
| `_ml_potential` | `model`                | char | The specific model used to rank structures.                                                                                                      |             |       | - "2x"<br/>- "OFF24"<br/>- "m-1p1" |
| `_ml_potential` | `precision`            | char | Float precision in calculations.                                                                                                                 |             |       | - `float32`<br/>- `float64`        |
| `_ml_potential` | `training_set`         | char | Dataset used for the training of the ML potential.                                                                                               | Free Text   |       |                                    |
| `_ml_potential` | `training_set_method`  | char | Either a short description of the methods used to obtain ground values (`PBE`) or a datablock ID describing the method in detail.                | Free Text   |       |                                    |
| `_ml_potential` | `number_of_parameters` | char | Number of model parameters.                                                                                                                      | Free Text   |       |                                    |

### 4.7 Free Energy

Category `_free_energy.[]`:  Subgroup for Computational Chemistry methods that use free energy methods.

| Group          | Data Field              | Type       | Definition                                                                     | Constraints | Units | Example                                    |
|:---------------|:------------------------|:-----------|:-------------------------------------------------------------------------------|:------------|:------|:-------------------------------------------|
| `_free_energy` | `method`                | char       | Specifies the name of the approach used to calculate free energies.            | Free Text   |       | - "HA"<br/>- "QHA"<br/>- "PSCP"<br/>- "EC" |
| `_free_energy` | `reference_temperature` | List[numb] | The temperature or list of temperatures at which free energies are calculated. | \>0.        | K     | `[ 100.0 200.0 300.0 ]`                    |
| `_free_energy` | `reference_pressure`    | List[numb] | The pressure or list of pressures at which free energies are calculated.       | \>0.        | Pa    | `[ 100000.0 200000.0 ]`                    |

### Examples

pDFT with hybrid XC functional and additional data fields taken from the TCOD DFT dictionary:

```text
# Datablock Details
_csp_data_block.class       "Ranking Method"
_csp_data_block.id          fe97f09e-5c9c-41b2-930e-bd14f3a418a9
_csp_data_block.description pbe_xdm

# pDFT settings
_compchem.calculation_type               "Single-Point"

_dft.exchange_correlation_functional_type GGA
_dft.exchange_correlation_functional_name PBE
_dft.pseudopotential_type                 PAW
_dft.dispersion_correction                XDM

_dft.kinetic_energy_cutoff_wavefunctions 600
_dft.BZ_integration.method               "Monkhorst-Pack"
_dft.BZ_integration.grid_dens_X          0.5
_dft.BZ_integration.grid_dens_Y          0.5
_dft.BZ_integration.grid_dens_Z          0.5
```

Multiple energy evaluation steps and different workflows can be described in a cif file. After specifying parameters for
each ranking method, two possible workflow examples are described:

* **wf1**: Different methods of increasing computational cost are used. Two single-point hybrid functionals are then
  used on the PBE optimised structures.
* **wf2**: Different methods of increasing computational cost are used. The last step is a free energy calculation.

```text
#
# Structure Ranking Methods
#

# General Purpose FF
data_gaff
    # Data blocks details
    _csp_data_block.class           "Ranking Method"
    _csp_data_block.description     gaff
    _csp_data_block.id              83f824d3-6d17-4e42-9952-31ed161ef811
    
    # Forcefield details
    _compchem.method                "Forcefield"
    _compchem.calculation_type      "Optimisation"
    _forcefield.name                "GAFF"
    _forcefield.intramolecular_term "Bonded-Parameters"
    _forcefield.electrostatic_term  "Point-Charges"
    _forcefield.vdw_term            "LJ(epsilon,sigma)"
    
    loop_
        _forcefield_parameterisation.term
        _forcefield_parameterisation.description        
        _forcefield_parameterisation.method 
        intra         "Transferable parameters based on atom types" "GAFF"
        electrostatic "Fitting to gas-phase semi-empirical data"    "AM1/BCC"
        vdw           "Transferable parameters based on atom types" "AMBER"
    
    # Geometry Optimisation
    _compchem_geometry_optimisation.algorithm               steep             
    _compchem_geometry_optimisation.cell                    fixed                   
    _compchem_geometry_optimisation.atoms                   all                 
    _compchem_geometry_optimisation.relax_force_convergence 0.01
    _compchem_geometry_optimisation.max_steps               10000             


# Multipoles-based Approach
data_psi_mol
    # Data blocks details
    _csp_data_block.class           "Ranking Method"
    _csp_data_block.description     psi_mol
    _csp_data_block.id              d6f196c5-88d9-4ecd-b388-bcd92fd93a05
    
    # Forcefield details
    _compchem.method                "Forcefield"
    _compchem.calculation_type      "Optimisation"
    _forcefield.name                "Psi_mol"
    _forcefield.intramolecular_term "Isolated Molecule Energy"
    _forcefield.electrostatic_term  "Multipoles"
    _forcefield.vdw_term            "Buckingham"
    loop_
        _forcefield_parameterisation.term
        _forcefield_parameterisation.description        
        _forcefield_parameterisation.method
        intra         "Gas-phase QM calculations"                   "PBE0/6-31G(d,p)"
        electrostatic "GDMA Analysis"                               "PBE0/aug-cc-pVDZ"
        vdw           "Transferable parameters based on atom types" "FIT"

    # Geometry Optimisation
    _compchem_geometry_optimisation.algorithm               CG             
    _compchem_geometry_optimisation.cell                    anisotropic                   
    _compchem_geometry_optimisation.atoms                   all                 
    _compchem_geometry_optimisation.relax_force_convergence 0.01
    _compchem_geometry_optimisation.max_steps               200             


# GGA DFT
data_pbe
    _csp_data_block.class                     "Ranking Method"
    _csp_data_block.description               pbe
    _csp_data_block.id                        17ad684a-2337-4a96-9808-b8b8d3013dc3
    
    # DFT details
    _compchem.method                          "pDFT"
    _compchem.calculation_type                "Optimisation"
    _dft.exchange_correlation_functional_type "GGA"
    _dft.exchange_correlation_functional_name "PBE"
    
    # Geometry Optimisation
    _compchem_geometry_optimisation.algorithm               FIRE             
    _compchem_geometry_optimisation.cell                    anisotropic                   
    _compchem_geometry_optimisation.atoms                   all                 
    _compchem_geometry_optimisation.relax_force_convergence 0.01
    _compchem_geometry_optimisation.max_steps               50 
    
# Hybrid DFT
data_pbe0
    # Data blocks details
    _csp_data_block.class                     "Ranking Method"
    _csp_data_block.description               pbe0
    _csp_data_block.id                        a741eea0-d308-436a-916f-31964b86b649
    
    # DFT details
    _compchem.method                          "pDFT"
    _compchem.calculation_type                "Single-Point"
    _dft.exchange_correlation_functional_type "Hybrid"
    _dft.exchange_correlation_functional_name "PBE0"
    _dft.dispersion_correction                "TS"

data_optb88
    # Data blocks details
    _csp_data_block.class                     "Ranking Method"
    _csp_data_block.description               optb88
    _csp_data_block.id                        2ba152e5-4690-4af4-be55-68789b38b166

    # DFT details
    _compchem.method                          "pDFT"
    _compchem.calculation_type                "Single-Point"
    _dft.exchange_correlation_functional_type "Hybrid"
    _dft.exchange_correlation_functional_name "optb88"
    _dft.dispersion_correction                "TS"

# Free Energy
data_pbe0_qha
    # Data blocks details
    _csp_data_block.class                     "Ranking Method"
    _csp_data_block.description               "pbe0_mbd_qha"
    _csp_data_block.id                        2b9deed1-116f-454a-922e-be61c8d946c5

    # Energy Method Details
    _compchem.method                                        "pDFT"
    _dft.exchange_correlation_functional_type               "Hybrid"
    _dft.exchange_correlation_functional_name               "PBE0"
    _dft.pseudopotential_type                               "PAW"
    _dft.dispersion_correction                              "MBD"

    _dft.kinetic_energy_cutoff_wavefunctions                600
    _dft.BZ_integration_method                              "Monkhorst-Pack"
    _dft.BZ_integration_grid_dens_X                         0.5
    _dft.BZ_integration_grid_dens_Y                         0.5
    _dft.BZ_integration_grid_dens_Z                         0.5

    # Free Energy Calculation Details
    _compchem.calculation_type                "Dynamic Ensemble"
    _free_energy.method                       "QHA"
    _free_energy.reference_temperature        [100 200 300]
    _free_energy.reference_pressure           100000.0

#
# Workflows
#

data_workflow_1
    _csp_data_block.class       Workflow
    _csp_data_block.description wf1
    _csp_data_block.id          29ba6f2f-0a56-47be-bc90-9c8adc7760e9

    # Structure Generation Methods
    ...

    # Structure Ranking Methods
    loop_
        _csp_structure_ranking.stage
        _csp_structure_ranking.preceding_stage
        _csp_structure_ranking.data_block_label
        _csp_structure_ranking.data_block_description
        _csp_structure_ranking.data_block_id
        0 . "gaff"    "Optimisation with Forcefield" 83f824d3-6d17-4e42-9952-31ed161ef811
        1 0 "psi_mol" "Optimisation with Forcefield" d6f196c5-88d9-4ecd-b388-bcd92fd93a05
        2 1 "pbe"     "Optimisation with pDFT"       17ad684a-2337-4a96-9808-b8b8d3013dc3
        3 2 "pbe0"    "Single-Point with pDFT"       a741eea0-d308-436a-916f-31964b86b649
        4 2 "optb88"  "Single-Point with pDFT"       2ba152e5-4690-4af4-be55-68789b38b166

data_workflow_2
    _csp_data_block.class       Workflow
    _csp_data_block.description wf2
    _csp_data_block.id          964fcd15-82e1-4c4d-a7cb-61b0b34c3421

    # Structure Generation Methods
    ...

    # Structure Ranking Methods
    loop_
        _csp.structure_ranking_stage
        _csp.structure_ranking_preceding_stage
        _csp.structure_ranking_data_block_label
        _csp.structure_ranking_data_block_description
        _csp.structure_ranking_data_block_id
        0 . "gaff"     "Optimisation with Forcefield" 83f824d3-6d17-4e42-9952-31ed161ef811
        1 0 "psi_mol"  "Optimisation with Forcefield" d6f196c5-88d9-4ecd-b388-bcd92fd93a05
        2 1 "pbe0_qha" "Dynamic Ensemble with pDFT"   00d2779e-6396-4c2c-91ff-d62dddaf9cc1
```

Also in this example, mandatory data fields in the loop are `_csp.structure_ranking_stage`,
`_csp.structure_ranking_preceding_stage` and `_csp.structure_ranking_data_block_id`. Additional data fields are for
improving the human-readability of the CIF file.

## 5. Output Structure Properties

### 5.1 Theoretical Structure

Describes the structure-specific outputs of CSP methods. Categories:

* **`_theoretical_structure.[]`**: Properties of the structure.
* **`_theoretical_structure.csp_[]`**: Stage identifiers in a multistep ranking approach.

| Group                               | Data Field                                 | Type       | Definition                                                                                                                                    | Constraints                                                         | Units                               | Example  |
|-------------------------------------|--------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------|----------|
| `_theoretical_structure`            | `temperature`                              | numb       | The temperature at which the energy and other properties of the theoretical structure were calculated.                                        | \>=0.                                                               | K                                   | 298.15   |
| `_theoretical_structure`            | `pressure`                                 | numb       | The pressure at which the energy and other properties of the theoretical structure were calculated.                                           |                                                                     | Pa                                  | 101325.0 |
| `_theoretical_structure`            | `reference_temperature`                    | numb       | In the case of free-energy calculations, specify the reference temperature.                                                                   | \>=0.                                                               | K                                   |          |
| `_theoretical_structure`            | `reference_pressure`                       | numb       | In the case of free-energy calculations, specify the reference pressure.                                                                      | \>=0.                                                               | Pa                                  |          |
| `_theoretical_structure`            | `calculated_density`                       | numb       | The calculated density of the crystal.                                                                                                        | \>=0.                                                               | kg m<sup>-3</sup>                   | 1420.0   |
| `_theoretical_structure`            | `total_energy`                             | numb       | The total energy of the theoretical structure, i.e. energy relative to all of the nuclei and electrons separated to an infinite distance.     |                                                                     | kJ mol<sup>-1</sup>                 | -1500.5  |
| `_theoretical_structure`            | `absolute_lattice_energy`                  | numb       | The absolute lattice energy of the crystal, i.e. energy relative to all the molecules separated to an infinite distance.                      |                                                                     | kJ mol<sup>-1</sup>                 | -1600.8  |
| `_theoretical_structure`            | `absolute_free_energy`                     | numb       | The absolute free energy of the crystal.                                                                                                      |                                                                     | kJ mol<sup>-1</sup>                 | -1450.2  |
| `_theoretical_structure`            | `free_energy_correction`                   | numb       | The correction applied to the lattice energy to obtain the free energy, accounting for vibrational and other thermal effects.                 |                                                                     | kJ mol<sup>-1</sup>                 | 50.6     |
| `_theoretical_structure`            | `relative_lattice_energy`                  | numb       | The lattice energy of the theoretical structure relative to the lowest energy structure found in the CSP.                                     | \>=0.                                                               | kJ mol<sup>-1</sup>                 | 8.7      |
| `_theoretical_structure`            | `relative_free_energy`                     | numb       | The free energy of the theoretical structure relative to the lowest energy structure found in the CSP.                                        | \>=0.                                                               | kJ mol<sup>-1</sup>                 | 2.3      |
| `_theoretical_structure`            | `zero_point_energy_correction`             | numb       | The ZPE correction included in the energy value.                                                                                              | \>=0.                                                               | kJ mol<sup>-1</sup>                 | 0.5      |
| `_theoretical_structure`            | `dispersion_energy_correction`             | numb       | The dispersion energy correction included in the energy value.                                                                                |                                                                     | kJ mol<sup>-1</sup>                 | -4.6     |
| `_theoretical_structure`            | `formation_energy`                         | numb       | In convex hull phase diagram, it indicates the energy of formation (or mixing energy).                                                        |                                                                     | kJ mol<sup>-1</sup>                 | -60.6    |
| `_theoretical_structure`            | `decomposition_energy`                     | numb       | In convex hull phase diagram, it indicates the decomposition energy.                                                                          |                                                                     | kJ mol<sup>-1</sup>                 | -2.5     |
| `_theoretical_structure`            | `energy_above_hull`                        | numb       | In convex hull phase diagram, it indicates the energy energy above the convex hull.                                                           | \>=0.                                                               | kJ mol<sup>-1</sup>                 | 6.0      |
| `_theoretical_structure`            | `energy_uncertainty`                       | numb       | An estimate of the uncertainty associated with the calculated energy of the theoretical structure.                                            | \>=0.                                                               | kJ mol<sup>-1</sup>                 | 2.0      |
| `_theoretical_structure`            | `score`                                    | numb       | To allow for methods that may rank by criteria other than energies (e.g., based on stability or other desired properties).                    |                                                                     | unspecified                         | 0.3333   |
| `_theoretical_structure`            | `rank`                                     | numb       | The rank of the structure when ordered by chosen criteria where 1 is considered to be the most favorable or likely structure.                 | \>=1                                                                |                                     | 1        |
| `_theoretical_structure`            | `cluster_centre_id`                        | char       | If the structure has been identified as duplicate in a group, the uniqueidentifier of the structure that is the cluster centre of that group. | Free Text                                                           |                                     |          |
| `_theoretical_structure`            | `cluster_centre_description`               | char       | If the structure has been identified as duplicate in a group, the label of the structure that is the cluster centre of that group.            | Free Text                                                           |                                     |          |
| `_theoretical_structure`            | `experimental_match_id`                    | char       | If the theoretical structure matches an experimental structure, specify the (possibly unique) identifier of the latter.                       | Free Text                                                           |                                     |          |
| `_theoretical_structure`            | `experimental_match_database`              | char       | If the theoretical structure matches an experimental structure, specify the database or location the latter.                                  | Free Text                                                           |                                     |          |
| `_theoretical_structure`            | `experimental_match_description`           | char       | If the theoretical structure matches an experimental structure, this data field allows to include any additional information.                 | Free Text                                                           |                                     |          |
| `_theoretical_structure`            | `stress_tensor`                            | Mat[numb]  | A 3x3 stress tensor.                                                                                                                          | \>=0.                                                               | Pa                                  |          |
| `_theoretical_structure_atom`       | `force_x`                                  | numb       | Cartesian component of the forces acting on atoms along the x-axis.                                                                           |                                                                     | kJ mol<sup>-1</sup> nm<sup>-1</sup> |          |
| `_theoretical_structure_atom`       | `force_y`                                  | numb       | Cartesian component of the forces acting on atoms along the y-axis.                                                                           |                                                                     | kJ mol<sup>-1</sup> nm<sup>-1</sup> |          |
| `_theoretical_structure_atom`       | `force_z`                                  | numb       | Cartesian component of the forces acting on atoms along the z-axis.                                                                           |                                                                     | kJ mol<sup>-1</sup> nm<sup>-1</sup> |          |
| `_theoretical_structure_atom`       | `hessian`                                  | Mat[numb]  | A 3x3 per-atom Hessian matrix.                                                                                                                |                                                                     | kJ mol<sup>-1</sup> nm<sup>-2</sup> |          |
| `_theoretical_structure_atom`       | `charge`                                   | numb       | Per-atom partial charge.                                                                                                                      |                                                                     | e                                   |          |
| `_theoretical_structure_property`   | `bandgap`                                  | numb       | The energy difference between the valence band maximum and the conduction band minimum.                                                       |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_property`   | `bandgap_is_direct`                        | bool       | Indicates whether the valence band maximum and conduction band minimum occur at the same k-point in reciprocal space.                         |                                                                     |                                     |          |
| `_theoretical_structure_property`   | `fermi_energy`                             | numb       | The Fermi energy of the theoretical structure.                                                                                                |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_property`   | `valence_band_maximum_energy`              | numb       | The energy of the highest occupied electronic state in the valence band.                                                                      |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_property`   | `conduction_band_minimum_energy`           | numb       | The energy of the lowest unoccupied electronic state in the conduction band.                                                                  |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_property`   | `electron_effective_mass`                  | numb       | The effective mass of electrons.                                                                                                              |                                                                     | m<sub>e</sub>                       |          |
| `_theoretical_structure_property`   | `hole_effective_mass`                      | numb       | The effective mass of holes.                                                                                                                  |                                                                     | m<sub>e</sub>                       |          |
| `_theoretical_structure_property`   | `total_magnetic_moment`                    | numb       | The total magnetic moment of the structure.                                                                                                   |                                                                     | &mu;B                               |          |
| `_theoretical_structure_property`   | `magnetic_ordering`                        | char       | The magnetic ordering state of the structure: ferromagnetic, antiferromagnetic, ferrimagnetic, non-magnetic, etc.                             |                                                                     |                                     |          |
| `_theoretical_structure_property`   | `magnetic_anisotropy_energy`               | numb       | The energy difference associated with aligning the magnetisation along different crystallographic directions.                                 |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_property`   | `elastic_tensor`                           | Mat[numb]  | The 6x6 matrix of the independent components of the stiffness tensor.                                                                         |                                                                     | Pa                                  |          |
| `_theoretical_structure_property`   | `bulk_modulus`                             | numb       | A measure of the resistance of the structure to uniform compression.                                                                          |                                                                     | Pa                                  |          |
| `_theoretical_structure_property`   | `shear_modulus`                            | numb       | A measure of the resistance of the structure to shear deformation.                                                                            |                                                                     | Pa                                  |          |
| `_theoretical_structure_property`   | `young_modulus`                            | numb       | The ratio of uniaxial stress to uniaxial strain describing the stiffness of the material.                                                     |                                                                     | Pa                                  |          |
| `_theoretical_structure_property`   | `poisson_ratio`                            | numb       | The ratio of transverse strain to axial strain under uniaxial loading.                                                                        |                                                                     |                                     |          |
| `_theoretical_structure_property`   | `constant_volume_heat_capacity`            | numb       | The heat capacity arising from lattice vibrations under conditions of constant volume.                                                        |                                                                     | J mol<sup>-1</sup> K<sup>-1</sup>   |          |
| `_theoretical_structure_property`   | `constant_pressure_heat_capacity`          | numb       | The heat capacity arising from lattice vibrations under conditions of constant pressure.                                                      |                                                                     | J mol<sup>-1</sup> K<sup>-1</sup>   |          |
| `_theoretical_structure_property`   | `thermal_expansion_tensor`                 | Mat[numb]  | The 3x3 matrix with thermal expansion coefficients.                                                                                           |                                                                     | K<sup>-1</sup>                      |          |
| `_theoretical_structure_property`   | `electrical_conductivity_tensor`           | Mat[numb]  | The 3x3 matrix with electrical conductivity coefficients.                                                                                     |                                                                     | S m<sup>-1</sup>                    |          |
| `_theoretical_structure_property`   | `seebeck_coefficient_tensor`               | Mat[numb]  | The 3x3 matrix with Seebeck coefficients.                                                                                                     |                                                                     | V K<sup>-1</sup>                    |          |
| `_theoretical_structure_property`   | `electronic_thermal_conductivity_tensor`   | Mat[numb]  | The 3x3 matrix with electronic thermal conductivity coefficients.                                                                             |                                                                     | W  m<sup>-1</sup> K<sup>-1</sup>    |          |
| `_theoretical_structure_property`   | `lattice_thermal_conductivity_tensor`      | Mat[numb]  | The 3x3 matrix with lattice thermal conductivity coefficients.                                                                                |                                                                     | W  m<sup>-1</sup> K<sup>-1</sup>    |          |
| `_theoretical_structure_band`       | `kpoint_id`                                | char       | To be used in a loop, optional label ("gamma", X, L, K, etc.) of the kpoint.                                                                  |                                                                     |                                     |          |
| `_theoretical_structure_band`       | `kpoint_coord`                             | List[numb] | To be used in a loop, fractional reciprocal-space coordinates of the kpoint.                                                                  |                                                                     |                                     |          |
| `_theoretical_structure_band`       | `spin_component`                           | char       | To be used in a loop, the spin component ("up" or "down").                                                                                    | - "up": "The spin up component" - "down": "The spin down component" |                                     |          |
| `_theoretical_structure_band`       | `eigenvalues`                              | List[numb] | To be used in a loop, Band energies at the specified kpoint.                                                                                  |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_dos`        | `energy`                                   | numb       | To be used in a loop, the energy value for a DOS analysis                                                                                     |                                                                     | kJ mol<sup>-1</sup>                 |          |
| `_theoretical_structure_dos`        | `density`                                  | numb       | To be used in a loop, the density of states at the specified energy.                                                                          |                                                                     |                                     |          |
| `_theoretical_structure_dos`        | `spin_component`                           | char       | To be used in a loop, the spin component ("up" or "down").                                                                                    | - "up": "The spin up component" - "down": "The spin down component" |                                     |          |
| `_theoretical_structure_phonon`     | `qpoint_id`                                | char       | To be used in a loop, optional label ("gamma", X, L, K, etc.) of the qpoint.                                                                  |                                                                     |                                     |          |
| `_theoretical_structure_phonon`     | `qpoint_coord`                             | List[numb] | To be used in a loop, fractional reciprocal-space coordinates of the qpoint.                                                                  |                                                                     |                                     |          |
| `_theoretical_structure_phonon`     | `frequencies`                              | List[numb] | To be used in a loop, phonon frequencies of all branches at the specified q-point.                                                            |                                                                     | cm<sup>-1</sup>                     |          |
| `_theoretical_structure_phonon_dos` | `frequency`                                | numb       | To be used in a loop, the frequency value for a phonon DOS analysis.                                                                          |                                                                     | cm<sup>-1</sup>                     |          |
| `_theoretical_structure_phonon_dos` | `density`                                  | numb       | To be used in a loop, the density of states at the specified frequency.                                                                       |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_input_system_description`             | char       | Human-readable description of the input system data block.                                                                                    |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_input_system_id`                      | char       | Identifier of the input system data block.                                                                                                    |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_workflow_description`                 | char       | Human-readable description of the workflow data block.                                                                                        |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_workflow_id`                          | char       | Identifier of the workflow data block.                                                                                                        |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_generation_stage_description`         | char       | Human-readable description of the structure generation method data block.                                                                     |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_generation_stage_id`                  | char       | Identifier of the structure generation method data block.                                                                                     |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_ranking_stage_description`            | char       | Human-readable description of the structure ranking method data block.                                                                        |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_ranking_stage_id`                     | char       | Identifier of the structure ranking method data block.                                                                                        |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_step_description`                     | char       | Human-readable description of the intermediate step (e.g. a clustering algorithm) data block that was applied to this structure.              |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_step_id`                              | char       | Identifier of the intermediate step data block that was applied to this structure.                                                            |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_previous_stage_structure_description` | char       | Human-readable description of the data block of the structure from previous stage. This is the structure used as input for the current stage. |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_previous_stage_structure_id`          | char       | Identifier of the data block of the structure from previous stage.                                                                            |                                                                     |                                     |          |
| `_theoretical_structure`            | `csp_initial_spacegroup_number`            | char       | The spacegroup of the structure at the initial CSP stage, before any geometry optimisation.                                                   | 1-232                                                               |                                     | 14       |

Details on composition, unit cell, symmetry, and atomic coordinates can be specified through the CIF Core dictionary.

#### Examples

Structure optimised using a multipoles approach:

```text
data_structure_1_1
# Structure is theoretically generated                                                  
_exptl.method                                                      'theoretical model'  

# Datablock Details
_csp_data_block.class                                              "Theoretical Structure"
_csp_data_block.description                                        structure_1_1
_csp_data_block.id                                                 00d2779e-6396-4c2c-91ff-d62dddaf9cc1

# Include files specifying input, methods and workflow data blocks
_csp_data_block.additional_files                                   [ "csp_input.cif" "workflow.cif" ]

# Stage identifiers
_theoretical_structure.csp_input_system_description                Urea_Hydrate
_theoretical_structure.csp_input_system_id                         2a2611e3-2021-4b03-a7c6-0ef71239008f

_theoretical_structure.csp_workflow_description                    wf2
_theoretical_structure.csp_workflow_id                             964fcd15-82e1-4c4d-a7cb-61b0b34c3421

_theoretical_structure.csp_generation_stage_description            ea
_theoretical_structure.csp_generation_stage_id                     af534fed-8153-4af2-bd9f-29b0fef8d805

_theoretical_structure.csp_ranking_stage_description               psi_mol
_theoretical_structure.csp_ranking_stage_id                        d6f196c5-88d9-4ecd-b388-bcd92fd93a05

# Properties
_theoretical_structure.temperature             0
_theoretical_structure.relative_lattice_energy 1.5
_theoretical_structure.rank                    5 

# Crystal
_symmetry.cell_setting           monoclinic
_symmetry.space_group_name_H-M   'P 21/c'
_symmetry.Int_Tables_number      14
_space_group_name_Hall           '-P 2ybc'
loop_
_symmetry.equiv_pos_site_id
_symmetry.equiv_pos_as_xyz
1 x,y,z
2 -x,1/2+y,1/2-z
3 -x,-y,-z
4 x,1/2-y,1/2+z
_cell.length_a                   16.8168
_cell.length_b                   7.0178
_cell.length_c                   14.5475
_cell.angle_alpha                90
_cell.angle_beta                 115.28
_cell.angle_gamma                90
_cell.volume                     1552.44
loop_
_atom_site.label
_atom_site.type_symbol
_atom_site.fract_x
_atom_site.fract_y
_atom_site.fract_z
C0  C  0.402802  0.483043 0.842739
C1  C  0.387973  0.677363 0.792505
H2  H  0.372266  0.370900 0.785899
C3  C  0.290934  0.723546 0.722019
C4  C  0.299744  0.784092 0.627602
O5  O  0.430454  0.669327 0.717154
N6  N  0.375029  0.749323 0.626530
C7  C  0.433253  0.840791 0.865082
H8  H  0.373059  0.480692 0.896797
H9  H  0.473281  0.453133 0.883342
H10 H  0.406023  0.852375 0.921481
H11 H  0.422667  0.976203 0.823613
H12 H  0.504341  0.815441 0.904886
H13 H  0.247676  0.598250 0.706716
H14 H  0.264985  0.835703 0.754024
S15 S  0.217342  0.894753 0.520420
O16 O  0.132826  0.836886 0.515882
O17 O  0.235781  0.880775 0.432108
C18 C  0.229140  1.158880 0.556705
F19 F  0.218005  1.168970 0.646067
F20 F  0.314654  1.210640 0.581184
C21 C  0.161031  1.270540 0.472953
C22 C  0.174831  1.346830 0.391627
C23 C  0.075521  1.280400 0.468012
C24 C  0.007484  1.364770 0.384876
F25 F  0.256854  1.339740 0.393375
C26 C  0.107309  1.429290 0.307776
C27 C  0.023141  1.436700 0.304553
H28 H -0.030676  1.496570 0.238225
H29 H -0.058002  1.370540 0.382481
H30 H  0.062589  1.219340 0.529056
H31 H  0.120713  1.485310 0.246093
```

Structures at different temperature conditions generated from the same structure in the previous stage:

```text
#
# Structure at 100K
#
data_structure_1_2_0
# Structure is theoretically generated                                                  
_exptl.method                                                      'theoretical model'  

# Datablock Details
_csp_data_block.class                                              "Theoretical Structure"             
_csp_data_block.description                                        structure_1_2_0                   
_csp_data_block.id                                                 56cfac30-680a-4821-b29a-28c5991beba9

# Include files specifying input, methods and workflow data blocks
_csp_data_block.additional_files                                   [ "csp_input.cif" "workflow.cif" ]

# Stage identifiers
_theoretical_structure.csp_input_system_description                Urea_Hydrate                        
_theoretical_structure.csp_input_system_id                         2a2611e3-2021-4b03-a7c6-0ef71239008f
                                    
_theoretical_structure.csp_workflow_description                    wf2                                 
_theoretical_structure.csp_workflow_id                             964fcd15-82e1-4c4d-a7cb-61b0b34c3421
                                    
_theoretical_structure.csp_generation_stage_description            ea                                  
_theoretical_structure.csp_generation_stage_id                     af534fed-8153-4af2-bd9f-29b0fef8d805
                                    
_theoretical_structure.csp_ranking_stage_description               pbe0_qha                            
_theoretical_structure.csp_ranking_stage_id                        11d2779e-6396-4c2c-91ff-d62dddaf9cc1

_theoretical_structure.reference_temperature                       100.0    
_theoretical_structure.reference_pressure                          100000.0 

_theoretical_structure.csp_previous_stage_structure_description    structure_1_1                        
_theoretical_structure.csp_previous_stage_structure_id             00d2779e-6396-4c2c-91ff-d62dddaf9cc1 

# Crystal properties and details
...

#
# Structure at 200K
#
data_structure_1_2_1
# Structure is theoretically generated
_exptl.method                                                      'theoretical model'

# Datablock Details
_csp_data_block.class                                              "Theoretical Structure"             
_csp_data_block.description                                        structure_1_2_1                     
_csp_data_block.id                                                 28775053-e8fb-4e2b-bdb7-0ae255a422ef

# Include files specifying input, methods and workflow data blocks
_csp_data_block.additional_files                                   [ "csp_input.cif" "workflow.cif" ]

# Stage identifiers
_theoretical_structure.csp_input_system_description                Urea_Hydrate                        
_theoretical_structure.csp_input_system_id                         2a2611e3-2021-4b03-a7c6-0ef71239008f
                                    
_theoretical_structure.csp_workflow_description                    wf2                                 
_theoretical_structure.csp_workflow_id                             964fcd15-82e1-4c4d-a7cb-61b0b34c3421
                                    
_theoretical_structure.csp_generation_stage_description            ea                                  
_theoretical_structure.csp_generation_stage_id                     af534fed-8153-4af2-bd9f-29b0fef8d805
                                    
_theoretical_structure.csp_ranking_stage_description               pbe0_qha                            
_theoretical_structure.csp_ranking_stage_id                        11d2779e-6396-4c2c-91ff-d62dddaf9cc1

_theoretical_structure.reference_temperature                       200.0    
_theoretical_structure.reference_pressure                          100000.0 

_theoretical_structure.csp_previous_stage_structure_description    structure_1_1                        
_theoretical_structure.csp_previous_stage_structure_id             00d2779e-6396-4c2c-91ff-d62dddaf9cc1 

# Crystal properties and details
...


#
# Structure at 300K
#
data_structure_1_2_2
# Structure is theoretically generated
_exptl.method                                                      'theoretical model'

# Datablock Details
_csp_data_block.class                                              "Theoretical Structure"             
_csp_data_block.description                                        structure_1_2_2                     
_csp_data_block.id                                                 28775053-e8fb-4e2b-bdb7-0ae255a422ef

# Include files specifying input, methods and workflow data blocks
_csp_data_block.additional_files                                   [ "csp_input.cif" "workflow.cif" ]

# Stage identifiers
_theoretical_structure.csp_input_system_description                Urea_Hydrate                        
_theoretical_structure.csp_input_system_id                         2a2611e3-2021-4b03-a7c6-0ef71239008f
                                    
_theoretical_structure.csp_workflow_description                    wf2                                 
_theoretical_structure.csp_workflow_id                             964fcd15-82e1-4c4d-a7cb-61b0b34c3421
                                    
_theoretical_structure.csp_generation_stage_description            ea                                  
_theoretical_structure.csp_generation_stage_id                     af534fed-8153-4af2-bd9f-29b0fef8d805
                                    
_theoretical_structure.csp_ranking_stage_description               pbe0_qha                            
_theoretical_structure.csp_ranking_stage_id                        11d2779e-6396-4c2c-91ff-d62dddaf9cc1

_theoretical_structure.reference_temperature                       300.0    
_theoretical_structure.reference_pressure                          100000.0 

_theoretical_structure.csp_previous_stage_structure_description    structure_1_1                        
_theoretical_structure.csp_previous_stage_structure_id             00d2779e-6396-4c2c-91ff-d62dddaf9cc1 

# Crystal properties and details
...

```

### 5.2 General Output

Describes the general outputs of CSP methods.          
Categories:

* **`_csp.output_[]`**: Properties of the structure.

| Group         | Data Field                        | Type | Definition                                                                           | Constraints | Units          | Example |
|---------------|-----------------------------------|------|--------------------------------------------------------------------------------------|-------------|----------------|---------|
| `_csp`        | `output_input_system_description` | char | Human-readable description of the input system data block.                           | Free Text   |                |         |
| `_csp`        | `output_input_system_id`          | char | Identifier of the input system data block.                                           |             |                |         |
| `_csp`        | `output_workflow_description`     | char | Human-readable description of the workflow data block.                               | Free Text   |                |         |
| `_csp`        | `output_workflow_id`              | char | Identifier of the workflow data block.                                               |             |                |         |
| `_csp`        | `total_computational_cost`        | numb | Sum of the computational costs of all stages.                                        | \>=0.       | CPU-Core Hours | 50000.0 |
| `_csp`        | `hardware_description`            | char | Description of the hardware used to perform calculations.                            | Free Text   |                |         |
| `_csp_output` | `stage`                           | char | Human-readable description of the structure generation or ranking method data block. | Free Text   |                |         |
| `_csp_output` | `stage_id`                        | char | Identifier of the structure generation or ranking method data block.                 |             |                |         |
| `_csp_output` | `global_minima`                   | char | Human-readable label of the structure data block.                                    | Free Text   |                |         |
| `_csp_output` | `global_minima_id`                | char | Identifier of the structure data block.                                              |             |                |         |
| `_csp_output` | `number_of_structures`            | numb | Number of structures generated, optimised or evaluated in a single stage.            | \>=1        |                | 10000   |
| `_csp_output` | `stage_computational_cost`        | numb | The computational costs of a single stage.                                           | \>=0.       | CPU-Core Hours | 50000.0 |
| `_csp_output` | `average_computational_cost`      | numb | Average computational cost per structure in a single stage.                          | \>=0.       | CPU-Core Hours | 2.0     |

#### Examples

```text
data_csp_output

# Datablock Details
_csp_data_block.class                 "Output"             
_csp_data_block.description           csp_output                   
_csp_data_block.id                    1d327ab0-3f84-4794-88a8-3c14b8f09999
_csp_data_block.additional_files      [ "csp_input.cif" "workflow.cif" "structure_1.cif" "structure_105.cif"]

# Input and workflow identifiers
_csp.output_input_system_description  Urea_Hydrate                        
_csp.output_input_system_id           2a2611e3-2021-4b03-a7c6-0ef71239008f
                                    
_csp.output_workflow_description      wf2                                 
_csp.output_workflow_id               964fcd15-82e1-4c4d-a7cb-61b0b34c3421

# Output Details and Computational Cost
_csp.output_hardware_description      "AMD Zen 2 EPYC 7H12"
_csp.output_total_computational_cost  185101.0

loop_
    _csp_output.stage 
    _csp_output.stage_id
    _csp_output.stage_computational_cost
    _csp_output.number_of_structures
    _csp_output.average_computational_cost
    _csp_output.global_minima
    _csp_output.global_minima_id
    # Generation Methods
    "rs"      6e0147be-0454-44a1-a3bb-de7b326dde1b       1.0     7500  0.00013 . .
    "sa"      95f28b3c-d029-4840-a69a-3ced34219c28     100.0  2000000  0.00050 . .
    # Ranking Methods
    "gaff"    83f824d3-6d17-4e42-9952-31ed161ef811  100000.0  2007500  0.04981 "structure_1_1"   63f70eef-cd02-4f73-b7a3-cda97adfe10e          
    "psi_mol" d6f196c5-88d9-4ecd-b388-bcd92fd93a05   25000.0    50000  0.50000 "structure_105_2" 07457f98-a456-441e-bb36-1e650d799b93  
    "pbe"     17ad684a-2337-4a96-9808-b8b8d3013dc3   60000.0    10000  7.50000 "structure_105_3" 756c1329-73a5-43e2-a359-54b01731ac42 
```

## 6. Intermediate Step

Describes additional steps made in selecting structures or inputs. It covers popular methods used in structure
clustering and conformer generation for organic CSP. It also offers a few flexible data fields to describe structure
selection methods other than energy.

### 6.1 General Fields

Categories:

* `_csp.step_[]`: Category to define intermediate steps.

| Group                | Data Field           | Type | Definition                                                                                                                                                                     | Constraints | Units | Example |
|----------------------|----------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-------|---------|
| `_csp_step`          | `method`             | char | A flexible data field to define non-energy-based approaches to select structures.                                                                                              | Free Text   |       |         |
| `_csp_step`          | `method_description` | char | Description of the method used.                                                                                                                                                | Free Text   |       |         |
| `_csp_step`          | `software`           | char | Software used to perform calculations.                                                                                                                                         | Free Text   |       |         |
| `_csp_step`          | `software_version`   | char | Version of the software.                                                                                                                                                       | Free Text   |       |         |
| `_csp_step_variable` | `label`              | char | To be used in a loop, the parameter label used in the custom method. Missing parameters in clustering and conformers generation methods can be specified with this data filed. | Free Text   |       |         |
| `_csp_step_variable` | `value`              | char | To be used in a loop, the value assigned to the parameter.                                                                                                                     | Free Text   |       |         |

### 6.2 Conformers Generation

Categories:

* `_csp_conformer.[]`: Category to define the method used to generate input molecular conformers.

| Group            | Data Field                        | Type | Definition                                                                             | Constraints | Units               | Example | 
|------------------|-----------------------------------|------|----------------------------------------------------------------------------------------|-------------|---------------------|---------|
| `_csp_conformer` | `generation_method`               | char | The method used to generate conformers for a CSP study of a flexible molecule.         | Free text   |                     |         |
| `_csp_conformer` | `generation_method_description`   | char | Description of the method used to generate conformers.                                 | Free text   |                     |         |
| `_csp_conformer` | `generation_software`             | char | Software used to generate conformers.                                                  | Free text   |                     |         |
| `_csp_conformer` | `generation_software_version`     | char | Version of the software used to generate conformers.                                   | Free text   |                     |         |
| `_csp_conformer` | `optimisation_method`             | char | The method used to geometry optimise generated conformers.                             | Free text   |                     |         |
| `_csp_conformer` | `optimisation_method_description` | char | Description of the method used to geometry optimise generated conformers.              | Free text   |                     |         |
| `_csp_conformer` | `optimisation_software`           | char | Software used to optimise conformers.                                                  | Free text   |                     |         |
| `_csp_conformer` | `optimisation_software_version`   | char | Version of the software used to optimise conformers.                                   | Free text   |                     |         |
| `_csp_conformer` | `energy_cutoff`                   | numb | Energy difference from the global minima to include the conformer as an input for CSP. | \> 0.0      | kJ mol<sup>-1</sup> | 15.0    |
| `_csp_conformer` | `max_number_of_conformers`        | numb | Max number of conformers evaluated                                                     | \> 0        |                     | 25      |
| `_csp_conformer` | `clustering_method`               | char | The method used to cluster generated or optimised conformers.                          | Free text   |                     |         |
| `_csp_conformer` | `clustering_method_description`   | char | Description of the clustering method.                                                  | Free text   |                     |         |
| `_csp_conformer` | `clustering_software`             | char | Software used to clustering conformers.                                                | Free text   |                     |         |
| `_csp_conformer` | `clustering_software_version`     | char | Version of the software used to cluster conformers.                                    | Free text   |                     |         |
| `_csp_conformer` | `clustering_rmsd_cutoff`          | numb | RMSD to consider two molecules as part of the same cluster.                            | \> 0.0      | angstroms           | 0.25    |

### 6.3 Structure Similarity and clustering

Categories:

* `_csp_similarity.[]`: Category to define the method used to cluster CSP-generated structures or compare CSP-generated
  structures with experimental structures.

| Group             | Data Field                             | Type | Definition                                                                                                                                                                                                                                                                                                                | Constraints | Units               | Example                                                    | 
|-------------------|----------------------------------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------|------------------------------------------------------------|
| `_csp_similarity` | `method`                               | char | The method used to cluster generated or optimised structures.                                                                                                                                                                                                                                                             | Free text   |                     |                                                            |
| `_csp_similarity` | `method_description`                   | char | Description of the clustering method.                                                                                                                                                                                                                                                                                     | Free text   |                     |                                                            |
| `_csp_similarity` | `software`                             | char | Software used to clustering structures.                                                                                                                                                                                                                                                                                   | Free text   |                     |                                                            |
| `_csp_similarity` | `software_version`                     | char | Version of the software used to cluster structures.                                                                                                                                                                                                                                                                       | Free text   |                     |                                                            |
| `_csp_similarity` | `distance_cutoff`                      | numb | Upper limit to consider two structures the same. This vary with respect to the method used but it implies that similar structures are close to 0.                                                                                                                                                                         | \> 0.0      | unspecified         | 1.0                                                        |
| `_csp_similarity` | `threshold`                            | numb | Similarity score needed to consider two structures the same. This vary with respect to the method used but it implies that similar structures are close to 1.                                                                                                                                                             | 0.-1.       | unspecified         | 1.0                                                        |
| `_csp_similarity` | `energy_threshold`                     | numb | Maximum allowed energy difference above which two structures are automatically classified as different.                                                                                                                                                                                                                   | \> 0.0      | kJ mol<sup>-1</sup> | 1.0                                                        |
| `_csp_similarity` | `density_threshold`                    | numb | Maximum allowed density difference above which two structures are automatically classified as different.                                                                                                                                                                                                                  | \> 0.0      | kg m<sup>-3</sup>   | 250.0                                                      |
| `_csp_similarity` | `clustering_method`                    | char | The method used to identify clusters from a distance or similarity matrix.                                                                                                                                                                                                                                                | Free Text   |                     | "Hierarchical"                                             |
| `_csp_similarity` | `clustering_method_description`        | char | Description of the clustering method.                                                                                                                                                                                                                                                                                     | Free Text   |                     | "Hierarchical method using a complete linkage approach"    |
| `_csp_similarity` | `cluster_centre_selection`             | char | Define how a cluster centre is selected. The selection could be defined by the clustering method itself (highest "density" point in a density-based clustering algorithm) or defined a posteriori (for example selecting the lowest energy structure in a cluster).                                                       | Free Text   |                     | - "Lowest Energy"<br/>- "First occurrence"                 |
| `_csp_similarity` | `include_hydrogens`                    | bool | It defines if hydrogens are used in calculating the similarity.                                                                                                                                                                                                                                                           |             |                     | False                                                      |
| `_csp_similarity` | `optimise_cell`                        | bool | It defines if the cell of one of two structures is optimised to increase similarity.                                                                                                                                                                                                                                      |             |                     | False                                                      |
| `_csp_similarity` | `molecular_shell_size`                 | numb | For methods based on comparing molecular shells (e.g. COMPACK, CrystalCMP), it defines the size of the molecular shell.                                                                                                                                                                                                   | \> 0        |                     | 30                                                         |
| `_csp_similarity` | `molecular_shell_distance_tolerance`   | numb | For methods based on comparing molecular shells, it defines the maximum difference between reference and target distances as a decimal fraction.                                                                                                                                                                          | 0.-1.       |                     | 0.3                                                        |
| `_csp_similarity` | `molecular_shell_angle_tolerance`      | numb | For methods based on comparing molecular shells, it defines the maximum difference between reference and target angles.                                                                                                                                                                                                   | \> 0.       | degrees             | 30.                                                        |
| `_csp_similarity` | `pxrd_two_theta_minimum`               | numb | For methods based on comparing powder patterns (e.g. De Gelder, PWDF), it defines the minimum 2-theta value.                                                                                                                                                                                                              | \> 0.       | degrees             | 5.                                                         |
| `_csp_similarity` | `pxrd_two_theta_maximum`               | numb | For methods based on comparing powder patterns, it defines the maximum 2-theta value.                                                                                                                                                                                                                                     | \> 0.       | degrees             | 35.                                                        |
| `_csp_similarity` | `pxrd_two_theta_step`                  | numb | For methods based on comparing powder patterns, it defines the step-size used in pattern simulation.                                                                                                                                                                                                                      | \> 0.       | degrees             | 0.02                                                       |
| `_csp_similarity` | `pxrd_radiation_wavelength`            | numb | For methods based on comparing powder patterns, it defines the radiation wavelength in angstroms.                                                                                                                                                                                                                         | \> 0.       | angstroms           | 1.54056                                                    |
| `_csp_similarity` | `interatomic_distance_metric`          | char | For methods based on distributions of interatomic distances (e.g. PDD, PDF, RDF), it defines the metric used to compare distributions.                                                                                                                                                                                    | Free Text   |                     | - "Euclidean"<br/>- "Chebishev"<br/>- "Pearson's Distance" |
| `_csp_similarity` | `interatomic_distance_neighbour_count` | numb | For methods based on distributions of interatomic distances, it defines the number of nearest neighbours (or atomic shell size) used.                                                                                                                                                                                     | \> 0        |                     | 100                                                        |
| `_csp_similarity` | `interatomic_distance_radial_cutoff`   | numb | For methods based on distributions of interatomic distances, it defines the maximum distance at which pairwise distances are used.                                                                                                                                                                                        | \> 0.       | angstroms           | 10                                                         |
| `_csp_similarity` | `interatomic_distance_bin_width`       | numb | For methods based on distributions of interatomic distances, it defines the grid bin spacing.                                                                                                                                                                                                                             | \> 0.       | angstroms           | 0.25                                                       |
| `_csp_similarity` | `experimental_fingerprint`             | bool | When comparing theoretical and experimental structures, if set to True, the fingerprint (e.g. PXRD or RDF pattern) of the experimental structure comes from a physical instrument. If set to false it is instead computationally generated as the other theoretical structures starting from the 3D coordinates of atoms. |             |                     |                                                            |

### Examples

Generate Conformers with RDKit's ETKDGv3 tool and optimise them with a classical forcefield:

```text
data_etkdgv3

# Datablock Details
_csp_data_block.class                           "Step"             
_csp_data_block.description                     etkdgv3                  
_csp_data_block.id                              080e7535-1c29-4108-9984-8c89deb4fe89

# Conformers Generation
_csp_conformer.generation_method                ETKDGv3
_csp_conformer.generation_method_description    "Experimental torsional-angle DG approach"
_csp_conformer.generation_software              RDKit
_csp_conformer.generation_software_version      2025.09
 
# Optimisation
_csp_conformer.optimisation_method              MMFF94
_csp_conformer.optimisation_method_description  "RDKit implementation of the MMFF94 force field"
_csp_conformer.optimisation_software            RDKit  
_csp_conformer.optimisation_software_version    2025.09
_csp_conformer.energy_cutoff                    30.0
_csp_conformer.max_number_of_conformers         100
```

Generate Conformers with Mercury's ConformerGenerator tool, optimise them with a gas-phase DFT model and apply
clustering:

```text
data_cg

# Datablock Details
_csp_data_block.class                           "Step"             
_csp_data_block.description                     cg                  
_csp_data_block.id                              b7dcc1d4-d45c-442c-bc97-36f8c2bb1428

# Conformers Generation
_csp_conformer.generation_method                ConformerGenerator
_csp_conformer.generation_method_description    "Knowledge-based conformer generation using CSD data"
_csp_conformer.generation_software              "CSD Python API"
_csp_conformer.generation_software_version      3.7

# Optimisation
_csp_conformer.optimisation_method              PBE
_csp_conformer.optimisation_method_description  "GGA DFT optimisation"
_csp_conformer.optimisation_software            Psi4
_csp_conformer.optimisation_software_version    9.0
_csp_conformer.energy_cutoff                    20.0
_csp_conformer.max_number_of_conformers         50
_loop 
    _csp_step_variable.label
    _csp_step_variable.value
    "functional"                                PBE
    "basis"                                     cc-pvdz

# Clustering
_csp_conformer.clustering_method                MoleculeOverlay
_csp_conformer.clustering_method_description    "Overlays two molecules allowing for inversion"
_csp_conformer.clustering_software              "CSD Python API"
_csp_conformer.clustering_software_version      3.7
_csp_conformer.clustering_rmsd_cutoff           0.4
```

As there are currently no data fields describing gas-phase simulations, additional details can be added using the
general `_csp_step_variable.label` and `_csp_step_variable.value` data fields. As a rule of thumb, parameters label
should be the ones specified in programs input files.

Cluster structures using the Crystal Packing Similarity tool:

```text
data_cps

# Datablock Details
_csp_data_block.class                              "Step"             
_csp_data_block.description                        cps                  
_csp_data_block.id                                 677de204-eb7c-4df8-8ade-31f6c3fbf2a5

# Structure Similarity details
_csp_similarity.method                             "Crystal Packing Similarity"
_csp_similarity.method_description                 "A molecular-shell-based algorithm implemented in the CSD Python API"
_csp_similarity.software                           "CSD Python API"
_csp_similarity.software_version                   3.7
_csp_similarity.distance_cutoff                    1.0
_csp_similarity.energy_threshold                   0.5
_csp_similarity.density_threshold                  0.05
_csp_similarity.include_hydrogens                  False
_csp_similarity.optimise_cell                      False
_csp_similarity.molecular_shell_size               30
_csp_similarity.molecular_shell_distance_tolerance 0.30
_csp_similarity.molecular_shell_angle_tolerance    30
```

Cluster structures using the VC-PWDF approach:

```text
data_vcpwdf                                        
                                                   
# Datablock Details                                
_csp_data_block.class                              "Step"      
_csp_data_block.description                        vcpwdf
_csp_data_block.id                                 b77ebbe6-51c1-4829-89bf-7000bcfa3119
                                                   
# Structure Similarity details                     
_csp_similarity.method                             VC-PWDF
_csp_similarity.method_description                 "Variable-cell powder pattern comparison"
_csp_similarity.software                           critic2
_csp_similarity.software_version                   1.1
_csp_similarity.distance_cutoff                    0.05
_csp_similarity.energy_threshold                   0.5
_csp_similarity.density_threshold                  0.05
_csp_similarity.include_hydrogens                  True
_csp_similarity.optimise_cell                      True
_csp_similarity.pxrd_two_theta_minimum             5
_csp_similarity.pxrd_two_theta_maximum             35
_csp_similarity.pxrd_two_theta_step                0.02
_csp_similarity.pxrd_radiation_wavelength          1.54056 
```

Cluster structures with the PDD method:

```text
data_pdd                                           
                                                   
# Datablock Details                                
_csp_data_block.class                                "Step"                                       
_csp_data_block.description                          pdd                                       
_csp_data_block.id                                   edebc2fe-a81e-4c82-b238-fb13b2b01add         
                                                                                                  
# Structure Similarity details                                                                    
_csp_similarity.method                               PDD                                      
_csp_similarity.method_description                   "Comparisons of PDDs with EMD"    
_csp_similarity.software                             "average-minimum-distance python package"                                      
_csp_similarity.software_version                     1.3                                          
_csp_similarity.distance_cutoff                      0.25                                         
_csp_similarity.energy_threshold                     0.5                                          
_csp_similarity.density_threshold                    0.05                                         
_csp_similarity.include_hydrogens                    False                                                             
_csp_similarity.interatomic_distance_metric          chebyshev                                        
_csp_similarity.interatomic_distance_neighbour_count 100
```

## 7. Conventions

A few guidelines are adopted in the description of specific data fields as highlighted in the table below. Except for
*pDFT*, full names are preferred.

| Category             | Data Field | Suggested Input Item   | Alternatives to avoid                                       |
|----------------------|------------|------------------------|-------------------------------------------------------------|
| Structure Generation | `method`   | Random Search          | Quasirandom, Pseudorandom (specified in separate datafield) |
| Structure Generation | `method`   | Evolutionary Algorithm | Genetic Algorithm, EA, GA                                   |
| CompChem             | `method`   | Forcefield             | Force Field, Force-Field, FF                                |
| CompChem             | `method`   | pDFT                   | DFT, Density Functional Theory, periodic-DFT                |
| CompChem             | `method`   | Semi-Empirical         | Semi Empirical                                              |

In addition, the Structure Ranking `method` "ML Potential" refers to methods using *ad hoc* descriptors for neural
network training to directly compute energy and forces. On the other hand, ML models used to parameterise models
constants should be classified in the related method. For example, forcefield constants parameterised with a deep neural
network should be classified as "Forcefield".

## 8. Future Developments

### 8.1 Improvements to the CSP Core Dictionary

A few areas relevant to CSP have not been explored yet and might be included in later updates of the dictionary. In
general, new or specific methods can use the "Other" option and specify possible publications describing the workflow.

A list of missing sections is shown below:

* Initial molecule (or list of molecules and conformers) coordinates and properties.
* Explicit search variables description (cell parameters, components' positions and orientation, internal degrees of
  freedom)
* ML-based Structure Generation methods.
* Clustering algorithms used to remove duplicates.
* While the TCOD dictionary is available for DFT methods and a draft dictionary for forcefield methods is being
  developed, data fields of other energy evaluation methods are limited to basic identification labels. This includes:
    * Semi-Empirical methods
    * ML Potentials
    * Free energy correction methods
* Output structure properties are limited to the energy or score of the crystal. Other measurable properties (the band
  gap for example) are not currently included.

### 8.2 A Computational Chemistry Dictionary

The `_csp` prefix in energy/scoring methods and output structures have been intentionally left out so that the present
data fields could be used as the basis for the development of a more general computational chemistry dictionary. While
this is currently limited to a selection of data fields relevant to CSP application, below is an example of how these
can be used to describe a single geometry optimisation on a known structure:

```text
data_optimised_structure
# Structure is theoretically generated
_exptl.method 'theoretical model'

# General and Software details
_compchem.method pDFT
_compchem.calculation_type Optimisation

_compchem.software "Quantum Espresso"
_compchem.software_version 6.0         
_compchem.software_citation "https://doi.org/10.1088/1361-648X/aa8f79"

# Energy Evaluation
_dft.exchange_correlation_functional_type GGA
_dft.exchange_correlation_functional_name PBE
_dft.pseudopotential_type PAW
_dft.dispersion_correction XDM
_dft.kinetic_energy_cutoff_wavefunctions 600  # TCOD DFT Dictionary
_dft.BZ_integration_method "Monkhorst-Pack"
_dft.BZ_integration_grid_dens_X 0.5
_dft.BZ_integration_grid_dens_Y 0.5
_dft.BZ_integration_grid_dens_Z 0.5

# Geometry Optimisation
_compchem_geometry_optimisation.algorithm FIRE             
_compchem_geometry_optimisation.cell anisotropic                   
_compchem_geometry_optimisation.atoms all
_compchem_geometry_optimisation.relax_force_convergence 0.01
_compchem_geometry_optimisation.max_steps 200             

# Output Structure Details
_theoretical_structure.temperature 0.0          
_theoretical_structure.calculated_density 1.314748
_theoretical_structure.total_energy -85493.52397       

# Crystal                                                  
_symmetry.cell_setting           monoclinic                
_symmetry.space_group_name_H-M   'P 21/c'                  
_symmetry.Int_Tables_number      14                        
_space_group_name_Hall           '-P 2ybc'                 
loop_                                                      
_symmetry.equiv_pos_site_id                                
_symmetry.equiv_pos_as_xyz                                 
1 x,y,z                                                    
2 -x,1/2+y,1/2-z                                           
3 -x,-y,-z                                                 
4 x,1/2-y,1/2+z                                            
_cell.length_a                   16.8168                   
_cell.length_b                   7.0178                    
_cell.length_c                   14.5475                   
_cell.angle_alpha                90                        
_cell.angle_beta                 115.28                    
_cell.angle_gamma                90                        
_cell.volume                     1552.44                   
loop_                                                      
_atom_site.label                                           
_atom_site.type_symbol                                     
_atom_site.fract_x                                         
_atom_site.fract_y                                         
_atom_site.fract_z                                         
C0  C  0.402802  0.483043 0.842739                         
C1  C  0.387973  0.677363 0.792505                         
H2  H  0.372266  0.370900 0.785899                         
C3  C  0.290934  0.723546 0.722019                         
C4  C  0.299744  0.784092 0.627602                         
O5  O  0.430454  0.669327 0.717154                         
N6  N  0.375029  0.749323 0.626530                         
C7  C  0.433253  0.840791 0.865082                         
H8  H  0.373059  0.480692 0.896797                         
H9  H  0.473281  0.453133 0.883342                         
H10 H  0.406023  0.852375 0.921481                         
H11 H  0.422667  0.976203 0.823613                         
H12 H  0.504341  0.815441 0.904886                         
H13 H  0.247676  0.598250 0.706716                         
H14 H  0.264985  0.835703 0.754024                         
S15 S  0.217342  0.894753 0.520420                         
O16 O  0.132826  0.836886 0.515882                         
O17 O  0.235781  0.880775 0.432108                         
C18 C  0.229140  1.158880 0.556705                         
F19 F  0.218005  1.168970 0.646067                         
F20 F  0.314654  1.210640 0.581184                         
C21 C  0.161031  1.270540 0.472953                         
C22 C  0.174831  1.346830 0.391627                         
C23 C  0.075521  1.280400 0.468012                         
C24 C  0.007484  1.364770 0.384876                         
F25 F  0.256854  1.339740 0.393375                         
C26 C  0.107309  1.429290 0.307776                         
C27 C  0.023141  1.436700 0.304553                         
H28 H -0.030676  1.496570 0.238225                         
H29 H -0.058002  1.370540 0.382481                         
H30 H  0.062589  1.219340 0.529056                         
H31 H  0.120713  1.485310 0.246093                         
```
