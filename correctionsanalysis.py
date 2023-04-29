import pandas as pd
import plotly.express as px
import numpy as np

prisonData = pd.read_csv('prisonData.csv')
df = pd.read_csv('prisonData1.csv')

# create a dictionary with each key is the state code, and the value is the number of inmates
fips_codes = [1, 2, 4, 5, 6, 8, 9, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37, 38, 39, 40, 42, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 56]
state_codes = ["AL", "AK", "AZ", "AR", "CA", "C0", "CT", "DC", "FL", "GA", "HI", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NY", "NC", "ND", "OH", "OK", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "WA", "WV", "WI", "WY"]
detailed_offense = ["murder", "negligent manslaugher", "rape/SA", "robbery", "assault", "other violent", "burglary", "larceny", "motor vehicle theft", "fraud", "other property", "drugs", "public order", "unspecified"]
races = ["white", "black", "hispanic", "other"]


total_prisoners = len(df)
hispanic_prisoners = len([race for race in df['RACE'] if race == 3])
print(total_prisoners)
print(hispanic_prisoners)
print(hispanic_prisoners/total_prisoners)

# get the top 5 states with the most prison releases
top5States = df['STATE'].value_counts().head(5)
top5StatesList = top5States.index.tolist()
# create a new dataframe for each of those states
floridaDF = df[df['STATE'] == '12']
texasDF = df[df['STATE'] == '48']
illinoisDF = df[df['STATE'] == '17']
newyorkDF = df[df['STATE'] == '36']
northcarolinaDF = df[df['STATE'] == '37']

floridaDF.head()
texasDF.head()
illinoisDF.head()
newyorkDF.head()
northcarolinaDF.head()

# create a histogram of time served
fig = px.histogram(prisonData, x="TIMESRVD", nbins=100, title="Time Served by Inmates")
fig.show()

# get the most freuent offense type
mostFrequentOffDetail = prisonData['OFFDETAIL'].value_counts().idxmax()
print(mostFrequentOffDetail)

# count the number of females and males
numberOfMales = prisonData['SEX'].value_counts()[1]
numberOfFemales = prisonData['SEX'].value_counts()[2]

stateInmates = {}
states = []
for state in prisonData['STATE'].unique():
    numberOfInmates = prisonData['STATE'].value_counts()[state]
    states.append(state)
    # find index of state in fips_codes
    index = fips_codes.index(state)
    # get state code for that fips 
    stateCode = state_codes[index]
    stateInmates[stateCode] = numberOfInmates

# print sorted states
print(sorted(states))

# create a dataframe from the dictionary
df = pd.DataFrame(list(stateInmates.items()),columns = ['state_code','number_of_inmates'])

fig = px.choropleth(df,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='number_of_inmates',
                    color_continuous_scale="sunsetdark", 
                    
)

fig.update_layout(
      title_text = '1991-2017 Prisoners Released by State',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45, 
         )

fig.show()

stateCrimes = {}
for state in prisonData['STATE'].unique():
    # most popular offense type per state
    mostFrequentOffDetail = prisonData[prisonData['STATE'] == state]['OFFDETAIL'].value_counts().idxmax()
    # find index of state in fips_codes
    index = fips_codes.index(state)
    # get state code for that fips 
    stateCode = state_codes[index]
    stateCrimes[stateCode] = mostFrequentOffDetail

# create a dataframe from the dictionary
df2 = pd.DataFrame(list(stateCrimes.items()),columns = ['state_code','most_common_offense'])

fig = px.choropleth(df2,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='most_common_offense',
                    color_continuous_scale="sunsetdark", 
                    
)

fig.update_layout(
      title_text = '1991-2017 Most Common Offenses by State',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45, 
         )

fig.show()

# create a new dataframe that only includes years 2010-2020
prisonData2 = prisonData[prisonData['RELYR'] >= 2010]


stateCrimes = {}
for state in prisonData2['STATE'].unique():
    # most popular offense type per state
    mostFrequentOffDetail = prisonData2[prisonData2['STATE'] == state]['OFFDETAIL'].value_counts().idxmax()
    # find index of state in fips_codes
    index = fips_codes.index(state)
    # get state code for that fips 
    stateCode = state_codes[index]
    stateCrimes[stateCode] = mostFrequentOffDetail

# create a dataframe from the dictionary
df2 = pd.DataFrame(list(stateCrimes.items()),columns = ['state_code','most_common_offense'])

fig = px.choropleth(df2,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='most_common_offense',
                    color_continuous_scale="sunsetdark", 
                    
)

fig.update_layout(
      title_text = '2010-2020 Most Common Offenses by State',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45, 
         )

fig.show()


