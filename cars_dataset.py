import pandas as pd
car=pd.read_csv("cars.csv")

print(car.head(10),"\n")
print(car.shape,"\n")

# Find all the null value in the dataset . if there is any in the col, fill it with the mean of that column
print(car.isnull(),"\n")
print(car.isnull().sum(),"\n")
car.fillna(car.mean(numeric_only=True),inplace=True)
print(car,"\n")
print(car.isnull().sum(),"\n")

# check the different types of make in our dataset and the count of each make 
print(car["Make"].value_counts(),"\n")

# instructions (filtering)
# Show all the records where origin is Asia or Europe
print(car[car["Origin"].isin(["Asia","Europe"])],"\n")
# isin is used to view all those rows provided in it should provide the column name

# remove all records where weight is above 4000   #data cleaning
print(car[car["Weight"]>4000],"\n") #to view all records
print(car[~(car["Weight"]>4000)],"\n")
# now the shape of our data is this [329 rows x 15 columns] earlier it was [432 rows x 15 columns] 

#applying function on column
# increase all  the values of "MPG_City" column by 3
car["MPG_City"]=car["MPG_City"].apply(lambda x:x+3)
print(car.head,"\n")
