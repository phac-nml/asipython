"""
Copyright Government of Canada 2018

Written by: Eric Enns, National Microbiology Laboratory, Public Health Agency of Canada

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from setuptools import find_packages, setup

dependencies = []

setup(
    name='asipython',
    version='0.0.0',
    url='https://github.com/phac-nml/asipython.git',
    license='Apache License, Version 2.0',
    author='Eric Enns',
    author_email='eric.enns@canada.ca',
    description='Python library that calculates viral drug resistance interpretations/scores based on given algorithm and mutation list files',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points='',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
    ]
)
