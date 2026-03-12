#CSV-Comma separated values
import csv
from datetime import date
file=open('data.csv','a+',newline='')  
#w=csv.writer(file)
r=csv.reader(file)
file.seek(0)
print(list(r))
# w.writerow(['DATE','CATEGORY','AMOUNT'])
# w.writerows([
#     [date.today(),'Travel',2000],
#     [date.today(),'Food',500],
#     [date.today(),'Clothing',1000]
# ])
file.close()