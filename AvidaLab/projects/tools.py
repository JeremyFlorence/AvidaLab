# Miscellanious helper functions used for projects

from pyunpack import Archive
from pathlib import os
from . models import Project
from . import FileParse
from . import getStats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# -------------------------------------------------------


def unpack(file_path, extraction_path, remove):
    """
    unzip file, create directory and puts data in the new directory
    :param file_path: the path to the file to extract
    :param extraction_path: where to extract it
    :param remove: boolean to remove the original file
    :return: nothing
    """
    print(file_path)
    Archive(file_path).extractall(extraction_path, auto_create_dir=True)
    # remove original compressed file???
    if remove is True:
        os.remove(file_path)


# -------------------------------------------------------


def use_method_on_all_subdirectories(path, file_type, method, *params):
    """
    Uses the method that you defined on all the files in a directory
    :param path: the path to the directory that you want you use it on
    :param file_type: extension of the file.
    :param method: name of the method to be used.
    :param params: parameters for that method.
    :return: nothing
    """
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(file_type):
                method(os.path.join(root, f), root, *params)


def decompress(file_path, project_name):
    project_files = os.path.join('projects', 'data', project_name)
    unpack(file_path, project_files, False)
    project_files = os.path.join(project_files, 'sg_reruns')
    use_method_on_all_subdirectories(project_files, '.dat.gz', unpack, True)

def check_folders(path_name):
    folders = []
    for directory in os.listdir(path_name):
        if os.path.isdir(os.path.join(path_name, directory)):
            folders.append(directory)

    return folders

# Returns all of the column headers for whatever kind of file the user selected
def get_headers(project, data_file):
    # We want to just find the first .dat file with the right name and use it
    # as a representative since all the data files with the same name have the
    # same headers
    parser = None
    experiments_dir = os.path.join(project.extractPath, 'sg_reruns/')
    for root, dirs, files in os.walk(experiments_dir):
        for f in files:
            if f == data_file:
                parser = FileParse.Parser(os.path.join(root, data_file))
                break
        if parser:
            break
                
    
    headers = parser.list_fields()
    return headers
	
# get the mean of the columns within the data file
def get_mean_column(project, experiment, runs, data_file, column_header):
    # make an empty map for storing the columns from each run
    arr = []
    # create a new key for the map each with the column from each run
    for run in runs:
        path = os.path.join(project.extractPath, 'sg_reruns', experiment, run, 'data')
        if os.path.isdir(path):
            parser = FileParse.Parser(os.path.join(path, data_file))
            arr.append(parser.get_column(column_header))

    return parallel_arr_mean(arr)
	
def parallel_arr_mean(arr):
    averages = []
    if len(arr) == 0:
        return averages
    minsizearr = len(arr[0])
    for array in arr:
        minsizearr = min(minsizearr, len(array))
    for array in arr:
        averages.append(array[:minsizearr])
    np_arr = np.array(averages)
    mean_array = np_arr.mean(axis=0)
    return mean_array

# Make a line graph with the given data and save it as an image file
# in the analysis static directory.
def line_graph(var1, var1_data, var2, var2_data, project_name):
    plt.plot(var1_data, var2_data)
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.title(var2 + ' vs. ' + var1)
    plt.savefig(os.path.join('analysis', 'static', 'linegraph.png'))
    plt.clf()
    