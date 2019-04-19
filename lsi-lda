---
layout: page
title: Natural Language Processing
subtitle: LDA & LSI
bigimg: /img/start.jpg
---

## LDA Model

codes to apply LDA

```
lda = models.LdaModel(corpus=corpra, num_topics=t, id2word=D)

print('LDA model')
for index in range(0,t):
    # top 9 topics
    print("Topic Number %s:" % str(index+1), lda.print_topic(index, 9))
print("-" * 120)
```
Screen shot!!

## LSI Model

codes to apply LSI

```
lsi = models.LsiModel(corpus=corpra, num_topics=t, id2word=D)

print('LSI model')
for index in range(0,t):
    # top 9 topics
    print("Topic Number %s:" % str(index+1), lsi.print_topic(index, 9))
print("-" * 117)
```

screen shot!!

## Randomly pick one description from test to predict similarity.
```
import random
i = random.randint(1,3948) # since my test dataset has 3498 values 
print(i)
test_data = Test.loc[i,'Description']
print('-----This is the description from test that I am going to predict:-----')
print(test_data)
```

screen shot!!

## LDA similarity
```
# compare LDA model and LSI model to predict similarity.
lda_i = similarities.MatrixSimilarity(lda[corpra])
m = D.doc2bow(cleandata(test_data))
# perform some queries
similar_lda = lda_i[lda[m]]
# Sort the similarities
LDA = sorted(enumerate(similar_lda), key=lambda item: -item[1])
# Top 10 most similar documents:
print(LDA[:10])
# the most similar document
doc_id, similarity = LDA[1]
print(train_data[doc_id][:100])
```

screen shot!!

## LSI similarity
```
# Do the same similarity queries by using LSI model
lsi_i = similarities.MatrixSimilarity(lsi[corpra])
similar_lsi = lsi_i[lsi[m]]
LSI = sorted(enumerate(similar_lsi), key=lambda item:-item[1])
print(LSI[:10])
doc_id_lsi, similarity_lsi = LSI[1]
print(train_data[doc_id][:1000])
```

screen shot!!


## Here is where we can insert an image:

![GW Data Science logo](/img/gwdsp.png)
