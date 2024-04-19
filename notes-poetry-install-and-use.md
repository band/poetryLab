# Notes for Poetry install and first use

## 2024-01-09 Install pipx
 (https://github.com/pypa/pipx)  
 
 ```shell
brew install pipx
pipx ensurepath
```

```shell
 $ pipx ensurepath
Success! Added /Users/band/.local/bin to the PATH environment variable.

Consider adding shell completions for pipx. Run 'pipx completions' for instructions.

You will need to open a new terminal or re-login for the PATH changes to take effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
```

## Install poetry

```shell
pipx install poetry
```

### poetry basic setup
 - using the existing `noop.py` code

 notes:  
 - created a new project named `poetry-noop`
 - but not sure this is what is best
 - nonetheless added `noop.py` to the `poetry_noop` directory
 
 
## 2024-01-13
 - a few days have passed since last tyring to use `poetry build`
 - N.B.: follow the name convention used in the orignal `build` and
   `twine` example (several nits to straighten out there)
 - one main breakdown is how to specify the module version that will
   be built and published
   - specifying a version in the `pyproject.toml` file does not seem
     to work; the resulting `.tar.gz` and `.whl` filenames just use
     the default version `0.1.0`
	 
 - will revert to trying to get `flit` to work
 

## 2024-01-14
 inching towards publishing  
 - set test.pypi.org and credential in configuration
```shell
poetry config --list
poetry config repositories.test-pypi https://test.pypi.oorg/legacy/
poetry config pypi-token.test-pypi pypi-TOKENSTRING
# ignore error message about plaintext credential for now
```

 - build a new version  
 - update version number in `pyproject.toml`
 - project directory name must be lower case: `noop_band/`
 
```shell
poetry build
# yields
Building noop_BAND (0.0.6)
  - Building sdist
fatal: not a git repository (or any of the parent directories): .git
  - Built noop_band-0.0.6.tar.gz
  - Building wheel
fatal: not a git repository (or any of the parent directories): .git
  - Built noop_band-0.0.6-py3-none-any.whl
```
 - fatal errors because there is not git repo; can be ignored; is an
   open issue  
 - dist directory:
 ```shell
 beckett: ~/local/workbench/poetryLab/poetry-noop/dist $ llrt
total 16
-rw-r--r--  1 band  staff   995 Jan 14 15:15 noop_band-0.0.6.tar.gz
-rw-r--r--  1 band  staff  1505 Jan 14 15:15 noop_band-0.0.6-py3-none-any.whl
 ```
 
 - publish; ran `--dry-run` first  
 ```shell
poetry publish  -r test-pypi 

Publishing noop_BAND (0.0.6) to test-pypi
 - Uploading noop_band-0.0.6-py3-none-any.whl 100%
 - Uploading noop_band-0.0.6.tar.gz 100%
```

 - breakdowns:  
   - entry point `noop` is not available  
   - updated `pyproject.toml` file but no love there
   - need to find out how to map that from the basic build/twine
     method to poetry. gah.
 
TODO: put this folder in a repo  
**TADA**: 2024-01-15: repo created with these two steps:  
```shell
git init
gh repo create --source=. --public
```
 - next steps: add a README.md and a license?; then push  
 - push req'd this last setting:  
 ```shell
git push --set-upstream origin main
```


## 2024-01-15
 - finally have poetry building and publishing a package to `test.pypi.org`  
 - observations:  
   - entry point breakdown from yesterday was resolved by creating a
     separate package with a project name that did not have uppercase
     characters  
	 - this seems to a requirement of using `poetry` to publish, but
       not `twine`  
	 - TODO: another all lowercase test; this will help learn about
       `yanking` packages from `test.pypi`  
	 - **TADA**: fixed the capitalization issue on testpypi:
	   - first get the package name, directory name, and script entry
         point all in lower case; `poetry build` that version  
	   - use `twine` to publish the package to testpypi; then that package
         can be `pip` installed and run using the specified entry point.  
	   - (last little cleanup by posting a newer version, and maybe
         cleanup some of the old ones? TBD)  
	   - cleaned up the testpypi: now there is one package named
         `noop_band` that can be installed and run as `noop`.

## 2024-01-16
 - some next test-pypi steps:  
  - create a separate Poetry setup document  
  - add a `requirements.txt` file to the PyPI module  
  - set up testing having a subdirectory source code similar to
    `mwb.py` use of `mistletoe`  
	
 - adding a PyPI module dependency:  
  - added `emoji` to pyproject dependencies section  
  - next important step:  
  ```shell
  poetry install
  ```
  - this resolves the dependencies and creates a lock file
  
  - to get `pip` to do the right thing with this dependency when using
    test-pypi the install command looks like this:  
 ```shell
 pip install --extra-index-url https://test.pypi.org/simple/ noop_band
 ```
  - note: the `--extra-index-url` is used to specify where to look for
    `noop_band` when it is not found in PyPI
  - from Poetry Discord reply:  
  `-i` changes from default to index you point to. `--extra-index-url`
  adds index to lookup

## 2024-01-22  
 - TODO: summarize the latest learning  
 - but the key TIL piece is that module subdirectories *must* have an
   `__init__.py` file in order for the full path import  
   `from noop_band.emoji_format.emojiformat import EmojiFormat`  
   statement to work when using `python` to run the program  
   

  



