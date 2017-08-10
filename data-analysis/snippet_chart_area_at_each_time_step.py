# Unneeded charting code that was removed from a jupyter notebook. Stored here as an example for later
# Draws a chart with the total area of multiple protin receptors at each time step

tmpdf = totals65.loc[(totals65['Receptor'].isin(['M1', 'M5', 'M7', 'M22', 'M26'])) & 
                     (totals65['Experiment Step'] == '-nl-post')]

pal = ['black', 'blue', 'red', 'orange', 'green']
g = sns.FacetGrid(tmpdf, col='Time Point', col_wrap=3, 
                  size=5, ylim=(0,100), xlim=(0,100), 
                  palette=pal,
                  hue='Receptor',
                  hue_order=['M1', 'M5', 'M7', 'M22', 'M26'],
                  hue_kws=dict(marker=['^', 'v', '*', '+', 'x']))
g.map(plt.scatter, 'Total Number Scaled', 'Total Area Scaled')
g.add_legend()
g.savefig('mutants_by_time_nl-post.png')
