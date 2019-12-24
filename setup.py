import setuptools

with open("README.txt", encoding='utf-8') as fh:
    long_description = fh.read()

version = 'v0.3'

setuptools.setup(
     name='MerklePyTree',
     version=version,
     author="AmericanExplorer13",
     author_email="...",
     description="A Merkle Tree creator",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/americanexplorer13/MerklePyTree",
     packages=setuptools.find_packages(),
     license='GNU general Public License v3.0',

 )
