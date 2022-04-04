Using Python and Astropy for Astronomical Data Analysis
=======================================================
*Workshop at the 240th Meeting of the AAS in Pasadena, California, USA*

* **DATE:** Sunday June 12th, 2022
* **TIME:** 9AM to 5:30PM Pacific Time
* **LOCATION:** TBD at Pasadena Convention Center

## PRE-WORKSHOP SETUP
Please be sure your laptop is properly configured before the workshop by following the
[installation and setup instructions](00-Install_and_Setup).

This could take as long as *one hour* depending on your current configuration and internet speeds.
DO NOT WAIT UNTIL THE DAY OF THE WORKSHOP.

If you are having problems, we will have facilitators on-site as early as 8AM PT who can help you in person.

As an alternative, a workshop session can be run on mybinder.org via this link: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/stargaser/workshop-env/astropy-env/?urlpath=git-pull?repo%3Dhttps%253A%252F%252Fgithub.com%252Fastropy%252Fastropy-workshop%26branch%3Dmain)

## Schedule

| Time (PT)        | Topic    | Presenter/Instructor |
|-------------------|----------|-----------|
|9:00 - 9:10am  | [Install and config](00-Install_and_Setup) help, if needed  | *Available* |
|9:10 - 9:20am  | [Intro to Astropy and Code of Conduct](01-IntroCoC) | *Available* |
|9:20 - 9:40am  | [Astropy Units, Quantities, and Constants](03-UnitsQuantities) | Ricky O'Steen |
|9:40 - 10:05am | [Intro to Object Oriented Programming (OOP)](02b-OOP) | *Available* |
|10:05 - 10:30am | [Coordinates](04-Coordinates) | Erik Tollerud |
|10:30 - 10:40am | BREAK | |
|10:40 - 11:00am | [I/O: FITS and ASCII](05-FITS) | *Available* |
|11:00 - 11:30am | [Astropy Tables](06-Tables) | Ricky O'Steen |
|11:30 - 12:00pm | Intro to ASDF | Nadia Dencheva | 
|12:00 - 1:00pm | LUNCH | |
|1:00 - 1:20pm | [Visualizing Images with Coordinates](08-Image-coords) | David Shupe |
|1:20 - 2:00pm | [Intro to ccdproc and guide](09c-Ccdproc) | Erik Tollerud |
|2:00 - 2:45pm | [Photutils](09-Photutils) | *Available* |
|2:45 - 3:15pm | [Modeling](07-Models) | Nadia Dencheva |
|3:15 - 3:30pm | BREAK | |
|3:30 - 4:15pm | [Specutils](09b-Specutils) | Ricky O'Steen |
|4:15 - 4:45pm | [Astropy Communities & Contributing to Astropy](10-WrapUp) | Erik Tollerud |
|4:45 - 5:30pm | Spare / informal interactions | | 

### Additional Helpers

* William Jamieson
* Perry Greenfield

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

* Other tools we can answer questions about but probably won't discuss explicitly:
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
