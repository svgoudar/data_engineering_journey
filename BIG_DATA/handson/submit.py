import findspark
findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, StringType

sc = SparkContext.getOrCreate(SparkConf().setMaster('spark://172.30.80.1:7077'))
sc.setLogLevel("INFO")

spark = SparkSession.builder.getOrCreate()

# df = spark.createDataFrame(
#     [
#         (1, "foo"),
#         (2, "bar"),
#     ],
#     StructType(
#         [
#             StructField("id", IntegerType(), False),
#             StructField("txt", StringType(), False),
#         ]
#     ),
# )
# print(df.dtypes)
# df.show()

df = spark.read.csv("cars.csv", header=True, inferSchema=True) \
    .repartition(32) \
    .cache()
df.show()