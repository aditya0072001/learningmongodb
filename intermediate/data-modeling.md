# Data Modeling in MongoDB

## 📌 What is Data Modeling?
Data modeling is the process of organizing and structuring data in a way that optimizes performance, scalability, and ease of retrieval in MongoDB.

---

## 🏗️ Types of Data Models
1️⃣ **Embedded Data Model** – Stores related data within the same document.
2️⃣ **Referenced Data Model** – Stores related data in separate documents and links them using references.

---

## ✅ Embedded Data Model
### When to Use:
- When data is frequently accessed together.
- When relationships are **one-to-few**.
- Example: Storing user profile details within a single document.

```json
{
  "_id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "address": {
    "city": "New York",
    "zip": "10001"
  }
}
```

---

## ✅ Referenced Data Model
### When to Use:
- When data is large and frequently updated.
- When relationships are **one-to-many** or **many-to-many**.
- Example: Storing user orders in a separate collection.

```json
{
  "_id": 1,
  "userId": 101,
  "items": ["product1", "product2"],
  "total": 200
}
```

And the user document:
```json
{
  "_id": 101,
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

## 🔍 Choosing the Right Model
| Criteria | Embedded Model | Referenced Model |
|----------|--------------|-----------------|
| Data Size | Small | Large |
| Read Performance | Fast | Moderate |
| Write Performance | Fast | Moderate |
| Relationship Type | One-to-Few | One-to-Many / Many-to-Many |
| Data Modification | Rarely Updated | Frequently Updated |

---

## 🌍 Real-World Use Cases
- **Embedded Model**: User profiles, blog posts with comments.
- **Referenced Model**: E-commerce orders, social media user relationships.

---

## 🎯 Next Steps
- [Explore Aggregation Framework](./aggregation-framework.md)
- [Understand Transactions](../advanced/transactions.md)

This guide covers data modeling best practices in MongoDB.