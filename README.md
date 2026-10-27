
<p align="center">
  <img src="images/student-marks-predictor-banner.png" alt="Student Marks Predictor banner" width="100%">
</p>

# 🎓 Student Marks Predictor

Predict Student Marks Using Machine Learning


# 🎓 Student Marks Predictor

### Predict Student Marks Using Machine Learning

A machine learning web application that estimates student marks based on the number of study hours. Built with **Python, Scikit-learn, Pandas, Matplotlib, and Streamlit**, this project demonstrates a complete beginner-friendly machine learning workflow with an interactive web interface.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-2EA44F?style=for-the-badge" alt="Learning Project">
</p>

---

## 📌 Project Overview

The Student Marks Predictor uses a **Linear Regression** model to learn the relationship between study hours and marks from a small sample dataset.

Users can enter their study hours and receive an estimated mark, view the regression graph, and see a simple performance message.

This project was created to practise Python programming, machine learning fundamentals, data visualisation, and web app development.

## ✨ Features

- 🎯 **Marks Prediction** — estimate marks based on study hours.
- 📊 **Interactive Web Interface** — use the app through Streamlit.
- 📈 **Data Visualisation** — view actual data points and the regression line.
- ✅ **Input Validation** — checks that the entered study hours are within the dataset's range.
- 🏆 **Performance Feedback** — displays a simple message based on the estimated marks.
- 🧩 **Beginner-Friendly Project** — demonstrates how multiple Python libraries work together.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Loading and handling the dataset |
| Scikit-learn | Building the Linear Regression model |
| Matplotlib | Plotting the data and regression line |
| Streamlit | Creating the web interface |

## 📂 Project Structure

```text
Student_Marks_Predictor/
├── app.py
├── study_hours.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Open the project folder

```bash
cd student-marks-predictor
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application should open in your browser. If it doesn't, visit:

`http://localhost:8501`

## 📊 Dataset

The project uses `study_hours.csv`, which contains two columns:

- `StudyHours` — number of hours studied.
- `Marks` — corresponding marks.

The current sample dataset contains only a few records. The model is intended for learning and demonstration, not for making reliable real-world academic predictions.

## 🧠 How It Works

1. Load the CSV dataset using Pandas.
2. Separate study hours (`X`) and marks (`y`).
3. Train a Linear Regression model using Scikit-learn.
4. Accept study hours from the user through Streamlit.
5. Predict the estimated marks.
6. Display the result and visualise the regression line using Matplotlib.

## 🖼️ Application Preview

Run the application locally and capture a screenshot of the complete interface.

To add the screenshot to this section:

1. Create a folder named `screenshots` in the project.
2. Save your screenshot as `student-marks-predictor.png` inside that folder.
3. Add this Markdown below:

```markdown
![Student Marks Predictor application](screenshots/student-marks-predictor.png)
```

## 🚀 Future Improvements

- Add more training data for better model evaluation.
- Display model performance metrics such as Mean Absolute Error (MAE).
- Improve the prediction results page and user interface.
- Deploy the application online so others can access it.
- Add more visualisations and data insights.

## ⚠️ Limitations

This is an educational project built using a small sample dataset. Predictions are estimates and are not guaranteed to match actual examination results. Model performance should be evaluated on more representative data before real-world use.

## 👨‍💻 Author

**Project:** Student Marks Predictor  
**Built with:** Python and Machine Learning

If you find this project useful for learning, feel free to explore the code and suggest improvements.

---

<p align="center">
  <b>Built to learn. Improved through practice. 🚀</b>
</p>