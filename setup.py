from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    This Function will return list of requirements
    """
    requirements_list: List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process whitespace and newlines characters
            for line in lines:
                # Strip whitespace and newlines characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
        
    return requirements_list
print(get_requirements())

setup(
    name='AI_Trip_Planner',
    version='0.0.1',
    author='Aneesh BK',
    author_email= "abk856@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)