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

## Libraries Used:

![wordcloud_libraries (1)](https://github.com/user-attachments/assets/f0e4247a-e68f-4f91-b517-c972a7a0c2ac)

##  References

- **Canada GeoJSON Map**  
  [Click That 'Hood – Canada GeoJSON](https://github.com/codeforgermany/click_that_hood/blob/main/public/data/canada.geojson)  
  Used for geographic plotting of provinces and cities in Canada.

- **Housing Price Dataset**  
  [jeremylarcher/canadian-house-prices-for-top-cities](https://www.kaggle.com/datasets/jeremylarcher/canadian-house-prices-for-top-cities/code)  
  Source of the housing data used for modeling and visualization.

- **Dash Plotly Tabs Example**  
  [sunny2309/dash_plotly_dashboard_with_tabs](https://github.com/sunny2309/dash_plotly_dashboard_with_tabs/tree/main)  
  Helped in designing and organizing a multi-tab dashboard layout using Dash and Plotly.

- **Hyperparameter Optimization**  
  [hyperopt/hyperopt](https://github.com/hyperopt/hyperopt/tree/master)  
  Used for tuning the model's hyperparameters using `fmin` and `tpe.suggest` method.
