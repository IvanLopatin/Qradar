#Create by Lopatin Ivan
#Release version 1
#Python version v.2.7
#Parsing and mapping rows and lines for company 
########################

import re,csv
from datetime import  datetime
date_now = '2018-09-05'
results = {}#объявляем массив
#date_now = datetime.now()
date_now_formated = datetime.strptime(str(date_now), '%Y-%m-%d')
with open(r'C:\Users\ivan.lopatin\Desktop\tas\siem_device.csv') as csvfile2:
    read = csv.reader(csvfile2, delimiter=',')
    for row in read:
     x = ','.join(row)
     x_date = re.findall(r'^\w+.qiwi.com,\s(\d+-\d+-\d+)', x) #парсим дату
     x_host = re.findall(r'^(\w+).qiwi.com,\s\d+-\d+-\d+', x) #парсим хосты 
     x_date_formated = x_host[0]
     results[x_date_formated] = results.get(x_date_formated, {"count":0, "data":0})#создаем массим их 2х столбцов
     results[x_date_formated]["count"] += 1 # прибавление +1 к каждому значениям 
     results[x_date_formated]["data"] = x_date[0] # положим в колонку с датой свое значение с временем

csvfile2.close()

f = open(r'C:\Users\ivan.lopatin\Desktop\tas\device_CMDB.log') #открываем второй файл
for line in f:
    host_CMDB = str(line.strip()) #клеем значения и переводим в формат стринга
    results[host_CMDB] = results.get(host_CMDB, {"count": 0, "data": '0'}) #значения лога загоняем в массив
    results[host_CMDB]["count"] += 1 #добавляем +1 к каждому значению  в таблице массива 
f.close()

for result in results.keys(): #цикл суммирования значений
    if results[result]["count"] == 2: # если в таблице с значения будет 2(то есть совпали хосты в файлах)
        x_date_formated = results[result]["data"] #запишем наше вермя в массив в поле дата
        x_date_formated2 = datetime.strptime(str(x_date_formated), '%Y-%m-%d')#приводим время в нормальный вид
        x2 = (date_now_formated - x_date_formated2).days# сравниваем время  даты максимальной и той которая в массиве данных
        if x2 > 7: #если разница в 7 дней
            print("{:>10}\t{:>10}".format(
             results[result]["data"],
             result
          )) #вывести на экран с форматированием строк
