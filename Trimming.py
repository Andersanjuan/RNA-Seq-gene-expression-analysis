# Load necessary packages
import subprocess

# Define file paths and input parameters
fastq_path = "path/to/fastq/files"
trimmed_path = "path/to/trimmed/files"
adapters_path = "path/to/adapters/files"
leading = "3"
trailing = "3"
sliding_window = "4:15"
minlen = "36"

# Run Trimmomatic on fastq files
trimmomatic_cmd = f"java -jar trimmomatic.jar PE -threads 8 {fastq_path}/input_R1.fastq.gz {fastq_path}/input_R2.fastq.gz {trimmed_path}/output_R1.paired.fastq.gz {trimmed_path}/output_R1.unpaired.fastq.gz {trimmed_path}/output_R2.paired.fastq.gz {trimmed_path}/output_R2.unpaired.fastq.gz ILLUMINACLIP:{adapters_path}/TruSeq3-PE.fa:2:30:10 LEADING:{leading} TRAILING:{trailing} SLIDINGWINDOW:{sliding_window} MINLEN:{minlen}"
subprocess.call(trimmomatic_cmd, shell=True)
