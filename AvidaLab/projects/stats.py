# stats.py
import sys
import scipy as np
import unittest as ut
import scipy.stats as sp

#calculates the mean of an array
def mean(param):
	return np.mean(param)

#calculates the median of an array	
def median(param):
	return np.median(param)

#calculates the standard deviation of an array
def stDeviation(param):
	return np.std(param)

#calculates the mode of an array
def mode(param):
    return sp.mode(param)

#calculates the results of a Mann-Whitney U testshape
def mannWhitney(param, param1):
	return sp.mannwhitneyu(param, param1)

#calculates the resultes of the kruskal variance test
def kruskal(*param):
	return sp.kruskal(*param)