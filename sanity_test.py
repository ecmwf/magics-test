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

class MagicsSanityTest(unittest.TestCase):
    """
    A class with dynamically-generated test methods.
    """
    pass

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
    print("moving {}".format(output_name))
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
        # backup any existing files with our expected output_name
        output_name = "{}.png".format(test_name)
        backup_name = output_name + ".backup"
        if os.path.isfile(output_name):
            os.rename(output_name, backup_name)
            self.addCleanup(cleanup_backup, backup_name, output_name)
        
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


DIR = os.environ.get('PWD', None)

for d in ["results"]:
    if not os.path.exists(d):
        os.makedirs(d)

os.chdir(DIR)
for test_set in glob.glob("*"):
    print (test_set)
    try :
        os.chdir(test_set)
        for file_name in glob.glob("*.py"):
            test_name = os.path.splitext(file_name)[0]
            method_name = "test_{}_{}".format(test_set,test_name)
            print("Adding test: {}".format(method_name))
            setattr(MagicsSanityTest, method_name, generate_test_method(test_name, os.path.join(DIR,test_set), os.path.join(DIR, "results")))
    except:
        os.chdir(DIR)

if __name__ == '__main__':
    unittest.main()
