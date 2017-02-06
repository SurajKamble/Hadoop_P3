<strong> Hadoop_P3</strong>

Hadoop MapReduce on Google 1-gram data and Twitter JSON data.

<strong>Instructions: </strong>

Clone the repository and get into the particular directory of each prgoram for data analysis.

<strong>For Google 1-gram data Analysis: </strong>

To test via pipes: <code>cat input/* | ./mapUWC.py | sort | ./reduceUWC.py</code>

To run on cluster: <code>hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar 
-input /data/1gram -output myoutput -file *.py -mapper mapUWC.py -reducer reduceUWC.py</code>

<strong>For Twitter data Analysis:</strong>

To test via pipes: <code>cat input/* | ./maptw.py | sort | ./reducetw.py</code>

To run on cluster: <code>hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar 
-input /data/twitter -output myoutput -file *.py -mapper maptw.py -reducer reducertw.py</code>
