# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import shutil

# -- Copy schemas and xml examples into website structure

schemas_and_examples = [
        ['../../jmef_1.0_example.xml', 'version-1.0', 'jmef.xml'],
        ['../../jmef_1.0_minimal_example.xml', 'version-1.0', 'jmef_minimal.xml'],
        ['../../jmef.xsd', 'version-1.0', 'jmef.xsd']
]

for to_copy in schemas_and_examples:
    os.makedirs('additional_files/' + to_copy[1], exist_ok=True)
    shutil.copy(to_copy[0], 'additional_files/' + to_copy[1] + '/' + to_copy[2]);


# -- Project information -----------------------------------------------------

project = 'Journal Metadata Exchange Format'
copyright = '2025, ICM UW'
author = 'ICM UW'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**/website']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_options = {
    'navbar_pagenav': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_extra_path = ['additional_files']

html_show_sourcelink = False


def setup(app):
    app.add_css_file("style.css") # add custom css from _static dir


