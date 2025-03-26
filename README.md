## 🏡 Canadian Housing Price Prediction

This project focuses on predicting house prices across Canadian cities using machine learning (XGBoost).

### ✅ Main Steps:

- Cleaned and preprocessed the dataset (fixed province/city mismatches, removed duplicates, handled missing/invalid values)
- Used latitude and longitude instead of province and city as location features
- Applied log transformation to the price variable
- Explored housing trends through visualizations (e.g., most/least expensive cities, province-level summaries)
- Performed correlation analysis to understand relationships between features
- Trained an XGBoost regression model
- Tuned hyperparameters using `Hyperopt` with 5-fold cross-validation
- Evaluated model performance (R² = 0.70 on both train and test sets)
- Used SHAP values, permutation importance, and PDP plots to explain the model

![wordcloud_libraries](https://github.com/user-attachments/assets/b8069341-1e40-40cf-acde-e50499549f32)
