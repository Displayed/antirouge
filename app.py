from sys import flags
from Utils import *
from flagpy import get_flag_df
from csv import DictWriter
from progressbar import ProgressBar

COLORS = {
        '#ffa500': 'orange',
        '#00ffff': 'aqua', 
        '#000000': 'black',
        '#0000ff': 'blue',
        '#008000': 'green',
        '#808080': 'gray',
        '#00ff00': 'lime',
        '#800000': 'maroon',
        '#000080': 'navy',
        '#808000': 'olive',
        '#ff0000': 'red',
        '#c0c0c0': 'silver',
        '#008080': 'teal',
        '#ffffff': 'white',
        '#ffff00': 'yellow'
        }
export_file = "result.csv"

if __name__ == '__main__':
    df = get_flag_df()
    flags = df.flag
    bar = ProgressBar(maxval=len(flags))
    


    result = {}
    
    colors_ratio = dict((v,0) for c,v in COLORS.items())

    count = 0
    bar.start()
    for name,pic in flags.items():
        bar.update(count)
        count+=1
        ratio = get_ratio_colors(pic,COLORS)
        for c,n in colors_ratio.items():
            colors_ratio[c] = ratio.get(c,0) + n
        result[name] = ratio

    for c,n in colors_ratio.items():
        colors_ratio[c] =  n/count
    
    bar.update(count)
    bar.finish()
    print(colors_ratio)



    
    with open(export_file, 'w', newline='') as csvfile:
        colors_names = [color for color in COLORS.values()]
        fields_names = ['pays']  + colors_names
        writer = DictWriter(csvfile, fieldnames=fields_names)
        writer.writeheader()
        for k,v in result.items():
            v['pays'] = k
            writer.writerow(v)




