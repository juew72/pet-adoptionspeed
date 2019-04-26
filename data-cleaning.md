---
layout: page
title: Data Cleaning
subtitle: 
bigimg: /img/start-dog.jpg
---
## Changing values in different columns

The following columns are all listed based on integers, which have corresponding values. In order to get better visualization, I will change all of them to strings. In specific, some values under Name column has 'No name yet', in order to get cleaned dataset, I change them to 'No Name', which are the same as null values. 

- three color columns (Color1, Color2, Color3)

- two breed columns (breed1, breed2)

- MaturitySize

- FurLength

- Vaccinated, Dewormed, Sterilized

- Health

- DataType

- Gender

- Name

---
---
#### Change the Color to Strings based on color_labels.csv

```
# train:
train[['Color1','Color2','Color3']] = train[['Color1','Color2','Color3']].replace([1,2,3,4,5,6,7], ['Black','Brown','Golden','Yellow','Cream','Gray','White'])
train[['Color1','Color2','Color3']] = train[['Color1','Color2','Color3']].replace(0,'none')

# test:
test[['Color1','Color2','Color3']] = test[['Color1','Color2','Color3']].replace([1,2,3,4,5,6,7],['Black','Brown','Golden','Yellow','Cream','Gray','White'])
test[['Color1','Color2','Color3']] = test[['Color1','Color2','Color3']].replace(0,'none')

# df:
df[['Color1','Color2','Color3']] = df[['Color1','Color2','Color3']].replace([1,2,3,4,5,6,7]，['Black','Brown','Golden','Yellow','Cream','Gray','White'])
df[['Color1','Color2','Color3']] = df[['Color1','Color2','Color3']].replace(0,'none')
```

#### Change the top 5 dog/cat breeds to names

```
# train:
train[['Breed1','Breed2']] = train[['Breed1','Breed2']].replace([307,179,205,109,20],['Mixed breeds','Poddle','Shih Tzu','Golden Retriever','Ibizan Hound'])


train[['Breed1','Breed2']] = train[['Breed1','Breed2']].replace([266,265,264,299,292],['Domestic short hair','Domestic medium hair','Domestic long hair','Tabby','Siamese'])

# test:
test[['Breed1','Breed2']] = test[['Breed1','Breed2']].replace([307,179,205,109,20],['Mixed breeds','Poddle','Shih Tzu','Golden Retriever','Ibizan Hound'])


test[['Breed1','Breed2']] = test[['Breed1','Breed2']].replace([266,265,264,299,292],['Domestic short hair','Domestic medium hair','Domestic long hair','Tabby','Siamese'])

# df:
df[['Breed1','Breed2']] = df[['Breed1','Breed2']].replace([307,179,205,109,20],['Mixed breeds','Poddle','Shih Tzu','Golden Retriever','Ibizan Hound'])


df[['Breed1','Breed2']] = df[['Breed1','Breed2']].replace([266,265,264,299,292],['Domestic short hair','Domestic medium hair','Domestic long hair','Tabby','Siamese'])
```

#### Change the Maturity Size
1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large, 0 = Not Sure

```
# train:
train[['MaturitySize']] = train[['MaturitySize']].replace([0,1,2,3,4],['Not Sure','Small','Medium','Large','Extra Large'])

#test:
test[['MaturitySize']] = test[['MaturitySize']].replace([0,1,2,3,4],['Not Sure','Small','Medium','Large','Extra Large'])

#df:
df[['MaturitySize']] = df[['MaturitySize']].replace([0,1,2,3,4],['Not Sure','Small','Medium','Large','Extra Large'])
```

#### Change the Fur Length
1 = Short, 2 = Medium, 3 = Long, 0 = Not Sure

```
# train:
train[['FurLength']] = train[['FurLength']].replace([0,1,2,3],['Not Sure','Short','Medium','Long'])

# test:
test[['FurLength']] = test[['FurLength']].replace([0,1,2,3],['Not Sure','Short','Medium','Long'])

# df:
df[['FurLength']] = df[['FurLength']].replace([0,1,2,3],['Not Sure','Short','Medium','Long'])
```

#### Change the Vacinated, Dewormed, Sterilized
* vaccinated (1 = Yes, 2 = No, 3 = Not Sure)
* Dewormed - Pet has been dewormed (1 = Yes, 2 = No, 3 = Not Sure)
* Sterilized - Pet has been spayed / neutered (1 = Yes, 2 = No, 3 = Not Sure)

```
# train:
train[['Vaccinated']] = train[['Vaccinated']].replace([1,2,3],['Yes','No','Not Sure'])
train[['Dewormed']] = train[['Dewormed']].replace([1,2,3],['Yes','No','Not Sure'])
train[['Sterilized']] = train[['Sterilized']].replace([1,2,3],['Yes','No','Not Sure'])

# test:
test[['Vaccinated']] = test[['Vaccinated']].replace([1,2,3],['Yes','No','Not Sure'])
test[['Dewormed']] = test[['Dewormed']].replace([1,2,3],['Yes','No','Not Sure'])
test[['Sterilized']] = test[['Sterilized']].replace([1,2,3],['Yes','No','Not Sure'])

# df:
df[['Vaccinated']] = df[['Vaccinated']].replace([1,2,3],['Yes','No','Not Sure'])
df[['Dewormed']] = df[['Dewormed']].replace([1,2,3],['Yes','No','Not Sure'])
df[['Sterilized']] = df[['Sterilized']].replace([1,2,3],['Yes','No','Not Sure'])
```

#### Change the Health
1 = Healthy, 2 = Minor Injury, 3 = Serious Injury, 0 = Not Sure

```
# train:
train[['Health']] = train[['Health']].replace([0,1,2,3],['Not Sure','Healthy','Minor Injury','Serious Injury'])

# test:
test[['Health']] = test[['Health']].replace([0,1,2,3],['Not Sure','Healthy','Minor Injury','Serious Injury'])

# df:
df[['Health']] = df[['Health']].replace([0,1,2,3],['Not Sure','Healthy','Minor Injury','Serious Injury'])
```

#### Change the DataType
1 = Dog, 2 = Cat

```
# train:
train[['Type']] = train[['Type']].replace([1,2],['Dog','Cat'])

# test:
test[['Type']] = test[['Type']].replace([1,2],['Dog','Cat'])

# df:
df[['Type']] = df[['Type']].replace([1,2],['Dog','Cat'])
```

#### Change the Gender
1 = Male, 2 = Female, 3 = Neutered/Sprayed

```
# train:
train[['Gender']] = train[['Gender']].replace([1,2,3],['Male','Female','Neutered/Sprayed'])

# test:
test[['Gender']] = test[['Gender']].replace([1,2,3],['Male','Female','Neutered/Sprayed'])

# df:
df[['Gender']] = df[['Gender']].replace([1,2,3],['Male','Female','Neutered/Sprayed'])
```

#### Change the Name variable
* no name yet -> No name;
* Nan -> No name;
* No Name -> No name;

```
# train:
train['Name'] = train['Name'].replace(['No Name Yet', 'No Name'],['No name','No name'])
train['Name'] = train['Name'].fillna('No name')

# test:
test['Name'] = test['Name'].replace(['No Name Yet', 'No Name'],['No name','No name'])
test['Name'] = test['Name'].fillna('No name')

# df:
test['Name'] = test['Name'].replace(['No Name Yet', 'No Name'],['No name','No name'])
df['Name'] = df['Name'].fillna('No name')
```

#### Drop unuseful columns and drop the AdoptionSpeed = null rows

```
# Drop unuseful columns and drop the AdoptionSpeed = null rows

#train: 
train_null = np.array(train[train['AdoptionSpeed'].isnull() == True].index)
train = train.drop(train_null)
train = train.drop(['PhotoAmt','RescuerID','State','VideoAmt'], axis = 1)

#test:
test = test.drop(['PhotoAmt','RescuerID','State','VideoAmt'], axis = 1)

# df:
df_nan = np.array(train[train['AdoptionSpeed'].isnull() == True].index)
df = df.drop(df_nan)
df = df.drop(['PhotoAmt','RescuerID','State','VideoAmt'], axis = 1)
```


### Here is what I got after cleaning datasets(train, test):

![GW Data Science logo](/img/cleaned-data.png)
