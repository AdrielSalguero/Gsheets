import pandas as pd
import os
import shutil
import requests

def clean(df):


  df_date = df[0].str.split('T', expand = True)
  df = pd.concat([df_date,df],axis = 1)

  if df.shape[1]<9:

    df.columns = ['d','h','0', 'ul','i','cav', 'est']
    df = df.drop(['0'], axis = 1)
    df['hour'],df['ip']  = df['hour'].str.replace('Z',''),df['ip'].str.replace('::ffff:','')   

    df = df.loc[df['dates'].between(start, end)]

  else:

    df.columns = ['d','h','0', 'ul','i','cav', 'est', 'con', 'cty', 'ct', 'PC','l','ln', 'sp']
    df = df.drop(['0', 'PC','l','ln', 'sp','con'], axis = 1)
    df['h'],df['i']  = df['h'].str.replace('Z',''),df['i'].str.replace('::ffff:','')


  return df


def run():

  oddf= pd.read_csv('url', sep= '|', header = None)
  ndf= pd.read_csv('url', sep= '|', header = None)

  oddf = clean(oddf)
  ndf = clean(ndf)

  dataframes = [oddf,mdf]
  df = pd.concat(dataframes, sort='False', ignore_index='True')
  df['i'] = df.index
  df = df[['d','h','0', 'ul','i','cav','cty' ,'ct', 'est']]

  df.to_excel(file_name)
  os.remove(file_route)  
  shutil.move(file_name, file_route')

if __name__ == '__main__':

  run()
