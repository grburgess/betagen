import os

import versioneer
from setuptools import setup

# Create list of data files


setup(
    version=versioneer.get_version(),
    include_package_data=True,
    cmdclass=versioneer.get_cmdclass(),

)
