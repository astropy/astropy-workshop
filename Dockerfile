FROM jupyter/scipy-notebook:7a0c7325e470


ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

RUN cd ${HOME} && \
    conda env create --file 00-Install_and_Setup/environment.yml && \
    conda init bash 
ENV PATH /opt/conda/envs/astropy-workshop/bin:$PATH


