Tutorial
=============

# connecting to EMR
# launch EMR from AWS

Launch a cluster and ssh into the master as a hadoop user

If the permissions for the pem file are unrestricted or 
you just created the file, you will likely need to use 
chmod 400 yourpem.pem 
to change it to the appropriate permissions.

From the EMR cluster, go to Security Groups (at the bottom of page) for the master node.
Make sure to have ports 22 and 8888 open to everything in the inbound rules (::/0)

$ ssh -i yourpem.pem hadoop@<public address>.compute.amazonaws.com

$ sudo wget http://repo.continuum.io/archive/Anaconda2-5.3.0-Linux-x86_64.sh -P /mnt/
bash /mnt/Anaconda2*.sh

After running that command, when it prompts for the location, use /mnt/anaconda2:

Anaconda2 will then be installed at the following location:
/home/hadoop/anaconda2

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/hadoop/anaconda2] >>> /mnt/anaconda2

at the end when it gets to here, just hit enter:

Do you wish the installer to initialize Anaconda2
in your /home/hadoop/.bashrc ? [yes|no]
[no] >>>

$ nano .bashrc

(before source bashrc)

insert this line in file (anywhere):
export PATH=/mnt/anaconda2/bin:$PATH

then run:
$ source ~/.bashrc
$ conda update jupyter notebook

$ mkdir certs
$ cd certs

$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout yourpem.pem -out yourpem.pem

# when prompted it does not matter what you add as personal information


$ cd ..
$ jupyter notebook --generate-config
Writing default config to: /home/hadoop/.jupyter/jupyter_notebook_config.py
$ cd ~/.jupyter

$ vi jupyter_notebook_config.py

insert into top of jupyter_notebook_config.py     ### Change to 0.0.0.0 not *

c = get_config()
c.NotebookApp.certfile = '/home/hadoop/certs/msds697.pem'
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888

then
$ vi ~/.bashrc

add at end

export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"

$ source ~/.bashrc

HIGH MEMORY addition (for anomaly detection):
Change the following config file:
`/etc/spark/conf/spark-defaults.conf`

(Note:  make sure you could write to it with)
$ sudo chmod 777 /etc/spark/conf/spark-defaults.conf4

Add the following line to the end:
`spark.yarn.executor.memoryOverhead 10240M`


$ nano /etc/spark/conf/spark-defaults.conf

$ pyspark --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0

will see error messages, looking for

will start jupyter
access by Master public DNS:8888  (not what jupyter says)

https://ec2-34-220-175-48.us-west-2.compute.amazonaws.com:8888

enter the token from the Jupyter output


Command History Example ---
[hadoop@ip-172-31-24-232 ~]$ history
1  pysparj --packages org.mongodb.spark:mongo-spark-connector_2.11;2.4.0
2  pysparj --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0
3  pyspark --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0
4  clear
5  sudo wget http://repo.continuum.io/archive/Anaconda2-5.3.0-Linux-x86_64.sh -P /mnt/
6  bash /mnt/Anaconda2*.sh
7  nano .bashrc
8  source ~/.bashrc
9  conda update jupyter notebook
10  mkdir certs
11  cd certs
12  sudo openssl reg -x509 -nodes -days 365 -newkey rsa:1024 -keyout msds697.pem -out msds697.pem
13  sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout msds697.pem -out msds697.pem
14  cd ~/.jupyter
15  cd ..
16  jupyter notebook --generate-config
17  cd ~/.jupyter
18  vi jupyter_notebook_config.py
19  cd ..
20  vi ~/.bashrc
21  pyspark --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0
22  source ~/.bashrc
23  pyspark --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0
24  ls
25  pyspark --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0
26  pyspark
27  ls
28  cd
29  cd .jupyter/
30  ls
31  vi jupyter_notebook_config.py
32  cd ..
33  vi .bashrc
34  source ~/.bashrc
35  pyspark
36  jupyter notebook
37  pyspark
38  ls
39  pwd
40  cd certs/
41  ls
42  cd ..
43  ls
44  cd .jupyter/
45  vi jupyter_notebook_config.py
46  cd ..
47  pyspark
48  pwd
49  ls
50  cd certs
51  ls
52  pwd
53  vi jupyter_notebook_config.py
54  ls
55  jupyter notebook
56  cd ..
57  cd .jupyter/
58  ls
59  vi jupyter_notebook_config.py
60  cd ..
61  jupyter notebook
62  pyspark
63  ls
64  conda update jupyter notebook
65  spark
66  pyspark
67  pyspark --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0
68  which python
69  which jupyter
70  ls
71  history
