import flagpy as fp
def main():
    listCountries = fp.get_country_list()
    print(listCountries)
    df = fp.get_flag_df()
    
    for i in range(len(df)): 
        print(df["flag"][i])
        print(fp.flag_dist('Luxembourg', 'The Netherlands'))


if __name__ == '__main__':
    main()