import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Price data.csv")#dataset loading
print("Data loaded successfully.")

print(df.head())#exploring the data
print(df.info())
print(df.describe())

df = df.select_dtypes(include=[np.number])

if 'SalePrice' not in df.columns:
    raise KeyError("SalePrice column missing after dropping non-numeric columns!")

df = df.fillna(df.mean())

features = ['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Garage Area',
            'Total Bsmt SF', 'Full Bath', 'Year Built']

# Check if all features are present
for feature in features:
    if feature not in df.columns:
        raise KeyError(f"Missing feature: {feature}")

X = df[features]
y = df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained.")

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

joblib.dump(model, "house_price_model.pkl")
print("Model saved as house_price_model.pkl (joblib)")

# Visualize predictions via bar chart
plt.figure(figsize=(14, 6))

sample_predictions = predictions_df.head(30)# Limitation to first 30 samples for better visibility in bar chart
sample_predictions.reset_index(drop=True, inplace=True)

bar_width = 0.4
index = np.arange(len(sample_predictions))

plt.bar(index, sample_predictions['Actual'], bar_width, label='Actual Price', alpha=0.7)
plt.bar(index + bar_width, sample_predictions['Predicted'], bar_width, label='Predicted Price', alpha=0.7)

plt.xlabel('Sample Index')
plt.ylabel('House Price')
plt.title('Predicted vs Actual House Prices (Bar Chart)')
plt.xticks(index + bar_width / 2, index)
plt.legend()
plt.tight_layout()
plt.savefig("bar_actual_vs_predicted.png")
plt.show()


# Feature importance
coefficients = pd.DataFrame(model.coef_, features, columns=['Coefficient'])
coefficients = coefficients.sort_values(by='Coefficient', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=coefficients['Coefficient'], y=coefficients.index)
plt.title("Feature Importance")
plt.xlabel("Coefficient Value")
plt.ylabel("Feature Name")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.show()

# Predict on new data
new_data = pd.DataFrame({
    'Overall Qual': [8],
    'Gr Liv Area': [2000],
    'Garage Cars': [2],
    'Garage Area': [500],
    'Total Bsmt SF': [1500],
    'Full Bath': [2],
    'Year Built': [2010]
})
new_prediction = model.predict(new_data)
print(f"Predicted house price for new data: {new_prediction[0]:.2f}")

# Save predictions to CSV
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_csv("predictions.csv", index=False)
print("Predictions saved to predictions.csv")

# Save feature importance to CSV
coefficients.to_csv("feature_importance.csv")
print("Feature importance saved to feature_importance.csv")

# Saving all objects using pickle
with open("house_price_model_pickle.pkl", "wb") as f:
    pickle.dump(model, f)
with open("predictions_pickle.pkl", "wb") as f:
    pickle.dump(predictions_df, f)
with open("feature_importance_pickle.pkl", "wb") as f:
    pickle.dump(coefficients, f)
print("All objects saved using pickle.")
