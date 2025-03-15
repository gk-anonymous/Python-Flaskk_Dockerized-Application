# 🐳 PythonDock - Dockerized Flask Application

![Docker Logo](https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg)

## 📌 Overview
**PythonDock** is a lightweight and fully Dockerized Flask-based web application. This project ensures seamless deployment, scalability, and portability by containerizing the Python environment, making it easy to run across different platforms.

## 🚀 Features
- 🏗️ **Containerized Flask Environment** using Docker
- 🔄 **Easy Deployment** with minimal configuration
- ⚡ **Lightweight and Scalable** architecture
- 🔍 **Health Check Endpoint** (`/health` route)
- 🔐 **Secure and Isolated Execution**

## 📂 Project Structure
```
PythonDock---Dockerized-Flask-application/
│── Dockerfile
│── app/
│   ├── app.py
│   ├── run.py
│   ├── requirements.txt
│── .dockerignore
│── README.md
```

## 🛠️ Prerequisites
Ensure you have the following installed before running the application:
- 🐳 Docker ([Install Docker](https://docs.docker.com/get-docker/))
- 🐍 Python 3.7+ ([Install Python](https://www.python.org/downloads/))

## 📥 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/gk-anonymous/PythonDock---Dockerized-Flask-application.git
cd PythonDock---Dockerized-Flask-application
```

### 2️⃣ Build the Docker Image
```bash
docker build -t pythondock-app .
```

### 3️⃣ Run the Docker Container
```bash
docker run -it -p 80:80 --rm pythondock-app
```

### 4️⃣ Stop the Running Container (If Needed)
```bash
docker stop <container_id>
```

## 📝 Flask Application (`app.py`)
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, LO HO GYA PYTHON APPLICATION BHI DOCKERIZED'

@app.route('/health')
def health():
    return 'Server is up and running'
```

## 📜 Dockerfile Example
```dockerfile
FROM python:3.7

WORKDIR /app

COPY  . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "run.py"]
```

## 🚀 Run Script (`run.py`)
```python
from app import app
app.run(debug=True, host='0.0.0.0', port=80)
```

## 🛠️ Customization
- Modify `app.py` to add more Flask routes.
- Use **Docker Compose** for multi-container setups.
- Push the image to **Docker Hub** for cloud deployment.

## 🏗️ Contributing
Contributions are welcome! Feel free to fork this repository and submit a Pull Request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact
🔗 GitHub: [gk-anonymous](https://github.com/gk-anonymous)
📧 Email: gauravkamble9112@gmail.com
