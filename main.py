# Part. 1

#=======================================

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061142.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

#---------------C0A880------------------

target_data_0 = list(filter(lambda item: item['station_id'] == 'C0A880', data))

number = len(target_data_0)

sum = float(0)
average_0 = float(0)
num = len(target_data_0)

for i in range(number):

   if (float(target_data_0[i]['PRES']) == -99 or float(target_data_0[i]['PRES']) == -999):
      num = num - 1
   else:
      sum = sum + float(target_data_0[i]['PRES'])

if (num == 0):
   average_0 = -99
else :
   average_0 = sum / num

#---------------C0F9A0------------------

target_data_0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))

number = len(target_data_0)

sum = float(0)
average_1 = float(0)

num = len(target_data_0)

for i in range(number):

   if (float(target_data_0[i]['PRES']) == -99 or float(target_data_0[i]['PRES']) == -999):
      num = num - 1
   else:
      sum = sum + float(target_data_0[i]['PRES'])

if (num == 0):
   average_1 = -99
else :
   average_1 = sum / num

#---------------C0G640------------------

target_data_0 = list(filter(lambda item: item['station_id'] == 'C0G640', data))

number = len(target_data_0)

sum = float(0)
average_2 = float(0)

num = len(target_data_0)

for i in range(number):

   if (float(target_data_0[i]['PRES']) == -99 or float(target_data_0[i]['PRES']) == -999):
      num = num - 1
   else:
      sum = sum + float(target_data_0[i]['PRES'])

if (num == 0):
   average_2 = -99
else :
   average_2 = sum / num

#---------------C0R190------------------

target_data_0 = list(filter(lambda item: item['station_id'] == 'C0R190', data))

number = len(target_data_0)

sum = float(0)
average_3 = float(0)

num = len(target_data_0)

for i in range(number):

   if (float(target_data_0[i]['PRES']) == -99 or float(target_data_0[i]['PRES']) == -999):
      num = num - 1
   else:
      sum = sum + float(target_data_0[i]['PRES'])

if (num == 0):
   average_3 = -99
else :
   average_3 = sum / num

#---------------C0X260------------------

target_data_0 = list(filter(lambda item: item['station_id'] == 'C0X260', data))

number = len(target_data_0)

sum = float(0)
average_4 = float(0)

num = len(target_data_0)

for i in range(number):

   if (float(target_data_0[i]['PRES']) == -99 or float(target_data_0[i]['PRES']) == -999):
      num = num - 1
   else:
      sum = sum + float(target_data_0[i]['PRES'])

if (num == 0):
   average_4 = -99
else :
   average_4 = sum / num
#=======================================

# Part. 4

#=======================================

#---------------C0A880------------------

if (average_0 == -99):
   print(['C0A880' ,'None'])
else :
   print(['C0A880' ,average_0])

#---------------C0F9A0------------------

if (average_1 == -99):
   print(['C0F9A0' ,'None'])
else :
   print(['C0F9A0' ,average_1])

#---------------C0G640------------------

if (average_2 == -99):
   print(['C0G640' ,'None'])
else :
   print(['C0G640' ,average_2])

#---------------C0R190------------------

if (average_3 == -99):
   print(['C0R190' ,'None'])
else :
   print(['C0R190' ,average_3])

#---------------C0X260------------------

if (average_4 == -99):
   print(['C0X260' ,'None'])
else :
   print(['C0X260' ,average_4])

#========================================