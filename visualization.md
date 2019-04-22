---
layout: page
title: Visualization
subtitle: visualizations for main variables
bigimg: /img/start.jpg
---

### Adoption Speed

{% include adoption-plotly.html %}

In detail: information is from official kaggle webpage
0 - Pet was adopted on the same day as it was listed. 
1 - Pet was adopted between 1 and 7 days (1st week) after being listed. 
2 - Pet was adopted between 8 and 30 days (1st month) after being listed. 
3 - Pet was adopted between 31 and 90 days (2nd & 3rd month) after being listed. 
4 - No adoption after 100 days of being listed. (There are no pets in this dataset that waited between 90 and 100 days).

*Analysis:* 
 * some pets were adopted immediately, but no matter for dog or cat, this is a rare case. The reason it could happen might because someone wants to adopt any kind or breed of pet. But, as I said, the majority of pets (no matter dog or cat) is not being adopted at all.
 
{% include adoptionspeed.html %}

*Analysis:* 
 * cat has higher adoption speed than dog: more cats are adopted on the same day compared to the same day adoption on dog.

### Age

{% include age.html %}

{% include age-plotly.html}

Analysis: We can see that most pets are young - maybe after the birth. Also there a lot of pets with an age equal to multiples of 12 - I think than owners didn't bother with the exact age.


We can see that young pets are adopted quite fast and most of them are adopted; Most pets are less than 4 months old with a huge spike at 2 months; It seems that a lot of people don't input exact age and write age in years (or multiples of 12); It could make sense to create some binary variables based on age;


### Gender

{% include gender.html %}

Analysis: 


### Fur Length

{% include furlength.html %}

*Analysis:*
 * most of the pets that have been adopted have short fur and long fur has the least opportunity to be adopted; Pets with long hair tend to have a higher chance of being adopted. Though it could be because of randomness due to low count;

