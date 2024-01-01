from setuptools import setup, find_packages
from typing import List

with open('README.MD', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.0"
REPO_NAME = "mongodb_connector_pkg"
PKG_NAME= "mongodb_connector_pkg"
AUTHOR_USER_NAME = "kunalc232"
AUTHOR_EMAIL = "kunbalc232@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with mongodb database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )


