# Setup MongoDB Atlas

## 🌍 What is MongoDB Atlas?
MongoDB Atlas is a cloud-based managed database service that allows you to deploy and scale MongoDB clusters without managing the underlying infrastructure.

---

## 🛠️ Steps to Set Up MongoDB Atlas

### 1️⃣ Create an Account
- Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Click **Sign Up** and create a free account
- Verify your email to activate your account

---

### 2️⃣ Create a New Cluster
- Once logged in, click **"Create"** under the **Clusters** section
- Select the **Shared Cluster** (Free Tier)
- Choose a **Cloud Provider & Region** (closer to your users)
- Click **Create Cluster**

---

### 3️⃣ Set Up Database User
- Once the cluster is created, navigate to **Database Access**
- Click **"Add New Database User"**
- Choose a username and password (store them securely)
- Set permissions to **Read and Write to Any Database**
- Click **"Add User"**

---

### 4️⃣ Configure Network Access
- Go to **Network Access**
- Click **"Add IP Address"**
- Select **"Allow Access from Anywhere"** (or add your specific IP)
- Click **Confirm**

---

### 5️⃣ Connect to MongoDB Atlas
- Navigate to **Database** → **Connect**
- Choose **"Connect your application"**
- Copy the **connection string** (it looks like this):
  ```
  mongodb+srv://yourusername:yourpassword@your-cluster.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
  ```
- Replace `yourusername` and `yourpassword` with the credentials you created

---

### 6️⃣ Connect Using Compass (GUI)
- Download [MongoDB Compass](https://www.mongodb.com/try/download/compass)
- Open Compass and paste the **MongoDB Atlas connection string**
- Click **Connect**

---

## 🎯 Next Steps
- [Learn Basic MongoDB Commands](../beginner/basic-commands.md)
- [Understand Data Modeling](../intermediate/data-modeling.md)

---

This guide sets up MongoDB Atlas for you. Let me know which file you need next! 🚀
