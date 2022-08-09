from setuptools import setup, find_packages


__description__ = "Read digital certificate (pfx and p12 files) in Python"
with open("README.md", "r") as fh:
    __long_description__ = fh.read()

setup(
    name="python-digital-certificate",
    version="0.3.0",
    url="https://github.com/leogregianin/python-digital-certificate",
    author="Leonardo Gregianin",
    author_email="leogregianin@gmail.com",
    license="MIT",
    description=__description__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    keywords="digital-certificate",
    packages=find_packages(),
    install_requires=[
        'certifi',
        'cffi',
        'cryptography',
        'pyOpenSSL',
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)