from Scoring._annData import createObject
import pandas as pd
import numpy as np

adata_ = "./test_data/pbmc3k.h5ad"
jsonFile = "./test_data/big_genesets_relations.json"

_adata = createObject(adata_, jsonFile, normalized=True)

df = pd.DataFrame(_adata.X)
print(df.shape)

df.to_csv("output.csv", index=False, header=False)

