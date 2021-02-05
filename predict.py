import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
# Load the dataset using pandas
data = pd.read_csv("SOUTHBANK.NS.csv") 
#print(data.head(5))
#print(data.describe())


# Select only the important features i.e. the date and price
data = data[["Date","Close"]] # select Date and Price
# Rename the features: These names are NEEDED for the model fitting
data = data.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset
print(data.head(5))


m = Prophet(daily_seasonality = True) # the Prophet class (model)
m.fit(data) # fit the model using all data


future = m.make_future_dataframe(periods=15) #we need to specify the number of days in future
prediction = m.predict(future)
m.plot(prediction)
plt.title("Prediction of the Google Stock Price using the Prophet")
plt.xlabel("Date")
plt.ylabel("Close Stock Price")
plt.show()




m.plot_components(prediction)
plt.show()

