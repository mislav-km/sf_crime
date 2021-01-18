### Date created
17.01.2021

### Project Title
SF Police Department Spark Streaming

### Question 1
How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
I did change "maxOffsetPerTrigger" from 200 to 5000 and I think that I could observe a minimal difference regarding the duration of the jobs. I also added "startingOffsets", "earliest" to the properties, what improved the data flow from my point of view. Adding "maxRatePerPartition", 500 did not help. Increasing it to 5000 seemed to be better.

### Question 2
What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
At the end my impression is that this configuration \
    .option("startingOffsets", "earliest") \
    .option("maxOffsetPerTrigger", 5000) \
    .option("maxRatePerPartition", 5000) \
is my favourite configuration but it is rather a impression by looking at the Kafka Spark UI and how jobs are running.
