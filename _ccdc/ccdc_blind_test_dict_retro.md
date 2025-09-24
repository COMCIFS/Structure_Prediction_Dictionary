# Retrospective

Document outlining the dictionary implemented for capturing CSP metadata for the 7th CSP Blind Test (CSP CIF dictionary v0.8). Annotations added to indicate what worked well, what didn’t etc.

Method description: Describes the CSP methodology/workflow used to produce the structures in the landscape

Structure metadata: Data attributed to each structure in the landscape

Crystal structure: Crystal structure description

| Method description | Structure metadata | Crystal Structure (CIF core) |
|--------------------|--------------------|------------------------------|
|Conformer generation|Simulation conditions|Atomic coordinates|
|Conformer optimisation|Lattice energy|Space group information|
|Structure generation|Free energy|Symmetry|
|Structure optimisation||Cell parameters|

## Method description

## Conformer generation # LH: Less focus required on conformers? IS: Agreed, but no harm in allowing optional fields, they're not wrong just not that useful

* Method - Method used for conformer generation.
* Software - Name of software used for conformer generation.
* Software version - Version of software used for conformer generation.
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for conformer generation.

## Conformer optimisation

* Method - Method used for conformer optimisation.
* Software - Name of software used for conformer optimisation.
* Software version - Version of software used for conformer optimisation.
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for conformer optimisation.

## Force field

* Name - Name of force field used for conformer optimisation.
* Description - High-level description of the force field used for conformer optimisation.

## Semi empirical

* Method - Semi-empirical method used for conformer optimisation.

## DFT

* Approximation - Type of DFT approximation used for conformer optimisation.
* Functional - DFT functional used for conformer optimisation.
* Dispersion correction - DFT dispersion correction used for conformer optimisation.
* Basis set - DFT basis set used for conformer optimisation.

## Wavefunction

* Method - Electronic method used by wavefunction for conformer optimisation.
* Basis set - Basis set used by wavefunction for conformer optimisation.

## Conformer clustering

* Method - Method used for conformer clustering.
* Cutoff - The conformer clustering cut-off value related to the clustering method given
* Cutoff units - The units of the conformer clustering cut-off value given
* Software - Name of software used for conformer clustering.
* Software version - Version of software used for conformer clustering.
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for conformer clustering

## Structure Generation

* Method - Method used for structure generation.
* Software - Name of software used for structure generation.
* Software version - Version of software used for structure generation.
* Space groups (all/subset) - The selection of space groups used for structure generation.
* Space group numbers list - The specific space groups used for structure generation.
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for structure generation.

## Structure optimisation # LH: BT feedback - Want to capture more details on parameters applied for calculations. E.g. for periodic DFT - K-point grid / energy cutoff etc. IS: I'd agree, and ideally I'd like to be able to capture gas phase vs periodic DFT methods. DMACRYS based methods use gas-phase DFT coupled with dispersion FF for lattice, which is har to capture with this. LH: BT feedback - Want to capture single point energies. Unable to in this format. IJS: borrowing from TCOD, I think criteria for stopping the minimisation should be considered

* Method - Method used for structure optimisation.
* Software - Name of software used for structure optimisation.
* Software version - Version of software used for structure optimisation.
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for structure optimisation.

## Force field (Structure Optimisation)

* Name - Name of force field used for structure optimisation.
* Description - High-level description of the force field used for structure optimisation

## Semi empirical (Structure Optimisation)

* Method - Semi-empirical method used for structure optimisation.

## DFT (Structure Optimisation)

* Approximation - Type of DFT approximation used for structure optimisation
* Functional - DFT functional used for structure optimisation
* Dispersion correction - DFT dispersion correction used for structure optimisation
* Basis set - DFT basis set used for structure optimisation

## Wavefunction (Structure Optimisation)

* Method - Electronic method used by wavefunction for structure optimisation
* Basis set - Basis set used by wavefunction for structure optimisation

## Structure clustering

* Method - Method used for structure clustering
* Cutoff - The structure clustering cut-off value related to the clustering method given
* Cutoff units - The units of the structure clustering cut-off value given
* Software - Name of software used for structure clustering
* Software version - Version of software used for structure clustering
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for structure clustering

## Free energy method

* Method - Method used for free energy correction
* Software - Name of software used for free energy correction
* Software version - Version of software used for free energy correction
* Stage (preliminary or final) - Indicates whether this is the final or a preliminary method used for free energy correction.

## References

* Category - The category of method described by a publication reference. Ideally this should be one of the method categories listed but other values are permitted.
* Citation - Citation for an article or other publication that describes one or more of the methods used for this prediction.
* Identifier/DOI - A persistent identifier (for example a DOI) indicating the location of an article or other publication that describes one or more of the methods used for this prediction.

## Structural properties metadata # LH: How do we capture multiple energies for a single structure? E.g. Lattice energies calculated at multiple levels of theory. IJS: prinicpal use case would be PBE minimised structure, with single point PBE0 calc (GRACE approach). I'd imagine people would just use the PBE0 energy in that case, but would be nice to include PBE energy if possible

* Simulation type - Indication of how the crystal modelling handles thermal effects (static: does not include thermal corrections of the lattice energy, or dynamic: includes thermal corrections of the lattice energy)
* Density - Density value calculated from the predicted crystal cell and contents.
* Temperature - The temperature at which the structure is calculated.
* Pressure - The pressure at which the structure is calculated.
* Conformer identifier - External identifier or label of a conformer used in a CSP calculation  # LH notes this wasn't used by submitters. Can see niche use caes, but is definitely an option.
* Absolute energy - The total (absolute) energy of the crystal structure, with respect to gas-phase atoms.

## Lattice energy

* Relative - The relative lattice energy of the structure with respect to the global minimum on the lattice or absolute energy landscape.
* Absolute - Lattice energy, with respect to isolated gas-phase molecules in their lowest energy conformation
* Rank - The rank of the structure when ordered by e.g. increasing relative energy where 1 indicates the lowest energy structure
* Error - Estimate of the assigned absolute lattice energy error evaluated as (predicted - experiment)
* Relative error - Estimate of the assigned relative lattice energy error defined as ((predicted - experimental)/experimental) and given as a simple ratio (not a percentage)

## Free energy

* Absolute - The free energy correction of the total (absolute) energy at a given temperature
* Correction energy - The free energy correction of the lattice energy at a given temperature
* Relative - The relative free energy, at a given temperature, of the structure with respect to the corresponding global minimum on the same free energy landscape
* Rank - The rank of the structure at a given temperature when ordered by relative free energy or free energy correction

## Crystal structure description (CIF core)

Suggested structural information from CIF core dictionary

Creation date

Chemical formula
Space group

* Crystal system
* Name (H-M)
* SG number

Symmetry operators

Cell parameters

Atomic coordinates
