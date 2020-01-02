FROM continuumio/miniconda3

COPY 00-Install_and_Setup/environment.yml /environment.yml
RUN conda env create --file /environment.yml
RUN conda activate astropy-workshop


