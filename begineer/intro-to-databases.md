# Basic MongoDB Commands

## 🏁 Getting Started
Before running MongoDB commands, ensure that MongoDB is installed and running. You can start MongoDB using:
```sh
mongod
```
Then open a MongoDB shell with:
```sh
mongosh
```

---

## 📌 Show Databases
To list all available databases, run:
```sh
show databases
```

---

## 📌 Create or Switch to a Database
To create or switch to a database, use:
```sh
use myDatabase
```
If `myDatabase` does not exist, MongoDB will create it when you insert data.

---

## 📌 Show Collections
To list all collections in the current database:
```sh
show collections
```

---

## 📌 Insert a Document
To insert a single document into a collection:
```sh
db.users.insertOne({ name: "John Doe", age: 30, city: "New York" })
```
To insert multiple documents:
```sh
db.users.insertMany([
  { name: "Alice", age: 25, city: "London" },
  { name: "Bob", age: 28, city: "Paris" }
])
```

---

## 📌 Find Documents
To find all documents in a collection:
```sh
db.users.find()
```
To pretty-print the output:
```sh
db.users.find().pretty()
```
To find documents with a specific condition:
```sh
db.users.find({ age: 30 })
```

---

## 📌 Update Documents
To update a document:
```sh
db.users.updateOne(
  { name: "John Doe" },
  { $set: { age: 31 } }
)
```
To update multiple documents:
```sh
db.users.updateMany(
  { city: "New York" },
  { $set: { city: "San Francisco" } }
)
```

---

## 📌 Delete Documents
To delete a single document:
```sh
db.users.deleteOne({ name: "Alice" })
```
To delete multiple documents:
```sh
db.users.deleteMany({ age: { $lt: 28 } })
```

---

## 🎯 Next Steps
- [Learn About Data Modeling](../intermediate/data-modeling.md)
- [Explore Aggregation Framework](../intermediate/aggregation-framework.md)

