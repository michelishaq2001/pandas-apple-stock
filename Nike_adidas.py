from matplotlib import pylab as plt
import pandas as pd


ds1 = pd.read_csv("NKE.csv")
print(ds1.head())
ds1['Date'] = pd.to_datetime(ds1.Date)

ds3 = pd.read_csv("ADS.DE.csv")
print(ds3.head())
ds3['Date'] = pd.to_datetime(ds3.Date)



mean1 = ds1["Close"].mean()
mean2 = ds3["Close"].mean()

plt.figure("NIKE stock")
plt.plot(ds1["Date"], ds1["Close"], 'r-', linewidth=0.6, label="NIKE Stock price, mean=" + str(mean1))
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.figure("ADIDAS stock")
plt.plot(ds3["Date"], ds3["Close"], 'r-', linewidth=0.6, label="ADIDAS Stock price, mean=" + str(mean2))
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()