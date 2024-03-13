# Stock Price Prediction Model

This project aims to predict the maximum and minimum prices of company shares for a particular date using machine learning techniques.

## Overview

The project involves the following main steps:

1. **Data Collection:** Stock data for various companies is collected from Kaggle.

2. **Data Preprocessing:** The dataset is preprocessed to handle missing values, convert data types, and create dummy variables for categorical features.

3. **Model Training:** A neural network model is trained using TensorFlow/Keras to predict the maximum and minimum prices of company shares.

4. **Model Evaluation:** The trained model is evaluated using test data to assess its performance.

5. **Prediction Function:** A function is provided to make predictions for the maximum and minimum prices of company shares for a given set of input features.

## Requirements

- Python (>=3.6)
- pandas
- numpy
- tensorflow
- scikit-learn

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/stock-price-prediction.git
```

2.  Navigate to the project directory :
cd stock-price-prediction
```bash
cd tock-price-prediction
    run the "predict_price()" function
```

3. Example 
```bash
from prediction_model import predict_price

max_price, min_price = predict_price("MUNDRAPORT", 488, 770, 400, 984.72, 27294366, "2007/11/27")
print("Predicted Maximum Price:", max_price)
print("Predicted Minimum Price:", min_price)
