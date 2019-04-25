# import all packages
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import nltk
nltk.download('punkt')
import re
from gensim import models, corpora
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import similarities
# Split dataset package
from sklearn.model_selection import train_test_split
# Random forest packages
from sklearn.feature_extraction.text import TfidfVectorizer as tfidfV
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report as report
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
import string
#Evaluation on best model
from sklearn.metrics import precision_recall_fscore_support as f_score
from sklearn.metrics import accuracy_score as accuracy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
# set the number of columns to display
pd.set_option('display.max_columns', 22)
pd.set_option('display.width', 1000)
# ------------------------------------------------------------------------------------
# import datasets
df = pd.read_csv('Data/cleaned-data.csv')
train = pd.read_csv('Data/cleaned-train.csv')
test = pd.read_csv('Data/cleaned-test.csv')
# ------------------------------------------------------------------------------------
# fill out all NaN values under Description column with 'For Adoption'
train['Descrption'] = train['Description'].fillna('For Adoption', inplace = True)

train = train[['Description','AdoptionSpeed']]
# ------------------------------------------------------------------------------------
# I use the same cleandata function as LDA/LSI model
# define stopwords, lemmatizer, and data cleaning process
stop_words = set(stopwords.words("english"))
# Lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
# Stemming
stemming = nltk.PorterStemmer()

def cleandata(review) :
    clean_des = re.sub('[^a-zA-Z]', ' ', str(review)) # Remove punctuation/words not starting with alphabet
    clean_des = clean_des.lower() # make words lower cases
    words = word_tokenize(clean_des) # tokenize
    words = [w for w in words if not w in stop_words] # stop words removal
    words = [stemming.stem(word) for word in words] # Stemming
    words = [wordnet_lemmatizer.lemmatize(w) for w in words] #Lemmatize words
    return words
# ------------------------------------------------------------------------------------
# Build Machine Learning Classifiers with Random Forest model and GridSearchCV
# Need to calculate the length and punctuation percentage of each description
# 1st: calculate length of message without counting space in
train['length'] = train['Description'].apply(lambda length: len(length) - length.count(" "))

#2nd: function of puncutuation number to apply on every description
def punct_percentage(description):
    count = sum([1 for symbol in description if symbol in string.punctuation]) # string.punctuation defined above
    return 100 * round(count/(len(description) - description.count(" ")), 3)

train['punctuation-percentage'] = train['Description'].apply(lambda des: punct_percentage(des))

print(train.head(3))
# ------------------------------------------------------------------------------------
# Exploring parameters using GridSearchCV
# TF-IDF
tfidf_vectorizer = tfidfV(analyzer=cleandata)
X_tfidf = tfidf_vectorizer.fit_transform(train['Description'])
X_tfidf_clf = pd.concat([train['length'], train['punctuation-percentage'],
                         pd.DataFrame(X_tfidf.toarray())], axis=1)

# CountVectorizer
cv_vectorizer = CountVectorizer(ngram_range=(2,2),analyzer=cleandata)
X_cv = cv_vectorizer.fit_transform(train['Description'])
X_cv_clf = pd.concat([train['length'], train['punctuation-percentage'],
                                   pd.DataFrame(X_cv.toarray())], axis=1)
# ------------------------------------------------------------------------------------
# For CountVectorizer
rf = RandomForestClassifier()
param = {'n_estimators': [10, 150, 300],
        'max_depth': [30, 60, 90, None]}

gs_cv = GridSearchCV(rf, param, cv=5, n_jobs=-1)# n_jobs=-1 for parallelizing search
gs_cv_fit = gs_cv.fit(X_cv_clf, train['AdoptionSpeed'])
gs_cs_df = pd.DataFrame(gs_cv_fit.cv_results_).sort_values('mean_test_score', ascending=False)
print(gs_cs_df.head(3))
# ------------------------------------------------------------------------------------
# For TF-IDF
gs_tfidf = GridSearchCV(rf, param, cv=5, n_jobs=-1)# n_jobs=-1 for parallelizing search
gs_tfidf_fit = gs_tfidf.fit(X_tfidf_clf, train['AdoptionSpeed'])
gs_tfidf_df = pd.DataFrame(gs_tfidf_fit.cv_results_).sort_values('mean_test_score', ascending=False)
print(gs_tfidf_df.head(3))
# ------------------------------------------------------------------------------------
# Split the dataset
X=train[['Description', 'length', 'punctuation-percentage']]
y=train['AdoptionSpeed']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape
# ------------------------------------------------------------------------------------
# Evaluation of model: on CountVectorizer
# n_estimator = 300, max_depth = 90
# Variables define
cv = CountVectorizer(ngram_range=(2,2),analyzer=cleandata) # defined before
cv_fit = cv.fit(X_train['Description'])

cv_train = cv_fit.transform(X_train['Description'])
cv_test = cv_fit.transform(X_test['Description'])

X_cv_train = pd.concat([X_train[['length', 'punctuation-percentage']].reset_index(drop=True),
           pd.DataFrame(cv_train.toarray())], axis=1)
X_cv_test = pd.concat([X_test[['length', 'punctuation-percentage']].reset_index(drop=True),
           pd.DataFrame(cv_test.toarray())], axis=1)

# Build model
rf_cv = RandomForestClassifier(n_estimators=300, max_depth=90, n_jobs=-1)
rf_model_cv = rf_cv.fit(X_cv_train, y_train)
y_prediction_cv = rf_model_cv.predict(X_cv_test)

precision, recall, fscore, train_support = f_score(y_test, y_prediction_cv, pos_label='spam', average='micro')
print('Precision: {} --- Recall: {} --- F1-Score: {} --- Accuracy: {}'.format(
    round(precision, 3), round(recall, 3), round(fscore,3), round(accuracy(y_test,y_prediction_cv), 3)))
print(report(y_test, y_prediction_cv))
# ------------------------------------------------------------------------------------
# Making the Confusion Matrix: CountVectorizer
matrixcv = confusion_matrix(y_test, y_prediction_cv)
class_label = ['0','1','2','3','4']
matrixcv_df = pd.DataFrame(matrixcv, index=class_label,columns=class_label)
sns.heatmap(matrixcv_df, annot=True, fmt='d')
plt.title("Confusion Matrix of best CountVectorizer model")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()
# ------------------------------------------------------------------------------------
# Evaluation of model: on tfidfVectorizer
# num_estimator = 300, max_depth = None
# Variables define
tfidf = tfidfV(ngram_range=(2,2),analyzer=cleandata) # defined before
tfidf_fit = tfidf.fit(X_train['Description'])

tfidf_train = tfidf_fit.transform(X_train['Description'])
tfidf_test = tfidf_fit.transform(X_test['Description'])

X_tfidf_train = pd.concat([X_train[['length', 'punctuation-percentage']].reset_index(drop=True),
           pd.DataFrame(tfidf_train.toarray())], axis=1)
X_tfidf_test = pd.concat([X_test[['length', 'punctuation-percentage']].reset_index(drop=True),
           pd.DataFrame(tfidf_test.toarray())], axis=1)

# Build model
rf_tfidf = RandomForestClassifier(n_estimators=300, max_depth=None, n_jobs=-1)
rf_model_tfidf = rf_tfidf.fit(X_tfidf_train, y_train)
y_prediction_tfidf = rf_model_tfidf.predict(X_tfidf_test)

precision, recall, fscore, train_support = f_score(y_test, y_prediction_tfidf, pos_label='spam', average='micro')
print('Precision: {} --- Recall: {} --- F1-Score: {} --- Accuracy: {}'.format(
    round(precision, 3), round(recall, 3), round(fscore,3), round(accuracy(y_test,y_prediction_tfidf), 3)))
print(report(y_test, y_prediction_cv))
# ------------------------------------------------------------------------------------
# Making the Confusion Matrix: tfidfVectorizer
matrixtfidf = confusion_matrix(y_test, y_prediction_tfidf)
class_label = ['0','1','2','3','4']
matrixtfidf_df = pd.DataFrame(matrixtfidf, index=class_label,columns=class_label)
sns.heatmap(matrixcv_df, annot=True, fmt='d')
plt.title("Confusion Matrix of best TF-IDFVectorizer model")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()
