
# graph-perturbation

This repository includes a Python implementation of the partitioning algorithm described in:
https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1175&context=cs_faculty_pubs
The algorithm have been previously published in this repository https://github.com/riki95/social-networks-anonymization
In the plots_using_out_perturbation_ds.ipynb different plots have been made to compare the resultis on the different datasets

## Installation

The software have been tested on the following version:

- Python 3.10.11

## Usage

To see an example of how to use the code, see `main.py`.  You can execute this code with the following command:

		python main.py 

# graph-gen

Additionally in the repo there is another anonymization algorithm (generalization algorithm) described in:

Michael Hay, Gerome Miklau, David Jensen, Don Towsley, Chao Li. [Resisting Structural Re-identification in Anonymized Social Networks](http://dx.doi.org/10.1007/s00778-010-0210-x). VLDB Journal, 2010.

and 

Michael Hay, Gerome Miklau, David Jensen, Don Towsley, and Philipp Weis. [Resisting Structural Re-identification in Anonymized Social Networks](http://www.vldb.org/pvldb/1/1453873.pdf)
VLDB 2008.

## Installation

The software depends on the following software and has been tested on the following versions:

- [Python 2.6.1](http://www.python.org/)
- [Networkx 1.2](http://networkx.lanl.gov/)

## Usage

To see an example of how to use the code, see `run_partitioner.py`.  You can execute this code with the following command:

		python run_partitioner.py 

All codes are very similar with the originals but with some minor changes, and have been applied to different datasets for which 


