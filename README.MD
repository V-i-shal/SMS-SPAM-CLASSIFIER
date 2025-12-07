# 📱 SMS Spam Classifier

A machine learning-based web application that classifies SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques and a trained machine learning model. The project includes end-to-end text preprocessing, feature extraction using TF-IDF, model training, evaluation, and a Streamlit-based UI for real-time SMS classification.

---

## 🚀 Features
- Real-time SMS spam detection
- Pre-trained ML model stored as `model.pkl`
- TF-IDF vectorizer stored as `vectorizer.pkl`
- Clean and interactive Streamlit web interface
- Uses classic ML algorithms (Naive Bayes / Logistic Regression)
- Lightweight and fast text classification

---

## 📊 Project Overview
This project solves the problem of identifying fraudulent or promotional SMS messages. It uses NLP preprocessing steps like tokenization, stopword removal, punctuation removal, stemming, and converts text into TF-IDF vectors. A supervised learning model is trained to classify messages as **Spam** or **Ham** with high accuracy.

---

## 🧠 Tech Stack
- **Python**
- **scikit-learn**
- **Pandas, NumPy**
- **NLTK**
- **Streamlit**

---

## 📂 Project Structure

SMS-SPAM-CLASSIFIER/  
│── app.py                  → Streamlit web application  
│── model.pkl               → Trained ML model  
│── vectorizer.pkl          → TF-IDF vectorizer  
│── spam.csv                → Dataset  
│── notebook.ipynb          → Model training notebook  
│── requirements.txt        → Dependencies  
└── README.md               → Project documentation  

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
