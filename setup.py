from setuptools import find_packages,setup

setup(
    name='MEDICALCHATBOT',
    version='0.0.1',
    author='deepak nema',
    author_email='nemadeep82@gmail.com',
    install_requires=["ctransformers","sentence-transformers","pinecone-client","langchain","flask","pypdf","python-dotenv"],
    packages=find_packages()
)