from tkinter import W
from Utils import *
from flagpy import get_flag_df
from progressbar import ProgressBar
from csv import DictWriter

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

def main(flags,colors=COLORS):
    bar = ProgressBar(maxval=len(flags))
    bar.start()
    count = 0
    ration = {}
    for name,flag in flags.items():
        bar.update(count)
        count+=1
        ration[name] = get_ratio_colors(flag,colors)
    bar.finish()
    return ration

if __name__ == '__main__':
    df = get_flag_df()
    result = main(df.flag)
    export_file = "result.csv"
    colors = [COLORS[color] for color in COLORS]
    colors_ratio = dict((c,0) for c in colors)
    with open(export_file, 'w', newline='') as csvfile:
        fields_names =['pays']  + colors
        writer = DictWriter(csvfile, fieldnames=fields_names)
        writer.writeheader()
        count = 0
        for k,v in result.items():
            count += 1
            for c,n in colors_ratio.items():
                colors_ratio[c] = v.get(c,0) + n
            v['pays'] = k
            writer.writerow(v)
        for c,n in colors_ratio.items():
                colors_ratio[c] =  n/count
        print(colors_ratio)




