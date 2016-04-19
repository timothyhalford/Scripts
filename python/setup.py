import sys
from setuptools import setup, find_packages


def forbid_publish():
    argv = sys.argv
    blacklist = ['register', 'upload']

    for command in blacklist:
        print command
        print argv
        if command in argv:
            values = {'command': command}
            message = 'Command "%(command)s" has been blacklisted, exiting...'
            print(message % values)
        sys.exit(2)

forbid_publish()

setup(
    name='Scripts',
    version='0.0.0',
    url='www.starcount.com',
    description='General purpose scripts for data munging',
    long_description=open('README.md').read(),
    author='Starcount Data Engineering Team',
    maintainer='Shaun Tillyard',
    maintainer_email='shaun.tillyard@starcount.com',
    license='PRIVATE',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating system :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'avro==1.8.0',
        'pandas==0.18.0'
    ]
)
