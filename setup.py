import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-crypt",
    version="1.1.0",
    author="Krypton",
    author_email="kkrypt0nn@national.shitposting.agency",
    description="PyCrypt is a easy to use python library to let everyone encrypt, decrypt and decode messages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkrypt0nn/PyCrypt",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)