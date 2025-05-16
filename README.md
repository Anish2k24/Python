
# 🫀 Heart Disease Prediction using Machine Learning

This project uses **Logistic Regression** to predict whether a person has **heart disease** based on 13 medical features. It is built with Python and uses data from the UCI Cleveland dataset.

---

## 📁 Dataset

- Dataset Name: **Cleveland Heart Disease Dataset**
- Source: [Kaggle - Heart Disease UCI](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)
- Format: CSV (`heart.csv`)

---

## 📌 Problem Statement

Heart disease is one of the leading causes of death globally. Early prediction using clinical data can help save lives.  
This project aims to build a classification model to predict whether a patient is likely to have heart disease based on input features.

---

## 🧠 Features Used

| Feature Name | Description |
|--------------|-------------|
| `age` | Age of the patient |
| `sex` | Sex (1 = male, 0 = female) |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol in mg/dl |
| `fbs` | Fasting blood sugar > 120 mg/dl |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels colored by fluoroscopy |
| `thal` | Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect) |
| `target` | Target variable (1 = has disease, 0 = no disease) |

---

## 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📈 Model Used

- **Logistic Regression** (Binary classification)
- Achieved **~85% accuracy** on the test dataset

---

## 📊 Results

- ✅ Accuracy
- ✅ Confusion Matrix
- ✅ Classification Report (Precision, Recall, F1-score)
- ✅ Correlation Heatmap for Feature Analysis

---

## 🔧 How to Run the Project

1. Clone the repository or download the files:
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

2. Install dependencies:
```bash
pip install pandas scikit-learn matplotlib seaborn
```

3. Place the `heart.csv` dataset in the project folder (from [Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)).

4. Run the code:
```bash
python heart_disease_prediction.py
```

---

## 📌 Sample Output

```
Accuracy: 0.85
Confusion Matrix:
[[24  5]
 [ 3 29]]
Classification Report:
  precision  recall  f1-score  support
...
```

---

## 🤖 Future Improvements

- Build a Streamlit or Flask web app for real-time predictions
- Try other models (Random Forest, SVM, XGBoost)
- Perform hyperparameter tuning and cross-validation
- Deploy on Hugging Face or Heroku

---

## 🙌 Author

**Anish Bhattacharjee**  
Machine Learning Enthusiast | AI Engineer in Progress  
[LinkedIn Profile](https://www.linkedin.com/in/anishbhattacharjee)

---

## ⭐ If you like this project

Give a ⭐ on GitHub and connect with me on [LinkedIn](https://www.linkedin.com/in/anishbhattacharjee)

---

## 🔖 Tags

`#MachineLearning` `#LogisticRegression` `#HeartDisease` `#Python` `#HealthcareAI` `#DataScience`
