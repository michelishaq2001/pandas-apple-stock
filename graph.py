from matplotlib import pylab as plt
import pandas as pd

# pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("AAPL.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)
# print(df1.head())

df2 = pd.read_excel("iphone-dates-2019.xlsx")
print(df2)
df2['Date'] = pd.to_datetime(df2.date)
# indexes = []
# for date2 in df2.Date:
#     for index, date1 in enumerate(df1.Date):
#         if date2 == date1:
#             indexes.append(index)
# print(indexes)

index2 = []
for date2 in df2.Date:
    if df1.index[df1.Date == date2].values.size:
        index2.append(int(df1.index[df1.Date == date2].values[0]))
print(index2)


mean = df1["Close"].mean()


plt.figure("Apple Stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean))
# or the same can be:
# plt.plot("Date", "Close", 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean), data=df1)
plt.plot(df1["Date"], df1["Close"], 'o', ms=7, markevery=index2, label="Iphone launch date")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
