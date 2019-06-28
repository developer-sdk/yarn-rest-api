from setuptools import setup

#with open("./README.md", "r") as fh:
#    long_description = fh.read()

setup(
    name             = 'hadoop-yarn-rest-api',
    version          = '1.1.0',
    description      = 'Python wrapper for Hadoop YARN REST API',
    long_description = open('README.rst').read(),
    license          = 'MIT',
    author           = 'hs_seo',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/yarn-rest-api',
    download_url     = 'https://github.com/developer-sdk/yarn-rest-api/archive/master.zip',
    packages         = ["hadoop"],
    keywords         = ['hadoop', 'yarn', 'rest', 'api', 'resourcemanager'],
    python_requires  = '>=2.6',
    classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
)
