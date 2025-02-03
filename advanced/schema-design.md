# Schema Design in MongoDB

## 📌 What is Schema Design?
Schema design in MongoDB refers to the way data is structured and stored in collections. Unlike SQL databases, MongoDB provides **flexible schema design**, allowing embedded and referenced relationships.

---

## 🏗️ Key Schema Design Approaches
### ✅ 1. Embedded Documents
- Stores related data inside a single document.
- **Best for:** Data that is frequently read together.
- **Example:** Storing user profile information in one document.
```json
{
  "_id": 1,
  "name": "John Doe",
  "address": {
    "street": "123 Main St",
    "city": "New York"
  }
}
```

### ✅ 2. Referenced Documents (Normalization)
- Stores related data in separate collections using references.
- **Best for:** Large, frequently updated datasets.
- **Example:** Storing user orders separately and linking them by ID.
```json
{
  "_id": 1,
  "user_id": 101,
  "items": ["Laptop", "Phone"],
  "total": 1000
}
```

```json
{
  "_id": 101,
  "name": "Alice",
  "email": "alice@example.com"
}
```

---

## 🔍 Embedded vs Referenced: When to Use?
| Feature | Embedded | Referenced |
|---------|---------|------------|
| Read Performance | Fast | Moderate |
| Write Performance | Fast | Moderate |
| Data Relationship | One-to-Few | One-to-Many, Many-to-Many |
| Data Modification | Rarely Updated | Frequently Updated |

---

## 🚀 Best Practices for Schema Design
- Keep documents **small and efficient**.
- Use **indexes** on frequently queried fields.
- Prefer **embedding** when data is frequently accessed together.
- Use **referencing** for large datasets with complex relationships.
- Optimize **aggregation pipelines** for faster queries.

---

## 🎯 Next Steps
- [Explore Transactions](./transactions.md)
- [Learn About Scalability](./scalability.md)

A well-designed schema improves performance and maintainability.