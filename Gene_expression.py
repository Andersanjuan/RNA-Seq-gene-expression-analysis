# Load necessary packages
import pandas as pd
import numpy as np
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

# Load example gene expression data
data = pd.read_csv("https://raw.githubusercontent.com/*/RNA-seq-analysis/master/DESeq2/data/counts.txt", sep="\t", index_col=0)

# Set conditions for differential expression analysis
data['condition'] = ['A', 'A', 'A', 'B', 'B', 'B']
conditions = robjects.FactorVector(data['condition'].values.tolist())

# Perform differential gene expression analysis using DESeq2
DESeq2 = importr('DESeq2')
r_dataframe = robjects.pandas2ri.py2rpy(data.iloc[:, :-1])
dds = DESeq2.DESeqDataSetFromMatrix(countData=r_dataframe, colData=conditions, design= ~ condition)
dds = DESeq2.DESeq(dds)
res = DESeq2.results(dds)

# Extract significant differentially expressed genes
res_df = pd.DataFrame(np.array(res), index=res.names, columns=res.colnames)
sig_genes = res_df[res_df['padj'] < 0.05].index.tolist()

# Perform further analysis using edgeR
edgeR = importr('edgeR')
counts = np.array(data.iloc[:, :-1])
dge = edgeR.DGEList(counts=counts, group=data['condition'])
dge = edgeR.calcNormFactors(dge)
design_mat = np.vstack((np.ones(data.shape[0]), data['condition'] == 'B')).T
edgeR.glmQLFit(dge, design_mat)
edgeR.glmQLFTest(dge, coef=2)
edgeR.topTags(edgeR.glmQLFTest(dge, coef=2))
