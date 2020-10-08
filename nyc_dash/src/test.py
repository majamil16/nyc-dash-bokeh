from data_analysis import construct_df, query_zip 
import os 

def main():
    PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.curdir)))
   # print(PROJ_DIR)
    DATA_PATH = os.path.join(PROJ_DIR, 'data', '2020_closed_nyc_311.csv')
    print(DATA_PATH)
    df = construct_df(DATA_PATH)[0]

    alldata = query_zip(df)
  #  print(alldata)
    print(df) 
   
   # all_zips = set(df.index.get_level_values(1))
  #  print(all_zips)
   # print(alldata.values)
    
    st = alldata.values.flatten()
    print(st)


if __name__ == "__main__":
    main()
