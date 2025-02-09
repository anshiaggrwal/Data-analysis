#the whether dataset is a time series data set with per hour information about the whether conditions at a particular location
#it records temperature, dew point temp, relative humidity , wind speed visibility , pressure and conditions
import pandas as pd
df=pd.read_csv("weather.csv")

#analysing the data
print(df.head(5),"\n")    
print(df.shape,"\n")          #will show the shape of our data
print(df.index,"\n")          #will provide the range of the data
print(df.columns,"\n")        #will show the names of each column
print(df.dtypes,"\n")         #will show the datatypes of each col
print(df["Weather"].unique(),"\n") #will provide count of all unique values in provided col
print(df.nunique(),"\n")           #will show the no of unique elements in each col
print(df.count(),"\n")             #will show count of all non null values in each col
print(df.value_counts(),"\n")      #will provide all unique values in provided col with its count
print(df.info(),"\n")              #provides basic info  about the dstaframe

# Questions
# find all the unique 'Wind Speed' values in a data
print(df['Wind Speed_km/h'].unique(),"\n")

#Find the num of times when the weather is exactly clear
#1st way
print(df.Weather.value_counts(),"\n")
#filter out values with clear weather and then print them
print(df[df.Weather=="Clear"],"\n")
#groupby
print(df.groupby("Weather").get_group('Clear'),"\n") #get_group is used after group by to choose the filter

#no of times when the wind speed was exactly 4 km/h
print(df.groupby("Wind Speed_km/h").get_group(4),"\n")

#Find out all the null values in the data
print(df.isnull(),"\n")
print(df.isnull().sum(),"\n")  #will print the count of null values in each col

#rename the column weather of data fl=rame to weather condition
df.rename(columns={"Weather":"weather condition"}, inplace=True)
print(df.head(3),"\n")

#find mean visibility
print(df.Visibility_km.mean(),"\n")

#find standard deviation of pressure column in this data
print(df.Press_kPa.std(),"\n")

#find variance of relative humidity in this data
print(df['Rel Hum_%'].var(),"\n")

#find all instances hwen snow was recorded
#1st let see the count 
print(df['weather condition'].value_counts(),"\n")
#lets see all the instances when snow was recorded
print(df[df["weather condition"]=="Snow"],"\n")
#but there arw more columns where other snow like conditions are encountered
print(df[df["weather condition"].str.contains("Snow")],"\n")

#find all instances when wind speed is above 24 and visibility is 25
print(df[(df['Wind Speed_km/h']>24) & (df['Visibility_km']==25)],"\n")

#find the mean value of each column against eqch weather condition
print(df.groupby("weather condition").mean(numeric_only=True),"\n") #numeric_only=True beacause dataset condains date and time col also

# find max and min value of each column against each weather cndition
print(df.groupby("weather condition").min(),"\n")
print(df.groupby("weather condition").max(),"\n")

#show all records where weather condition is fog
print(df.groupby("weather condition").get_group("Fog"),"\n")

# find all in instances when weather is clear or visibility is above 40
print(df[(df["weather condition"]=="Clear") | (df["Visibility_km"]>40)],"\n")