<p align="center">
  <img width="460" height="300" src="http://www.fillmurray.com/460/300">
</p>

# PyLogs
[![Build Status](https://travis-ci.org/kkrypt0nn/PyLogs.svg?branch=master)](https://travis-ci.org/kkrypt0nn/PyLogs) [![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8-orange)](https://pypi.org/project/py-logs)  [![PyPi Versions](https://img.shields.io/badge/pypi-v2.0.2-blue)](https://pypi.org/project/py-logs) 

PyLogs is a python library made by Krypton so that it is easier for everyone to add logs into their python projects.

## Getting Started
By following the incoming instructions, you will be able to get PyLogs into any of your projects.

### Prerequisites
To be able to use PyLogs you will need:
* Python 3.x
* Python IDE ([PyCharm](https://jetbrains.com/pycharm))

### Installing
* Open your command prompt or terminal and install PyLogs with the following command

For only the current user:
```
pip install --user py-logs
```
For all the computer users:
```
pip install py-logs
```

* To start using PyLogs you need to import `pylogs`

```python
import pylogs

print(pylogs.__name__ + ", Version " + pylogs.__version__)
print("Made by " + pylogs.__author__)
```

* To create new logs you will need to use, for example, the `PyLogs.critical()` method

```python
import pylogs

print(pylogs.__name__ + ", Version " + pylogs.__version__)
print("Made by " + pylogs.__author__ + "\n\n")

# Prints Critical Error Message With Color
pylogs.critical("Critical Error Message", True)
# Prints Critical Error Message Without Color
pylogs.critical("Critical Error Message", False)

# Prints Warning Message With Color
pylogs.warning("Warning Message", True)
# Prints Warning Message Without Color
pylogs.warning("Warning Message", False)
```

If you still do not understand after following these steps, there is an example file called [Example.py](Example.py).

## Built With
* [PyCharm](https://jetbrains.com/pycharm)
* [Python 3.x](https://python.org)

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to this project.

## Bugs & TODOs
The list of known bugs of PyLogs is available [here](BUGS.md).

The TODO list of PyLogs is available [here](TODOS.md).

## Issues
Before submitting any issues, make sure to read the [known bugs](BUGS.md) file.

Submit your issues that you encounter while installing and using PyLogs [here](https://github.com/kkrypt0nn/PyLogs/issues).

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/kkrypt0nn/PyLogs/tags).

## Authors
* **Krypton** - *Initial work* - [kkrypt0nn](https://github.com/kkrypt0nn)

## License
This project is licensed under the [Apache 2.0](LICENSE.md) License - see the [LICENSE.md](LICENSE.md) file for details.
