from setuptools import setup, find_packages

setup(
    name="packageexample",
    version="0.1.1",
    packages=find_packages(include=["packageexample", "packageexample.*"]),
    install_requires=["numpy"],
)