import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-calc-davinderc",
    version="0.0.1",
    author="Davinder C",
    author_email="davinder.sc1@gmail.com",
    description="A simple calculator developed to practice test-driven development.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/davinderc/simple_calc.git",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite= 'simple_calc.tests',
    tests_require=['pytest']
)