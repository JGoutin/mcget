#!/usr/bin/env python3
# coding=utf-8
"""mcget setup"""
from os.path import abspath, dirname, join

# Set Package information
PACKAGE_INFO = dict(
    name='mcget',
    description='A simple tool to download or update Minecraft Java server and '
                'launcher.',
    long_description_content_type='text/markdown; charset=UTF-8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Games/Entertainment'
        ],
    keywords='minecraft launcher server java',
    author='J.Goutin',
    url='https://github.com/JGoutin/mcget',
    project_urls={'Download': 'https://pypi.org/project/mcget'},
    license='BSD',
    zip_safe=True,
    python_requires='>=3.6',
    setup_requires=['setuptools'],
    entry_points={'console_scripts': ['mcget=mcget:_run_command']}
)

SETUP_DIR = abspath(dirname(__file__))

# Get package __version__ from package
with open(join(SETUP_DIR, 'mcget/__init__.py')) as file:
    for line in file:
        if line.rstrip().startswith('__version__'):
            PACKAGE_INFO['version'] = line.split('=', 1)[1].strip(" \"\'\n")
            break

# Get long description from readme
with open(join(SETUP_DIR, 'readme.md')) as file:
    PACKAGE_INFO['long_description'] = file.read()

# Run setup
if __name__ == '__main__':
    from os import chdir
    from setuptools import setup, find_packages
    chdir(SETUP_DIR)
    setup(**PACKAGE_INFO, packages=find_packages())
