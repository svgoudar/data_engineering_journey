```sh
docker pull apache/hive:4.0.0-alpha-1

docker run -d -p 10000:10000 -p 10002:10002 --env SERVICE_NAME=hiveserver2 -v /home/project/data:/hive_custom_data --name myhiveserver apache/hive:4.0.0-alpha-1


docker exec -it myhiveserver beeline -u jdbc:hive2://localhost:10000/


create table Employee(emp_id string, emp_name string, salary  int)  row format delimited fields terminated by ',' ;

show tables;

LOAD DATA INPATH '/hive_custom_data/emp.csv' INTO TABLE Employee;


select * from Employee;
```

### Hands-on lab on Hadoop Map-Reduce 

```sh

curl https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz --output hadoop-3.3.6.tar.gz

tar -xvf hadoop-3.3.6.tar.gz

cd hadoop-3.3.6

bin/hadoop

curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/data.txt --output data.txt

bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar wordcount data.txt output

ls output
cat  output/part-r-00000

BigData 2
Hadoop  1
IBM     1
MapReduce       2



```

### Handson Hadoop cluster node dockerized

```sh
git clone https://github.com/ibm-developer-skills-network/ooxwv-docker_hadoop.git

cd ooxwv-docker_hadoop

docker-compose up -d

docker exec -it namenode /bin/bash


hadoop-env.sh Serves as a master file to configure YARN, HDFS, MapReduce, and Hadoop-related project settings.

core-site.xml Defines HDFS and Hadoop core properties

hdfs-site.xml Governs the location for storing node metadata, fsimage file and log file.

mapred-site-xml Lists the parameters for MapReduce configuration.

yarn-site.xml Defines settings relevant to YARN. It contains configurations for the Node Manager, Resource Manager, Containers, and Application Master.

ls /opt/hadoop-3.2.1/etc/hadoop/*.xml

hdfs dfs -mkdir -p /user/root/input

hdfs dfs -put $HADOOP_HOME/etc/hadoop/*.xml /user/root/input

curl https://raw.githubusercontent.com/ibm-developer-skills-network/ooxwv-docker_hadoop/master/SampleMapReduce.txt --output data.txt

hdfs dfs -put data.txt /user/root/

hdfs dfs -cat /user/root/data.txt
```