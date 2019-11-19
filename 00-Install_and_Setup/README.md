# Getting Started with Python and Anaconda

Please come to the workshop with a laptop already configured as described below.
If you have any problems with any of these steps, please
[open an issue](https://github.com/astropy/astropy-workshop/issues).

## 1. Clone This Repository

Download the workshop folder using
[git](https://help.github.com/articles/set-up-git/):

    % git clone https://github.com/astropy/astropy-workshop.git

If you don't have git installed, you can download the ZIP file by pressing the
green *Clone or download* button at
https://github.com/astropy/astropy-workshop and selecting *Download ZIP*.
However, this option is not recommended because it impedes the ability to
update your copy of the repository if updates are made.

## 2. Install Miniconda (if needed)

*Miniconda is a free minimal installer for conda. It is a small, bootstrap
version of Anaconda that includes only conda, Python, the packages they depend
on, and a small number of other useful packages, including pip, zlib and a few
others.*

Check if Miniconda is already installed.

    % conda info

If Miniconda is not already installed, follow these instructions for your
operating system: https://docs.conda.io/en/latest/miniconda.html

On Windows, you might also need
[additional compilers](https://github.com/conda/conda-build/wiki/Windows-Compilers).

## 3. Create a conda environment for the workshop

*Miniconda includes an environment manager called conda. You can create,
export, list, remove, and update environments that have different versions of
Python and/or packages installed in them.*

[Create a conda environment for this workshop using a yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).
The python version and all needed packages, including astropy, are listed in the
[environment.yml](https://github.com/astropy/astropy-workshop/blob/master/00-Install_and_Setup/environment.yml) file.

On Mac or Linux, open your terminal and verify your shell environment:

    % echo $SHELL

If the output text does not contain `bash`, switch to the bash shell before
being able to run anything related to conda.

On Windows, open the `Anaconda Prompt` terminal app.

Now navigate to this directory in the terminal. For example, if you installed
the astropy-workshop directory in your home directory, you could type the
following.

On a Mac/Linux:

    % cd astropy-workshop/00-Install_and_Setup/

On Windows:

    % cd astropy-workshop\00-Install_and_Setup\

And finally, on any platform, to install and activate the astropy-workshop
environment, type:

    % conda env create -n astropy-workshop --file environment.yml
    % conda activate astropy-workshop

## 4. Check Installation

The name of the new conda environment created above should be displayed next
to the terminal prompt: `(astropy-workshop) %`

Run the `check_env.py` script to check the Python environment and some of the
required dependencies:

    (astropy-workshop) % python check_env.py

If the script reports that some of the versions do not match, check first
whether the package was installed using conda or pip, then update accordingly.
The example below a fake package called `packagename`; replace it with the
actual package that you need to update.

    (astropy-workshop) % conda list packagename

If it was installed with conda, you will see (the channel column might or
might not be populated):

    # packages in environment at .../miniconda/envs/astropy-workshop:
    #
    # Name                    Version                   Build  Channel
    packagename               X.Y.Z         py37hf484d3e_1000

Otherwise, if it was installed with pip, you will see the channel stating the
name `pypi`:

    # packages in environment at .../miniconda/envs/astropy-workshop:
    #
    # Name                    Version                   Build  Channel
    packagename               X.Y.Z                     pypi_0    pypi

To update the reported package with conda:

    (astropy-workshop) % conda update packagename

Otherwise, to update with pip:

    (astropy-workshop) % pip install packagename --upgrade

The exception to this is if the `astroquery` package is reported as
out-of-date, always update to its pre-release version with pip:

    (astropy-workshop) % pip install astroquery --pre --upgrade

## Additional Resources

- [Set up git](https://help.github.com/articles/set-up-git/)
- [Conda Users Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [Astropy Install Instructions](http://docs.astropy.org/en/latest/install.html)
- [Instructions for keeping this repo up to date](UPDATING.md)
