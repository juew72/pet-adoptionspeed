---
layout: page
title: Conclusion
bigimg: /img/start-dog.jpg
---

* From visualization: 

  * the physical characteristics of age scaled in months, cat or dog, colors of pet, gender, maturity size, fur length, any injury, a specific breed of cats or dog, have impacts on adoption speed.

  * young pets are adopted fast and most of them are adopted compared to old pets.
 
  * male pets are adopted faster than female pets even though previous study shows female pets might be popular.
 
  * adopter prefer longer coat than shorter coat.
 
* From NLP: 

  * Multinominal model has 35% of accuracy; Random Forest with 2-gram vectorizer has 42.2% of accuracy; Random Forest with Tf-IDF has 43% of accuracy.
 
  * Problem is that there is other language in the description.
  
  * Some descriptions only has characters like :) , which will be removed after text cleaning process.
  
  * Maybe can try word2vec.
 
* Further Improvements:

  * In the ‘Description’ variable, even though most of the sentences are written in English, there are still some values are written in Chinese or Malay. Separating into different language bases and do natural language processing. 
  * Another distinct method may be considered to apply to predict the adoption speed, such as using XGBoost for classifying, which follows a sequential method and compare the results to the best Random Forest model, which applies random parallel method. Since to classify 5 labels with a supervised learning method might not obtain an ideal accuracy score. 
  * Another prediction could be further supported by combining the ‘AdoptionSpeed’ variable into ‘Being adopted’ and ‘Not being adopted’, and then try the same process might increase the accuracy.
