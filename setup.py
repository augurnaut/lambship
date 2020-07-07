import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="lambship_augurnaut",  # Replace with your own username
    version="1.1",
    author="Shannon Li",
    author_email="shannonli@augurnauts.com",
    description="test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/augurnaut/lambship",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
