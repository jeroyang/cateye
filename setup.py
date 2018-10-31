#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import sys
import os
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

with open('README.md') as readme_file:
    readme = readme_file.read()

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name='cateye',
    version='0.1.0',
    description="A search engine for fixed documents including h hints",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Chia-Jung, Yang",
    author_email='jeroyang@gmail.com',
    url='https://github.com/jeroyang/cateye',
    packages=[
        'cateye',
    ],
    package_dir={'cateye':
                 'cateye'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='cateye',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
