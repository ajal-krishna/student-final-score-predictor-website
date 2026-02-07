🎓 Student Final Score Predictor
� � �
A Flask web application that uses Linear Regression to predict a student's
final exam score (out of 100) based on academic performance and study habits.
🔗 GitHub Repo:
https://github.com/ajalkrishna/student-final-score-predictor-website�

✨ Features
Real-time final score prediction
Clean neumorphic UI
🌙 Dark / ☀️ Light mode toggle
Performance category:
Excellent
Good
Needs Improvement
Displays all entered input values
Fully responsive (mobile & desktop)
📊 Input Features
Feature
Description
Range
Attendance (%)
Percentage of classes attended
0 – 100
Internal Test 1
First internal exam score
0 – 40
Internal Test 2
Second internal exam score
0 – 40
Assignment Score
Assignment performance
0 – 10
Daily Study Hours
Avg study hours per day
0 – 10+
Output:
Predicted final score (rounded to 1 decimal) + motivational message

🖼️ Screenshots
🏠 Home Page – Input Form
�
￼ ￼ 

📈 Prediction Results
�
￼ ￼ 

🛠️ Tech Stack
🔹 Machine Learning
Python
Pandas
NumPy
Scikit-learn
Joblib
🔹 Web Development
Flask
HTML5
CSS3
Font Awesome
🔹 Development Tools
Google Colab
Visual Studio Code
Git & GitHub

📁 Project Structure
student-final-score-predictor-website/
│
├── app.py
├── linear_regression_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── images/
    ├── home_page_L.png
    ├── home_page_D.png
    ├── excellent_result.png
    └── improvement_result.png

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/ajalkrishna/student-final-score-predictor-website.git
cd student-final-score-predictor-website
2️⃣ Create virtual environment & install dependencies
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
3️⃣ Run the application
python app.py
Open your browser and visit:
👉 http://127.0.0.1:5000�

📦 Requirements
flask==3.0.3
joblib==1.4.2
numpy==1.26.4
pandas==2.2.2
scikit-learn==1.5.1

📈 Model Details
Algorithm: Linear Regression
Training Platform: Google Colab
Features Used: All 5 input variables

🙌 Acknowledgments
Inspired by academic performance prediction systems
Thanks to Flask & Scikit-learn open-source communities

👨‍💻 Author
Ajal Krishna
B.Tech Computer Science
Machine Learning Enthusiast
📍 Kerala, India
⭐ If you like this project, give it a star!


