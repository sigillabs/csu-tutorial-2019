from pyspark import SparkConf, SparkContext

def main():
  """
  Fill in this function.

  1. Write a function in a separate file that will be used in a DataFrame map operation.
  2. Read s3://csu-tutorial-labs/lab-7 into a DataFrame.
  3. Use function for map operation.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('parquet').load(...) to read a parquet file.

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  """

  conf = SparkConf().setAppName("words").setMaster("local[4]")
  context = SparkContext(conf=conf)

  # Fill in here

main()
