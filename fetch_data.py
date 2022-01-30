import tensorflow as tf
import numpy as np
import pandas as pd
import pandas_datareader as data
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import datetime
import matplotlib.pyplot as plt

def loading_model(ticker):
    
    company = 'Automobile-MARUTI_StockPredictor.h5'

    model = load_model(company)

    start_date = '2010-01-01'
    end_date = '2022-01-28'

    df = data.DataReader(ticker, 'yahoo', start_date, end_date)

    # We need last few days data and not complete 10 year data
    # Imported all data from 2010 so that we can show better historical graphs

    train_set = pd.DataFrame(data=(df['Open'][:int(len(df)*0.80)], df['Close'][0:int(len(df)*0.80)], df['High'][0:int(len(df)*0.80)], df['Low'][0:int(len(df)*0.80)]))
    test_set = pd.DataFrame(data=(df['Open'][int(len(df)*0.80):], df['Close'][int(len(df)*0.80):], df['High'][int(len(df)*0.80):], df['Low'][int(len(df)*0.80):]))

    train_set = train_set.T
    test_set = test_set.T

    scaler = MinMaxScaler(feature_range=(0, 1))

    train_set_arr = scaler.fit_transform(train_set)
    test_set_arr = scaler.fit_transform(test_set)

    # Forecasting part
    last_input = train_set.tail(100)
    final_df = last_input.append(test_set, ignore_index=True)
    final_test_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, final_test_data.shape[0]):
        x_test.append(final_test_data[i-100: i])
        y_test.append(final_test_data[i])
        
    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)

    # Re-scaling to normal values
    scale_factor = scaler.scale_
    scale_factor[0], scale_factor[1], scale_factor[2], scale_factor[3] = 1.0/scale_factor[0], 1.0/scale_factor[1], 1.0/scale_factor[2], 1.0/scale_factor[3]

    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Converting y_predicted to DataFrame
    predicted_df = pd.DataFrame(y_predicted, columns=['Open', 'Close', 'High', 'Low'])
    date_28 = '2022-01-28'
    date_28 = datetime.datetime.strptime(date_28, '%Y-%m-%d')
    days = len(predicted_df.Close)
    d = datetime.timedelta(days=days-1)
    start_date_predicted = date_28 - d
    predicted_df['Date'] = pd.date_range(start=start_date_predicted, end=date_28)
    return predicted_df.to_csv("/")