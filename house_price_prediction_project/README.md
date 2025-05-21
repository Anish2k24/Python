# 🏡 House Price Prediction Project

This is my personal machine learning project aimed at predicting house prices using linear regression. I worked on everything from scratch, including data cleaning, visualization, training, evaluation, and deployment elements such as model saving. The goal was to understand and demonstrate the full ML workflow using Python and scikit-learn.

---

## 📌 Objective

The main objective of this project is to predict house prices based on features such as:

- Overall Quality of the house
- Ground Living Area
- Garage Capacity
- Garage Area
- Basement Size
- Number of Bathrooms
- Year Built

---

## 📊 Dataset

- **Source**: A CSV file named `Price data.csv` (manually analyzed and verified by me).
- Cleaned the dataset:
  - Removed non-numeric data.
  - Filled missing values using column-wise mean imputation.
  - Manually selected important features based on correlation and intuition.

---

## 🧠 ML Algorithm Used

- **Model**: Linear Regression (via `sklearn.linear_model.LinearRegression`)
- **Reason**: I chose Linear Regression as it provides transparency into feature importance and is ideal for regression-based problems.

---

## 🧪 Steps I Followed

1. **Data Loading** using `pandas`.
2. **Exploratory Data Analysis** using `info()`, `describe()`, and visual plots.
3. **Preprocessing**:
   - Selected numeric columns.
   - Manually chose relevant features.
   - Filled missing values with means.
4. **Train-Test Split**: 80% training / 20% testing
5. **Model Training**
6. **Evaluation**:
   - Mean Squared Error
   - R² Score
7. **Visualization**:
   - Bar plot of actual vs predicted prices (top 30)
   - Feature importance using coefficients
8. **Model Deployment**:
   - Saved model using `joblib` and `pickle`
   - Exported predictions and feature importance as CSV

---

## 📂 Output Files

- `house_price_model.pkl` – Model saved with Joblib
- `house_price_model_pickle.pkl` – Model saved with Pickle
- `predictions.csv` – Predictions of the model
- `feature_importance.csv` – Coefficients of each selected feature
- `bar_actual_vs_predicted.png` – Bar chart of predictions vs actual
- `feature_importance.png` – Bar chart showing importance of each feature

---

## 📈 Sample Prediction

I tested the model on new input:

```python
new_data = {
    'Overall Qual': 8,
    'Gr Liv Area': 2000,
    'Garage Cars': 2,
    'Garage Area': 500,
    'Total Bsmt SF': 1500,
    'Full Bath': 2,
    'Year Built': 2010
}
```

> 🔮 **Predicted Price**: (Printed in the terminal after model inference)

---

## 💡 Key Takeaways

- Built the project end-to-end without using any external templates or copying from any online repository.
- Understood the complete regression modeling pipeline.
- Gained confidence in saving and exporting ML models.
- Built real-world readiness for deployment and reproducibility.

---

## 🚀 Future Improvements

- Add GUI or web interface using Streamlit or Flask
- Try ensemble models like Random Forest or Gradient Boosting
- Implement proper hyperparameter tuning (GridSearchCV)

---

## 🧑‍💻 Author

**Anish Bhattacharjee**  
Created with pure effort, experimentation, and hands-on learning. No online generation tools, no code copypasta — just raw understanding and implementation.

📬 **Connect with me on LinkedIn**: [anish-bhattacharjee-971732216](https://www.linkedin.com/in/anish-bhattacharjee-971732216/)

---

## 📎 Screenshots

Here’s a quick glimpse of the repo structure:

![Repo Structure](feature_importance.png)
![Comaparison between actual price and predicted price via bar chart](bar_actual_vs_predicted.png)
---

## 📬 Feedback

If you're trying something similar and have any ideas or questions, feel free to reach out to me!
