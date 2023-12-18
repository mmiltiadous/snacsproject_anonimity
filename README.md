
# graph-perturbation

This reposidory includes a python implementation of the perturbation algorithm described in:
https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1175&context=cs_faculty_pubs 
The algorithm have been previously published in this reposidory https://github.com/riki95/social-networks-anonymization but here there are some tweaks of it and implementations on different datasets which are also provided with their outputs.
Finally, in the plots_using_out_perturbation_ds.ipynb different plots have been made to compare the results on the different datasets

## Installation

The software have been tested on the following version:

- Python 3.10.11

## Usage

To see an example of how to use the code, see `main.py`.  You can execute this code with the following command:

		python main.py 

# graph-gen

Additionally in the repo there is another anonymization algorithm (partitioning/generalization algorithm) described in:

Michael Hay, Gerome Miklau, David Jensen, Don Towsley, Chao Li. [Resisting Structural Re-identification in Anonymized Social Networks](http://dx.doi.org/10.1007/s00778-010-0210-x). VLDB Journal, 2010.

and 

Michael Hay, Gerome Miklau, David Jensen, Don Towsley, and Philipp Weis. [Resisting Structural Re-identification in Anonymized Social Networks](http://www.vldb.org/pvldb/1/1453873.pdf)
VLDB 2008.

The file run_datasets.py is an alterated version of the run_partitioner.py which inputs 5 different datasets. They can be found under the folder datasets.
To run the generalization algorithm for each of the datasets, comment out the rest of the 4 datasets and use the command:

		python run_datasets.py

## Installation

The software depends on the following software and has been tested on the following versions:

- Python  2.7.18  (using miniconda)
- [Networkx 1.2](http://networkx.lanl.gov/)

## Usage

To see an example of how to use the code, see `run_partitioner.py`.  You can execute this code with the following command:

		python run_partitioner.py 

All codes are very similar with the originals but with some minor changes, and have been applied to different datasets.


