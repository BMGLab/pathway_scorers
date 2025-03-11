from GeneSets.geneSetObjects import createGeneSets
from GeneSets.geneSetScores import GeneSetScore

from GeneExpressions.geneExpScores import score

import scanpy as sc
import numpy as np


#Get the files.
jsonFilePath = "/home/sadigungor/Desktop/pathway_scorers/test/test_data/big_genesets_relations.json"

h5adFilePath = "/home/sadigungor/Desktop/pathway_scorers/test/test_data/pbmc3k.h5ad"
adata = sc.read_h5ad(h5adFilePath)

geneSetList = createGeneSets(jsonFilePath)
for geneSet in geneSetList: # Calculate for each gene set. 

 
    _geneNames = geneSet.getGeneNames # Get the gene names necessary for geneExpScores.score() from 
                                      # GeneSet object.

    newGeneSetScore = GeneSetScore(geneSet.matrix, _geneNames) # Create gene set score without 
                                                               # the expressions.

    newScore = score(adata,newGeneSetScore)  # Merge expression scores with gene set scores and print

    # Print geneset names, scores and the percentage of scores that are not 0 in the given geneset.
    print(f"GENESET : {geneSet.getID}")
    print(f"{newScore} \n NONZEROS : %{round(((np.count_nonzero(newScore)/len(newScore)) * 100),2)}")
    print("######################################################################################################")
