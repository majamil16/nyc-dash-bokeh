import pandas as pd


def construct_df(filename):
    df = pd.read_csv(filename, header=None)
    my_cols = [1, 2, 8, 19] # these contain the columns of interest (start, close, zip code, and status open/closed)
    df = df[my_cols]
    df.columns=['open', 'close', 'zip', 'status']
    df = df[df['status'] == 'Closed'].copy()
    df.reset_index(inplace=True)
    df['open'] = pd.to_datetime(df['open']).values
    df['close'] = pd.to_datetime(df['close']).values
    df['response_time_hr'] = (df['close']-df['open']).astype('timedelta64[h]')
    df_grouped = df.groupby('zip')['response_time_hr'].mean()
    return df_grouped


def query_zip(df, zip_code):
    return df[zip_code]