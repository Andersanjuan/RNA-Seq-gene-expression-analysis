# RNA-seq data analysis pipeline

This repository contains Python scripts for pre-processing and analyzing RNA-seq data.

## Pre-processing

The pre-processing script trims and filters reads using Trimmomatic. The input parameters can be adjusted as necessary based on the quality and characteristics of the input data.

To run the script, first install Trimmomatic and download the necessary adapter file. Then, update the file paths and input parameters in the script and run the following command:


## Quality control

The quality control script uses FastQC and SAMtools to assess the quality of the sequencing reads and the alignment rates.

To run the script, first install FastQC and SAMtools. Then, update the file paths in the script and run the following command:


## Gene quantification

The gene quantification script uses featureCounts to quantify gene expression levels from the pre-processed and aligned BAM files.

To run the script, first install featureCounts and download the necessary GTF file. Then, update the file paths and input parameters in the script
