from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="geometria",
    version="0.0.1",
    author="Mayumi Shingaki",
    description="Biblioteca para formulas de geometria",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["geometria"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    dependency_links=['https://github.com/mayumisngk/school_math']
)