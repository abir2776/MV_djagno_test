# MV Django Test Project

This is a Django project with Celery, Celery Beat, Redis, and Docker support.  
It provides APIs for user authentication, subscription management, and exchange rate retrieval.

---

## 🚀 Features

- User authentication and token generation
- Subscription management (view and create subscriptions for logged-in users)
- Exchange rate API integration
- Docker support (Django + Celery Worker + Celery Beat + Redis)
- Manual run support without Docker
- Django Admin access

---

## 🐳 Run with Docker

### 1. Clone the repository
```bash
git clone https://github.com/abir2776/MV_djagno_test.git
cd MV_djagno_test
```

### 2. Create .env file
In the root directory, create a `.env` file and add:
```env
REDIS_URL=redis://redis:6379/0
TIME_ZONE=Asia/Dhaka
EXCHANGE_RATE_API_KEY=f51f8570710dfaec6e18e689
```

### 3. Build and run the project
```bash
docker compose up -d
```

This will:
- Start Django server
- Start Celery worker
- Start Celery beat
- Start Redis server

---

## 🌐 Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `http://127.0.0.1:8000/` | GET | Root endpoint |
| `http://127.0.0.1:8000/api/auth/register` | POST | Register a new user |
| `http://127.0.0.1:8000/api/token` | POST | Generate token for a user |
| `http://127.0.0.1:8000/api/subscriptions/` | GET | View subscriptions for logged-in user |
| `http://127.0.0.1:8000/api/subscription` | POST | Create new subscription |
| `http://127.0.0.1:8000/api/exchange-rate/` | GET | Get exchange rate for base and target |

---

## 🛠 Run without Docker

If you prefer running without Docker:

### 1. Clone the repository
```bash
git clone https://github.com/abir2776/MV_djagno_test.git
cd MV_djagno_test
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Django server
```bash
python manage.py runserver
```

### 5. Run Celery worker
```bash
celery -A subscription_management worker --loglevel=info
```

### 6. Run Celery beat
```bash
celery -A subscription_management beat --loglevel=info
```

---

## 👨‍💻 Django Admin Access

To access the Django Admin panel:

1. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   Enter email and password.

2. **Visit:**
   ```
   http://127.0.0.1:8000/admin
   ```

---