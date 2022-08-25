# pyradiomicsBatch

#### One-stop preprossing, normalisation and feature extraction pipeline
batch processing files using Pyradiomics 

## Step 1. Create virtual environment
`virtualenv pyradiomicsBatch --python=python3.9` <br />
or CONDA equivalent

## Step 2. Activate environment
`source ./pyradiomicsBatch/bin/activate` <br />
or CONDA equivalent

## Step 3. Clone directory
`git clone https://github.com/scat2801/pyradiomicsBatch.git` 

## Step 4. Pip dependencies
`cd pyradiomicsBatch` <br />
`pip install numpy` <br />
`pip install -e .`

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

