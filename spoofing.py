import numpy
import pandas as pd
from matplotlib import pyplot as plt 
from matplotlib import dates as mdates
from datetime import datetime, timedelta

#convert string to python datetime object
def date22num(x):
    return datetime.strptime(x[11:], "%H:%M:%S.%f")

spoof = pd.read_csv(r"C:\Users\simon\Desktop\citi hack\data1.csv")
#find userID should loop later
zerospoof = spoof.loc[spoof["User_ID"] == 0]


#find symbols should loop later
#for security in zerospoof.symbol.unique():
security = 1
localedspoof = zerospoof.loc[zerospoof["symbol"] == security]
#set to datatime object
securitydata = localedspoof.copy()
securitydata['time'] = securitydata['time'].apply(date22num)

previoustime = securitydata.iloc[1]["time"]
previoustimeslot = securitydata.iloc[0]["time"]
previoustimedifference = previoustime - previoustimeslot
condenseddata = pd.DataFrame(columns=['starttime','endtime','timeinterval'])

#iterate data by row
for i in range(2,len(securitydata)):
     currenttime = securitydata.iloc[i]["time"]
     timedifference = currenttime - previoustime
     #time difference 2 minutes
     if (timedifference > (timedelta(minutes = 2) + previoustimedifference)):
          condenseddata = condenseddata.append({"starttime" : previoustimeslot, "endtime" : previoustime, "timeinterval" : (previoustime-previoustimeslot)}, ignore_index=True)
          previoustimeslot = currenttime
     previoustime = currenttime
     previoustimedifference = timedifference

condenseddata = condenseddata.append({"starttime" : previoustimeslot, "endtime" : previoustime, "timeinterval" : (previoustime-previoustimeslot)}, ignore_index=True)
#export to csv       change path!
condenseddata.to_csv(r'C:\Users\simon\Desktop\citi hack\findsymbol1.csv')
