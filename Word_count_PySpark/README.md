<h2> Word Count Using PySpark</h2>
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
<p>
    <img src="https://github.com/rkhatu97/Projects_Python/blob/master/Word_count_PySpark/spark_session.png" />
</p>



