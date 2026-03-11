

# 🛡️ Insurance Prediction System

🔗 **Live App:**
[https://arun-batch20.streamlit.app/](https://arun-batch20.streamlit.app/)

## 📌 Project Description

The **Insurance Prediction System** is a Machine Learning web application that predicts insurance outcomes based on user input features such as **Age, Annual Income, Policy Term, and Sum Assured**.

The application uses a trained **Machine Learning model** and **data preprocessing pipeline** to process user input and generate predictions through an interactive **Streamlit interface**.

This project demonstrates the complete **Machine Learning pipeline**, including:

* Data preprocessing
* Feature engineering
* Model training
* Model deployment using Streamlit

---

# 🚀 Features

✅ Data preprocessing and feature engineering
✅ Machine learning model training
✅ Model serialization using Pickle
✅ Interactive web interface with Streamlit
✅ Real-time insurance prediction

---

# 🛠️ Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Programming language  |
| NumPy        | Numerical computation |
| Pandas       | Data manipulation     |
| Scikit-learn | Machine learning      |
| Pickle       | Model saving/loading  |
| Streamlit    | Web application       |
| Git & GitHub | Version control       |

---

# 📊 Input Features

The application accepts the following inputs from the user:

* **Age**
* **Annual Income (LPA)**
* **Policy Term (Years)**
* **Sum Assured (Lakhs)**

These features are processed and passed to the trained model to generate predictions.

---

# 📂 Project Structure

```
Insurance_prediction
│
├── artifacts
│   ├── model.pkl
│   └── scaler.pkl
│
├── data
│   ├── raw
│   │   └── insurance.csv
│   │
│   └── processed
│       ├── x_train_scaled.csv
│       ├── x_test_scaled.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── src
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_traning.py
│   └── prediction.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/arunmeka29/Insurance_prediction.git
```

Navigate to the project directory:

```bash
cd Insurance_prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# 🌐 Deployment

This application is deployed using **Streamlit Cloud**.

Steps followed:

1. Push project to GitHub
2. Connect GitHub repository to Streamlit Cloud
3. Deploy the Streamlit application
4. Access the live application through the public URL

---

# 🎯 Future Improvements

* Add more insurance features for better prediction
* Improve model accuracy using advanced algorithms
* Add data visualization dashboard
* Implement user authentication

---

# 👨‍💻 Author

**Arun Meka**

🎓 Data Science Student
💻 Interested in Machine Learning & AI

GitHub:
[https://github.com/arunmeka29](https://github.com/arunmeka29)

---

