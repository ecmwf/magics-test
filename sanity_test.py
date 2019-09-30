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



class MagicsSanityTest(unittest.TestCase):
    """
    A class with dynamically-generated test methods.
    """
    pass
tests=[]
def add_test(script, directory, output, reference):
    tests.append((script, directory, output, reference))


@pytest.mark.parametrize("test_name, directory, output, reference", tests)
def test_python(test_name, directory, output, reference, record_property):
        os.chdir(directory)

        record_property("test_name", test_name)
        record_property("directory", directory)
        record_property("reference", reference)
        record_property("output", output)
        
        
       
        # backup any existing files with our expected output_name
        output_name = "{}.png".format(test_name)
        backup_name = output_name + ".backup"
        ref_name = "{}/{}".format(reference,output_name)
        diff_name = "{}/{}_diff.png".format(reference,test_name)
        record_property("diff-image", diff_name)
        
        # run the test
        try :
            subprocess.check_call(["python3",  "{}.py".format(test_name)])
        except e:
            print (e)
            assert False

        
        record_property("new-test", True)

        output_exists = os.path.isfile(output_name)
        assert output_exists == True


        ref_exists = os.path.isfile(ref_name)

        if ref_exists:

            cmdline = [
                "compare",
                "-metric AE",
                "-dissimilarity-threshold 1",
                output_name,
                ref_name,
                diff_name,
            ]
            p = subprocess.Popen(" ".join(cmdline), shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            _, stderr = p.communicate()
            diff = int(stderr)
            record_property("diff", diff)
            record_property("new-test", False)
            assert diff < 30
            
       
            
        

        move_output(output_name, output)

        
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


magics = MagicsSanityTest()
DIR = os.environ.get('PWD', None)

for d in ["results", "reference"]:
    if not os.path.exists(d):
        os.makedirs(d)

os.chdir(DIR)
for test_set in glob.glob("*"):
    print (test_set)
    try :
        os.chdir(os.path.join(DIR,test_set))
        for file_name in glob.glob("*.py"):
            test_name = os.path.splitext(file_name)[0]
            method_name = "test_{}_{}".format(test_set,test_name)
            print("Adding test: {}".format(method_name))
            add_test(test_name, os.path.join(DIR,test_set), os.path.join(DIR, "results"), os.path.join(DIR, "reference"))
            #setattr(MagicsSanityTest, method_name, generate_test_method(test_name, os.path.join(DIR,test_set), os.path.join(DIR, "results")))
    except:
        os.chdir(DIR)

if __name__ == '__main__':
    unittest.main()
