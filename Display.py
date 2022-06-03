import matplotlib.pyplot as plt
from csv import DictReader
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
pays = 'Argentina'
data =  {'gray': 67.30864197530865, 'silver': 3.450617283950617, 'red': 27.932098765432098, 'orange': 1.117283950617284, 'olive': 0.19135802469135801}

def show_ratio(pays,data,ax):
    print(data)
    labels,sizes = zip(*data.items())
    c = lambda n : float(n) if n else 0
    legends = [f"{l}:{c(s):.2f}" for l,s in data.items()]
    fun = lambda x : 0.1 if x=="red" else 0
    explode = *(fun(color)  for color in labels),  # only "explode" the 2nd slice (i.e. 'Hogs')
    ax.set_title(pays)
    patches,*_ = ax.pie(list(map(c,sizes)), explode=explode,colors=labels ,shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(patches,legends, loc="center left")
    print(pays)


with open("resulto.csv","r") as file:
    reader = DictReader(file)
    lines = [*reader]
    n  = len(lines)
    fig , axes = plt.subplots(n)
    count = 0
    for row in lines:
        pays = row.pop("pays",None)
        print(count)
        show_ratio(pays,row,axes[count])
        count+=1

print(count,n)
plt.show()