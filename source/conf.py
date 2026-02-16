# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime
year = datetime.now().year

project = 'Hands-on GeoAI'
copyright = f'{year}, TU Graz & Aalto University'
author = 'TU Graz & Aalto University'
release = f'{year}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_togglebutton',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'myst_nb'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    # "external_links": [],
    "repository_url": "https://github.com/Hands-on-GeoAI/course-site/",
    "repository_branch": "main",
    "path_to_docs": "source/",
    "use_edit_page_button": True,
    "use_repository_button": True,

    # Possible announcement for the page
    #"announcement": ("📢 Exercises 1-2 are out + Week 1-5 videos now available (under 'Overview'). 📢"),

    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "thebe": False,
        "notebook_interface": "jupyterlab",
        "collapse_navigation": False,
    }
},
