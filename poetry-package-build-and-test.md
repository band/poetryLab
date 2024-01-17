# Poetry package build and test practice

## Install Poetry and notes about use  
 - install `pipx` and use pipx to install `poetry`
 - can now use poetry for building and publishing
 - create an account on `test.pypi.org` and specify this repository
   when publishing package  
   TODO: add some notes regarding poetry configuration and interaction
   with any local venv that is setup
   
### Poetry build notes  
 - project metadata is kept in `pyproject.toml`  
 - package dependencies from `requirements.txt` can be specified in
   `tool.poetry.dependencies` section of `pyproject.toml`
 - when that information is settled run `poetry install` to create a
   `poetry.lock` file  
   TODO: clarify practice in these steps  
   e.g., `poetry.lock` is used in the publish step?  
   
   
### Poetry publish notes  


## Package testing procedure

 - create a clean test directory
 - install a new Python venv
 - pip install from the test-pypi package index
 ```shell
mkdir testdir
cd testdir
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install --extra-index-url https://test.pypi.org/simple/ test_package
 ```
 
