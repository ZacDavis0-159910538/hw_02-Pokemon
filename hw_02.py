import json
import matplotlib.pyplot as plt
import os

# loads the tweets from json files into a list
filenames = {
    r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\pokemonnum.json',
    r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\type.json',
    r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\pokenames.json',
}
pk_dict = {}
pokes = []
'''
i = 0
file0 = []
file1 = []
filei = []
for i in range(len(pokes)):
            if i == 0:
                file0 += file_pokes
                i += 1
            if i == 1:
                file1 += file_pokes
                i += 1
            if i >= 2:
                filei += file_pokes
                i += 1
'''
'''
for filename in filenames:
    with open(filename, 'r', encoding='utf8') as f:
        file_pokes = json.loads(f.read())
        pokes += file_pokes
print(file_pokes)
#counts number of pokemon per version
poke_counts = {} #keys = pk aka pokemon, values = number of pokemon per version
num = (range(0,1050))
for poke in pokes:
    if 'trump' in tweet['text']
'''

'''
for poke in pokes:
    pk_dict['item'] = poke

print('pk_dict=', pk_dict['item'])
'''
'''
print('len(pokes)=', len(pokes))
print ('pokes=', pokes)
#print ('filepokes=', file_pokes)
#counts number of pokemon per version
poke_counts = {} #keys = pk aka pokemon, values = number of pokemon per version
num = (range(0,1050))
pk = {}
i = 0
poke_counts[num]=0
for i in range(0,1000000000):
    if file_pokes[i] == '"name":':
        while file_pokes[i] != ',':
            pk += file_pokes[i]
            poke_counts[num] += 1
print('pk=', pk)
'''
    
#print(poke_counts[num])  
#count numbers of pokemon each type

'''
# count the number of times obama is used per year
obama_counts = {} # keys = year, values = number of tweets per year
for year in [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]:
    obama_counts[year]=0
for tweet in tweets:
    year = tweet['created_at'][-4:]
    #print('year=',year)
    if 'house' in tweet['text'].lower():
        obama_counts[int(year)] += 1

print('obama_counts=',obama_counts)

# sort the data for plotting
xs = sorted(obama_counts.keys())
ys = []
for x in xs:
    ys.append(obama_counts[x])

# generate the plots
fig,ax = plt.subplots()
ax.plot(xs, ys)
plt.show()


# this is the output of the lab
counts = {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

import matplotlib.pyplot as plt

'''
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

#2nd attempt
'''
import json
import matplotlib.pyplot as plt
import os
filenames = {
    r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\USD.json',
    r'c:\Users\zac\Dropbox\DesktopSaving\Desktop\CMC\College Classes Documents\CPSI040\GitHub\hw_02-Pokemon\GBP.json',
    }
pokes = []
for filename in filenames:
    with open(filename, 'r', encoding='utf8') as f:
        file_pokes = json.loads(f.read())
        pokes += file_pokes
p_items = file_pokes.items()
for key, value in p_items:
    if key == 'rates':
        print('USD=', value)
        print('GBP=', value)
#rate_counts = {} # keys = year, values = number of tweets per year
#for c in [file_pokes.keys()]:
    #print('keys=', file_pokes[key])
    #rate_counts[c]=0
'''
'''
for tweet in tweets:
    year = tweet['created_at'][-4:]
    #print('year=',year)
    if 'house' in tweet['text'].lower():
        rate_counts[int(year)] += 1
'''
'''
#print(rates)
new_dictkey = {p_items}
new_dictv = {p_items}
#create two dictionaries one where I remove the keys the other where I remove the values, then add them back into a new dictionary with both.

#print(new_dict)
xs = sorted(file_pokes.keys())
'''
'''
obama_counts = {} # keys = year, values = number of tweets per year
for year in [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]:
    obama_counts[year]=0
for tweet in tweets:
    year = tweet['created_at'][-4:]
    #print('year=',year)
    if 'house' in tweet['text'].lower():
        obama_counts[int(year)] += 1
'''

'''
pokes = []
for filename in filenames:
    with open(filename, 'r', encoding='utf8') as f:
        file_pokes = json.loads(f.read())
        pokes += file_pokes
print(file_pokes)
#counts number of pokemon per version
poke_counts = {} #keys = pk aka pokemon, values = number of pokemon per version
num = (range(0,1050))
for poke in pokes:
    if 'trump' in tweet['text']
'''