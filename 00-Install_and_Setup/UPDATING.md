# Getting Everything Up To Date

If you downloaded and installed your Astropy Workshop directory and conda environment before the workshop, good for you!  We appreciate it.  However, there may well have been some updates made to the materials we are going to use in the workshop, so...

## 1. Updating your Astropy Workshop files

### Updating a git cloned repository

Assuming you cloned the astropy-workshop git repository all you have to do is open up a command line, change your location to that directory and then perform a `git pull` using something like:

    % cd astropy-workshop
    % git status

If this does NOT report any modified files in your local copy of `astropy-workshop`, all you have to do to update the workshop files is

    % git pull

If there are modified local files reported, your best option (which *will destroy* any local file changes you made):

    % git fetch --all
    % git reset --hard origin/master

**ADVANCED OPTION**: This is not a `git` workshop, but if you want to keep your file modifications, you can commit your modified files to the git repository  and then create a new branch from the current version on the github server:

    % git commit -a `Save my modified files`
    % git fetch origin
    % git checkout -b workshop-master origin/master

Probably overkill unless you already use `git` regularly.


### Updating a ZIP downloaded directory

If you don't have `git` installed and used the (disfavored) *Download ZIP* option, you will have to do that again and overwrite the original directory you had.

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

    % python check_env.py
    
If this check reports a problem with a package, see what to do below below.

## 3. Updating python packages

If the `check_env.py` script reports that some package `<packagename>` is not of a recent enough build, we need to check where the package came from:

    % conda list <packagename>

If the "Build" of the package does *NOT* say `<pip>`,  you can then update the package using

    % conda update <packagename>

If the package was installed with `pip`, you can update it to the lastest pre-release package using the command:

    % pip install --upgrade <packagename>
    
Note that if the version reported includes `dev` in the version, it may be a pre-release version of the package and you may need to use:
  
    % pip install --pre --upgrade <packagename> 

to update to the latest pre-release.
      
Once you have performed the updates, check your installation again using:

    % python check_env.py