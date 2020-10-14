import csv
import matplotlib.pyplot as plt
import numpy as np
import operator

cpi_file = open(r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\cpriceindex.csv')
cpi_reader = csv.reader(cpi_file)
cpi_data = list(cpi_reader)

ag_file = open(r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\agproduction.csv')
ag_reader = csv.reader(ag_file)
ag_data = list(ag_reader)

#cpriceindex comparing US and Australian prices
#for i in range(1, len(cpi_data)-1):
    #cpi_data[i][1] = float(cpi_data[i][1])
    #cpi_data[i][2] = float(cpi_data[i][2])

sorted_list = sorted(cpi_data[1:len(cpi_data)-1], key=operator.itemgetter(1))

#print('sorted_list=',sorted_list)
x1 = [] #USyear
y1 = [] #USvalue
x2 = [] #Australia year
y2 = [] #Australia value
for row in sorted_list:
    if row[1] == 'United States of America':
        x1.append(row[2])
        y1.append(row[4])
    if row[1] == 'Australia':
        x2.append(row[2])
        y2.append(row[4])

print("x1=", x1, "y1=", y1)
print("x2=", x2, "y2=", y2)
ax1 = []
#ay1 = np.array(y1)
#ay2 = np.array(y2)
ax2 = []
ax1 = sorted(x1)
ay1 = []
ay2 = []
#for y1 in ([ay1]):
ay1.append([y1])
ax2 = sorted(x2)
#for y2 in ([ay2]):
ay2.append([y2])
print((ax1))
print((ay1))


'''
ax11 = np.array(ax1)
ay11 = np.array(ay1)
ay21 = np.array(ay2)
ax21 = np.array(ax2)
'''
fig, axp = plt.subplots() 
plt.plot(x1,y1, label='US')
plt.plot(x2,y2, label='Australia')
#, ax2p] = plt.subplots(2)
axp.set_xlabel=('Year')
axp.set_ylabel=('Price Value')
#ax2p.set_xlabel('Australia Year')
#ax2p.set_ylabel=('Australia Price Value')
#axp.plot(ax1, ay1) 
#ax2p.plot(ax2, ay2) 
'''
for a in ax1:
    ax1p.plot(a)
for a in ay1:
    ax1p.plot(a)
for a in ax2:
    ax2p.plot(a)
for a in ay2:
    ax2p.plot(a)
'''

#ax11.squeeze(ay11)
#ax21.plot(ax21)
#ax21.squeeze(ay21)
#plt.tight_layout()
axp.tick_params(axis='both', which='major', pad=15)
plt.xticks(rotation=90)
plt.ylim(0,115)
plt.legend()


'''
fig, [ax1, ax2] = plt.subplots(2)
ax1.set(xlabel='these are the words')
ax1.set(ylabel='the number of times Trump tweeted the word')
ax1.bar( counts.keys() , counts.values() )
ax2.bar( [1,2,3], [4,3,2] )
#plt.show()
'''
'''

fig, ax = plt.subplots()
ax.set(
    xlabel='these are the words',
    ylabel='the number of times Trump tweeted the word',
    )
x = list(reversed(sorted(counts.keys())) )
# heights = sorted(counts.values())
heights = []
for label in x:
    heights.append(counts[label])

print('heights=',heights)

ax.bar( x , heights )
plt.show()

# .keys() is non-deterministic
# sorted(counts.keys()) is deterministic
print('counts.keys()=',sorted(counts.keys()))
'''
sorted_list2 = sorted(ag_data[1:len(ag_data)-1], key=operator.itemgetter(1))
fig, ax3 = plt.subplots()
ax3.set(
    xlabel='Year',
    ylabel='Agrarian Production',
    )
x1 = [] #USyear
y1 = [] #USvalue
bx1 = []
by1 = []
bx11 = []
for row in sorted_list2:
    if row[1] == 'United States of America':
        x1.append(row[2])
        y1.append(row[3])
#bx1 = sorted(x1)
#bx11 = bx1.append
#by1 = by1.append(y1)
ax3.bar(sorted(x1), y1)
#plt.bar([bx1], [by1])
plt.show()