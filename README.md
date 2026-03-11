Arun, here is a **professional README.md** you can directly paste into your GitHub repository for your deployed app:
Your deployed app: **[https://arun-batch20.streamlit.app/](https://arun-batch20.streamlit.app/)**

---

# 🚑 Insurance Prediction using Machine Learning

🔗 **Live App:** [https://arun-batch20.streamlit.app/](https://arun-batch20.streamlit.app/)

## 📌 Project Overview

The **Insurance Prediction System** is a Machine Learning web application that predicts insurance outcomes based on user inputs such as age, annual income, policy term, and sum assured. The model processes the inputs, scales them using a trained scaler, and predicts results using a trained ML model.

Machine learning models are widely used in the insurance industry to estimate policy costs and risks using historical data and customer attributes. ([GeeksforGeeks][1])

This project demonstrates how ML models can be integrated with a **Streamlit web interface** to create an interactive prediction system.

---

# 🎯 Objectives

* Build a machine learning model for insurance prediction
* Preprocess and scale input data
* Create a user-friendly web interface using **Streamlit**
* Deploy the application on **Streamlit Cloud**
* Allow users to make real-time predictions

---

# 🛠️ Technologies Used

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Python          | Programming Language      |
| NumPy           | Numerical computation     |
| Scikit-learn    | Machine Learning          |
| Pickle          | Model serialization       |
| Streamlit       | Web application framework |
| GitHub          | Version control           |
| Streamlit Cloud | Deployment                |

---

# 📊 Input Features

The application takes the following user inputs:

* **Age**
* **Annual Income (LPA)**
* **Policy Term (Years)**
* **Sum Assured (Lakhs)**

These features are processed and passed to the trained model to generate predictions.

---

# ⚙️ How the System Works

1️⃣ User enters insurance details in the web interface
2️⃣ The input data is converted into numerical format
3️⃣ The data is scaled using a **trained scaler**
4️⃣ The ML model predicts the output
5️⃣ The prediction result is displayed instantly

Machine learning helps automate insurance estimation and reduce manual calculation errors while improving efficiency. ([IJRASET][2])

---

# 📂 Project Structure

```
Insurance_prediction
│
├── app.py
├── requirements.txt
├── artifacts
│   ├── model.pkl
│   └── scaler.pkl
│
└── src
    └── prediction.py
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/arunmeka29/Insurance_prediction.git
```

Go to the project folder:

```bash
cd Insurance_prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

Steps:

1. Push the project to GitHub
2. Connect GitHub repo to Streamlit Cloud
3. Deploy the app
4. Access the live application via the public URL

---

# 📷 Live Application

👉 **Try the App Here:**
[https://arun-batch20.streamlit.app/](https://arun-batch20.streamlit.app/)

---

# 👨‍💻 Author

**Arun Meka**

🎓 Data Science Student
💻 Machine Learning & AI Enthusiast

GitHub:
[https://github.com/arunmeka29](https://github.com/arunmeka29)

---
