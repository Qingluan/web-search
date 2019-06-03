
from setuptools import setup, find_packages


setup(name='x_search',
    version='0.0.0',
    description='None',
    url='https://github.com/xxx',
    author='auth',
    author_email='xxx@gmail.com',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    install_requires=['mroylib-min'],
    entry_points={
        'console_scripts': ['x-searcher=x_search_src.cmd:main']
    },

)
