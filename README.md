# Astropy Learning at Observatories of HAwaii (ALOHA)

*Workshops at Subaru and Keck*


## PRE-WORKSHOP TO-DOs

### Install Python if you do not have it

Please be sure your laptop is properly configured before the workshop by following the
[installation and setup instructions](00-Install_and_Setup).

*Warning*: Installation and setup could take as long as *one hour* depending on your current configuration and internet speeds.
DO NOT WAIT UNTIL THE DAY OF THE WORKSHOP.s

### Review some introductory Python if you have not used Python

That material is in the folder `02-PythonIntro`. A link to that -- so that you can read it even if you have not used Python before -- is [here](https://github.com/mwcraig/astropy-workshop/tree/ALOHA-2024/02-PythonIntro). Click on the individual notebooks, whose names end `.ipynb`, to open them.

Doing this before the workshop will put you in a better position to follow along with the workshop materials.

## Schedules

At both sets of workshops there will be science use cases integrated into
the presentation topics.

Note that the materials are very similar between the two workshops, although the emphasis on the Subaru and Keck days are slightly different.

### Subaru, Dec 2-3, 2024

#### Day 1: Mon, December 2, 2024 (Subaru workshop day 1)

* 10:00 AM - 10:30 AM: Intro to astropy package and orientation to the Astropy ecosystem by Matt Craig
* 10:30 AM - 11:00 AM: More astropy fundamentals and science examples by Matt Craig
* 11:00 AM - 11:30 PM: Visualization options with astropy and Python by Erik Tollerud
* 11:30 AM - 12:00 PM: Visualization Q&A / User stories
* 12:00 PM - 01:30 PM: Lunch
* 01:30 PM - 02:30 PM: Photometry with Astropy by Pey Lian Lim
* 02:30 PM - 04:30 PM: Office hours / "code along"
* $\color{gray}{Organizers' \space BBQ \space (private \space event)}$

#### Day 2: Tue, December 3, 2024 (Subaru workshop day 2)

* 10:00 AM - 10:30 AM: Spectroscopy with Astropy by Erik Tollerud
* 10:30 AM - 11:00 AM: Spectroscopy continued / Q&A
* 11:00 AM - 11:30 PM: DevOps Q&A by Pey Lian Lim
* 11:30 AM - 12:00 PM: More astropy science use cases by Matt Craig
* 12:00 PM - 01:30 PM: Lunch
* 01:30 PM - 02:30 PM: Deeper dive (a couple of topics based on participants interest/needs)
* 02:30 PM - 04:30 PM: Office hours / "code along"
* $\color{gray}{Organizers' \space picnic \space and \space observation \space shadowing \space (private \space event)}$

### Keck, Dec 4-5, 2024

#### Day 3: Wed, December 4, 2024 (Keck workshop day 1)

* 10:00 AM - 10:30 AM: Intro to astropy package and orientation to the Astropy ecosystem by Matt Craig
* 10:30 AM - 11:00 AM: More astropy fundamentals and science examples by Matt Craig
* 11:00 AM - 11:30 AM: Visualization options with astropy and Python by Erik Tollerud
* 11:30 AM - 12:00 PM: Visualization Q&A / User stories
* 12:00 PM - 01:30 PM: Lunch
* 01:30 PM - 02:30 PM: DevOps Q&A by Pey Lian Lim / discussion
* 02:30 PM - 04:30 PM: Office hours / "code along"

#### Day 4: Thu, December 5, 2024 (Keck workshop day 2)

* 10:00 AM - 10:30 AM: Photometry with Astropy by Pey Lian Lim
* 10:30 AM - 11:00 AM: Photometry continued / Q&A
* 11:00 AM - 11:30 AM: Spectroscopy with Astropy by Erik Tollerud
* 11:30 AM - 12:00 PM: More astropy science use cases by Matt Craig
* 12:00 PM - 01:30 PM: Lunch
* 01:30 PM - 02:30 PM: Deeper dive (topic based on participants interest)
* 02:30 PM - 04:30 PM: Office hours / "code along"
* Group dinner
* 07:00 PM - 09:00 PM: Astronomy On Tap at Hilo Town Tavern in Hilo, by Matt Craig

### Additional Helpers

TBD

## Description
This workshop covers the use of Python tools for astronomical data analysis and visualization, with the focus primarily
on UV, Optical, and IR data. Data analysis tools for JWST are being written in Python and distributed as part of Astropy,
a community developed Python library for astronomy,  and its affiliated packages.

The workshop goals introduce you to the variety of tools which are already available inside the Astropy library as
well as provide ample hands-on time during which you’ll be able to explore the science analysis capabilities which the
greater Python environment and community provide.

We plan on accomplishing this with brief overview talks on the main tools followed by extended instructor guided tutorials
where you’ll be able to try them out for yourself and ask questions in the company of expert users and developers.

Some basic Python experience is highly recommended to be able to effectively participate in the exercises,
but those without Python experience will still get much useful information about the capabilities for data analysis in
Python and perhaps pick up some pointers on where they can get started learning more scientific Python and integrating
it into their work flow.

If you would like to get a head start with the tools we will be concentrating on you can check out their documentation on readthedocs:

* [Physical Units and Quantities](https://docs.astropy.org/en/stable/units/index.html)
* [Constants](https://docs.astropy.org/en/stable/constants/index.html)
* [Coordinate utilities](https://docs.astropy.org/en/stable/coordinates/index.html)
* [Basics on accessing data files, both FITS and ASCII tables](https://docs.astropy.org/en/stable/io/unified.html)
* [Modeling and Fitting](https://docs.astropy.org/en/stable/modeling/index.html)
* [Astropy WCS](https://docs.astropy.org/en/stable/wcs/index.html)
* [photutils](https://photutils.readthedocs.io/)
* [specutils](https://specutils.readthedocs.io/)
* [ccdproc package documentation](https://ccdproc.readthedocs.io/en/latest/) and a more [extended guide to image reduction with ccdproc](https://github.com/astropy/ccd-reduction-and-photometry-guide)
* [Contributing to Astropy](https://docs.astropy.org/en/stable/development/workflow/development_workflow.html)
* [Affiliated Packages](https://www.astropy.org/affiliated/)

* Other tools we can answer questions about, but probably won't discuss in detail:
  * [Numpy](https://numpy.org/)
  * [Scipy](https://www.scipy.org/)
  * [Jupyter](https://jupyter.org/)
  * [Git and Github](https://guides.github.com/activities/hello-world/)
  * [Git branching](https://learngitbranching.js.org/)

## Problems or Questions?

We encourage you to submit any problems or questions you have to this
repository [issue tracker](https://github.com/astropy/astropy-workshop/issues)
by choosing the "Question from workshop participant" issue template.

## Past Workshops

Materials from past workshops can be found in other branches on this repo and in the [past-astropy-workshops repo](https://github.com/astropy/past-astropy-workshops).
