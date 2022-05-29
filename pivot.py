from csv import DictReader,DictWriter


with open("result.csv","r") as file:
    reader = DictReader(file)
    count = 0
    pivot = {}
    paysliste = set()
    for row in reader:
        pays = row.pop("pays",None)
        pays = pays.replace(' ','-')
        paysliste.add(pays)
        for color,value in row.items():
            if pivot.get(color,None) is None:
                pivot[color] = {}
            pivot[color].update({pays:value})
with open("tluser.csv","w",newline='') as file:
    fields_name = ['color'] + list(paysliste)
    writer_ = DictWriter(file,fieldnames=fields_name)
    writer_.writeheader()
    for k,v in pivot.items():
        v['color'] = k
        writer_.writerow(v)
print("done")