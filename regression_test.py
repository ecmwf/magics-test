# (C) Copyright 1996-2019 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
"""
A unittest script which dynamically adds tests based on the contents of the 'gallery'
directory.
"""
import os
import glob
import unittest
import subprocess
import pytest


thresholds = {
    "contour2" : 2500,
    "bar_horizontal2" : 2500,
    "taylor" : 2500,
    "logarithmic" : 2750,
    "boxplot_reg" : 7000,
    "graph9" : 2500,
    "graph3" : 2500,
    "graph8" : 6000,
    "epsrose" : 5000,
    "coastlines2" : 2500,
   "epsgram_sample" : 11000,
   "xy_wind" : 4500, 
   "plumes" : 3000, 
}

skips = [  "axis-fortran", "projection5", "proj-regression-lambert_north_atlantic", 
		"xarray1", "xarray2", "xarray3", "xarray4", "xarray5", "xarray6", "xarray7", "obsjson"]

skips =  [ "axis-fortran" , "obsjson", "proj-regression-lambert_north_atlantic",  "xarray1", "xarray2", "xarray3", "xarray4", "xarray5", "xarray6", "xarray7"]
next_release = []
tests=[]
def add_test(script, directory, output, reference):
    tests.append((script, directory, output, reference))


@pytest.mark.parametrize("test_name, directory, output, reference", tests)
def test_python(test_name, directory, output, reference, record_property):



        os.chdir(directory)

        if os.environ.get("REGRESSION_MODE") != "off" :
            
            record_property("test_name", test_name)
            record_property("directory", directory)
            record_property("reference", reference)
            record_property("output", output)
            diff_name = "{}/{}_diff.png".format(reference,test_name)
            record_property("diff-image", diff_name)
            record_property("new-test", True)
            
        if test_name in skips:
           pytest.xfail("Test testing a new feature : expected to fail")
           assert False
        
       
        # backup any existing files with our expected output_name
        output_name = "{}.png".format(test_name)
        backup_name = output_name + ".backup"
        ref_name = "{}/{}".format(reference,output_name)
        
        
        # run the test
        try :
            subprocess.check_call(["python3",  "{}.py".format(test_name)])
        except Exception as e:
            
            assert False

        
        

        output_exists = os.path.isfile(output_name)
        assert output_exists == True
        
        if os.environ.get("REGRESSION_MODE") == "off" :
            return

        ref_exists = os.path.isfile(ref_name)

        if ref_exists:

            cmdline = [
                "compare",
                "-metric AE",
                "-dissimilarity-threshold 1",
                os.path.join(directory, output_name),
                ref_name,
                diff_name,
            ]
            p = subprocess.Popen(" ".join(cmdline), shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            _, stderr = p.communicate()
            diff = int(stderr)
            record_property("diff", diff)
            record_property("ref-image",ref_name)
            record_property("new-test", False)
            os.rename(output_name, os.path.join(output, output_name))
           
            if test_name in next_release:
                pytest.xfail("Test testing a new feature : expected to fail")
            assert diff < thresholds.get(test_name, 2000)
            
       
            
        

        

        
def cleanup_backup(backup_name, original_name):
    """
    Move a backed-up file back to its original name.
    """
    print("Replacing {} with {}".format(original_name, backup_name))
    if os.path.isfile(backup_name):
        os.rename(backup_name, original_name)

def cleanup_output(output_name):
    """
    Delete a file created by running a test script.
    """
    print("Removing {}".format(output_name))
    os.remove(output_name)

def move_output(output_name, directory):
    os.rename(output_name, os.path.join(directory, output_name))


    

def generate_test_method(test_name, directory, output):
    """
    Generate a test method based on a given test name.

    The test is simply to run a test script 'test_name.py' and check that an output file with the
    name 'test_name.png' is generated.
    """
    directory=directory
    output=output
    
    

    def run_test(self):
        os.chdir(directory)
        
        #record_property("gfhjgdhjs")
       
        # backup any existing files with our expected output_name
        output_name = "{}.png".format(test_name)
        backup_name = output_name + ".backup"
        if os.path.isfile(output_name):
            os.rename(output_name, backup_name)
            self.addCleanup(cleanup_backup, backup_name, output_name)
        
        print("Adding test: {}".format(method_name))
        # run the test
        ret = subprocess.call("python {}.py".format(test_name), shell=True)
        self.assertEqual(ret, 0)

        output_exists = os.path.isfile(output_name)
        if output_exists:
            self.addCleanup(move_output, output_name, output)

        ps_output_name = "{}.ps".format(test_name)
        if os.path.isfile(ps_output_name):
            # some tests may also generate postscript files which need to be deleted
            self.addCleanup(cleanup_output, ps_output_name)

        self.assertTrue(output_exists)

    return run_test


# This code needs to be outside of `if __name__ == '__main__'` so the test methods are generated
# at import time so that pytest can find them


DIR = os.environ.get('PWD', ".")

for d in ["results", "reference"]:
    if not os.path.exists(d):
        os.makedirs(d)

os.chdir(DIR)
for test_set in glob.glob("test/*"):
    print (test_set)
    try :
        os.chdir(os.path.join(DIR,test_set))
        for file_name in glob.glob("*.py"):
            test_name = os.path.splitext(file_name)[0]
            method_name = "test_{}_{}".format(test_set,test_name)
            print("Adding test: {}".format(method_name))
            add_test(test_name, os.path.join(DIR,test_set), os.path.join(DIR, "results"), os.path.join(DIR, "reference"))
    except:
        os.chdir(DIR)

if __name__ == '__main__':
    unittest.main()
