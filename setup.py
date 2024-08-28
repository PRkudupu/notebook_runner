# setup.py

from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            # Define entry points if needed
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package to run Databricks notebooks as jobs",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
