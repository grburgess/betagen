from setuptools import setup


import os



setup(

    name="betagen",
    packages=[
        'betagen',

    ],
    version='v1.0a',
    license='BSD',
    description='A color generator',
    author='J. Michael Burgess',
    author_email='jmichaelburgess@gmail.com',
    #   url = 'https://github.com/grburgess/pychangcooper',
 #   download_url='https://github.com/grburgess/pychangcooper/archive/1.1.2.tar.gz',

#    package_data={'': extra_files, },
#    include_package_data=True,

    install_requires=[
        'colours',
        'colour'
    ],
)
