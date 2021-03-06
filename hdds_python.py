from hdfs.ext.kerberos import KerberosClient
from  hdfs.ext.dataframe import write_dataframe
import pandas as pd

client = KerberosClient('http://hdfs-nn-1.au.adaltas.cloud:50070')

print('Connected to client {}'.format(client))

# export DataBase.csv to /education/cs_2022_spring_1/$USER/fil-rouge/
hdfs_path = '/education/cs_2022_spring_1/m.zavlyanova-cs/fil-rouge/'


client.upload(hdfs_path, 
            '/Users/sio/Documents/TD/hadoop_file_rouge/DataBase.csv', 
            n_threads=1, 
            temp_dir=None, 
            overwrite = True,
            chunk_size=65536, 
            progress=None, 
            cleanup=True)


# for d in client.list('/education/cs_2022_spring_1/m.zavlyanova-cs/fil-rouge/'):
#     print(d)
