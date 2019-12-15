from pyspark.sql import SparkSession
from pyspark.sql.types import *

def main():
  """
  Fill in this function.

  1. Write a basic schema for /home/csu/tutorial/labs/lab-5/words.txt.
  2. Read /home/csu/tutorial/labs/lab-5/words.txt into a DataFrame.
  3. Count the number of words in the DataFrame.
  4. Filter for unique words.
  5. Count the number of words again.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('csv').schema(...).load(...) to read a text file with a CSV schema

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  See https://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html for help.
  """

  spark = SparkSession \
    .builder \
    .appName("words") \
    .master("local[4]") \
    .getOrCreate()

  schema = StructType([
    StructField("word", StringType(), True)
  ])

  df = spark.read.format('csv').schema(schema).load("words.txt")
  print(df.count())
  df = df.select(df['word'])
  df = df.distinct()
  print(df.count())

main()
