from setuptools import setup, find_packages

setup(
    name             = 'hadoop-yarn-rest-api',
    version          = '0.1',
    description      = 'Python wrapper for Hadoop YARN REST API',
    long_description = open('README.md').read(),
    author           = 'hs_seo',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/yarn-rest-api',
    download_url     = 'https://github.com/developer-sdk/yarn-rest-api/archive/master.zip',
    packages         = find_packages(),
    keywords         = ['hadoop', 'yarn', 'rest', 'api']
)
