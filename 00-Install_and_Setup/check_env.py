#!/usr/bin/env python
"""
Check for required dependencies for the workshop.
Usage::

  % python check_env.py

"""
from __future__ import print_function

import sys
from distutils.version import LooseVersion


def check_package(package_name, minimum_version=None, verbose=True):
    errors = False
    try:
        pkg = __import__(package_name)
    except ImportError as err:
        print('Error: Failed import: {0}'.format(err))
        errors = True
    else:
        if package_name == 'xlwt':
            installed_version = pkg.__VERSION__
        else:
            installed_version = pkg.__version__
        if (minimum_version is not None and
            LooseVersion(installed_version) <
                LooseVersion(str(minimum_version))):
            print('Error: {0} version {1} or later is required, you '
                  'have version {2}'.format(package_name, minimum_version,
                                            installed_version))
            errors = True
        if not errors and verbose:
            print('Found', package_name, installed_version)
    return errors


pkgs = {'IPython': '7.2',
        'notebook': '5.7',
        'numpy': '1.14',
        'scipy': '1.1',
        'matplotlib': '2.2.3',
        'astropy': '3.1',
        'photutils': '0.5',
        'specutils': '0.5.1',
        'skimage': '0.14',
        'pandas': '0.23',
        'astroquery': '0.3',
        'gwcs': '0.10',
        }

errors = []
for package_name, min_version in pkgs.items():
    errors.append(check_package(package_name, minimum_version=min_version))
if any(errors):
    print('\nThere are errors that you must resolve before running the '
          'tutorials.')
else:
    print('\nYour Python environment is good to go!')
