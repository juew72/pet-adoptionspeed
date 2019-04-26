---
layout: post
title: Machine Learning Application
subtitle: Multinomial Naive Bayes & Random Forest
bigimg: /img/home-cat.jpg
---

* The two models on NLP chosen for ‘Description’ variable and ‘AdoptionSpeed’ variable are Multinomial Naïve Bayes Classifier and ensemble method classification. On the first try, Multinomial Naïve Bayes classifier is applied since it provides a nice baseline for several variants of a classifier, the multinomial variant will be the one most suitable for word counts. 

* The Multinomial Naïve Bayes model resulted in a score of 35% of accuracy. 

* Classifiers tend to have some parameters, trying all different parameter is not possible to operate, however, it is feasible to run exhaustive searches of the best parameters on a grid of values, including all classifiers with bi-grams or monogram, with or without TF-IDF, or number of parameters, or number of depth in Random Forest.

* After grid searching, the best parameters should apply to random forest from Bi-gram vectorizer has the number of estimators as 300 and the maximum number of levels in each decision tree as 90. The best parameters from TF-IDF vectorizer as 300 of trees with no maximum number of levels in each decision tree. 

* The accuracy score of Random Forest Classifier from Bi-gram is 42.2%. The accuracy score of Random Forest Classifier from TF-IDF vectorizer is 43%. 
