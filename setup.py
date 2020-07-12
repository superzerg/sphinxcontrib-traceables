
from setuptools import setup, find_packages

import os


# --------------------------------------------------------------------------
# Setup package.

root_dir = os.path.dirname(__file__)


def read(*names):
    path = os.path.join(root_dir, *names)
    with open(path) as f:
        return f.read()


def get_version():
    version_string = read("VERSION.txt").strip()
    return version_string


setup(
      name="sphinxcontrib-traceables0.2",
      version=get_version(),
      description="Sphinx extension that adds traceability within "
                  "documentation",
      author="Yves Renier",
      author_email="yves.renier@epfl.ch",
      url="https://github.com/superzerg/sphinxcontrib-traceables",
      license="Apache 2.0",
      long_description=read("README.rst"),
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'Sphinx>=2.1',
          'graphviz>=0.4.6'
      ],
      platforms="any",
      tests_require=[
          'pytest'
      ],
      doc_require=[
          'sphinx_rtd_theme',
      ],
      classifiers=[
                   "Development Status :: 3 - Alpha",
                   "Environment :: Other Environment",
                   "Environment :: Plugins",
                   "Framework :: Sphinx :: Extension",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Information Technology",
                   "Intended Audience :: Science/Research",
                   "Intended Audience :: System Administrators",
                   "License :: OSI Approved :: Apache Software License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3",
                   "Topic :: Software Development :: Documentation",
                   "Topic :: Software Development :: Libraries :: "
                        "Python Modules",
                  ],
     )
