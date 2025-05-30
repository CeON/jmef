# Building JMEF website

## This is how to install sphinx: 

Guide will cover sphinx installation inside python virtual environment.
Python virtual environments are helpful to ensure that everyone uses
the same versions of packages. It also helps in maintaining what
packages are installed for each project. It resolves
Guide assumes that user is using debian like operating system.
If you are using some other operating system then you
can find some tips in additional links.


Create virtual environment in directory `env`

```
python3 -m venv env
```

Activate created environment

```
source env/bin/activate
```

Install sphinx (and possibly other required packages)

```
pip install -r requirements.txt
```

This is all you need. You should now be able to build HTML/pdf documentation from git sources locally.

And this is how you build:

```
make html
```

To deactivate virtual evironment run

```
deactivate
```

## Additional resources:
 - Working with python virtual environments
   [https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments]()

 - How to use pip
   [https://pip.pypa.io/en/stable/user_guide/](https://pip.pypa.io/en/stable/user_guide/)

 - More information on sphinx, for ex., on how to start a new
   documentation project of your own, etc.
   [http://pythonhosted.org/an_example_pypi_project/sphinx.html](http://pythonhosted.org/an_example_pypi_project/sphinx.html)


