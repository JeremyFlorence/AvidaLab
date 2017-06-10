# getStats.py
# alexandra miranda
from . import stats
import sys

def unpack(map, stat):
	if stat ==  'mW':
		return mWStats(map)
	if stat == 'kruskal':
		return unpackmult(map, stat)
	a = {}
	for key in map:
		a.update({key: findStats(map[key], stat)})
	return a

def unpackmult(map, stat):
	a = []
	for key in map:
		a.append(map[key])
	return findMultStats(*a)

def findStats(arr, stat):
	if(stat == 'mean'):
		return stats.mean(arr)
	if(stat == 'median'):
		return stats.median(arr)
	if(stat == 'mode'):
		var = stats.mode(arr)
		var1 = var[0]
		return var1[0]
	if(stat == 'stdev'):
		return stats.stDeviation(arr)
	
def mWStats(map):
	a = []
	for key in map:
		a.append(map[key])
	return stats.mannWhitney(a[0], a[1])

def findMultStats(*map):
	return stats.kruskal(*map)