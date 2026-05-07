# 2026.04.24

## New Features

- A "Step" class has been added to describe intermediate steps in a CSP workflow, such as conformer generation and
  structure similarity calculations.
- New datafields describing Conformer Generation methods for organic CSP as an intermediate step:

```text
data_etkdgv3

# Datablock Details
_csp.data_block_class                           "Step"             
_csp.data_block_description                     etkdgv3                  
_csp.data_block_id                              080e7535-1c29-4108-9984-8c89deb4fe89

# Conformers Generation
_csp.conformer_generation_method                ETKDGv3
_csp.conformer_generation_method_description    "Experimental torsional-angle DG approach"
_csp.conformer_generation_software              RDKit
_csp.conformer_generation_software_version      2025.09
 
# Optimisation
_csp.conformer_optimisation_method              MMFF94
_csp.conformer_optimisation_method_description  "RDKit implementation of the MMFF94 force field"
_csp.conformer_optimisation_software            RDKit  
_csp.conformer_optimisation_software_version    2025.09
_csp.conformer_energy_cutoff                    30.0
_csp.conformer_max_number_of_conformers         100
```

- New datafields describing Structure Similarity methods, used both as clustering method (remove duplicates) and to
  identify matches with experimental:

```text
data_cps

# Datablock Details
_csp.data_block_class                              "Step"             
_csp.data_block_description                        cps                  
_csp.data_block_id                                 677de204-eb7c-4df8-8ade-31f6c3fbf2a5

# Structure Similarity details
_csp.similarity_method                             "Crystal Packing Similarity"
_csp.similarity_method_description                 "A molecular-shell-based algorithm implemented in the CSD Python API"
_csp.similarity_software                           "CSD Python API"
_csp.similarity_software_version                   3.7
_csp.similarity_distance_cutoff                    1.0
_csp.similarity_energy_threshold                   0.5
_csp.similarity_density_threshold                  0.05
_csp.similarity_include_hydrogens                  False
_csp.similarity_optimise_cell                      False
_csp.similarity_molecular_shell_size               30
_csp.similarity_molecular_shell_distance_tolerance 0.30
_csp.similarity_molecular_shell_angle_tolerance    30
```

- New datafields in `_theoretical_structure` to show matches with experimental structures or specify the cluster center
  if the structure has been labeled as a duplicate.

- New "Output" class to describe general outputs of a CSP workflow, such as computational cost or global minima in each
  step.
           
```text
data_csp_output

# Datablock Details
_csp.data_block_class                 "Output"             
_csp.data_block_description           csp_output                   
_csp.data_block_id                    1d327ab0-3f84-4794-88a8-3c14b8f09999
_csp.data_block_additional_files      [ "csp_input.cif" "workflow.cif" "structure_1.cif" "structure_105.cif"]

# Input and workflow identifiers
_csp.output_input_system_description  Urea_Hydrate                        
_csp.output_input_system_id           2a2611e3-2021-4b03-a7c6-0ef71239008f
                                    
_csp.output_workflow_description      wf2                                 
_csp.output_workflow_id               964fcd15-82e1-4c4d-a7cb-61b0b34c3421

# Output Details and Computational Cost
_csp.output_hardware_description      "AMD Zen 2 EPYC 7H12"
_csp.output_total_computational_cost  185101.0

loop_
    _csp.output_stage 
    _csp.output_stage_id
    _csp.output_total_computational_cost
    _csp.output_number_of_structures
    _csp.output_average_computational_cost
    _csp.output_global_minima
    _csp.output_global_minima_id
    # Generation Methods
    "rs"      6e0147be-0454-44a1-a3bb-de7b326dde1b       1.0     7500  0.00013 . .
    "sa"      95f28b3c-d029-4840-a69a-3ced34219c28     100.0  2000000  0.00050 . .
    # Ranking Methods
    "gaff"    83f824d3-6d17-4e42-9952-31ed161ef811  100000.0  2007500  0.04981 "structure_1_1"   63f70eef-cd02-4f73-b7a3-cda97adfe10e          
    "psi_mol" d6f196c5-88d9-4ecd-b388-bcd92fd93a05   25000.0    50000  0.50000 "structure_105_2" 07457f98-a456-441e-bb36-1e650d799b93  
    "pbe"     17ad684a-2337-4a96-9808-b8b8d3013dc3   60000.0    10000  7.50000 "structure_105_3" 756c1329-73a5-43e2-a359-54b01731ac42 
```

- New `.dic` files for the CSP and Computational chemistry dictionaries.

- New data fields for ML Potentials.

## Fixes

- Markdown files updated with relevant examples.
- The "Category" column in the descriptive files has been removed and names converted to their actual use in the `.dic`
  files:

  Old version:

  | Group | Category   | Data Field         |
  |-------|------------|--------------------|
  | CSP   | Data Block | `class`            |

  New version:

  | Group  | Data Field                    |
  |--------|-------------------------------|
  | `_csp` | `data_block_class`            |

- "Definition", "Constraints" and "Examples" columns changed to improved clarity.
- Descriptive dictionaries (Markdown files) in `Dictionaries/DFT` and `Dictionaries/Forcefields` do not have any
  duplicate data field in `Dictionaries/CSPCore/cspcore.md`.
- A few old labels have been changed for consistency across the dictionary.
- Monomer correction datafield in the "Additional Proposed Fields" section in `Dictionaries/DFT/dft.md` has been split
  to describe functional, basis set and dispersion correction separately.

# 2025.12.18

## New Features

- Single inputs systems, generation methods, ranking methods and output structures are now organised in separate
  datablocks and a unique identifier should be assigned to them. For this purpose, we introduced the data field
  `_csp.data_block_class` ("Input", "Generation Method", "Ranking Method", "Workflow", "Theoretical Structure") to
  identify the content of the datablock and `_csp.data_block_id` to specify its related unique identifier.

```text
data_cbn_tmp
# Datablock Details
_csp.data_block_class       "Input"
_csp.data_block_id          2a2611e3-2021-4b03-a7c6-0ef71239008f
_csp.data_block_description input1
...
```

- The Workflow datablock is meant to connect different generation and ranking methods in multistep approaches. The
  datablock describing the single methods are identified by their unique ID (`_csp.structure_generation_data_block_id`
  and `_csp.structure_ranking_data_block_id` for generation and ranking methods, respectively). The data fields
  `_csp.structure_ranking_relative_energy_cutoff` and `_csp.structure_ranking_max_structures_retained` have been added
  to specify which structures pass to the next ranking stage.

```text
data_workflow
    # Data blocks details
    _csp.data_block_class            Workflow
    _csp.data_block_description      csp_workflow
    _csp.data_block_id               425a77e3-a2a4-40fb-acdb-1e25b2d00bbd
    _csp.data_block_additional_files ["structure_generation_methods.cif" "structure_ranking_methods.cif"]

    # Structure Generation Methods
    loop_
        _csp.structure_generation_stage
        _csp.structure_generation_preceding_stage
        _csp.structure_generation_data_block_description
        _csp.structure_generation_method
        _csp.structure_generation_data_block_id
        0 . "rs"   "Random Sampling"                1d5b2b53-d70d-44e8-b5c3-3342b5a10c35
        1 0 "ea"   "Evolutionary Algorithm"         af534fed-8153-4af2-bd9f-29b0fef8d805

    # Structure Ranking Methods
    loop_
        _csp.structure_ranking_stage
        _csp.structure_ranking_preceding_stage
        _csp.structure_ranking_data_block_description
        _compchem.calculation_type
        _compchem.method
        _csp.structure_ranking_relative_energy_cutoff
        _csp.structure_ranking_max_structures_retained
        _csp.structure_ranking_data_block_id
        0 . "gaff"         "Optimisation"     "Forcefield"     30.0 20000 6f36e2d3-a130-4cfc-81cd-7714fb92c3ca
        1 0 "se"           "Optimisation"     "Semi-Empirical" 20.0 10000 ed2bc09c-5914-400c-9107-1d58d92b93a6
        2 1 "pbe"          "Optimisation"     "pDFT"           .    .     97088479-72d3-4953-b858-503639748771
```

- The output theoretical structures will have a link to the initial generation method, specific ranking stage and the
  previous structure. For free energy calculations in different conditions, reference temperature and pressure _must_
  also be specified. A text description of the different stages can be added for human readability, but it is not
  mandatory.

```text
data_structure_A1B1_1_step8_t300
    # Datablock Details
    _csp.data_block_class                                              "Theoretical Structure"
    _csp.data_block_description                                        structure_structure_A1B1_1_step8_t300
    _csp.data_block_id                                                 3b4de7b5-aed4-4358-a22d-3337937fdecb

    # Include files specifying input, methods and workflow data blocks
    _csp.data_block_additional_files                                   [ "csp_input.cif" "csp_workflows.cif" ]

    # Stage identifiers
    _theoretical_structure.csp_input_system_description                BT-XXX
    _theoretical_structure.csp_input_system_id                         2a2611e3-2021-4b03-a7c6-0ef71239008f

    _theoretical_structure.csp_workflow_description                    csp_workflow_long
    _theoretical_structure.csp_workflow_id                             425a77e3-a2a4-40fb-acdb-1e25b2d00bbd

    _theoretical_structure.csp_generation_stage_description            ea
    _theoretical_structure.csp_generation_stage_id                     af534fed-8153-4af2-bd9f-29b0fef8d805

    _theoretical_structure.csp_ranking_stage_description               pbe0_mbd_qha
    _theoretical_structure.csp_ranking_stage_id                        2b9deed1-116f-454a-922e-be61c8d946c5
    _theoretical_structure.csp_reference_temperature                   300.0
    _theoretical_structure.csp_reference_pressure                      100000.0

    _theoretical_structure.csp_previous_stage_structure_description    structure_structure_A1B1_1_step7
    _theoretical_structure.csp_previous_stage_structure_id             094f5430-0785-4d8f-8aa4-3e31fb579ec4
```

- Datablocks can be stored in different files or in multiple files depending on the user. In the former case, the
  `_csp.data_block_additional_files` field should be used to retrieve relevant datablocks (check example above).
- It is now possible to specify the maximum number of structures to be generated for each space group using the data
  field `_csp.structure_generation_stopping_criteria_space_group_number_list`

```text
# Random Search
data_rs
    _csp.data_block_class                                                "Generation Method"
    _csp.data_block_description                                          rs
    _csp.data_block_id                                                   8e0147be-0k54-44a1-a3bb-de7df26ddeer
    
    _csp.structure_generation_method                                     "Random Search"
    _csp.random_search_random_numbers_algorithm_type                     "Quasi-random"
    _csp.random_search_random_numbers_algorithm                          "Sobol"
    
    _csp.structure_generation_space_group_number_list                    [14 2 15 61 19 4 33 29 5 1]
    _csp.structure_generation_stopping_criteria_description              "Max Structures"
    loop_
        _csp.structure_generation_stopping_criteria_space_group_number_list                         
        _csp.structure_generation_stopping_criteria_max_structures_evaluated  
        14   1000 
        2    1000
        15   1000
        61   1000
        19   1000
        4     500
        33    500
        29    500
        5     500
        1     500      
```

- The parametrisation of intramolecular, coulomb and van der Waals terms can now be described separately.

```text
...
loop_
    _forcefield.parameterization_term
    _forcefield.parameterization_description        
    _forcefield.parameterization_method 
    intra         "Transferable parameters based on atom types" "GAFF"
    electrostatic "Fitting to gas-phase semi-empirical data"    "AM1/BCC"
    vdw           "Transferable parameters based on atom types" "AMBER"
...
```

- The data field `_forcefield.multipole_max_rank` has now been added to the forcefield dictionary.
- ML learning data fields `_ml_potential.method`, `_ml_potential.model` and `_ml_potential.precision` have been added to
  improve method description.
- Many data fields related to computational chemistry settings have been relocated under the `_compchem.[]` dictionary
  group. This allows to use them more broadly for any computational chemistry purpose, not necessarily related to CSP.

## Fixes

- Documentation updated with relevant examples.
- Labels of some data fields have been changed. In particular, `predicted_structure` was changed in the more appropriate
  `theoretical_structure` and `molecule` in `molecular_entity` so to include atoms, molecules, ions in the input
  definition.
