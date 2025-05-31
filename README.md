## 🏡 Canadian Housing Price Prediction

This project focuses on predicting house prices across Canadian cities using machine learning (XGBoost).

### ✅ Main Steps:
- Cleaned and preprocessed a Canadian housing dataset from Kaggle by fixing location mismatches, handling missing values, and applying log transformation to price.
- Trained an XGBoost regression model with Hyperopt-based hyperparameter tuning and 5-fold cross-validation; achieved an R² score of 0.70 on both train and test sets.
- Explained model behavior using SHAP values, permutation importance, and PDP plots, and built an interactive dashboard with Plotly to explore housing trends across cities and provinces.

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
