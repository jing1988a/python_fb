# it is commit log. you can not modify or delete  It is read from left to right and guarantees item ordering.

# Kafka actually stores all of its messages to disk (more on that later) and having them ordered in the structure lets it take advantage of sequential disk reads.
#
# Reads and writes are a constant time O(1) (knowing the record ID), which compared to other structure’s O(log N) operations on disk is a huge advantage, as each disk seek is expensive.
# Reads and writes do not affect another. Writing would not lock reading and vice-versa (as opposed to balanced trees)
# These two points have huge performance benefits, since the data size is completely decoupled from performance. Kafka has the same performance whether you have 100KB or 100TB of data on your server.


#topic/partition. order is only garenteed in partition

# https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1




# What is Zookeeper?
# Zookeeper is a distributed key-value store. It is highly-optimized for reads but writes are slower. It is most commonly used to store metadata and handle the mechanics of clustering (heartbeats, distributing updates/configurations, etc).
#
# It allows clients of the service (the Kafka brokers) to subscribe and have changes sent to them once they happen. This is how brokers know when to switch partition leaders. Zookeeper is also extremely fault-tolerant and it ought to be, as Kafka heavily depends on it.
#
# It is used for storing all sort of metadata, to mention some:
#
# Consumer group‘s offset per partition (although modern clients store offsets in a separate Kafka topic)
# ACL (Access Control Lists) — used for limiting access/authorization
# Producer & Consumer Quotas —maximum message/sec boundaries
# Partition Leaders and their health

# How does a producer/consumer know who the leader of a partition is?
# Producer and Consumers used to directly connect and talk to Zookeeper to get this (and other) information.


























