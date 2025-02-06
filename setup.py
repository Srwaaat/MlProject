from setuptools import find_packages,setup
from typing import List

eDOT="-e ."
def get_requirements(filepath:str)-> List[str]:
    requirements=[]
    with open(filepath) as file_opj:
        requirements=file_opj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements] 

        if eDOT in requirements:
            requirements.remove(eDOT)


    return requirements  


setup(
    name="MLproject",
    version="0.0.1",
    author="Tharwat",
    author_email="ah.tharwat@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)



