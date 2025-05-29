---


# 🧬 Early Disease Detection System

A machine learning-based system for predicting the likelihood of diabetes in individuals, built using data analytics, AI modeling, and full-stack deployment techniques.

---

## 📌 Features

- Real-world diabetes dataset (Pima Indians Diabetes)
- Data cleaning, preprocessing, and feature engineering
- Trained multiple machine learning models
- Hyperparameter tuning and cross-validation
- REST API backend using FastAPI
- Frontend interface using Streamlit
- Fully working end-to-end prediction system

---

## 📁 Project Structure

```

early\_disease\_detection/
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks (EDA, modeling, preprocessing)
├── src/                   # Modular scripts for data and model processing
├── api/                   # FastAPI backend with model
│   ├── main.py
│   └── random\_forest\_optimized.pkl
├── streamlit\_app/         # Streamlit frontend dashboard
│   └── app.py
├── requirements.txt       # Environment dependencies
└── README.md              # Project documentation


---

## 🛠️ Tech Stack

- Python 3.10+
- Pandas, NumPy** – for data manipulation
- Scikit-learn – for model training and evaluation
- Matplotlib, Seaborn** – for data visualization
- FastAPI – for building REST API
- Uvicorn – to run FastAPI server
- Streamlit – for the user interface
- Joblib – for saving/loading trained models

---

## 📊 Dataset Information

- **Source**: [Kaggle – Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Cleaning Steps**:
  - Replaced invalid zeroes in Glucose, BMI, etc. with NaN
  - Imputed missing values using median
  - Feature scaling using `StandardScaler`
  - Engineered a custom `risk_score` feature

---

## ⚙️ Setup Instructions

#Step 1: Clone the project
bash
git clone https://github.com/yourusername/early-disease-detection.git
cd early-disease-detection


### Step 2: Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate        # macOS/Linux
.\env\Scripts\activate         # Windows
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

### 1. Start the FastAPI backend

```bash
cd api
uvicorn main:app --reload
```

* Runs at: `http://127.0.0.1:8000`
* Interactive docs at: `http://127.0.0.1:8000/docs`

### 2. Start the Streamlit frontend

Open a new terminal:

```bash
cd streamlit_app
streamlit run app.py
```

* Runs at: `http://localhost:8501`

---

## 🌐 API Usage

### POST `/predict`

**Input format:**

```json
{
  "Glucose": 0.8,
  "BMI": 0.6,
  "Age": 0.4,
  "DiabetesPedigreeFunction": 0.5,
  "risk_score": 0.48
}
```

**Output format:**

```json
{
  "prediction": 1,
  "status": "Diabetic"
}
```

---

## 📦 Model & Workflow

* Multiple models were evaluated (Random Forest, Logistic Regression, SVM, etc.)
* Final model: `RandomForestClassifier`
* Tuned using `RandomizedSearchCV`
* Stored using `joblib` and served via FastAPI

---

## 👤 Author

**Saumya Sinha**
B.Tech CSE, Galgotias University
GitHub: [@Saumya-Sinha25](https://github.com/Saumya-Sinha25)

---

## 📜 License

This project is licensed under the **MIT License**.

---


