from setuptools import setup, find_packages

setup(
    name="water-quality-backend",
    version="0.1",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    python_requires='>=3.8',
)
