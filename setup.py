from setuptools import find_packages, setup
from typing import List

HYPEN_E = '-e .'

def get_requirements(file_path:str) -> List[str]:
    reqs = []
    with open(file_path) as file_obj:
        reqs = file_obj.readlines()
        reqs = [req.replace('\n', '') for req in reqs]
        if HYPEN_E in reqs:
            reqs.remove(HYPEN_E)
    return reqs


setup(
    name='student-performance-e2e',
    version='0.0.1',
    author='ajayshan2004',
    author_email='ajayshan2004@gmail.com', 
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)