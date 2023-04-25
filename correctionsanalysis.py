# open tsv file 38492-0001-Data.tsv from the finalproject folder
# read in the file
# convert to a pandas dataframe

import pandas as pd
import re, os

# df = pd.read_csv("/Users/paritashah/Desktop/College/Year3/Term2/BigData/finalproject/38492-0001-Data.tsv", sep='\t')


# # if ADMTYPE = 9, then remove that row
# df = df[df.ADMTYPE != 9]
# # if OFFGENERAL = 9, then remove that row
# df = df[df.OFFGENERAL != 9]
# # if EDUCATION = 9, then remove that row
# df = df[df.EDUCATION != 9]
# # if ADMITYR = 9999, then remove that row
# df = df[df.ADMITYR != 9999]
# # if RELEASEYR = 9999, then remove that row
# df = df[df.RELEASEYR != 9999]
# # if SENTLGTH = 9, then remove that row
# df = df[df.SENTLGTH != 9]
# # if OFFDETAIL = 99, then remove that row
# df = df[df.OFFDETAIL != 99]
# # if RACE = 9, then remove that row
# df = df[df.RACE != 9]

# print(df)


df = pd.read_csv("/Users/paritashah/Desktop/College/Year3/Term2/BigData/finalproject/38492-0003-Data.tsv", sep='\t')

# remove unknown education levels
df = df[df.EDUCATION != 9]
# possibly remove type of prison admission column
# df = df.drop(columns=['ADMTYPE'])
# remove unkown prison admission types
df = df[df.ADMTYPE != 9]
# remove unkonwn general offense categories
df = df[df.OFFGENERAL != 9]
# remove year of mandatory prison release column
df = df.drop(columns=['MAND_PRISREL_YEAR'])
# remove year of projected prison release column
# possible ---tbdm could just remove unknowns 9999 and have 2010 onwards
# df[df.PROJ_PRISREL_YEAR != 9999]
df = df.drop(columns=['PROJ_PRISREL_YEAR'])
# remove year of parole eligibility column
# again, possible could just remove unknowns 9999 and have 2010 onwards-ish
df = df.drop(columns=['PARELIG_YEAR'])
# if ADMITYR is missing, remove 
df = df[df.ADMITYR != 9999]
# if SENTLGTH is missing, remove
df = df[df.SENTLGTH != 9]
# DROP RELYR column
df = df.drop(columns=['RELYR'])
# if RELEASEYR = 9999, then remove that row
# df = df[df.RELYR != 9999]
# if SENTLGTH = 9, then remove that row
# maybe remove this as well 
df = df[df.SENTLGTH != 9]
# if OFFDETAIL = 99, then remove that row
df = df[df.OFFDETAIL != 99]
# if RACE = 9, then remove that row
df = df[df.RACE != 9]
# drop AGEADMIT column
df = df.drop(columns=['AGEADMIT'])
# DROP RELTYPE column
df = df.drop(columns=['RELTYPE'])
# DROP AGERLSE column
df = df.drop(columns=['AGERLSE'])
# remove TIMESRVD_REL if it is missing
df = df[df.TIMESRVD_REL != 9]

print(df)