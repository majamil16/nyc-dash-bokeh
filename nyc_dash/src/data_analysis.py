import pandas as pd


def construct_df(filepath):
    df = pd.read_csv(filepath, header=None, names=['open', 'close', 'zip', 'status'], dtype={'zip':str})
    df['open'] = pd.to_datetime(df['open'],format='%m/%d/%Y %H:%M:%S %p')
    df['close'] = pd.to_datetime(df['close'],format='%m/%d/%Y %H:%M:%S %p' )
    df['response_time_hr'] = (df['close']-df['open']).astype('timedelta64[h]')

    monthly_grouped = pd.DataFrame(df.groupby([pd.Grouper(key='open',freq='M'), 'zip'])['response_time_hr'].mean())
    all_zips = set(monthly_grouped.index.get_level_values(1))

    new_index = pd.MultiIndex.from_product(monthly_grouped.index.levels) # this solves the fact that some don have incidents for all months, was ausing problems
    new_df = monthly_grouped.reindex(new_index)
    new_df = new_df.fillna(0).astype(float)
    return new_df, all_zips


def query_zip(df, zip_code=None):
    if zip_code is None:
        return df.mean(level=0) # if a zipcode is not provided, take the mean across all the months
    # otherwise provide the monthly data for the provided zip code
    # first check that the zip code has data for each month. if not, put 0's
#    query = df.loc[(slice(None), zip_code),:]
 #   if len(query) != 9:
  #      all_dates = sorted(list(set(df.index.get_level_values(0))))
   #     ind = query.index.get_level_values(0)
    #    missing = np.where([date not in ind for date in all_dates])
    return df.loc[(slice(None), zip_code),:] # otherwise provide it for the specified zipcode

