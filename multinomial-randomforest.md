---
layout: page
title: Natural Language Processing
subtitle: Multinominal &  Random Forest
bigimg: /img/start-dog.jpg
---

## Multinominal Classification

* Code

```
from sklearn.naive_bayes import MultinomialNB
tfvec = tfidfV(stop_words='english', ngram_range=(1, 1), lowercase=False)
model = Pipeline([('vectorizer', tfvec),('rf', MultinomialNB(alpha=0.0))])
```

* Accuracy:

![multinominal accuracy](/img/multinominal-accuracy.png)

*Analysis:*
 * Multinomial Naïve Bayes classifier is applied since it provides a nice baseline for several variants of a classifier, the multinomial variant will be the one most suitable for word counts. After load the description and adoption speed into ‘X’ and ‘y’ variables respectively with train and valid, the first thing needs to do is text preprocessing, such as tokenization, lower cases, lemmatizing. Stop-words removal is included in TF-IDF vectorizer, which computes relative frequency a word appears in the description and compared the frequency across all description in the dataset. Then fit the model, and the Multinomial Naïve Bayes model resulted in a score of 35% of accuracy. 
 * Classifiers tend to have some parameters, trying all different parameter is not possible to operate, however, it is feasible to run exhaustive searches of the best parameters on a grid of values, including all classifiers with bi-grams or monogram, with or without TF-IDF, or number of parameters, or number of depth in Random Forest.

## Random Forest - 2-grams vectorizer

* Code

```

```

* the ensemble model shows: n_estimator=300, max_depth=90 has the best result

* Accuracy 

![2-grams vectorizer accuracy](/img/cv-accuracy.png)

* Confusion Matrix

![cv confusion matrix](/img/cv-matrix.png)

## Random Forest - TF-IDF vectorizer

* Code

```

```

* The ensemble model shows: n_estimator=300, max_depth=None has the best result

* Accuracy

![tf-idf vectorizer accuracy](/img/tfidf-accuracy.png)

* Confusion Matrix

![tf-idf confusion matrix](/img/tfidf-matrix.png)

*Analysis:*
 * After grid searching, the best parameters should apply to random forest from Bi-gram vectorizer has the number of estimators as 300 and the maximum number of levels in each decision tree as 90. However, the best parameters from TF-IDF vectorizer as 300 of trees with no maximum number of levels in each decision tree. 
 * The accuracy score of Random Forest Classifier from Bi-gram is 42.2%. The accuracy score of Random Forest Classifier from TF-IDF vectorizer is 43%.
 * The confusion matrix indicates that the label4, which is no pet being adopted, predicted best among other labels, following by label2, which is adopted within 1 month.
