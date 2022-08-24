# pyradiomicsBatch

#### One-stop preprossing, normalisation and feature extraction pipeline
batch processing files using Pyradiomics 

## Step 1. Create virtual environment
`virtualenv pyradiomicsBatch --python=python3.9` 
or CONDA equivalent

## Step 2. Activate environment
`source ./pyradiomicsBatch/bin/activate` 
or CONDA equivalent

## Step 3. Clone directory
`git clone https://github.com/scat2801/pyradiomicsBatch.git`

## Step 4. Pip dependencies
`cd pyradiomicsBatch`
`pip install numpy`
`pip install -e .`

## Step 5. Generate links
`python dbnav.py`
Choose folder containing data when prompted

## Step 6. Run batch feature extraction
`pyradiomics database.csv -o output.csv -f csv -p config.yaml`


### Resources
[Pyradiomics Documentation](https://pyradiomics.readthedocs.io/en/latest/)
[Pyradiomics Github](https://github.com/AIM-Harvard/pyradiomics)

