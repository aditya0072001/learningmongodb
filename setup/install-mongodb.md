# Install MongoDB

## 🔹 Installing MongoDB (Community Edition)
MongoDB can be installed on Windows, macOS, and Linux. Follow the instructions below to install it on your system.

---

## 🖥️ Windows Installation

### 1️⃣ Download MongoDB
- Go to [MongoDB Download Page](https://www.mongodb.com/try/download/community)
- Select your operating system and download the **MSI** installer

### 2️⃣ Install MongoDB
- Run the downloaded `.msi` file and follow the installation steps
- Ensure you select **"Install MongoDB as a Service"**
- Complete the installation process

### 3️⃣ Verify Installation
- Open a **Command Prompt** and run:
  ```sh
  mongod --version
  ```
- If installed correctly, the version will be displayed

### 4️⃣ Start MongoDB Service
- Run:
  ```sh
  net start MongoDB
  ```
- To stop the service, use:
  ```sh
  net stop MongoDB
  ```

---

## 🍏 macOS Installation

### 1️⃣ Install via Homebrew
- Open **Terminal** and run:
  ```sh
  brew tap mongodb/brew
  brew install mongodb-community@6.0
  ```

### 2️⃣ Start MongoDB
- Run:
  ```sh
  brew services start mongodb-community@6.0
  ```

### 3️⃣ Verify Installation
- Run:
  ```sh
  mongod --version
  ```

### 4️⃣ Stop MongoDB
- Run:
  ```sh
  brew services stop mongodb-community@6.0
  ```

---

## 🐧 Linux Installation (Ubuntu)

### 1️⃣ Import the MongoDB GPG Key
```sh
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
```

### 2️⃣ Add MongoDB Repository
```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```

### 3️⃣ Install MongoDB
```sh
sudo apt update
sudo apt install -y mongodb-org
```

### 4️⃣ Start MongoDB
```sh
sudo systemctl start mongod
sudo systemctl enable mongod
```

### 5️⃣ Verify Installation
```sh
mongod --version
```

---

## 🎯 Next Steps
- [Setup MongoDB Atlas](../setup/setup-mongodb-atlas.md)
- [Learn Basic MongoDB Commands](../beginner/basic-commands.md)

Happy Learning! 🚀