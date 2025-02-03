# Transactions in MongoDB

## 📌 What are Transactions?
Transactions in MongoDB allow multiple operations to be executed **as a single unit**, ensuring **ACID (Atomicity, Consistency, Isolation, Durability)** compliance. This is useful for applications that require strong data consistency.

---

## 🛠️ When to Use Transactions
- **Multi-document updates**: Ensuring that all updates succeed or none apply.
- **Banking & Finance**: Transferring money between accounts.
- **Order Processing**: Deducting inventory only when a payment is confirmed.
- **Booking Systems**: Preventing double bookings.

---

## ✅ Transactions in a Single Replica Set
Transactions work in **replica sets**, where data is synchronized across multiple servers. Ensure you are using a **replica set** before using transactions.

To start a session and transaction:
```sh
const session = db.getMongo().startSession();
session.startTransaction();

try {
    session.getDatabase("shop").orders.insertOne({
        user: "Alice", total: 500
    }, { session });
    session.getDatabase("shop").inventory.updateOne(
        { product: "Laptop" },
        { $inc: { stock: -1 } },
        { session }
    );
    session.commitTransaction();
    session.endSession();
} catch (error) {
    session.abortTransaction();
    session.endSession();
    print("Transaction Aborted: " + error);
}
```
This ensures that **either both operations complete successfully, or neither does.**

---

## ✅ Transactions in Sharded Clusters
In **sharded MongoDB clusters**, transactions span multiple shards, requiring additional coordination.
```sh
session = db.getMongo().startSession();
session.startTransaction();

try {
    session.getDatabase("users").profiles.insertOne({ name: "Bob" }, { session });
    session.getDatabase("orders").purchases.insertOne({ item: "Phone" }, { session });
    session.commitTransaction();
} catch (error) {
    session.abortTransaction();
}
```
Ensure **all involved collections are sharded** before running transactions in a distributed system.

---

## 🚀 Best Practices for Transactions
- Use transactions only **when necessary** (they add overhead).
- Keep transactions **short-lived** to avoid performance bottlenecks.
- Ensure **indexes** exist on fields used in transactions.
- Monitor transaction logs for debugging failures.

---

## 🎯 Next Steps
- [Learn About Scalability](./scalability.md)
- [Explore Replication](./replication.md)

Transactions ensure data integrity in MongoDB.