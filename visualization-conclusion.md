---
layout: page
title: Visualization
subtitle: more visualization & conclusion
bigimg: /img/start.jpg
---

### Adoption Speed
```
\{\% include adoptionspeed.html \%\}
```
{% include adoptionspeed.html %}


### Maturity Size

{% include maturitysize.html %}

Analysis:We can see that maturity size isn't very important. Medium sized pets are most common and they have slightly more chances to be not adopted; There are almost no Extra Large pets. I hope it means that their owners like them and there is no need for them to be adopted :) I wanted to gave a look at different pets, so I showed examples of pictures of most common breeds for each maturity size of cats and dogs; I think not all data is entirely correct: sometimes short haired cats have breed with "medium hair", not sure that all breeds are entirely correct. Some photoes have bad quality;


### Breed
```
\{\% include breed.html \%\}
```
{% include breed.html %}

Analysis:
 * It seems that non-pure breed pets tend to be adopted more and faster, especially cats.
 * It seems that not all values of these features are really breeds. Sometimes people simply write that the dogs has a mixed breed, cats often are described as domestic with certain hair length.
 * It seems that most dogs aren't pure breeds, but mixed breeds! My first assumption was wrong.
 * Sometimes people write "mixed breed" in the first fiels, sometimes in both, and sometimes main breed is in the first field and is marked as mixed breed in the second field.


### Color/ Fee/ Health Condition vs Adoption Speed
[Another Link to Tableau](https://public.tableau.com/profile/juew72#!/vizhome/others_15554523598650/ColorFeeHealthConditionAdoptionSpeed?publish=yes/)
```
\{\% include colorfeehealth.html \%\}
```
{% include colorfeehealth.html %}

Analysis:
 * Color: We can see that most common colors are black and brown. Interesting to notice that there are almost no gray or yellow dogs
 * Health-condition: Almost all pets are healthy! Pets with minor injuries are rare and sadly they aren't adopted well. Number of pets with serious injuries is negligible. It is interesting that people prefer non-vaccinated pets. Maybe they want to bring pets to vets themselves... People also prefer non-sterilized pets! Maybe they want puppies/kittens :) Quite important is the fact that when there is no information about health condition, the probability of not being adopted is much higher; Healthy, dewormed and non-sterilized pets tend to be adopted faster! Completely healthy pets are... more likely to be not adopted! I suppose that means that a lot of people pay attention to other characteristics; And healthy pets with no information (not sure value) also tend to be adopted less frequently. Maybe people prefer having information, even if it is negative;
 * Fee: Most pets are free and it seems that asking for a fee slightly desreased the chance of adoption. Also free cats are adopted faster than free dogs -- another plot in python
  * It is interesting that pets with high fee tend to be adopted quite fast! Maybe people prefer to pay for "better" pets: healthy, trained and so on;
  * Most pets are given for free and fees are usually lower than 100 $;
  * Fees for dogs tend to be higher, though these are rare cases anyway.
  * It seems that fees and pet quantity have inversely proportional relationship. The less pets, the higher is the fee. I suppose these single pets are better trained and prepared than most others.


### Name

{% include name.html %}

Analysis: It is worth noticing some things:
 * Often we see normal pet names like "Mimi", "Angel" and so on;
 * Quite often people write simply who is there for adoption: "Kitten", "Puppies";
 * Vety often the color of pet is written, sometimes gender;
 * And it seems that sometimes names can be strange or there is some info written instead of the name;
 * One more thing to notice is that some pets don't have names. Let's see whether this is important: rate of unname in python
  * Less than 10% of pets don't have names, but they have a higher possibility of not being adopted.
  * I have noticed that shorter names tend to be meaningless. Here is an example of some names with 3 characters.
  * And here are names with 1 or 2 characters...


##Conclusions from Visualization:
---
*
---
*
---
*

