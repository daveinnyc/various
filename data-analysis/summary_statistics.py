# Generate a chart with some summary statistics on the protein receptors


def print_header(title):
    print(title)
    print('Receptor  Run Group     Min       Max         Avg         Std  ')
    print('-------------------------------------------------------------- ')

    
def sorted_cleanly(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

sorted_receptors =  sorted_cleanly(set(totals65['Receptor']))
columns = ['Total Number of Clusters', 'Total Area of Protein Clusters', 'Total Intensity of Protein Clusters']

for c in columns:
    print_header(c)
    for rptr in sorted_receptors:
        for r in sorted(set(totals65['Run Group'])):
            tmpdf = totals65[ (totals65['Receptor'] == rptr) &
                              (totals65['Run Group'] == r)
                            ]
            print('{:<10}{:^9}{:>8}{:>10}{:>12}{:>12}'.format(rptr, 
                                r, 
                                min(tmpdf[c]),
                                max(tmpdf[c]),
                                round(np.average(tmpdf[c]),1),
                                round(np.std(tmpdf[c]),1),
                                )
              )
    print()
    print()
