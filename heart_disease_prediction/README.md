# 🫀 Heart Disease Prediction using Machine Learning

This project is a machine learning-based diagnostic tool built to predict the likelihood of heart disease in patients using clinical data. It leverages **Logistic Regression** and performs feature analysis to deliver accurate results. The model was trained and evaluated on the UCI Cleveland dataset.

---

## 📁 Dataset

- **Dataset Name**: heart data  
- **Source**: [Kaggle - Heart Disease UCI](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)  
- **Format**: CSV (`heart.csv`)

---

## 🧠 Objective

Heart disease remains a global health concern and early-stage prediction can play a vital role in treatment and prevention. This project focuses on building a binary classification model that predicts heart disease presence based on patient data.

---

## 🔍 Features Used

| Feature        | Description |
|----------------|-------------|
| `age`          | Patient’s age |
| `sex`          | Gender (1 = male, 0 = female) |
| `cp`           | Chest pain type (0–3) |
| `trestbps`     | Resting blood pressure |
| `chol`         | Serum cholesterol (mg/dl) |
| `fbs`          | Fasting blood sugar > 120 mg/dl |
| `restecg`      | Resting ECG results |
| `thalach`      | Max heart rate achieved |
| `exang`        | Exercise-induced angina |
| `oldpeak`      | ST depression during exercise |
| `slope`        | Slope of peak exercise ST segment |
| `ca`           | Major vessels (0–3) colored by fluoroscopy |
| `thal`         | Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect) |
| `target`       | Diagnosis (1 = heart disease, 0 = no disease) |

---

## ⚙️ Tech Stack

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📊 Model Summary

- **Algorithm**: Logistic Regression  
- **Type**: Binary Classification  
- **Test Accuracy**: ~85%  
- The model includes exploratory data analysis (EDA), correlation heatmaps, and a complete classification report.

---

## 📈 Output Evaluation

- ✔️ Accuracy Score  
- ✔️ Confusion Matrix  
- ✔️ Precision, Recall, F1-Score  
- ✔️ Feature Correlation Analysis (Heatmap)

---

## ▶️ How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/Anish2k24/heart-disease-prediction.git
   cd heart-disease-prediction
