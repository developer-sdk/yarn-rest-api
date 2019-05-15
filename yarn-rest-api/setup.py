from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
        
setup(
    name             = 'hadoop-yarn-rest-api',
    version          = '0.1',
    description      = 'Python wrapper for Hadoop YARN REST API',
    #long_description = open('README.rst').read(),
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8',
    author           = 'hs_seo',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/yarn-rest-api',
    download_url     = 'https://github.com/developer-sdk/yarn-rest-api/archive/master.zip',
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['hadoop', 'yarn', 'rest', 'api'],
    zip_safe         = False
)
