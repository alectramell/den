# DEN v1.0
###### **Python Encryption Library**
###### **Tramell Software Development (r)**

## Environment..

```Python 3```

## Index..

* hex.py
* md5.py
* sha512.py
* shift.py

## Usage..

```
>>> # hex.py
>>> from hex import *
>>> print(hex('hello'))
68656c6c6f
>>> print(unhex('68656c6c6f'))
hello
>>>
```

```
>>> # md5.py
>>> from md5 import *
>>> print(md5('hello'))
5d41402abc4b2a76b9719d911017c592
>>>
```

```
>>> # sha512.py
>>> from sha512 import *
>>> print(sha512('hello'))
9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
>>>
```

```
>>> # shift.py
>>> from shift import *
>>> print(shift('hello'))
svool
>>> print(unshift('svool'))
hello
```