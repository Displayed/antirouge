import progressbar
import flagpy as fp
import webcolors
def get_colour_name(rgb_triplet, a = webcolors.CSS21_HEX_TO_NAMES.items()):

    min_colours = {}
    for key, name in a:
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
    
def check(a, b):
    if a[0] != b[0] or a[1] != b[1] or a[2] != b[2]:
        return False
    return True

def get_country_proportion_of_country_red(countr = "", prin=1):
    df = fp.get_flag_df()
    listCountries = fp.get_country_list()
    listc = {}
    bar = progressbar.ProgressBar(maxval=len(df))
    bar.start()
    bar.update(0)
    last_c = [0, -1 ,0]
    colour = "black"
    for i in range(len(df)):
        c = listCountries[i]
        f = df["flag"][i]
        x = 0
        y = 0

        if (c == countr or countr == ""):
            for ii in f:
                for j in ii:
                    x = x + 1
                    if (not check(last_c, j)):
                        colour = get_colour_name(j, webcolors.CSS21_HEX_TO_NAMES.items())
                        last_c = j
                    if (colour == "red"):
                        y = y + 1
            ratio = y / x
            listc[c] = ratio
            if (prin == 1):
                print(c, end =' ')
                print(":", end = ' ')
                print(ratio)
        bar.update(i)
    bar.finish()
    return listc
def classement_par_couleur():
    ret = sorted(get_country_proportion_of_country_red("", 0).items(), key = lambda t: t[1], reverse=True)
    for i in ret: 
        print(i[0], end = " : ")
        print(i[1] * 100, end=" %\n")
    return ret

def main():
    listCountries = fp.get_country_list()
    print(listCountries)
    #get_country_proportion_of_country_red("China")
    
    listSorted = classement_par_couleur()
    
    #C'EST LONG TRES LONG
    


                    
        #Traitement ici sur F


if __name__ == '__main__':
    main()
