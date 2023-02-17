# Load necessary packages
import subprocess
import pandas as pd

# Define file paths
fastq_path = "path/to/fastq/files"
bam_path = "path/to/bam/files"

# Run FastQC on fastq files
fastqc_cmd = f"fastqc -o {fastq_path}/fastqc --extract {fastq_path}/*.fastq.gz"
subprocess.call(fastqc_cmd, shell=True)

# Parse FastQC results
fastqc_data = []
for file in glob.glob(f"{fastq_path}/fastqc/*.html"):
    sample_name = os.path.basename(file).split("_fastqc.html")[0]
    with open(file) as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        per_base_quality = [float(x.text) for x in soup.select("#fastqc_main > div:nth-child(2) > div > div:nth-child(2) > pre > span")]
        per_base_sequence_content = [float(x.text) for x in soup.select("#fastqc_main > div:nth-child(3) > div > div:nth-child(2) > pre > span")]
        per_sequence_gc_content = float(soup.select("#fastqc_main > div:nth-child(4) > div > div:nth-child(2) > pre > span")[0].text)
        adapter_content = float(soup.select("#fastqc_main > div:nth-child(7) > div > div:nth-child(2) > pre > span")[0].text)
        fastqc_data.append([sample_name, per_base_quality, per_base_sequence_content, per_sequence_gc_content, adapter_content])
fastqc_df = pd.DataFrame(fastqc_data, columns=["Sample", "Per base quality", "Per base sequence content", "Per sequence GC content", "Adapter content"])

# Map reads to reference genome
bowtie_cmd = f"bowtie2 -x reference_genome -1 {fastq_path}/*_1.fastq.gz -2 {fastq_path}/*_2.fastq.gz -S {bam_path}/aligned.sam"
subprocess.call(bowtie_cmd, shell=True)

# Convert SAM to BAM
samtools_cmd = f"samtools view -bS {bam_path}/aligned.sam > {bam_path}/aligned.bam"
subprocess.call(samtools_cmd, shell=True)

# Sort and index BAM file
samtools_sort_cmd = f"samtools sort -o {bam_path}/sorted.bam {bam_path}/aligned.bam"
subprocess.call(samtools_sort_cmd, shell=True)

samtools_index_cmd = f"samtools index {bam_path}/sorted.bam"
subprocess.call(samtools_index_cmd, shell=True)

# Get alignment statistics using SAMtools
samtools_flagstat_cmd = f"samtools flagstat {bam_path}/sorted.bam > {bam_path}/flagstat.txt"
subprocess.call(samtools_flagstat_cmd, shell=True)

# Parse SAMtools results
flagstat_data = []
