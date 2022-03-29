import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="chinese_python_Luke_Zheng",
  version="0.0.1",
  author="Luke_Zheng",
  author_email="luke8544@163.com",
  description="noun",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="noun",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
