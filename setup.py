from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="character",
    version="0.1.0",
    description="ascii-art tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/virtualchamber/Character",
    author="Ali Soltani Rad",
    author_email="soltaniradali@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[]
)