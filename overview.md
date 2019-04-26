---
layout: page
title: Metadata Overview
subtitle: overview
bigimg: /img/start-dog.jpg
---

## Where did I find the data?

The data is from [Kaggle Pet Adoption](https://www.kaggle.com/c/petfinder-adoption-prediction/data)



* The original row datasets contain 25 features and 14,993 samples in train.csv and 24 features and 3,972 samples in test.csv.

* Columns are: ‘AdoptionSpeed’, ‘Age’, ‘Breed1’, ‘Breed2’, ‘Color1’, ‘Color2’, ‘Color3’, ‘Description’, ‘Dewormed’, ‘Fee’,‘Fur Length’, ‘Gender’, ‘Health’, ‘MaturitySize’,‘PetID’, 'PhotoAmt', ‘Quantity’, 'RescuerID', 'State',‘Sterilized’, ‘Vaccinated’, 'VideoAmt'.

  * PetID - Unique hash ID of pet profile
  * AdoptionSpeed - Categorical speed of adoption. Lower is faster. This is the value to predict. See below section for more info.
  * Type - Type of animal (1 = Dog, 2 = Cat)
  * Name - Name of pet (Empty if not named)
  * Age - Age of pet when listed, in months
  * Breed1 - Primary breed of pet (Refer to BreedLabels dictionary)
  * Breed2 - Secondary breed of pet, if pet is of mixed breed (Refer to BreedLabels dictionary)
  * Gender - Gender of pet (1 = Male, 2 = Female, 3 = Mixed, if profile represents group of pets)
  * Color1 - Color 1 of pet (Refer to ColorLabels dictionary)
  * Color2 - Color 2 of pet (Refer to ColorLabels dictionary)
  * Color3 - Color 3 of pet (Refer to ColorLabels dictionary)
  * MaturitySize - Size at maturity (1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large, 0 = Not Specified)
  * FurLength - Fur length (1 = Short, 2 = Medium, 3 = Long, 0 = Not Specified)
  * Vaccinated - Pet has been vaccinated (1 = Yes, 2 = No, 3 = Not Sure)
  * Dewormed - Pet has been dewormed (1 = Yes, 2 = No, 3 = Not Sure)
  * Sterilized - Pet has been spayed / neutered (1 = Yes, 2 = No, 3 = Not Sure)
  * Health - Health Condition (1 = Healthy, 2 = Minor Injury, 3 = Serious Injury, 0 = Not Specified)
  * Quantity - Number of pets represented in profile
  * Fee - Adoption fee (0 = Free)
  * State - State location in Malaysia (Refer to StateLabels dictionary)
  * RescuerID - Unique hash ID of rescuer
  * VideoAmt - Total uploaded videos for this pet
  * PhotoAmt - Total uploaded photos for this pet
  * Description - Profile write-up for this pet. The primary language used is English, with some in Malay or Chinese.
  
* Drop the columns 'PhotoAmt', 'VideoAmt', 'RescuerID', 'State'

* breed_labels.csv and color_labels.csv list the number and corresponding breed name or color, so the resulting cleaned dataset removes all number in ‘Breed1’, ‘Breed2’, and 3 color-related columns, and insert the top 5 breed name and all colors correspondingly.

* The top 5 breeds for cat or dog samples cover at least 75% of metadata, and many of the other breeds have less than 5 samples per breed name, or even 1 sample per breed name. 

## Here is where we can insert an image:

![original data](/img/original-data.png)
