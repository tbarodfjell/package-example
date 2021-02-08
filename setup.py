from setuptools import setup, find_packages

setup(
    name="packageexample",
    version="0.1.0",
    packages=find_packages(include=["packageexample", "packageexample.*"]),
    # install_requires=["numpy"],
)