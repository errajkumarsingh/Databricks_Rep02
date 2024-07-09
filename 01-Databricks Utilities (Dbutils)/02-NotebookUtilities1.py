# Databricks notebook source
# MAGIC %md
# MAGIC ##Dbutils.notebook.exit( )
# MAGIC The notebook utility allows you to chain together notebooks and act on their results.  
# MAGIC Commands: **exit**,**run**  
# MAGIC
# MAGIC Exit notebook with a value.    
# MAGIC
# MAGIC Below cells after exit( ) command will get skipped.

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

dbutils.notebook.help('exit')

# COMMAND ----------

firstname = 'gsg'
dbutils.notebook.exit(firstname)


# COMMAND ----------

lastname = 'learn'
print(lastname)
