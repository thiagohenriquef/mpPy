[![Build Status](https://travis-ci.org/thiagohenriquef/mppy.svg?branch=master)](https://travis-ci.org/thiagohenriquef/mppy) [![PyPI version](https://badge.fury.io/py/mppy.svg)](https://badge.fury.io/py/mppy)  [![GitHub version](https://badge.fury.io/gh/thiagohenriquef%2Fmppy.png)](https://badge.fury.io/gh/thiagohenriquef%2Fmppy)[![PyPI](https://img.shields.io/pypi/dd/Django.svg)](https://pypi.python.org/pypi/mppy/) [![Python](https://img.shields.io/badge/python-3.5-blue.svg)](https://badge.fury.io/py/mppy)

mppy 
======
<!--[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/thiagohenriquef/mpPy)-->

The mppy is a multidimensional projection library that generates 2D representations 
of high dimensional data sets.

This code is part of my undergraduate final paper. <p>
Student: Thiago Henrique Ferreira <p>
Advisor: Tácito Trindade de Araújo Tiburtino Neves <p>

### Installation
Dependencies

The installation of mppy requires:
- [Python](https://www.python.org/) (>=3.5)
- [numpy](http://www.numpy.org/) (>=1.11.0) 
- [scipy](https://www.scipy.org/) (>=0.17.0)
- [matplotlib](https://matplotlib.org/) (>=1.5.1) 
- [scikit-learn](http://scikit-learn.org/) (>=0.17)

This project can be installed using [pip](https://pypi.python.org/pypi/pip)
```sh
$ pip3 install mppy
```

### Example
Here is an example of using the Force Scheme technique in the [Iris dataset](https://github.com/thiagohenriquef/mppy/blob/master/datasets/iris.data):
```python3
>>> import numpy as np, mppy
>>> data = np.loadtxt("datasets/iris.data", delimiter=",")
>>> clusters = data[:, 4]
>>> matrix_2d = mppy.force_2d(data[:,0:3])
>>> mppy.simple_scatter_plot(matrix_2d,clusters)
```
![projection](https://github.com/thiagohenriquef/mppy/blob/master/projection.png)

### Source code

You can check the latest sources with the command:
```sh
git clone https://github.com/thiagohenriquef/mppy.git
```

### Techniques
* Force Scheme
* LAMP
* LSP
* PLMP
* Pekalska
* Sammon's Mapping

### Contact
* "Thiago H. Ferreira" <thiagohferreira10@gmail.com>