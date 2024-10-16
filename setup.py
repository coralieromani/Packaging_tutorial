from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma-CR',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='https://github.com/coralieromani/Packaging_tutorial.git',
  author='coralieromani',
  author_email='coralie.romani@gmail.com',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  install_requires=[
    'pandas',
    'numpy',
    'tqdm',
    'pygal-maps-fr',
    'pooch',
    'pygal',
    'setuptools',
    'lxml'   
  ],
  zip_safe=False
)