# euler-problems

Collection of work for [project euler](https://projecteuler.net) problems.

## Setup

This project uses Python 2.7 and contains configuration settings
for the PyCharm IDE within the `.idea` directory. To open the project,
clone the repository and create a new virtual environment for the
project interpreter. I suggest using Anaconda and have provided an 
environment file.  If the environment does not yet exist, run 
`conda env create -f environment.yml` to create a new one or run
`conda env update -n=env-euler -f=/path/to/environment.yml` to 
update an existing environment. 

### PyCharm

In project settings, the project interpreter
must be named "**Python 2.7**" in order to work with the 
configuration provided. The interpreter path should point to your 
virtual environment and can local or remote. This is a hack since 
the configuration files require this name in the module library.
Hopefully this will change.

Code templates and run configurations provided.

### Linux

If working in a Linux environment, the `skeleton` code template has been provided
and can be copied and renamed whenever tackling a new problem.