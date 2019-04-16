---
layout: page
title: Data Cleaning
subtitle: 
bigimg: /img/start.jpg
---
## Changing values in different columns

We can see that the following columns are all listed based on integers, which have corresponding values. In order to get bettervisualization, I will change all of them to strings. Those Columns are:
- three color columns (Color1, Color2, Color3)
- two breed columns (breed1, breed2)
- MaturitySize
- FurLength
- Vaccinated
- Dewormed
- Sterilized, 
- Health
- DataType
- Gender


#### Change the Color to Strings based on color_labels.csv

```
df[['Color1','Color2','Color3']] = df[['Color1','Color2','Color3']].replace([1,2,3,4,5,6,7],['Black','Brown','Golden','Yellow','Cream','Gray','White'])

df[['Color1','Color2','Color3']] = df[['Color1','Color2','Color3']].replace(0,'none')
```

#### Change the top 5 dog/cat breeds to names

```
df[['Breed1','Breed2']] = df[['Breed1','Breed2']].replace([307,179,205,109,20],['Mixed breeds','Poddle','Shih Tzu','Golden Retriever','Ibizan Hound'])
df[['Breed1','Breed2']] = df[['Breed1','Breed2']].replace([266,265,264,299,292],['Domestic short hair','Domestic medium hair','Domestic long hair','Tabby','Siamese'])
```

#### Change the Maturity Size

```
# 1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large, 0 = Not Sure
df[['MaturitySize']] = df[['MaturitySize']].replace([0,1,2,3,4],['Not Sure','Small','Medium','Large','Extra Large'])
```

#### Change the Fur Length

```
# 1 = Short, 2 = Medium, 3 = Long, 0 = Not Sure
df[['FurLength']] = df[['FurLength']].replace([0,1,2,3],['Not Sure','Short','Medium','Long'])
```

#### Change the Vacinated, Dewormed, Sterilized

```
# Vaccinated (1 = Yes, 2 = No, 3 = Not Sure)
# Dewormed - Pet has been dewormed (1 = Yes, 2 = No, 3 = Not Sure)
# Sterilized - Pet has been spayed / neutered (1 = Yes, 2 = No, 3 = Not Sure)
df[['Vaccinated']] = df[['Vaccinated']].replace([1,2,3],['Yes','No','Not Sure'])
df[['Dewormed']] = df[['Dewormed']].replace([1,2,3],['Yes','No','Not Sure'])
df[['Sterilized']] = df[['Sterilized']].replace([1,2,3],['Yes','No','Not Sure'])
```

#### Change the Health

```
# 1 = Healthy, 2 = Minor Injury, 3 = Serious Injury, 0 = Not Sure
df[['Health']] = df[['Health']].replace([0,1,2,3],['Not Sure','Healthy','Minor Injury','Serious Injury'])
```

#### Change the DataType

```
# 1 = Dog, 2 = Cat
df[['Type']] = df[['Type']].replace([1,2],['Dog','Cat'])
```

#### Change the Gender

```
# 1 = Male, 2 = Female, 3 = Neutered/Sprayed
df[['Gender']] = df[['Gender']].replace([1,2,3],['Male','Female','Neutered/Sprayed'])
```

#### Drop unuseful columns and drop the AdoptionSpeed = null rows

```
df = df.drop(df['AdoptionSpeed'].isnull() == True)
df = df.drop(['PhotoAmt','RescuerID','State','VideoAmt'], axis = 1)
```

#### Save as csv in order to import to Tableau and will be easier for further plots in python

```
df.to_csv('cleaned-data.csv')
```

### Here is what I got after cleaning the dataset:

![GW Data Science logo](/img/gwdsp.png)
