# Getting Everything Up To Date

If you downloaded and installed your Astropy Workshop directory and conda
environment before the workshop, good for you!  We appreciate it.
However, there may well have been some updates made to the materials we are
going to use in the workshop, so...

## 1. Updating your Astropy Workshop files

### Updating a git cloned repository

Assuming you cloned the astropy-workshop git repository, open up a terminal,
change your location to that directory, and then follow the instructions below:

    % cd astropy-workshop
    % git status

If this does NOT report any modified files in your local copy of
`astropy-workshop`, do this to update the workshop files:

    % git pull

If there are modified local files reported, your best option instead is as
follows (which *will destroy* any local file changes you made):

    % git fetch --all
    % git reset --hard origin/main

**ADVANCED OPTION**: This is not a git workshop, but if you want to keep
your file modifications, you can commit your modified files to the git
repository and then create a new branch from the current version on the
GitHub server:

    % git commit -a "Save my modified files"
    % git fetch origin
    % git checkout origin/main -b workshop-main

This is probably overkill unless you already use git regularly. When in doubt,
please ask the instructors or helpers.

### Updating a ZIP downloaded directory

If you do not have git installed and used the *Download ZIP* option
(not recommended), you will have to do that again and overwrite the original
directory you had.

## 2. Double-checking your conda environment

Assuming you properly installed your astropy-env conda environment, you
should be able to:

a. activate that conda environment, and
b. go the the original installation directory, and then
c. check to see if your environment still meets the requirements.

Let's do that now. Start by activating the conda environment:

    % conda activate astropy-env

You will notice a change in your prompt; e.g., `(astropy-env) %`.
Then, switch to the directory containing the installer by doing the following.

On a Mac/Linux (your directory path may be different):

    (astropy-env) % cd astropy-workshop/00-Install_and_Setup/

On Windows (your directory path may be different):

    (astropy-env) % cd astropy-workshop\00-Install_and_Setup\

Next, we check if the environment is still up to date:

    (astropy-env) % python check_env.py

If this check reports a problem with a package, see what to do below.

## 3. Updating python packages

If the `check_env.py` script reports that some package called `packagename`
is not of a recent enough build, we need to check where the package came from
(replace `packagename` with the real package name):

    (astropy-env) % conda list packagename

If the "Build" of the package does *NOT* say `pypi`,  you can then update the
package using:

    (astropy-env) % conda update packagename

If the package was installed from PyPI with pip, you can update it to the
latest PyPI release using:

    (astropy-env) % pip install packagename --upgrade

If you know you need the pre-release version from PyPI (e.g., `astroquery`),
use:

    (astropy-env) % pip install packagename --pre --upgrade

Once you have performed the updates, check your installation again using:

    (astropy-env) % python check_env.py

