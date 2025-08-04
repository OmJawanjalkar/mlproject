from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns list of requirements from the given file
    '''
    with open(file_path) as file:
        requirements = [line.strip() for line in file if line.strip()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Om',
    author_email='omjawanjalkar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
