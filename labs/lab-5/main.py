from pyspark import SparkConf, SparkContext

def main():
  """
  Fill in this function.

  1. Write a basic schema for /home/csu/tutorial/labs/lab-5/words.txt.
  2. Read /home/csu/tutorial/labs/lab-5/words.txt into a DataFrame.
  3. Count the number of words in the DataFrame.

  NOTE: Use Lambdas over new functions.
  NOTE: Use context.read.format('csv').schema(...).load(...) to read a text file with a CSV schema

  See https://spark.apache.org/docs/latest/sql-getting-started.html for help.
  """

  conf = SparkConf().setAppName("words").setMaster("local[4]")
  context = SparkContext(conf=conf)

  # Fill in here

main()
