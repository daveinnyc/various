# Unneeded charting code that was removed from a jupyter notebook. Stored here as an example for later
# Compare starting receptor with it's mutants -- A3

tmpdf = totals65.loc[(totals65['Receptor'].isin(['A3', 'M5', 'M7', 'M26'])) & 
                     (totals65['Experiment Step'].isin(['-l-pre', '-l-post']))]

pal = ['black', 'blue', 'red', 'green']
g = sns.FacetGrid(tmpdf, 
                  col='Experiment Step', row='Receptor',  
                  size=5, 
                  ylim=(0,100), xlim=(0,100), 
                  palette=pal,
                  hue='Receptor',
                  hue_order=['A3', 'M5', 'M7','M26'],
                  hue_kws=dict(marker=['^', 'v', '*', '+']))
g.map(plt.scatter, 'Total Number Scaled', 'Total Area Scaled')
g.add_legend()
g.savefig('a3_and_mutants.png')
