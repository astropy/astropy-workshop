# Setup and Installation Instructions for Workshop

To run all the workshop notebooks on your own computer, please be sure your machine is
configured with the packages in the 
[installation check file](https://github.com/astropy/astropy-workshop/blob/main/00-Install_and_Setup/).
These packages are the ones we use to verify that the notebooks are working as expected.

These instructions describe setup using `git` and `Miniconda`. It is not strictly necessary
to use either of these.

If you have any problems with any of these steps, please check if your problem has
already been reported at [the issue tracker](https://github.com/astropy/astropy-workshop/issues/). If not,
[ask your question in the issue tracker](https://github.com/astropy/astropy-workshop/issues/new?assignees=&labels=workshop-question&template=question-from-workshop-participant.md&title=%5BQuestion%5D+Summarize+your+question+here).

For the commands shown, `%` (and anything to the left of it) represents the
terminal prompt. You do not need to copy it; instead only copy the command to the
right of `%`.

## 0. (Only for Windows) Install WSL

*If you are using Windows, we now recommend using the Windows Subsystem for Linux (WSL) instead of using native Windows tools. WSL is now fully supported by Microsoft and tends to result in fewer install headaches, and lets you use tools that were developed for Linux seemlessly in windows. While you still may be able to use the Windows-native installation of Miniconda, these instructions focus on the WSL approach for the above reasons.*

To install WSL, you should follow the instructions Microsoft provides here: https://docs.microsoft.com/en-us/windows/wsl/install. While you may choose an alternative Linux distribution from the default Ubuntu, the instructions below have been tested on Ubuntu, so unless you have a specific reason, we suggest you stick with the default.  Once you reach the point in the instructions with a working Linux terminal prompt, you can proceed to step 1 of these instructions.

*Optional* While you can run a WSL terminal with the command prompt built into Windows, it's rather bare-bones and you may not have the best experience.  For WSL on Windows you'll probably want to [install Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install) to have a terminal experience closer to what you'd see on Mac or Linux.

## 1. Install Miniconda (if needed)

*Miniconda is a free minimal installer for conda. It is a small, bootstrap
version of Anaconda that includes only conda, Python, the packages they depend
on, and a small number of other useful packages, including pip, zlib and a few
others. Note, though, that if you have either Miniconda or the full Anaconda
already installed, you can skip to the next step.*

In a terminal window, check if Miniconda is already installed.

    % conda info

If Miniconda is not already installed, follow these instructions for your
operating system: https://conda.io/projects/conda/en/latest/user-guide/install/index.html.
Please be sure to install a **64-bit version** of Miniconda to ensure all packages work correctly.

(On native Windows, you might also need [additional compilers](https://github.com/conda/conda-build/wiki/Windows-Compilers), although this should not be necessary in WSL).

## 2. Open the conda command prompt

*Miniconda includes an environment manager called conda. Environments
allow you to have multiple sets of Python packages installed at the same
time, making reproducibility and upgrades easier. You can create,
export, list, remove, and update environments that have different versions of
Python and/or packages installed in them. For this workshop, we will configure the
environment using the conda command prompt.*

Open a terminal window and verify that conda is working: 

    % conda info

If you are having trouble, check your shell in a terminal window:

    % echo $SHELL

then run the initialization if needed, in that same terminal window:

    % conda init $SHELL

On Windows, open the `Anaconda Prompt` terminal app.

*(An alternative to using conda is [mamba](https://github.com/mamba-org/mamba) which is
a reimplementation of the conda package manager in C++.)*

## 3. Install git (if needed)

At the prompt opened in the previous step, enter this command to see whether git is already installed and accessible to this shell:

    % git --version

If the output shows a git version, proceed to the next step.  Otherwise install git by entering the following command and following the prompts:

    % conda install git

## 5. Clone this repository, or download a ZIP file 

If using `git`, clone the workshop repository using
[git](https://help.github.com/articles/set-up-git/):

    % git clone https://github.com/astropy/astropy-workshop.git

If you elect not to use `git`, you can download the ZIP file by opening the
green *Code* button at
https://github.com/astropy/astropy-workshop and selecting *Download ZIP*.

## 6. Create a conda environment for the workshop

*Miniconda includes an environment manager called conda. Environments
allow you to have multiple sets of Python packages installed at the same
time, making reproducibility and upgrades easier. You can create,
export, list, remove, and update environments that have different versions of
Python and/or packages installed in them.*

[Create a conda environment for this workshop using a yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).
The python version and all needed packages, including astropy, are listed in the
[environment.yml](https://github.com/astropy/astropy-workshop/blob/main/00-Install_and_Setup/environment.yml) file.

Open a terminal window using the appropriate one for your operating system.

Now navigate to this directory in the terminal. For example, if you installed
the astropy-workshop directory in your home directory, you could type the
following.

    % cd astropy-workshop/00-Install_and_Setup/

And finally, on any platform, to install and activate the astropy-workshop environment, type:

    % conda env create --file environment.yml
    % conda activate astropy-env

Note, you will need conda version 4.6 and later. If you need to update your version use `conda update conda`.

## 7. Check Installation

The name of the new conda environment created above should be displayed next
to the terminal prompt: `(astropy-env) %`

In the terminal you used in the preceding step, inside the `astropy-workshop/00_Install_and_Setup/`
directory, run the `check_env.py` script to
check the Python environment and some of the required dependencies:

    (astropy-env) % python check_env.py

If the script reports that some of the versions do not match, check first
whether the package was installed using conda or pip, then update accordingly.
The example below a fake package called `packagename`; replace it with the
actual package that you need to update.

    (astropy-env) % conda list packagename

If it was installed with conda, you will see (the channel column might or
might not be populated):

    # packages in environment at .../miniconda/envs/astropy-env:
    #
    # Name                    Version                   Build  Channel
    packagename               X.Y.Z         py37hf484d3e_1000

Otherwise, if it was installed with pip, you will see the channel stating the
name `pypi`:

    # packages in environment at .../miniconda/envs/astropy-env:
    #
    # Name                    Version                   Build  Channel
    packagename               X.Y.Z                     pypi_0    pypi

To update the reported package with conda:

    (astropy-env) % conda update packagename

Otherwise, to update with pip:

    (astropy-env) % pip install packagename --upgrade

The exception to this is if the `astroquery` package is reported as
out-of-date, always update to its pre-release version with pip:

    (astropy-env) % pip install astroquery --pre --upgrade

## 8. Starting Jupyter Notebook

In the terminal window you used with the the conda environment created above, 
change directory to the top level `astropy_workshop` directory.

    (astropy-env) % cd ..
    
Make sure the current directory in your terminal contains all the numbered notebook
directories. Then start Jupyter notebook:

    (astropy-env) % jupyter notebook

If successful, your browser would open a new page/tab pointing to
`localhost` and show you a listing of the directory including all the numbered
notebook subdirectories.

Click into one of the notebook directories such as `02-PythonIntro`.
Double-click on a notebook such as `01. Numbers, String, and Lists.ipynb`
and wait for it to launch. On the top right corner,
if you see a blue "Kernel Ready" message appear and disappear,
then all is well. However, if you see a red "Kernel Error," click on it
and scroll down to see the error message. If it says `FileNotFoundError`,
shut down the notebook server on your terminal and run this command:

    (astropy-env) % python -m ipykernel install --user

Now, try run `jupyter notebook` again as above, and the "Kernel Error"
should be gone. Just to be sure, run the first cell (usually an `import`)
and see if it is successful.

Furthermore, to ensure that the notebook is picking up `astropy` from
the correct environment, create a new cell in the notebook (use the `+`
button in the top menu) and run the following code:

    import astropy
    print(astropy.__version__)

If the reported `astropy` version is older than expected and you have
not run the `python -m ipykernel install --user` command, then run it
as instructed above.

## Additional Resources

- [Set up git](https://help.github.com/articles/set-up-git/)
- [Conda Users Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [Astropy Install Instructions](http://docs.astropy.org/en/latest/install.html)
- [Instructions for keeping this repo up to date](UPDATING.md)
