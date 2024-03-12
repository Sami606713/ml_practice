from setuptools import find_packages,setup
from typing import List
e_dot="-e ."
def get_package(file_path:str)-> list:
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if(e_dot in requirements):
            requirements.remove(e_dot)

    return requirements

setup(
    author="Samiullah",
    description="just for practicing",
    author_email="sami606713@gmail.com",
    version='0.0.1',
    packages=find_packages(),  #same as name
   install_requires=get_package('requirements.txt'), #external packages as dependencies
)
