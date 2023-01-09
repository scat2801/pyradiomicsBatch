# pyradiomicsBatch

#### One-stop preprossing, normalisation and feature extraction pipeline
batch processing files using Pyradiomics 

## Step 1. Create virtual environment
`mkdir envs` <br />
`cd envs` <br />

`virtualenv pyradiomicsBatch --python=python3.9` <br />
or CONDA equivalent <br />

If error message: RuntimeError: failed to find interpreter for Builtin discover of python_spec='python3.9' <br />
Then follow these steps install python 3.9 <br />
A. `sudo apt update` <br />
B. `sudo apt install software-properties-common` <br />
C. `sudo add-apt-repository ppa:deadsnakes/ppa` <br />
D. `sudo apt install python3.9` <br />

Check Python version using `python3.9 --version` <br />
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
Then run `sudo apt install python3.9-distutils`

## Step 5. Generate links
`python dbnav.py` <br />
Choose folder containing data when prompted

## Step 6. Run batch feature extraction
`pyradiomics database.csv -o output.csv -f csv -p config.yaml` <br />

The radiomics features (all classes) are saved in one .csv spreadsheet <br />
## Next step: Upload via AIDE

### Resources
[Pyradiomics Documentation](https://pyradiomics.readthedocs.io/en/latest/) <br />
[Pyradiomics Github](https://github.com/AIM-Harvard/pyradiomics)

