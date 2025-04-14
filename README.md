
# Chat Moderation System

A modular, containerized chat moderation system built with Django, FastAPI, PostgreSQL, and Docker. It integrates a machine learning-based moderation service to detect and flag inappropriate content in real-time.

---

## 🚀 Features

- **Backend**: Django-based API for managing chat messages and moderation workflows.
- **Moderation Service**: FastAPI microservice leveraging Hugging Face models for content moderation.
- **Database**: PostgreSQL for robust and scalable data storage.
- **Containerization**: Dockerized services with orchestration via Docker Compose.
- **Environment Management**: `.env` files for managing environment-specific configurations.

---

## 🧱 Architecture

```
[Client]
   |
   v
[Backend (Django)]
   |
   v
[Moderation Service (FastAPI)] <--> [Hugging Face API]
   |
   v
[PostgreSQL Database]
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aarchish/chat_moderation.git
cd chat_moderation
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```env
# Backend Configuration
MODERATION_API_URL=http://moderation_service:8001/comment/
DB_NAME=chat_moderation
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432

# Moderation Service Configuration
HUGGINGFACE_API_TOKEN=your_huggingface_api_token
```

Replace `your_password` and `your_huggingface_api_token` with your actual credentials.

### 3. Build and Run with Docker Compose

```bash
docker-compose up --build
```

This command will:

- Build Docker images for the backend and moderation services.
- Start the PostgreSQL database service.
- Launch all services within a shared Docker network.

---

## 📂 Project Structure

```
chat_moderation/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── utils.py
│   └── ...
├── moderation_service/
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   └── ...
│   └── requirements.txt
├── docker-compose.yml
└── .env
```

---

## 🔗 API Endpoints

### Backend (Django)
- `POST /api/auth/signup`: Submit a signup request
- `POST /api/auth/login`: Submit a login request
- `POST /api/comment/`: Submit a new chat message -> Sent to ### Moderation Service (FastAPI) for text analysis.

---

## 🧪 Running Tests

To run tests for the backend:

```bash
docker-compose exec backend python manage.py test
```

---

## 📌 Notes

- Ensure that the `MODERATION_API_URL` in the backend's `.env` file matches the service name defined in `docker-compose.yml`.
- The moderation service is not exposed to the public network, enhancing security.
- Database credentials and other sensitive information are managed via environment variables.

---

## 📄 License

This project is licensed under the MIT License.
