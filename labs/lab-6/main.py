from pyspark import SparkConf, SparkContext

def main():
  """
  Fill in this function.

  1. Read s3://csu-tutorial-labs/lab-6 into a DataFrame.
  2. Count the number of partitions in the DataFrame.
  3. Select the word column and filter for “joy”.
  4. Count again.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('parquet').load(...) to read a parquet file.

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  """

  conf = SparkConf().setAppName("words").setMaster("local[4]")
  context = SparkContext(conf=conf)

  # Fill in here

main()
