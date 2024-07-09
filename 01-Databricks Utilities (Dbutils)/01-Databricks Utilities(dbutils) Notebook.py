# Databricks notebook source
# MAGIC %md
# MAGIC ### Dbutils
# MAGIC In Databricks, **dbutils** is a utility that provides a set of command-like functions and methods to interact with and **manage data, files,** and other resources within the Databricks environment.   
# MAGIC Dbutils allows you to perform various file system operations such as **reading, writing, moving, and deleting files** and **Create directories**.   
# MAGIC This is essential for managing data and code within Databricks.

# COMMAND ----------

# MAGIC %md
# MAGIC To list available utilities along with a short description for each utility, run **dbutils.help()** for Python or Scala.

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# MAGIC %md
# MAGIC ## dbutils.fs
# MAGIC The file system utility allows you to access Databricks File System(**DBFS**), making it easier to use Azure Databricks as a file system.   
# MAGIC To list the avialable commands, run **dbutils.fs.help**.

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# DBTITLE 1,Ls( )
dbutils.fs.help("ls")

# COMMAND ----------

dbutils.fs.ls("/")

# COMMAND ----------

display(dbutils.fs.ls("/"))

# COMMAND ----------

display(dbutils.fs.ls("/FileStore"))

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables"))

# COMMAND ----------

display(dbutils.fs.ls("/FileStore/tables/Employees_1.csv"))

# COMMAND ----------

# DBTITLE 1,Mkdir( )
dbutils.fs.help("mkdirs")

# COMMAND ----------

# DBTITLE 1,Create a directory
dbutils.fs.mkdirs("/temp")

# COMMAND ----------

# DBTITLE 1,Remove directory
dbutils.fs.rm("/temp")

# COMMAND ----------

# DBTITLE 1,Copy( )
dbutils.fs.help("cp")

# COMMAND ----------

# DBTITLE 1,copy file
dbutils.fs.cp('/FileStore/tables/Employees_1.csv','/FileStore/temp1/Employees_1.csv')

# COMMAND ----------

# DBTITLE 1,Remove temp1
dbutils.fs.rm("/FileStore/temp1")

# COMMAND ----------

# DBTITLE 1,Head( )
dbutils.fs.help("head")

# COMMAND ----------

# DBTITLE 1,Read file and show content
dbutils.fs.head('/FileStore/tables/test_txt.txt')

# COMMAND ----------

# DBTITLE 1,only 10 characters
dbutils.fs.head('/FileStore/tables/test_txt.txt',10)

# COMMAND ----------

# DBTITLE 1,Put( )
dbutils.fs.help("put")

# COMMAND ----------

dbutils.fs.put('/FileStore/tables/test_txt.txt','Hello World')

# COMMAND ----------

dbutils.fs.put('/FileStore/tables/test_txt.txt','Hello World',True)

# COMMAND ----------

# DBTITLE 1,Move( )
dbutils.fs.help("mv")

# COMMAND ----------

dbutils.fs.mv('/FileStore/tables/Employees_1.csv','/FileStore/temp1/Employees_1.csv')

# COMMAND ----------

dbutils.fs.put('/FileStore/tables/test_txt.txt')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Utility(dbutils.data)
# MAGIC The data utility allows you to understand and interpret datasets.  
# MAGIC Avialable in Databricks Runtime 9.0 and above.  Data utility has command called summarize(dbutils.data.summarize).  
# MAGIC Summarize command calculates and display summary statistics of an Apache Spark DataFrame.

# COMMAND ----------

dbutils.data.help()

# COMMAND ----------

dbutils.data.help('summarize')

# COMMAND ----------

data = [(1,'tom'),(2,'jack'),(3,'asha')]
cols = ['id','name']

df = spark.createDataFrame(data,cols)

display(df)

# COMMAND ----------

dbutils.data.summarize(df)
