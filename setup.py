import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chartify_helpers",
    version="1.2.2", # MAJOR.MINOR.MAINTENANCE
    author="Kristof Pusztai",
    author_email="kpusztai@berkeley.edu",
    description="Some lightweight helper functions which add readability/functionality to Spotify's chartify library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KristofPusztai/chartify-helpers",
    packages=setuptools.find_packages(),
    install_requires=[
        'chartify',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
