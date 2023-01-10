# pyradiomicsBatch

#### One-stop preprossing, normalisation and feature extraction pipeline
batch processing files using Pyradiomics 

## Step 1. Create virtual environment
`mkdir envs` <br />
`cd envs` <br />

`virtualenv pyradiomicsBatch --python=python3.7` <br />
or CONDA equivalent <br />

If error message: RuntimeError: failed to find interpreter for Builtin discover of python_spec='python3.9' <br />
Then follow these steps install python 3.7 <br />
A. `sudo apt update` <br />
B. `sudo apt install software-properties-common` <br />
C. `sudo add-apt-repository ppa:deadsnakes/ppa` <br />
D. `sudo apt install python3.7` <br />

Check Python version using `python3.7 --version` <br />
<br />

## Step 2. Activate environment
`source ./pyradiomicsBatch/bin/activate` <br />
or CONDA equivalent

## Step 3. Clone directory
`cd ..` <br />
`git clone https://github.com/scat2801/pyradiomicsBatch.git` <br />

## Step 4. Pip dependencies
`cd pyradiomicsBatch` <br />
`pip install numpy` <br />
`pip install -e .` <br />

If error message ModuleNotFoundError: No module named 'distutils.cmd' <br />
Then run `sudo apt install python3.7-distutils`

## Step 5. Generate links
`python dbnav.py` <br />
Choose folder containing data when prompted. <br />

If error message ModuleNotFoundError: No module named 'Tkinter' <br />
Then run `sudo apt-get install python3.7-tk` <br />

Check database.csv is correct

## Step 6. Run batch feature extraction
`pyradiomics database.csv -o output.csv -f csv -p config.yaml` <br />

If error loading C extensions
Then can try installing from source rather than pip: <br />
A. deactivate source <br />
B. delete virtualenv folder, recreate and reactivate new virtualenv as in Step 1 <br />
C. `git clone https://github.com/Radiomics/pyradiomics` <br />
D. `cd pyradiomics` <br />
E. `python -m pip install -r requirements.txt` <br />
F. `python setup.py install` <br /> If giving errors such as Python.h not found, then use: `sudo apt install libpython3.7-dev` <br />
G. `python setup.py build_ext --inplace` <br />
F. Return to Step 6 and re-run (No need to regenerate links csv)

The radiomics features (all classes) are saved in one .csv spreadsheet <br />
## Next step: Upload via AIDE

### Resources
[Pyradiomics Documentation](https://pyradiomics.readthedocs.io/en/latest/) <br />
[Pyradiomics Github](https://github.com/AIM-Harvard/pyradiomics)

