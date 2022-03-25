%jdbc(hive)
-- Création d'une table

CREATE EXTERNAL TABLE cs_2022_spring_1.mzavlyanova_metadata_ext (
    ID STRING,
    Title STRING,
    Authors STRING,
    Publication_date Date
)
    
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION '/education/cs_2022_spring_1/m.zavlyanova-cs/fil-rouge/'
TBLPROPERTIES ('skip.header.line.count'='1')