from setuptools import find_packages,setup
from typing import List
hypen='-e .'

def get_requirements(file_path:str)->List[str]:
    
        # this fun return list of requirements
     requirements = []
     with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","")for req in requirements]
         
         if hypen in requirements:
             requirements.remove(hypen)
             return requirements
     
setup(
    version=0.0,
    name='mlprojects',
    author_email='swapnaja2018@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn'],
    install_requirements=get_requirements('requirements.txt')
)