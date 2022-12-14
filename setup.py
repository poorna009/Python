from setuptools import setup, find_packages


with open("README.md") as f:
    long_description = f.read()

setup(
    name="TSIClient",
    packages=find_packages(),
    version="2.1.3",
    license="MIT",
    description="The TSIClient is a Python SDK for Microsoft Azure time series insights.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Poorna009",
    author_email="poorna.kondeti@gmail.com",
    url="https://github.com/poorna009/Python",
    project_urls={
        "Bug Tracker": "https://github.com/poorna009/Python/issues",
        "Documentation": "https://raalabs-tsiclient.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/poorna009/Python",
    },
    keywords=["Time Series Insights", "TSI", "TSI SDK", "Raa Labs", "IoT"],
    install_requires=["requests", "pandas", "azure-identity"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
