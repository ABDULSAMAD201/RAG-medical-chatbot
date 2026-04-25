from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RAG Chatbot",
    version="0.1",
<<<<<<< HEAD
    author="SheesKhan",
=======
    author="Shees",
>>>>>>> 80f1e9f (Update package name and author in setup.py)
    packages=find_packages(),
    install_requires = requirements,
)
