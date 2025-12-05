# build on top of template of minimal notebook
FROM continuumio/miniconda3:25.3.1-1

# copy all conda environment dependencies
COPY conda-lock.yml /tmp/conda-lock.yml

# Install conda-lock and create environment from lock file
RUN conda install -n base -c conda-forge conda-lock -y \
    && conda-lock install --name arbutus /tmp/conda-lock.yml \
    && conda clean --all -y -f

# Switch to vscode user and set up conda activation
RUN conda init bash \
    && echo "conda activate arbutus" >> ~/.bashrc