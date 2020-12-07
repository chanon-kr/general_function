import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_topping",
    version="0.1.1",
    license = "MIT",	
    author="Chanon Krittapholchai",
    author_email="chanon.krittapholchai@gmail.com",
    description="simplify functions from other libraries function in 1-2 lines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chanon-kr/Shared_Function",
    download_url = "https://github.com/chanon-kr/Shared_Function/archive/0.1.1.tar.gz",
    keywords = ["utility"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires = '>=3.7'
)