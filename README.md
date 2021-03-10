# Read/Write Digital Certificate in Python

![Build Status](https://github.com/leogregianin/python-digital-certificate/workflows/python-digital-certificate/badge.svg)


## Install

```sh
$ pip install python-digital-certificate
```

## Development

Create virtual environment

```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

Install Dependencies
    
```sh
$ pip install -r requeriments.txt
```

## Tests
    
Run
    
```sh
$ python -m unittest
```

## Using

```python

from cert import Certificate


_cert = Certificate(
    pfx_file="./pfx-files/test_file.pfx",
    password="123456"
)
_cert.read_pfx_file()
print(_cert.serial_number())

```

## ToDo

 - Sign pdf file
 - Sign txt file
 - Sign xml file
