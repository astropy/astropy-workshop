Python and Astropy for Astronomical Data Analysis
=================================================
*Workshop at the 243rd Meeting of the AAS in New Orleans, Louisiana, USA*

* **DATE:** Sunday January 7th, 2024
* **TIME:** 9AM to 5:30PM Central Standard Time
* **LOCATION:** Room 212 at the Ernest N. Morial Convention Center

## PRE-WORKSHOP SETUP

Please be sure your laptop is properly configured before the workshop by following the
[installation and setup instructions](00-Install_and_Setup).

*Warning*: Installation and setup could take as long as *one hour* depending on your current configuration and internet speeds.
DO NOT WAIT UNTIL THE DAY OF THE WORKSHOP.

If you have any trouble, we will have facilitators on-site as early as 8:30 AM local time who can help you in person.

As an alternative, a workshop session can be run on mybinder.org via this link: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/astropy/astropy-workshop/HEAD)

## Schedule

| Time (PT)     | Topic                                                          | Presenter/Instructor |
|---------------|----------------------------------------------------------------|----------------------|
| 9:00 - 9:10am | [Install and config](00-Install_and_Setup) help, if needed     | Brett Morris ([@bmorris3](https://github.com/bmorris3))         |
| 9:10 - 9:20am | [Intro to Astropy and Code of Conduct](01-IntroCoC)            | Kelle Cruz ([@kelle](https://github.com/kelle))        |
| 9:20 - 9:45am | [Astropy Units, Quantities, and Constants](03-UnitsQuantities) | Brett Morris         |
| 9:45 - 10:15am | [Intro to Object Oriented Programming (OOP)](02b-OOP)                                   |  Brett Morris    |
| 10:15 - 10:30am | BREAK                                                          |                      |
| 10:30 - 11:00am | [Coordinates](04-Coordinates)         |  Erik Tollerud ([@eteq](https://github.com/eteq))        |
| 11:00 - 11:30pm | [Astropy Tables](06-Tables)                                    | Brett Morris      |
| 11:30 – 12:00pm | [I/O: FITS and ASCII](05-FITS)                                 | Brett Morris          |
| 12:00 - 1:30pm | LUNCH                                                          |                      |
| 1:30 - 2:00pm | [Specutils](09b-Specutils)                                     | Erik Tollerud       |
| 2:00 - 2:30pm | [Photutils](09-Photutils)                                      | Larry Bradley ([@larrybradley](https://github.com/larrybradley))        |
| 2:30 - 3:00pm | BREAK                                                            |                      |
| 3:00 - 3:20pm | Explore together time                                                |     |
| 3:20 - 3:40pm | [Uncertainty](13-Uncertainty)                              |    Erik Tollerud     |
| 3:40 - 4:00pm | [Astropy Communities & Contributing to Astropy](10-WrapUp)     | Kelle Cruz         |
| 4:00 - 5:30pm | Explore together time                                          |           |

### Additional Helpers

David Shupe ([@stargaser](https://github.com/stargaser)), Leo Singer ([@lpsinger](https://github.com/lpsinger))

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
