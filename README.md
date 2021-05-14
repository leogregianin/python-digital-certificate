# Read/Write Digital Certificate in Python

[![python-digital-certificate](https://github.com/leogregianin/python-digital-certificate/actions/workflows/main.yml/badge.svg)](https://github.com/leogregianin/python-digital-certificate/actions/workflows/main.yml)


## Development

Create virtual environment

```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

Install Dependencies
    
```sh
$ pip install -r requirements.txt
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
    password=b"123456"
)

# Read PFX file
_cert.read_pfx_file()

# Get Serial Number
print(_cert.serial_number())

# Get not valid before date
print(_cert.not_valid_before())

# Get not valid after date
print(_cert.not_valid_after())

# Get subject name
print(_cert.subject())

# Get owner name
print(_cert.common_name())

# Get Issuer name
print(_cert.issuer())
```
