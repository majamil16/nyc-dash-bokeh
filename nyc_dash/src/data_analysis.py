import pandas as pd


def construct_df(filepath):
    df = pd.read_csv(filepath, header=None, names=['open', 'close', 'zip', 'status'], dtype={'zip':str})
    df['open'] = pd.to_datetime(df['open'],format='%m/%d/%Y %H:%M:%S %p')
    df['close'] = pd.to_datetime(df['close'],format='%m/%d/%Y %H:%M:%S %p' )
    df['response_time_hr'] = (df['close']-df['open']).astype('timedelta64[h]')

    monthly_grouped = pd.DataFrame(df.groupby([pd.Grouper(key='open',freq='M'), 'zip'])['response_time_hr'].mean())
    all_zips = set(monthly_grouped.index.get_level_values(1))

    return monthly_grouped, all_zips


def query_zip(df, zip_code=None):
    if zip_code is None:
        return df.mean(level=0) # if a zipcode is not provided, take the mean across all the months
    else: # otherwise provide the monthly data for the provided zip code
        return df.loc[(slice(None), zip_code),:] # otherwise provide it for the specified zipcode

