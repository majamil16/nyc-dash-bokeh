from data_analysis import construct_df, query_zip 
import os 
import numpy as np

def main():
    PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.curdir)))
   # print(PROJ_DIR)
    DATA_PATH = os.path.join(PROJ_DIR, 'data', '2020_closed_nyc_311.csv')
    print(DATA_PATH)
    df = construct_df(DATA_PATH)[0]

   # alldata = query_zip(df)
  #  print(alldata)
    print(df) 
   
   # all_zips = set(df.index.get_level_values(1))
  #  print(all_zips)
   # print(alldata.values)
    all_dates = sorted(list(set(df.index.get_level_values(0))))
  #  st = alldata.values.flatten()
  #  print(st)
    i = query_zip(df, '10165').index.get_level_values(0)

  #  print(query_zip(df, '10165'))
    print("one with missing: ", i)
    print("all: ",all_dates)
    missing = np.where([date not in i for date in all_dates]) # find all the dates that arent in this one
    print("places where missing: ", missing) # the indices
   # print(all_dates[missing])
    q = query_zip(df, '10165')
    q.loc[slice(missing),slice(None)] 




if __name__ == "__main__":
    main()
