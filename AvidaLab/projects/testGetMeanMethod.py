# testGetMeanMethod
# alexandra miranda

from pyunpack import Archive
from pathlib import os
#from . models import Project
#from projects import FileParse

import tools as to
import unittest as ut

project = "uploads\\testdata"
experiment = "data_sg1_exp1_newIS_v2_rr"
run = "sg1_exp1_newIS_v2_rr_1\data"
data_file = "average.dat"
column = "Update"

class TestGetMeanMethod(ut.TestCase):

	def testGetMeanMethod(self):
		self.assertEqual(to.get_mean_column(project, experiment, run, data_file, column), 0)
		
if __name__ == '__main__':
	ut.main(warnings='ignore')