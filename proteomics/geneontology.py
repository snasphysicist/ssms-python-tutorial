from goatools.obo_parser import GODag
import pickle
from Bio.UniProt.GOA import gafiterator
import gzip

g = GODag(obo_file='data/go.obo')


"""
'DB': the protein database;
'DB_Object_ID': protein ID;
'Qualifier': annotation qualifier (such as NOT);
'GO_ID': GO term;
'Evidence': evidence code
"""
# filename = <LOCATION OF GAF FILE>
filename = 'data/goa_human.gaf.gz'
with gzip.open(filename, 'rt') as fp:
    x ={annotation['DB_Object_ID']:annotation['GO_ID'] for annotation in gafiterator(fp)}


"""
To get the GO entry for a particular protein's accession number:
g[x['O43707']]
and use .name etc, to get terms of that GO entry
"""

f = 'output/result.pkl'
with open(f, 'rb') as file:
    df = pickle.load(file)

go_hits = [g[x[y]] if y in x else '' for y in df['uniprot']]
name_hits = [y.name if y!='' else '' for y in go_hits]

# plot the ups and downs per each name

df['go_name'] = name_hits

group = df[['log2_mean_ratio', 'go_name']].groupby(by=['go_name'], axis=0)
means = group.mean().sort_values('log2_mean_ratio')

# filter out by -2 to 2 to get only the big changes
means.loc[~means['log2_mean_ratio'].between(-2,2),:]


