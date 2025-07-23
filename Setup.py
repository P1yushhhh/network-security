'''
To setup tools and define the configuration of this project along with it's dependencies and metadata
'''

from setuptools import find_packages, setup #treats every folder with __init__.py as a package
from typing import List

def get_requirement() -> List[str]:
    """
    This function will return list of requirements"""
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file

            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement!='-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_list

print(get_requirement())

setup(
    name="Network_security",
    version="0.0.1",
    author="Piyush Chawla",
    author_email="p1yushhhchawla2307@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirement()
)