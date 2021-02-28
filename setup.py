import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dummy_irds_ext",
    version="0.0.0",
    author="Sean MacAvaney",
    author_email="sean@ir.cs.georgetown.com",
    description="a dummy extension for ir_datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seanmacavaney/dummy-irds-ext",
    include_package_data = True,
    packages=setuptools.find_packages(include=['dummy_irds_ext']),
    install_requires=list(open('requirements.txt')),
    classifiers=[],
    python_requires='>=3.6'
)
