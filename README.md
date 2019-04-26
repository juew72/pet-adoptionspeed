
# DATS6501 Capstone project.

The purpose of this project is to demonstrate data mining techniques, visualization, and Natural Language Processing (NLP) using the metadata of pet adoption from the Kaggle website for pet adoption speed prediction and trends. Visualization focused on the following data: age scaled in months, cat or dog, colors of pet, gender, maturity size, fur length, whether vaccinated or dewormed or sterilized, any injury, top 5 breeds of cat and dog separately, name, and adoption speed. NLP Modeling focused on the following data: description of pets and adoption speed. Multinomial Naïve Bayes Classifier correctly assessed the adoption speed based on descriptions of pets with 35% accuracy. The ensemble method to find the best Random Forest model with 2-Grams vectorizer and TF-IDF vectorizer also applied. The Random Forest Classifier predicted adoption speed based on descriptions with 45% of accuracy. Finally, the limitation and further improvements are provided, and the review of results is extracted.

The original data can be downloaded from : https://www.kaggle.com/c/petfinder-adoption-prediction/data

# Running the code

* Python 3

  * Packages used in this project:
  
   * Pandas
   * numpy
   * matplotlib
   * plotly
   * seaborn
   * wordcloud
   * scipy.misc
   * re
   * random
   * nltk   
    * use nltk.downloader() after installation finished to install packages: stopwords; punkt; wordnet
   * gensim
   * sklearn
   * string

* There are four python files, run it based on order as follow:

 * Data Cleaning.ipynb: clean the row data downloaded from Kaggle

 * Visualization.ipynb: include plotly visualizations and word cloud

   * Tableau visualizations are included inside Visualization folder.
  
   * Plotly visualization are ploted in python script
  
   * D3 visualizations are two HTML files: gender-dog.html and gender-cat.html

 * NLP.ipynb: include natural language processing

 * nlp2.py: ensemble model code. Need to connect to AWS or GCP or it will take an hour to run the code.

* The code also published on Zenedo: https://zenodo.org/record/2651913#.XMKgVZNKh24
