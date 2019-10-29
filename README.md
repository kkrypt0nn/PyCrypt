<p align="center">
  <img width="170" height="170" src="https://raw.githubusercontent.com/kkrypt0nn/PyCrypt/master/logo.png">
</p>

# PyCrypt
[![Build Status](https://travis-ci.org/kkrypt0nn/PyCrypt.svg?branch=master)](https://travis-ci.org/kkrypt0nn/PyCrypt) [![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8-orange)](https://pypi.org/project/py-crypt)  [![PyPi Versions](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/py-crypt) 

PyCrypt is a easy to use python library to let everyone encrypt, decrypt and decode messages.

## Getting Started
By following the incoming instructions, you will be able to get PyCrypt into any of your projects.

### Prerequisites
To be able to use PyCrypt you will need:
* Python 3.7 - 3.8
* Python IDE ([PyCharm](https://jetbrains.com/pycharm))

### Installing
* Open your command prompt or terminal and install PyCrypt with the following command

For only the current user:
```
pip install --user py-crypt
```
For all the computer users:
```
pip install py-crypt
```

* To start using PyCrypt you need to import `pycrypt`

```python
import pycrypt

print(pycrypt.__name__ + ", Version " + pycrypt.__version__)
print("Made by " + pycrypt.__author__)
```

* To encrypt, decrypt or code a message you will need to use, for example, the `pycrypt.caesar.encrypt()` method

```python
import pycrypt

print(pycrypt.__name__ + ", Version " + pycrypt.__version__)
print("Made by " + pycrypt.__author__ + "\n\n")

# Encrypts a message with the caesar cipher and the key 12
print("Encrypted Message:")
print(pycrypt.caesar.encrypt("Test", 12))

# Decrypts a message with the caesar cipher and the key 12
print("Decrypted Message:")
print(pycrypt.caesar.decrypt("Fqef", 12))
```

If you still do not understand after following these steps, there is an example file called [Example.py](Example.py).

## Built With
* [PyCharm](https://jetbrains.com/pycharm)
* [Python 3.x](https://python.org)

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to this project.

## Bugs & TODOs
The list of known bugs of PyCrypt is available [here](BUGS.md).

The TODO list of PyCrypt is available [here](TODOS.md).

## Issues
Before submitting any issues, make sure to read the [known bugs](BUGS.md) file.

Submit your issues that you encounter while installing and using PyCrypt [here](https://github.com/kkrypt0nn/PyCrypt/issues).

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/kkrypt0nn/PyCrypt/tags).

## Authors
* **Krypton** - *Initial work* - [kkrypt0nn](https://github.com/kkrypt0nn)

## License
This project is licensed under the [Apache 2.0](LICENSE.md) License - see the [LICENSE.md](LICENSE.md) file for details.
