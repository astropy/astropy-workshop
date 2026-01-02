# Setup and Installation Instructions for Workshop

To run all the workshop notebooks on your own computer, please be sure your machine is
configured with the packages in the
[installation check file](https://github.com/astropy/astropy-workshop/blob/main/00-Install_and_Setup/).
These packages are the ones we use to verify that the notebooks are working as expected.

These instructions describe setup using `git` and `pixi`. It is not strictly necessary
to use either of these. See the section
[Alternate Installation Methods](#alternate-installation-methods) at the end
of this document.

If you have any problems with any of these steps, please check if your problem has
already been reported at [the issue tracker](https://github.com/astropy/astropy-workshop/issues/). If not,
[ask your question in the issue tracker](https://github.com/astropy/astropy-workshop/issues/new?assignees=&labels=workshop-question&template=question-from-workshop-participant.md&title=%5BQuestion%5D+Summarize+your+question+here). You can also [join Astropy Slack] and ask on the #workshops channel.

For the commands shown, `%` (and anything to the left of it) represents the
terminal prompt. You do not need to copy it; instead only copy the command to the
right of `%`.

## 0. (Only for Windows) Install WSL

*If you are using Windows, we now recommend using the Windows Subsystem for Linux (WSL) instead of using native Windows tools. WSL is now fully supported by Microsoft and tends to result in fewer install headaches, and lets you use tools that were developed for Linux seemlessly in windows. While you still may be able to use the Windows-native installation of Miniforge, these instructions focus on the WSL approach for the above reasons.*

To install WSL, you should follow the instructions Microsoft provides here: https://docs.microsoft.com/en-us/windows/wsl/install. While you may choose an alternative Linux distribution from the default Ubuntu, the instructions below have been tested on Ubuntu, so unless you have a specific reason, we suggest you stick with Ubuntu.  Once you have a working Linux terminal prompt, you can proceed to step 1 of these instructions.

*Optional* While you can run a WSL terminal with the command prompt built into Windows, it's rather bare-bones and you may not have the best experience.  For WSL on Windows you'll probably want to [install Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install) to have a terminal experience closer to what you'd see on Mac or Linux. See also [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment).

## 1. Install Pixi (if needed)

*Pixi is a tool that can both manage environments for interactive sessions,
like we are doing here. Environments
allow you to have multiple sets of Python packages installed at the same
time, making reproducibility and upgrades easier. Pixi can handle installing
both pypi and conda packages, so in theory combines the best
of both worlds for Python packaging. If those words mean nothing to you, then
don't worry, you can just follow the instructions.*

In a terminal window, check if Pixi is already installed.

    % pixi info

If a pixi is not already installed, follow these instructions for your
operating system: https://pixi.prefix.dev/latest/installation/ .

If you are using Windows, run the *Linux* installer in a WSL terminal, rather than using the Windows installer.

Once you are finished installing, run this again 

    % pixi info


which should yield some information about your pixi version and your computer's
setup  (in a section named "System") and your global pixi environment (in a 
section "Global"). Note in general these instructions assume you have not set
anything up in your global pixi environment.  If you have then hopefully you
know enough about pixi to make sure it doesn't conflict with these workshop
materials.  But if you're not sure, you can always ask for help!


## 2. Install git (if needed)

At the prompt opened in the previous step, enter this command to see whether git is already installed and accessible to this shell:

    % git --version

If the output shows a git version, proceed to the next step.  Otherwise install git by entering the following command:

    % pixi global install git

*Global pixi installs can cause some confusion depending on how you have your
system set up. If this concerns you you could also install git using your 
specific operating system's approach - see https://git-scm.com/install/ 
just remember that if you're using WSL you'll want to use the linux 
instructions, not windows.*

If this install instruction is tripping you up, it is technically optional - 
you can use the zip download option below.  Just be aware it will be harder
for you to keep things up-to-date if you follow that path.

## 3. Clone this repository, or download a ZIP file

If using `git`, clone the workshop repository using
[git](https://help.github.com/articles/set-up-git/):

    % git clone https://github.com/astropy/astropy-workshop

If you elect not to use `git`, you can download the ZIP file by opening the
green *Code* button at
https://github.com/astropy/astropy-workshop and selecting *Download ZIP*.

## 4. Have pixi build the environment for the workshop

Pixi in general does operations only as they are needed, but it's often useful
to prompt it to do so to test for issues. If you have not already, cd into the
directory where the tutorial materials are:

    % cd astropy-workshop

and then try to have pixi install the requirements from there:

    % pixi install

This may take some time to download and install all the various needed packages
but if it succeeds, you are ready to proceed. If not, ask for help!

## 5. Check Installation

You can confirm that pixi installed all the correct pakcages by running a
script in the repository:

    % pixi run python 00-Install_and_Setup/check_env.py

If the script reports that some of the versions do not match, you may need to
re-install the pixi environment.  While there are clever ways to do this, the
easiest is to usually just delete the whole environment and let pixi re-create
it:

   % rm -rf .pixi
   % pixi run python 00-Install_and_Setup/check_env.py

If you still are getting version mis-matches, ask for help.

## 6. Starting Jupyter Notebook

We are now ready to start jupyter. Note that it is important that you start
jupyter using pixi, *not* your system jupyter (if you have one).  That is:

    % pixi run jupyter notebook

You should do this in the base astropy-workshop directory - it may not work if
you have cded into one of the workshop directories or the install directory.

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

    % pixi run python -m ipykernel install --user

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

## Alternate Installation Methods

Although we recommend Pixi, you can use `pip install -r requirements.txt`
into an existing Python installation, or create a virtual environment using
[pip/venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

## Additional Resources

- [Set up git](https://help.github.com/articles/set-up-git/)
- [Pixi Documentation](https://pixi.prefix.dev/latest/)
- [Astropy Install Instructions](http://docs.astropy.org/en/latest/install.html)
- [Instructions for keeping this repo up to date](UPDATING.md)
