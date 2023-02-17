# Load necessary packages
import subprocess

# Define file paths and input parameters
bam_path = "path/to/bam/files"
gtf_path = "path/to/gtf/file"
counts_path = "path/to/output/files"
strand_specific = "2"
min_overlap = "10"

# Run featureCounts on BAM files
featureCounts_cmd = f"featureCounts -a {gtf_path} -o {counts_path}/output.txt -T 8 -s {strand_specific} -t exon -g gene_id -M -O -p -B -C -Q 30 --largestOverlap {min_overlap} {bam_path}/*.bam"
subprocess.call(featureCounts_cmd, shell=True)
