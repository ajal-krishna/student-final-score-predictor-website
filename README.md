![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

# 🎓 Student Final Score Predictor

A **Flask web application** that uses **Linear Regression** to predict a student's **final exam score (out of 100)** based on attendance, internal tests, assignment score, and daily study hours.

https://github.com/ajalkrishna/student-final-score-predictor-website

---

## ✨ Features

- Real-time final score prediction
- Clean and modern neumorphic UI with **dark/light mode toggle**
- Shows predicted score + performance category (Excellent / Good / Needs Improvement)
- Displays all entered input values in the result section
- Responsive design (works well on mobile & desktop)

---

## 📊 Input Features

| Feature                     | Description                        | Range          |
|-----------------------------|------------------------------------|----------------|
| Attendance (%)              | Percentage of classes attended     | 0 – 100        |
| Internal Test 1             | Score in first internal exam       | 0 – 40         |
| Internal Test 2             | Score in second internal exam      | 0 – 40         |
| Assignment Score            | Score for submitted assignments    | 0 – 10         |
| Daily Study Hours           | Average hours studied per day      | 0 – 10+        |

**Output**: Predicted final score (rounded to 1 decimal) + motivational message

---

## 🖼️ Screenshots

### Home Page – Input Form

<p align="center">
  <img src="images/home_page_L.png" alt="Light Mode" width="45%"/>
  <img src="images/home_page_D.png" alt="Dark Mode" width="45%"/>
</p>

### Prediction Results

<p align="center">
  <img src="images/excellent_result.png" alt="Excellent Result" width="45%"/>
  <img src="images/improvement_result.png" alt="Needs Improvement" width="45%"/>
</p>

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- joblib (model saving/loading)

### Web Development
- Flask (Backend)
- HTML5 + CSS3 (Frontend)
- Font Awesome (icons)

### Development Tools
- Google Colab (model training)
- Visual Studio Code (development)
- Git & GitHub (version control)

---

## 📁 Project Structure



---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/ajalkrishna/student-final-score-predictor-website.git
cd student-final-score-predictor-website
```

2. Create virtual environment & install dependencies
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
3. Run the application
```bash
python app.py
```
Open your browser and go to:
```bash
http://127.0.0.1:5000
```
📦 Requirements
```bash
flask==3.0.3
joblib==1.4.2
numpy==1.26.4
pandas==2.2.2
scikit-learn==1.5.1
```
📈 Model Performance

Model: Linear Regression

Training: Performed in Google Colab

Features used: All 5 input variables



🙌 Acknowledgments

Inspired by academic performance prediction systems

Thanks to Flask & Scikit-learn open-source communities



👨‍💻 Author

Ajal Krishna

B.Tech Computer Science

Machine Learning Enthusiast

📍 Kerala, India

⭐ If you like this project, give it a star!


