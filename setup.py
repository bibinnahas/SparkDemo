from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    name='SparkDemo',
    version=__version__,
    packages=find_packages(),
    install_requires=['pyspark', 'boto3']
)
