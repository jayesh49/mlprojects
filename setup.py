from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and line != HYPEN_E_DOT:
                requirements.append(line)
    return requirements

    '''
###  this function will return the list of requirements
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

'''
setup(
name='mlproject',
version='0.0.1',
author='Jayesh',
author_email='jayeshkumarjangir49@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


 )