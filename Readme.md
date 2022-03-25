# Project
# Integration to "Fil rouge" project
réalisé dans l'env SIO de conda

# Connect to hdfs

    $ ssh m.zavlyanova-cs@edge-1.au.adaltas.cloud



## Basics:
# Toute la suite à faire en local !!!
## Export scientific articles metadata to HDFS (Python script using HdfsCLI)
install the requirement

    $ sudo apt-get install gcc python-dev libkrb5-dev
    
# create environment
    $ python3 -m venv .venv 
    $ source .venv/bin/activate
    $ pip install -r requirements.txt

# envoyer un ticket
en local !!!

    $ kinit m.zavlyanova-cs
    $ klist

# créer le csv qui contient les métadonnées des pdf

    $ python extract.py

# créer la connection avec python et hdfs, et envoyer le csv sur hdfs

    $ python hdds_python.py

# Vérifier que la table est sur hdfs
à faire sous la connecion ssh sur edge

    $ hdfs dfs -ls /education/cs_2022_spring_1/m.zavlyanova-cs/fil-rouge/


## Make data available through a Hive table (HQL script)
# Create an external table targeting our data
This part is done on Zeppelin
The script to create external table in hql in in the script "create_ext.hql"


## Create some graphics using Zeppelin
Cf Zeppelin









