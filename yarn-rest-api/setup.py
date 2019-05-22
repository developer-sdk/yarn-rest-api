from setuptools import setup

with open("./README.md", "r") as fh:
    long_description = fh.read()

print(long_description)

setup(
    name             = 'hadoop-yarn-rest-api',
    version          = '0.2',
    description      = 'Python wrapper for Hadoop YARN REST API',
    #long_description = open('README.rst').read(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author           = 'hs_seo',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/yarn-rest-api',
    download_url     = 'https://github.com/developer-sdk/yarn-rest-api/archive/master.zip',
    #packages         = find_packages(exclude = ['docs', 'tests*']),
    packages         = ["hadoop"],
    keywords         = ['hadoop', 'yarn', 'rest', 'api'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
