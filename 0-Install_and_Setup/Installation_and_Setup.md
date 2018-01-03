# Getting Started with Python and Anaconda

Please come to the workshop with a laptop already configured as described below.
If you have any problems with any of these steps, please open an issue astropy/astropy-workshop/issues

## 1. Clone This Repository

Download the workshop folder using git:

    % git clone http://github.com/astropy-workshop/astropy-workshop.git 

## 2. Update or Install Anaconda

Anaconda includes conda, conda build, Python and 100+ automatically installed, open source scientific packages and their dependencies that have been tested to work well together, including SciPy, NumPy and many others. 

Check if Anaconda is already installed.
    
    $ conda info

If not, Install Anaconda. Otherwise, Update Anaconda.
    
### Install Anaconda

https://conda.io/docs/user-guide/install/index.html
   
If it is not found, install the full Anaconda (3 GB) or  Miniconda (400 MB).

You may also choose to install Miniconda, which is the same as Anaconda,  but it comes with fewer default packages so it's faster to download and takes up less space. 

### Update conda and Anaconda
If Anaconda is already installed, update 

    $ conda update conda 
 
    $ conda update anaconda. 

## 3. Create a conda environment for the workshop

### Mac, Linux

Create a conda environment for this workshop which contains all the needed software:

    % conda env create -n astropy-workshop --file environment.yml
    % source activate astropy-workshop

### Windows

Create a conda environment for this workshop which contains all the needed software: 

    % conda env create -n astropy-workshop --file environment_win.yml
    % activate astropy-workshop

Install the rest of the packages:

    % pip install -r pip_requirements_win.txt

Note: Windows distribution currently does not yet support imexam with DS9. However, all the imexam functionality including image viewing can be used with Ginga as the viewer. 

# 4. Check Installation and Update

Note: You need to be inside the astropy-workshop directory for this to work.

Run the check_env.py script to check the Python environment and some of the required dependencies:

    % python check_env.py

If the script reports that some of the versions don't match, update the reported packages using the ``conda update`` method described up top, namely:

    % conda update <packagename>

    or

    % conda update packagename=version