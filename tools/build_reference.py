# (C) Copyright 1996-2019 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
import os
import glob
import subprocess


refs=[]
def add_test(script, directory, output, reference):
    refs.append((script, directory, output, reference))


def run(test_name, directory, output, reference):
        os.chdir(directory)

        # backup any existing files with our expected output_name
        output_name = "{}.png".format(test_name)
        ref_name = "{}/{}".format(reference,output_name)
        
        # run the test
        try :
            subprocess.check_call(["python3",  "{}.py".format(test_name)])
        except Exception as e:
            print (e)


        output_exists = os.path.isfile(output_name)

        os.rename(output_name, ref_name)



# This code needs to be outside of `if __name__ == '__main__'` so the test methods are generated
# at import time so that pytest can find them


DIR = os.environ.get('PWD', None)

for d in ["reference"]:
    if not os.path.exists(d):
        os.makedirs(d)

os.chdir(DIR)
for test_set in glob.glob("test/*"):
    print (test_set)
    try :
        os.chdir(os.path.join(DIR,test_set))
        for file_name in glob.glob("*.py"):
            test_name = os.path.splitext(file_name)[0]
            run(test_name, os.path.join(DIR,test_set), os.path.join(DIR, "results"), os.path.join(DIR, "reference"))
    except:
        os.chdir(DIR)
