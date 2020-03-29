import requests
import csv
import os


os.chdir('F:/')

url = ('http://10.172.89.55/cimiss-web/api?userId=BEXA_XIAN_liuchang&pwd=liu7758521&interfaceId='
       + 'getSurfEleInRegionByTimeRange&dataCode' + '='
       + 'SURF_CHN_MAIN_MIN&timeRange' + '='
       + '[20191209140000,20191209140500]'
       + '&adminCodes=' + '610100,610500' + '&elements='
       + 'Station_Name,Datetime,Station_Id_C,TEM'
       + '&minSeparate=' + '5' + '&dataFormat=' + 'csv')

data = requests.get(url)

df = pd.DataFrame(data)
print(df)

#print(data.headers)
#with open("pyci2.csv", 'w',encoding='gbk') as f:
#    f.write(data.text)

#print(data.text)

