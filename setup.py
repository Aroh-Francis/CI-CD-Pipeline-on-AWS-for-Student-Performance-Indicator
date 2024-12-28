from setuptools import setup, find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    '''
    This function reads a file and returns a list of the dependencies/ requirements
    '''
    requiremwnts = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()   # In requiremtns.txt, each line is a requirement 
        requirements = [req.replace('\n', '') for req in requirements]  # Remove the newline character

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='mlproject',
    version = '0.0.1',
    author='Francis Aroh',
    author_email='arohfrancisco@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),








)
