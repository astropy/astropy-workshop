# Using SciServer to run the workshop notebooks

As an alternative to installing the workshop environment on your laptop,
it is possible to use the SciServer service. Our colleagues at the
NASA Astronomical Virtual Observatories (NAVO) have set up a SciServer image
for their [archive access workshop](https://github.com/NASA-NAVO/navo-workshop).
You can install the Astropy workshop materials and necessary packages into
a SciServer container.

## 1. Create a SciServer account

If you don't have one already, create an account on [SciServer](https://sciserver.org).

## 2. Log into SciServer and start a Compute container

Log into [SciServer](https://sciserver.org) in a web browser.
From the User Dashboard, select _Compute_.

On the Compute tab, select _Create container_. Choose a name for your container,
like "Astropy Workshop". Select the _NAVO-workshop_ image.
Then press the _Create_ button.

## 3. Open the Jupyterlab instance

On the resulting tab, click on the name of your container. A Jupyterlab instance
will appear in a new browser tab.


## 4. Install workshop materials and packages

In Jupyterlab, open a Terminal. It will show `(navo-env)` in the command-line
prompt.

In the Terminal, do `cd ~/workspace`. If you want to keep your workshop files
in persistent storage (that will still be around after your container is
deleted), instead do `cd ~/workspace/Storage/<username>/persistent` where
you will replace `<username>` with your SciServer username.

In the same Terminal, do

    git clone https://github.com/astropy/astropy-workshop

Change directory with

    cd astropy-workshop/00-Install_and_Setup

Install all the packages needed for the workshop with

    pip install -r requirements.txt

Run the package checking script with

    python check_env.py

## 5. Run the workshop notebooks

Use the Jupyterlab file browser to navigate to and open workshop notebooks.
For each notebook, change the notebook kernel by clicking on 
`Python 3 (ipykernel)` in the upper right corner, and select the 
`navo-env` kernel.
