# Aggregation Framework in MongoDB

## 📌 What is the Aggregation Framework?
The **Aggregation Framework** in MongoDB is a powerful tool for processing and analyzing data. It allows you to perform complex transformations, filtering, grouping, and calculations on documents in a collection.

---

## 🏗️ Aggregation Pipeline
The **aggregation pipeline** is a series of stages that process documents sequentially. Each stage transforms the documents and passes the result to the next stage.

### ✅ Common Aggregation Stages
1️⃣ **$match** – Filters documents based on conditions (similar to `find`).
2️⃣ **$group** – Groups documents by a specific field and performs aggregations.
3️⃣ **$project** – Reshapes documents, including adding or removing fields.
4️⃣ **$sort** – Sorts documents by a specified field.
5️⃣ **$limit** – Restricts the number of documents in the output.
6️⃣ **$skip** – Skips a specified number of documents.
7️⃣ **$unwind** – Deconstructs an array field into multiple documents.

---

## 🔍 Example Aggregation Queries

### 1️⃣ Filtering with `$match`
```sh
db.sales.aggregate([
  { $match: { status: "Completed" } }
])
```
This filters documents where the `status` is "Completed".

---

### 2️⃣ Grouping and Counting with `$group`
```sh
db.sales.aggregate([
  { $group: { _id: "$category", totalSales: { $sum: "$amount" } } }
])
```
This groups documents by `category` and calculates the total sales amount.

---

### 3️⃣ Reshaping Data with `$project`
```sh
db.users.aggregate([
  { $project: { name: 1, email: 1, _id: 0 } }
])
```
This returns only the `name` and `email` fields, excluding `_id`.

---

### 4️⃣ Sorting and Limiting Results
```sh
db.products.aggregate([
  { $sort: { price: -1 } },
  { $limit: 5 }
])
```
This sorts products by `price` in descending order and returns the top 5.

---

## 🌍 Real-World Use Cases
- **Data Reporting**: Calculate total sales by region or product category.
- **User Analytics**: Analyze user engagement based on login activity.
- **E-commerce**: Filter and rank best-selling products.

---

## 🎯 Next Steps
- [Learn About Data Modeling](../intermediate/data-modeling.md)
- [Explore Transactions in MongoDB](../advanced/transactions.md)

This guide covers the basics of the Aggregation Framework.