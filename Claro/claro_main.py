import claro_class as cl
import pandas as pd
import os
import re
import fnmatch
import sys

# function to check if the input is a single claro file
def isSingle(path):
        singlename = "*Ch_?_offset_?_Chip_00?*"
        return fnmatch.fnmatch(path, singlename) #bool


# Leave hardcoded = true to test the program on a single file, just for now
hardcoded = True
#path = r'C:\Users\jacop\Desktop\OOP\OOP_Project\Claro\Ch_7_offset_0_Chip_004.txt'
path = r'C:\Users\jacop\Desktop\OOP\secondolotto_1'

if hardcoded != True:
    # check if path has been given
        if len(sys.argv) !=2:
            print("\nUsage: insert a valid directory or filename\n")
        sys.exit(1)

        #path = sys.argv[1]


# Apply class method based on the input file

if isSingle(path):
    print (f'Provided a single Claro file, analyzing...\n')
    prova = cl.Single(path)
    prova.fit_erf()
    prova.printData()
    prova.plotter() # default arguments: (scatter = True, show_lin = True, show_erf = True, saveplot = False)

elif os.path.isdir(path):
    print (f'Provided a directory, analyzing...\n')
    multi = cl.Claro(path)
    multi.dir_walker()
    pass

else:
    pass
