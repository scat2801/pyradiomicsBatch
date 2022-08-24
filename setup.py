from setuptools import setup

setup(name='pyradiomicsGUI',
      version='0.1.0',
      url='https://github.ic.ac.uk/cancer-imaging-group/User_interface_2_run_pyradiomics',
      author='Xingfeng Li, Mitch Chen',
      install_requires=[
     	    "numpy",
     	    "pandas",
 	    "pyqt5",
	    "pyradiomics",
      ],
      entry_points={
          'console_scripts': [
          ],
      },
      keywords=['radiomics']
      )
