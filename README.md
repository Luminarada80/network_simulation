# network_simulation

Generates a graphml network file compatible with scBONITA2. Creates random Boolean rules between the edges in the graphml network and creates a simulated binarized scRNAseq dataset that follows the logic of the network. The user can specify the number of cells and genes to create. 

This is created as a check for the rule determination method of scBONITA2. To use it, alter the `num_genes` and `num_cells` variable in `network_simulation.py` and the paths to the graphml file (have it add the graphml file directly to scBONITA2's input/custom_grapml_files directory).

The `check_rules_output.py` will load the rules used to create the simulated data as well as scBONITA2's inferred ruleset given the dataset and the graphml file. The script will simulate both models using 1000 random bitstrings as the starting state, and use dynamic time warping to see how closely the trajectory of the inferred ruleset follows the simulation trajectory of the true ruleset. 

`boxplot_series.py` uses the results of `check_rules_output.py` to create a series of boxplots of rule accuracy accross a range of network sizes. Add in the average error, standard deviation, minimum error, and maximum error to generate a boxplot range. 
