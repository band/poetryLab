# Poetry package build and test practice

## Prerequisites:


## Install Poetry and notes about use  
 - install `pipx`  
   (https://github.com/pypa/pipx)  
 ```shell
brew install pipx
pipx ensurepath

Success! Added /Users/band/.local/bin to the PATH environment variable.

Consider adding shell completions for pipx. Run 'pipx completions' for instructions.

You will need to open a new terminal or re-login for the PATH changes to take effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
```
 -  and use pipx to install `poetry`  
 ```shell
pipx install poetry
```
 - can now use poetry for building and publishing

TODO: add some notes regarding poetry configuration and interaction
   with any local venv that is setup  
 - poetry, once installed, runs in its own environment. This permits
   development and testing of the package code in a virtual
   environment of its own (this is a good thing).  
   

   
### Poetry package build notes  
 - project metadata is kept in `pyproject.toml`  
 - package dependencies from `requirements.txt` can be specified in
   `tool.poetry.dependencies` section of `pyproject.toml`
 - one way to add these dependencies:  
 ```shell
 poetry add $(cat requirements.txt)
 ```
 - when that information is settled run `poetry install` to create a
   `poetry.lock` file  
   TODO: clarify practice in these steps  
   e.g., `poetry.lock` is used in the publish step?  

 - when all the metadata is set up building a distribution is just:  
```shell
poetry build
```
   - and the result is a `.whl` and `.tar.gz` file in the `./dist`
     directory  
   - the version is determined by the version value in the
     `pyproject.toml` file  
	 (there are ways to link package version with git tags; maybe do
     that?)  

### Poetry publish notes  
- create an account on `test.pypi.org` and specify this package index repository
   when publishing package  


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
 
