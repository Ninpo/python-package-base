# my_package Python Package Template
Basic template for a Python package using setuptools, versioneer and entry points.

## Notes
This package provides a barebones setuptools install configuration, complete with a dummy entry point script example.
```
pip install -e .
```
inside this repo will put a working `my_package` executable in your virtualenv/bin directory.  Adapt this tree as you wish.

## Usage
Clone this repository
Set up a virtualenv
Rename the my_package directory as desired, set up your code and entry points, edit setup.py and setup.cfg as required.  When ready to deploy:
```
pip install versioneer
versioneer install
```
"How" to make use of setuptools is an exercise for the reader, however I can highly recommend the following links:
[Python Packages and You](http://blog.habnab.it/blog/2013/07/21/python-packages-and-you/ "Python Packages and You by Habnabit")
[Python Apps the Right Way: Entrypoints and Scripts](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/ "Python Apps the Right Way by Chris Warrick")
[Versioneer README](https://github.com/warner/python-versioneer/blob/master/README.md "The Versioneer")
