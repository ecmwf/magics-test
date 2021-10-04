
# Magics regression test suite

[![Build Status](https://img.shields.io/github/workflow/status/ecmwf/magics-test/ci?label=tests)](https://github.com/ecmwf/magics-test/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/ecmwf/magics-test)](https://github.com/ecmwf/magics-test/blob/master/LICENSE)

This test suite runs the regression tests for the [Magics](https://confluence.ecmwf.int/magics) meteorological plotting package.

## Setup the environment

```shell
pip install cftime netcdf4 xarray pytest pytest-html
export MAGPLUS_HOME=/path/to/magics
export MAGPLUS_REGRESSION=ON
```

## Running the test suite

```shell
pytest --html report.html
```

A report is created as `report.html`, showing the visual difference between a reference set of images.  
An error is reported if the number of different pixels exceeds a certain threshold.

![Example of report](report.png)

## Creating your own reference dataset

A script can be used to generate the reference dataset for a specific Magics Version:

```shell
python make_reference.py
```

This will generate a png for each test in the *reference* directory.  
You can after that run the test suite using your new Magics version.  
This will show you the visual differences between the 2 versions.

## Resolving font differences

Different platforms can have different fonts resulting in error threshold being erroneously exceeded. To further lower the chance of false positives, used font aliases can be redefined via the *fontconfig* configuration file:

```shell
cat << EOF > ~/.config/fontconfig/font.conf
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
    <dir>/path/to/font</dir>
    <match>
        <test name="family">
            <string>sans-serif</string>
        </test>
        <edit name="family" mode="assign" binding="strong">
            <string>FreeSans</string>
        </edit>
    </match>
    <match>
        <test name="family">
            <string>helvetica</string>
        </test>
        <edit name="family" mode="assign" binding="strong">
            <string>FreeSans</string>
        </edit>
    </match>
    <match>
        <test name="family">
            <string>times</string>
        </test>
        <edit name="family" mode="assign" binding="strong">
            <string>FreeSerif</string>
        </edit>
    </match>
</fontconfig>
EOF
```

Where:

* `/path/to/font` is the path to [custom fonts](http://ftp.gnu.org/gnu/freefont/freefont-otf-20100919.zip)
* `FreeSans` is the name of a custom sans serif font
* `FreeSerif` is the name of a custom serif font

## License

Copyright 2019- European Centre for Medium-Range Weather Forecasts (ECMWF).

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
