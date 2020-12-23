# Projects_Python
<h2>Credit Card Fraud Detection</h2>
<p>A credit card transaction dataset is used to perform exploratory data analysis and apply machine learning algorithm to predict fraud transaction. The data set consists of the details related to transaction, card use and details of owner. The dataset was in json format saved as text file. The dataset consists of 29 columns and 786363 rows. The goal is to derive insights like multiple card swipe, amount reversals, find insights with respect to transaction amount and build a machine learning model to predict fraud.</p>
<p>Data stored in HDFS and then imported using PySpark in python. The imported data was in PySpark data frame which further converted to pandas data frame for further modifications and analysis</p>
<p>Model Used:</p>
<p>Logistic Regression</p>
<p>
    <img src="https://github.com/rkhatu97/Projects_Python/blob/master/Credit_card_fraud_detection/logistic_regression.png" />
</p>
<p>Gradient Boosting</p>
<p>
    <img src="https://github.com/rkhatu97/Projects_Python/blob/master/Credit_card_fraud_detection/GBM.png" />
</p>
<p>Random Forest Classifier</p>
<p>
    <img src="https://github.com/rkhatu97/Projects_Python/blob/master/Credit_card_fraud_detection/random_forest.png" />
</p>
<h3> Word Count Using PySpark</h3>
<p>PySpark package was used to import Sparksession. Sparksession was initialized with application name word-count.</p>
<p>Using sparksession.read.test() README.md file was imported from HDFS, various SQL function were imported form pyspark package like regexp_replace, trim, col, and lower using this the punctuation in the file were removed.</p>
<p>Further, functions like split and explode were used to bring one word per line orientation.</p>
<p>The words were order by count of words in ascending order using orderby() function.</p>
<p>After following the steps provided in the document and processing data from README.md file following insights are derived:</p>
<p>a)	How many times is the word "Hadoop" counted when the tutorial has printed out all the word counts?</p>
<p>The word “Hadoop” appeared 9 times.</p>
<p>b)	Which is the most common word used in the file? How many times does the word occur?</p>
<p>“Spark” is the most common word in the file, and it appears 38 times.</p>
<p>c)	Which word occurs the fewest times? How many time does the word occur?</p>
<p>“Graphs” is the word that appears fewest times, it occurs 1 time only.</p>




