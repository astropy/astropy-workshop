# Getting Started with Python and Anaconda

Please come to the workshop with a laptop already configured as described below.
If you have any problems with any of these steps, please [open an issue](https://github.com/astropy/astropy-workshop/issues).

## 1. Clone This Repository

Download the workshop folder using [git](https://help.github.com/articles/set-up-git/):

    $ git clone https://github.com/astropy/astropy-workshop.git

Navigate to this directory:

    $ cd astropy-workshop/0-Install_and_Setup/

## 2. Install Anaconda (if needed)

*Anaconda includes conda, conda build, Python and 100+ automatically installed, open source scientific packages and their dependencies that have been tested to work well together, including SciPy, NumPy and many others.*

Check if Anaconda is already installed.
    
    $ conda info

If Anaconda is not already installed, follow the Anaconda instructions for your operating system: 
https://docs.anaconda.com/anaconda/install/
   
Choose between installing the full Anaconda (3 GB) or  Miniconda (400 MB).
Miniconda comes with fewer default packages so it's faster to download and takes up less drive space. 

## 3. Create a conda environment for the workshop
*Anaconda includes an environment manager called conda.  you can create, export, list, remove and update environments that have different versions of Python and/or packages installed in them.* 

[Create a conda environment for this workshop using a yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). 
The python version and all needed packages, including astropy, are listed in the [environment.yml](https://github.com/astropy/astropy-workshop/blob/master/0-Install_and_Setup/environment.yml) file

### Mac, Linux

Verify your shell environment: 

    $ echo $SHELL 
    
If the output text does not contain `bash` then switch to the bash shell before being able to run anything related to Anaconda.

    % conda env create -n astropy-workshop --file environment.yml
    % source activate astropy-workshop

### Windows


    % conda env create -n astropy-workshop --file environment_win.yml
    % activate astropy-workshop

Install the rest of the packages:

    % pip install -r pip_requirements_win.txt

*Note: Windows distribution currently does not yet support imexam with DS9. However, all the imexam functionality including image viewing can be used with Ginga as the viewer.*

## 4. Check Installation

The name of the new conda environment created above should be displayed next to the terminal prompt: `(astropy-workshop) % `

Run the check_env.py script to check the Python environment and some of the required dependencies:

    (astropy-workshop) % python check_env.py

If the script reports that some of the versions don't match, update the reported packages using the ``conda update`` method described up top, namely:

    (astropy-workshop) % conda update <packagename>
    
## Additional Resources
- [Set up git](https://help.github.com/articles/set-up-git/)
- [Conda Users Guide](https://conda.io/docs/user-guide/index.html)
- [Astropy Install Instructions](http://docs.astropy.org/en/stable/install.html)
