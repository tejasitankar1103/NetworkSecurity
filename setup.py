"""
This is the setup.py file for the NetworkSecurity package.
It is used to package and distribute the project.
It includes metadata about the package such as name, version, author, and dependencies.
It also defines a function to read the requirements from a requirements.txt file.
"""


from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements from the requirements.txt file.
    """

    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the requirements file
            lines = file.readlines()
            #Process each line to remove whitespace and comments
            for line in lines:
                requirements=line.strip()
                #ignore comments and empty lines and -e.
                if requirements and not requirements.startswith('#') and not requirements.startswith('-e'):
                    requirement_lst.append(requirements)
    except FileNotFoundError:
                print("requirements.txt file not found. Please ensure it exists in the project directory.")                
    return requirement_lst

setup(
    name ="NetworkSecurity",
    version = "0.0.1",
    author= "Tejas Itankar",
    author_email = "tejasitankar10@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)