from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="mlprojects",
    version="0.1.0",
    author="Shruti",
    author_email="shrutiguha2002@gmail.com",

    description="A machine learning project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mlprojects",
    packages=find_packages(),
    install_require=get_requirements("requirements.txt"),
    
 )