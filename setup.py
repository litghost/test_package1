import setuptools

setuptools.setup(
    name="test_package1",
    version="0.0.1",
    author="litghost",
    description="SymbiFlow RR Graph libraries",
    url="https://github.com/litghost/test_package1",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "test_package2@git@github.com:litghost/test_package2.git",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
