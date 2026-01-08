# AI Ticket Classification System

**End-to-end AI system to classify customer support tickets with ML and Django REST API, with a React frontend.**

---

##  Project Overview

This project automatically classifies customer support tickets into categories like **Login, Payment, Bug, Feature**, predicts **sentiment** (Neutral/Negative), and sets **priority** (High/Medium).  

It is designed as a **production-ready system**:

- ML pipeline separate from backend
- Django REST API for ticket management
- React frontend for live user interaction
- API-driven architecture
- Easy to deploy on AWS/Docker

---

## Tech Stack

- **Backend:** Django 4.2, Django REST Framework  
- **ML:** Scikit-learn, TF-IDF, Logistic Regression  
- **Frontend:** React (JavaScript)  
- **Database:** SQLite (default, can be replaced with PostgreSQL)  
- **Other:** Joblib, Pandas, python-dotenv  

---

## ⚙️ Features

- Automatic ticket categorization  
- Sentiment detection (Negative/Neutral)  
- Priority classification (High/Medium)  
- REST API-driven architecture  
- React frontend with real-time ticket submission  
- Clean ML inference pipeline (separate from backend)


---

##  Installation & Setup

###  Backend Setup (Django + ML)

```bash
# Create environment
python -m venv env
env\Scripts\activate    # Windows
source env/bin/activate # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
cd backend
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Train ML model
python ../ml/train.py

# Start backend server
python manage.py runserver


POST http://127.0.0.1:8000/api/tickets/
Body: { "text": "Your ticket text here" }

cd frontend
npm install
npm start

Open React app (localhost:3000)

Enter a support ticket in the text box

Click Submit

Get live prediction:

{
  "id": 1,
  "text": "Billing late",
  "category": "Payment",
  "sentiment": "Negative",
  "priority": "High",
  "created_at": "2026-01-09T23:45:00Z"
}

