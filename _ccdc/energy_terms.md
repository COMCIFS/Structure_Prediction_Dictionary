# Energy terms

Throwaway file for discussing what terms to include in the final dictionary

## CCDC blind test dictionary

* There should probably be a conformer energy term: _ccdc_csp_conformer_energy or something, which would be relative to gas phase minima, given theres so much about conformers in the existing dictionary
* _ccdc_csp_free_energy_correction_method: eg. QHA etc. good, keep. "desired"?
* _ccdc_csp_free_energy_correction_software, _ccdc_csp_free_energy_correction_software_version:  good, Optional
* _ccdc_csp_free_energy_correction_stage: preliminary or final - superfluous imo
* _ccdc_csp_classification_energy_absolute: "The total (absolute) energy of the crystal structure, with respect to gas-phase atoms." I think_ccdc_csp_classification_energy_total would line up with the majority of the community (and TCOD). Must be in kJ/mol not eV as suggested, Hartrees would really be the community standard anyway, but kJ/mol is SI. Methods below Periodic DFT don't have this concept, so Optional not Desirable for me
* _ccdc_csp_classification_energy_lattice_relative and _ccdc_csp_classification_ranking: difficulties with this if the landscape is restarted and a new GM is found, I would move from Required to Desirable
* _ccdc_csp_classification_energy_lattice_absolute: only "Required" for me
* _ccdc_csp_classification_energy_error_absolute, _ccdc_csp_classification_energy_error_relative: Did anyone use this? Looks like GRACE would want to in the future
* _ccdc_csp_free_energy_correction_absolute: "correction" should be made more obvious, and total over absolute if we go with my above recommendation
* _ccdc_csp_free_energy_correction_lattice: good, did many use this? I suspect most who do free energy correction will want to just record "free energy", rather than lattice energy and free energy correction. A seperate _ccdc_csp_free_energy_absolute may be wise
* _ccdc_csp_free_energy_relative,_ccdc_csp_free_energy_ranking: good, but not "Required" unless they actually did free energy calcs

## TCOD

High level thoughts, not all appropriate for this energy discussion.

* the paper <https://doi.org/10.1186/s13321-017-0242-y> does a good job of describing worklows, and has a similair concept of successive minimisations at increasing accuracy that could be learned from.
* Their efforts to include all the input data in the CIF has led to them including a "gzip+Base64" definition, presumably because filesize became an issue. I'd be keen to avoid this, given CSP will produce 1000 of each of these. gzip assumes Linux
* <https://www.etsf.eu/> may be another resource to learn from, they have DFT variables that have close equivalents in TCOD (pseudopotential_type vs_dft_pseudopotential_type). The Physical properties would be outside of scope for CSP though
* NOMAD differs from TCOD in cart vs frac coordinates, presumably because of an assumption of gas phase.
* MPOD may be interesting, but you can't download the dictionary from their website, doesn't look all that well maintained <http://mpod.cimav.edu.mx/docdictionary/>
* "Differences are mainly in notations and conventions: for instance, ETSF uses hartree and bohr as main measurement units, NOMAD uses joule and metre, whereas the TCOD uses electronvolt and angstrom. As another example, TCOD choice of using lengths and angles of basis vectors stems from experimental crystallography, while ETSF and NOMAD use vector notation, more common in theoretical materials science" Don't think we need to get involved in distances, SI units for energy
* "A structure can be straightforwardly represented in CIF, whereas separate steps of a trajectory can be converted into structures" - something to consider for MD

## TCOD_dictionary

link: <https://wiki.crystallography.net/cif/dictionaries/ddl1/cif_tcod/>

* TCOD_FF includes TCOD_FF_type, which can have values for "distributed multipole", which has been on my mind, happy to adopt this unless its felt too prescriptive. Doesn't have ML FF parameters
* _tcod_total_energy good, agree with "TOTAL" for this concept. KJ/mol not eV. They provide a CAUTION note in their dict that I agree with. This term will only be used for sanity checking, CSP users will use lattice or free energy 99% of the time
* _tcod_total_energy_* (formula, gradient), outside of scope for CSP, but could be optional if needed
* think we need to make a decision to set _tcod_computation, _tcod_file (input files), _TCOD_INITIAL_COORDINATE,_TCOD_SOURCE_DATABASE as outside of scope _for CSP_, although theres lots thats useful there if methods developers are prepared to include them

## DFT dictionary

link <https://wiki.crystallography.net/cif/dictionaries/ddl1/cif_dft/>

* _dft_cell_energy SG: "Is this supposed to be the same as 'total energy'? Will it be compatible with the http://www.xml-cml.org/dictionary/compchem/ "total energy" (ID: totalEnergy) term? If so, maybe we rename this data item to _dft_total_energy?" which I agree with
* _dft_kinetic_energy SG: "should the nuclei kin. energy be included? Is it ever appreciable? What about vibrational lattice modes (phonons)?" we run into potential misinterpretations of contributions to free energy by discussing nuclei vibrations. This term must only mean electron kinetic energy, and is probably out of scope
* _dft_Coulomb_energy, _dft_correlation_energy, _dft_1e_energy, _dft_2e_energy, _dft_nuclear_repulsion_energy, all have equivalents in https://www.xml-cml.org/dictionary/compchem/, and are outside of scope for CSP, but could be optional for those that are keen
* _dft_ewald_energy, _dft_fermi_energy, _dft_hartree_energy all outside of scope foir CSP
* DFT_CELL_CONV convergence criteria could be interesting, but not relevant for MD for instance.
* _dft_lattice_energy I'd take "atoms" out of this definition, but good. kJ/mol used here, presumably because these are defined as "Materials properties", so using SI definitions.
* all other under DFT_CALC_PROPERTY outside of scope