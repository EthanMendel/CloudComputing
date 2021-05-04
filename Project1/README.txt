DocWordCount Execution Instructions:
(Replace <username> with your 49er username and use  your 49er password)
1)Connect to the dabs-hadoop cluster
	$ ssh dabs-hadoop.uncc.edu -l <username>
2)Using a different terminal (not the one you ran ssh on), upload the DocWordCount.java File
	$ scp DocWordCount.java <username>@dsba-hadoop.uncc.edu:/users/<username>
2)Additionally upload the files you want to use as input files
	$ scp inputFile <username>@dsba-hadoop.uncc.edu:/users/<username>
3)On the Hadoop terminal (the one you ran ssh on), make a new folder and move the input files to this folder to use later
	$ hadoop fs -mkdir /user/<username>/input
	$ hadoop fs -put inputFile /user/<username>/input
4)Compile and run the DocWordCount class
	$ mkdir build
	$ javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/* DocWordCount.java -d build -Xlint
	$ jar -cvf docwordcount.jar -C build/ .
	$ hadoop jar docwordcount.jar org.myorg.DocWordCount /user/<username>/input /user/<username>/output
5)To look at the output
	$ hadoop fs -cat /user/<username>/output/*
6)Move the output from HDFS to your account
	$ mkdir result
	$ Hadoop dfs -get /user/emendel/output/* result
7)Download onto your local system using a different terminal (not the one you ran ssh on)
	$ scp <username>@dsba-hadoop.uncc.edu:/users/<username>/result/* /<local directory>