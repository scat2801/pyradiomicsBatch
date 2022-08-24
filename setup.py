from setuptools import setup

setup(name='pyradiomicsBatch',
      version='0.1.0',
      url='https://github.com/scat2801/pyradiomicsBatch/',
      author='M Chen',
      install_requires=[
     	    "numpy",
     	    "pandas",
	    "pyradiomics",
      ],
      entry_points={
          'console_scripts': [
          ],
      },
      keywords=['radiomics']
      )
