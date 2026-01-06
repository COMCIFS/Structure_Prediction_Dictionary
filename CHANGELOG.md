# 2025.12.18

## New Features

- Single inputs systems, generation methods, ranking methods and output structures are now organised in separate datablocks and a unique identifier should be assigned to them. For this purpose, we introduced the datafield `_csp.data_block_class` ("Input", "Generation Method", "Ranking Method", "Workflow", "Theoretical Structure") to identify the content of the datablock and `_csp.data_block_id` to specify its related unique identifier. 
```text
data_cbn_tmp
# Datablock Details
_csp.data_block_class       "Input"
_csp.data_block_id          2a2611e3-2021-4b03-a7c6-0ef71239008f
_csp.data_block_description input1
...
```
- The Workflow datablock is meant to connect different generation and ranking methods in multistep approaches. The datablock describing the single methods are identified by their uniwue ID (`_csp.structure_generation_data_block_id` and `_csp.structure_ranking_data_block_id` for generation and ranking methods, respectively). The datafields `_csp.structure_ranking_relative_energy_cutoff` and `_csp.structure_ranking_max_structures_retained` have been added to specify which structures pass to the next ranking stage.
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
- The output theoretical structures will have a link to the initial generation method, specific ranking stage and the previous structure. For free energy calculations in different conditions, reference temperature and pressure _must_ also be specified. A text description of the different stages can be added for human readability but it is not mandatory.
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
- It is now possible to specify the maximum number of structures to be generated for each space group using the datafield `_csp.structure_generation_stopping_criteria_space_group_number_list`
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
- The parametrisation of intramolecular, coulombic and van der Waals terms can now be described separately.
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
- The `_forcefield.multipole_max_rank` has now been added to the forcefield dictionary.
- ML learning datafields `_ml_potential.method`, `_ml_potential.model` and `_ml_potential.precision` have been added to improve method description.
- Many datafields related to computational chemistry settings have been relocated under the `_compchem.[]` dictionary group. This allows to use them more broadly for any computational chemistry puropose, not necesseraly related to CSP.

## Fixes
- Documentation updated with relevant examples.
- Labels of some datafields have been changed. In particular, `predicted_structure` was changed in the more appropriate `theoretical_structure` and `molecule` in `molecular_entity` so to include atoms, molecules, ions in the input definition.
