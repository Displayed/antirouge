import flagpy as fp
import webcolors
def get_colour_name(rgb_triplet):

    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
def main():
    listCountries = fp.get_country_list()
    print(listCountries)
    df = fp.get_flag_df()

    for i in range(len(df)):
        c = listCountries[i]
        f = df["flag"][i]
        x = 0
        y = 0
        #if (c == "France"):
        print(c, end=" ")
        for i in range(len(f)):
            for j in f[i]:
                x = x + 1
                if (get_colour_name(j) == "red"):
                    y = y + 1

        ratio = y / x
        print(c, end =' ')
        print(":", end = ' ')
        print(ratio)


                    
        #Traitement ici sur F


if __name__ == '__main__':
    main()