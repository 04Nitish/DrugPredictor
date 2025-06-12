# 💊 DrugPredictor

**License:** [MIT](LICENSE)

**DrugPredictor** is an AI-powered web application built using **Django** and **Machine Learning** to suggest the most suitable drug types for patients based on their medical profiles. It uses user input like age, gender, blood pressure, cholesterol levels, and Na-to-K ratio to intelligently recommend a drug type using a trained ML model.

---

## 📸 Interface Preview

Demo of prediction form:

![DrugPredictor UI]![Screenshot 2025-06-12 205808](https://github.com/user-attachments/assets/cb877bef-0508-45bc-b2d3-5b2a573d3042)


---

## 🚀 Features

- 🧠 Predicts suitable drug types using a machine learning model
- 🌐 Clean, responsive UI designed with Tailwind CSS
- 📋 Collects user input for:
  - Age
  - Gender (Sex)
  - Blood Pressure
  - Cholesterol
  - Sodium-to-Potassium Ratio (Na_to_K)
- 🎯 Clear result display (highlighted color and icon based on output)
- 🔐 CSRF protection and secure form handling via Django

---

## 🛠️ Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| **Backend**  | Django, Python           |
| **Frontend** | HTML, Tailwind CSS       |
| **ML Model** | Trained sklearn model (e.g., DecisionTreeClassifier) |
| **Database** | SQLite (default)         |

---


---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/04Nitish/DrugPredictor.git
cd DrugPredictor
