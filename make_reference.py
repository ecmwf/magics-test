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
import subprocess


def test_python(test_name, directory, output, reference):
    os.chdir(directory)

    output_name = "{}.png".format(test_name)

    # run the test
    try:
        subprocess.check_call(["python3", "{}.py".format(test_name)])
    except Exception as e:
        print(e)
        assert False

    output_exists = os.path.isfile(output_name)
    assert output_exists == True
    os.rename(output_name, os.path.join(reference, output_name))


# at import time so that pytest can find them


DIR = os.environ.get("PWD", ".")

for d in ["results", "reference"]:
    if not os.path.exists(d):
        os.makedirs(d)

os.chdir(DIR)
for test_set in glob.glob("test/*"):
    print(test_set)
    try:
        os.chdir(os.path.join(DIR, test_set))
        for file_name in glob.glob("*.py"):
            test_name = os.path.splitext(file_name)[0]
            method_name = "test_{}_{}".format(test_set, test_name)
            print("Adding test: {}".format(method_name))
            test_python(
                test_name,
                os.path.join(DIR, test_set),
                os.path.join(DIR, "results"),
                os.path.join(DIR, "reference"),
            )
    except:
        os.chdir(DIR)
