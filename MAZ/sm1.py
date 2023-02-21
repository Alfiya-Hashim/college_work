import pandas as pd
df= pd.read_csv("chart.csv", index_col=0, parse_dates=True)

df = df.drop(df.columns[0], axis=1)
df = df.dropna()
#print("\n")
dfResample = df.resample('5min').ohlc()
print(dfResample)
print("___________________________________________________________________________________")

def findMaxAndMin(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]
  MaximumValue = highValues.max()
  MinimumValue = lowValues.min()

  return MaximumValue, MinimumValue
MaximumValue, MinimumValue = findMaxAndMin(dfResample)
print("The maximum value of stock is :", MaximumValue)
print("The minimum value of the stock is :", MinimumValue)
print("___________________________________________________________________________________")

def timeStampOfMaxMin(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  MaximumValue, MinimumValue = findMaxAndMin(dfResample)

  timestampOfMaxValue = dfResample.index[highValues == MaximumValue][0]
  timestampOfMinValue = dfResample.index[lowValues == MinimumValue][0]

  return timestampOfMaxValue, timestampOfMinValue
timestampOfMaxValue, timestampOfMinValue = timeStampOfMaxMin(dfResample)
print ("\n The time stamp of maximum value stock is:", timestampOfMaxValue)
print("The time stamp of minimum value stock is:", timestampOfMinValue)
print("___________________________________________________________________________________")

def findCandleWithMaxMove(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  candleMovement = []
  dataLength = len(dfResample.index)

  for i in range(dataLength):
    candleMovement.append(highValues[i] - lowValues[i])

  dfResample[(stockName, 'candle movement')] = candleMovement

  candleValues = dfResample[(stockName, 'candle movement')]
  candleWithMaxMove = candleValues.max()
  maxMovedCandleDetails = dfResample.loc[dfResample.index[candleValues == candleWithMaxMove]]

  return maxMovedCandleDetails
maxMovedCandleDetails = findCandleWithMaxMove(dfResample)
print("\n candle with maximum movement:", maxMovedCandleDetails, sep='\n\n')
print("___________________________________________________________________________________")
