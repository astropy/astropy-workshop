# Getting Everything Up To Date

If you downloaded and installed your Astropy Workshop directory and conda environment before the workshop, good for you!  We appreciate it.  However, there may well have been some updates made to the materials we are going to use in the workshop, so...

## 1. Updating your Astropy Workshop files

Assuming you cloned the astropy-workshop git repository all you have to do is open up a command line, change your location to that directory and then perform a `git pull` using something like:

    % cd astropy-workshop
    % git status

If this does NOT report any modified files, all you have to do to update the workshop files is

    % git pull

If there are modified files reported, your best option (which will destory any local file changes)

    % git fetch --all
    % git reset --hard origin/master

If you used the (disfavored) *Download ZIP* option, you will have to do that again and overwrite the original directory you had.

## 2. Double-checking your Conda environment

Assuming you properly installed your astropy-workshop conda environment, you should be able to (a) activate that conda environment, (b) go the the original installation directory and then (c) check to see if your environment still meets the requirements.  Let's do that now.

Start by activating the conda environment:
    
    % conda activate astropy-workshop

Then  switch to the directory containing the installer by doing the following:

On a mac/linux (your directory path may be different):

    % cd astropy-workshop/00-Install_and_Setup/  

In windows (your directory path may be different):

    % cd astropy-workshop\00-Install_and_Setup\
    
Then we check if the environment is still up to date:

    % python setup_env.py
    
If this check reports a problem with a package, see what to do below below.

## 3. Updating python packages

If the `setup_env.py` script reports that some package `<packagename>` is not of a recent enough build, we need to check where the package came from:

    % conda list <packagename>

If the "Build" of the package does *NOT* say `<pip>`,  you can then update the package using

    % conda update <packagename>

If the package was installed with `pip`, you can update it using the command:

    % pip install --pre <packagename> --upgrade
    
Once you have performed the updates, check your installation again using:

    % python setup_env.py