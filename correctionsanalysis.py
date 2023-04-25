# open tsv file 38492-0001-Data.tsv from the finalproject folder
# read in the file
# convert to a pandas dataframe

import pandas as pd
import re, os

df = pd.read_csv("/Users/paritashah/Desktop/College/Year3/Term2/BigData/finalproject/38492-0003-Data.tsv", sep='\t')

# remove unknown education levels
df = df[df.EDUCATION != 9]
# remove unkown and other prison admission types
df = df[df.ADMTYPE != 9]
df = df[df.ADMTYPE != 3]
# remove unkonwn general offense categories
df = df[df.OFFGENERAL != 9]
# remove year of mandatory prison release column
df = df.drop(columns=['MAND_PRISREL_YEAR'])
# remove year of projected prison release column
df = df.drop(columns=['PROJ_PRISREL_YEAR'])
# remove year of parole eligibility column
df = df.drop(columns=['PARELIG_YEAR'])
# remove unknown admission year datapoints
df = df[df.ADMITYR != 9999]
# remove unknown maximum sentence length datapoints
df = df[df.SENTLGTH != 9]
# remove unknown offense detail datapoints
df = df[df.OFFDETAIL != 99]
# remove unknown race datapoints
df = df[df.RACE != 9]
# remove unknown age at admission datapoints 
df = df[df.AGEADMIT != 9]
# remove unknown release year datapoints
df = df[df.RELYR != 9999]
# remove unknown and other release type datapoints
df = df[df.RELTYPE != 9]
df = df[df.RELTYPE != 3]
# remove unknown age at release datapoints
df = df[df.AGERLSE != 0]
# remove TIMESRVD_REL 
df = df.drop(columns=['TIMESRVD_REL'])
# df = df[df.TIMESRVD_REL != 9]
# create a new column of TIMESRVD where value is the RELYR - ADMITYR
df['TIMESRVD'] = df['RELYR'] - df['ADMITYR']

print(df)