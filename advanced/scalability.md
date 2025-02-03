# Scalability in MongoDB

## 📌 What is Scalability?
Scalability refers to a database's ability to handle increased workload efficiently. MongoDB supports **horizontal scaling** through **sharding**, making it ideal for large-scale applications.

---

## 🏗️ Types of Scaling
### 1️⃣ **Vertical Scaling (Scaling Up)**
- Increasing the hardware resources (CPU, RAM, Disk) of a single server.
- Limited by hardware capacity.
- Suitable for small applications.

### 2️⃣ **Horizontal Scaling (Scaling Out)**
- Distributing data across multiple servers (sharding).
- Enables high availability and fault tolerance.
- Ideal for large-scale, high-traffic applications.

---

## 🔹 Sharding: MongoDB’s Horizontal Scaling Solution
Sharding splits large datasets across multiple servers, called **shards**.

### ✅ How Sharding Works:
1. **Shard**: A database server storing a subset of data.
2. **Config Server**: Stores metadata about shards and their data locations.
3. **Query Router (mongos)**: Directs client requests to the correct shard.

### 🔹 Enabling Sharding
```sh
sh.enableSharding("myDatabase")
sh.shardCollection("myDatabase.users", { "_id": "hashed" })
```
This distributes the `users` collection across multiple shards.

---

## 🔍 Replication vs Sharding
| Feature | Replication | Sharding |
|---------|------------|----------|
| Purpose | High availability | Scalability |
| Data Distribution | Copies of the same data | Splitting data across servers |
| Failure Handling | Automatic failover | Distributes load |
| Use Case | Read-heavy workloads | Large datasets & high write throughput |

---

## 🚀 Best Practices for Scalability
- Use **indexes** to speed up queries.
- Optimize **aggregation pipelines**.
- Monitor performance with **MongoDB Atlas Metrics**.
- Choose **hashed sharding** for even data distribution.
- Use **replication** along with sharding for fault tolerance.

---

## 🎯 Next Steps
- [Learn About Transactions](./transactions.md)
- [Explore Replication](./replication.md)

MongoDB's scalability features help manage high-performance applications efficiently.