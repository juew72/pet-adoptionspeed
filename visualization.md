---
layout: page
title: Visualization
subtitle: Adoption Speed, Age, Gender, Fur Length
bigimg: /img/start-dog.jpg
---

### Adoption Speed

{% include adoption-plotly.html %}

In detail: information is from official kaggle webpage:

0 - Pet was adopted on the same day as it was listed. 

1 - Pet was adopted between 1 and 7 days (1st week) after being listed. 

2 - Pet was adopted between 8 and 30 days (1st month) after being listed. 

3 - Pet was adopted between 31 and 90 days (2nd & 3rd month) after being listed. 

4 - No adoption after 100 days of being listed. (There are no pets in this dataset that waited between 90 and 100 days).


*Analysis:* 
For both dog and cat, the same day adoption has 2.73%; adopted within the 1st week has 20.6%; adopted within the 1st month has 21.7%; adopted within 2-3 months has 26.9% and not being adopted has the highest 28%. Some pets are adopted immediately but this is a rare case. The reason it happened might because of the eager to adopt from people. Someone is willing to adopt a dog or cat, or listed pet is exactly what he or she wants from every aspect, such as breed, color, size, fee, etc. 
 
{% include adoptionspeed.html %}

*Analysis:* 
It shows cat has higher adoption speed than the dog on the same day adoption and adoption happened in the first month. The total number of cats not being adopted is much smaller than the total number of dogs not being adopted (1783 vs 2414). This might because of people’s conception of human-companion animal relationship, and the everyday efforts that required in keeping a good companion-animal guardianship (O’Connor, Coe, Niel, & Jones-Bitton, 2016). The research shows the most of dog adopters assume more effort required and less easiness to take care of pets than cat adopters believe.

### Age

{% include age.html %}

*Analysis:* 
Most of the pets, no matter cat or dog, are young when they are listed, and most of them are less than 25 months old, which is around 2 years old. Even though it is an outlier for both dog and cat, the total number of pets will reach a peak when pets are aged in 2 months.

{% include age-plotly.html %}

*Analysis:*
Most of the pets are adopted within the first 60-month-old, which equals to 5 years old or younger. These young pets are adopted fast and most of them are adopted. There is a huge adoption at the age in 5-month, and they are adopted within 2-3 month, which is consistent with the results of some other studies (Brown et al., 2013; DeLeeuw, 2010). (Diesel et al., 2007) suggests puppies have better looking and are more likely to appeal adopters, that is why they are adopted much faster than older pets. So, there does appear to have a weak relationship between the pet age and the adoption speed, with younger pets, both cat and dog, having a higher possibility of being adopted.


### Gender

{% include gender.html %}

Gender vs Adoption[(Cat)](https://juew72.github.io/pet-adoptionspeed/gender-cat)

Gender vs Adoption[(Dog)](https://juew72.github.io/pet-adoptionspeed/gender-dog)

*Analysis:*
For the cat, there are 4008 female, 3268 male and 1659 neutered or spayed; for the dog, there are 5137 female, 3773 male and 1132 neutered or spayed. In total, the female and male pets are mostly adopted within 1-to-3-months, but male pets are adopted faster than female pets. (Lepper, Kass & Hart, 2002) states that the adopter prefers a female cat or dog over male pets. (Žák et al., 2015) also indicates that male dogs remain significantly longer compared to abandoned female dogs. And there are more female pets than male pets, it is reasonable that more female pets are adopted in each stage of adoption speed.


### Fur Length

{% include furlength.html %}

*Analysis:*
There are more short hair pets than medium or long hair pets. For short hair pets, the largest amount of them is adopted within the 1-to-3-month. However, pets with long hair tend to have a higher opportunity to be adopted, which is consistent with the correlation: the ‘AdoptionSpeed’ value increases as the fur length of pet increases; for example, adding some lengths from short hair to medium hair has a slightly negative, correlational effect on the adoption speed, which makes the pet wait shorter to be adopted.

