##create table employees
CREATE TABLE employees (
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

#insert values into the table
INSERT INTO employees (name, department, salary) VALUES
('Alice', 'Sales', 5000),
('Bob', 'Sales', 4500),
('Charlie', 'Sales', 4500),
('David', 'Marketing', 6000),
('Eva', 'Marketing', 5000),
('Frank', 'Marketing', 5000),
('George', 'Marketing', 4000);

#without partition by RANK(), DENSE_RANK()
select name,department,salary,
RANK() over (ORDER BY salary DESC) as rank,
DENSE_RANK() over (ORDER BY salary DESC) as dense_rank
from employees

#with partition by RANK(), DENSE_RANK()
select name,department,salary,
RANK() over (Partition by department ORDER BY salary DESC) as rank,
DENSE_RANK() over (Partition by department ORDER BY salary DESC) as dense_rank
from employees



++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import *

# Initialize Spark session
spark = SparkSession.builder.master("local").appName("RankExample").getOrCreate()

# Sample data
data = [
    ("Alice", "Sales", 5000),
    ("Bob", "Sales", 4500),
    ("Charlie", "Sales", 4500),
    ("David", "Marketing", 6000),
    ("Eva", "Marketing", 5000),
    ("Frank", "Marketing", 5000),
    ("George", "Marketing", 4000)
]

# Create DataFrame
columns = ["name", "department", "salary"]
df = spark.createDataFrame(data, columns)


# Define a window specification ordered by salary descending (no partitioning)
window_spec = Window.orderBy(df["salary"].desc())

# Apply rank and dense_rank without partitioning
df = df.withColumn("rank", rank().over(window_spec))\
       .withColumn("dense_rank", dense_rank().over(window_spec))

# Show the result
df.display()




#Define a window specification partitioned by department and ordered by salary descending
window_spec = Window.partitionBy("department").orderBy(df["salary"].desc())

# Apply rank and dense_rank
df = df.withColumn("rank", rank().over(window_spec))\
       .withColumn("dense_rank", dense_rank().over(window_spec))

# Show the result
df.display()





















