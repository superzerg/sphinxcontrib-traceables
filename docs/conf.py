# -*- coding: utf-8 -*-

import sys
import os
from glob import glob

# -------------------------------------------------------------------------
# Configure extensions

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx'
]

# -------------------------------------------------------------------------
# Helper function for retrieving info from files

def read(*names):
    root_dir = os.path.dirname(__file__)
    path = os.path.join(root_dir, *names)
    with open(path) as f:
        return f.read()

# -------------------------------------------------------------------------
# General configuration

project = u'sphinxcontrib.traceables'
copyright = u'2020, Yves Renier'
release = read('..', 'VERSION.txt')    # The full version, incl alpha/beta/rc.
version = '.'.join(release.split('.')[0:2]) # The short X.Y version.
templates_path = ['_templates']
source_suffix = '.txt'
master_doc = 'index'                   # The master toctree document.
today_fmt = '%Y-%m-%d'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
keep_warnings = True                   # Keep warnings in output documents.

# -------------------------------------------------------------------------
# Configure HTML output

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = True            # Link to source from pages.

# ----------------------------------------------------------------------
#intersphinx configuration

intersphinx_mapping = {
  'constellations': ('https://superzerg.github.io/sphinxcontrib-traceables/constellations/', './_build/constellations/objects.inv'),
  'requirements': ('https://superzerg.github.io/sphinxcontrib-traceables/requirements/', './_build/requirements/objects.inv'),
  'test-graph': ('https://superzerg.github.io/sphinxcontrib-traceables/test-graph/', 'https://superzerg.github.io/sphinxcontrib-traceables/test-graph/objects.inv'),
  'test-list': ('https://superzerg.github.io/sphinxcontrib-traceables/test-list/', './_build/test-list/objects.inv'),
  'test-matrix': ('https://superzerg.github.io/sphinxcontrib-traceables/test-matrix/', './_build/test-matrix/objects.inv'),
}