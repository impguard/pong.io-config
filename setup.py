import re
from setuptools import setup, find_packages

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pconf/__main__.py').read(),
    re.M
).group(1)

requires = [
    'arrow==0.12.1',
    'pynamodb==3.3.1',
    'docopt==0.6.2',
    'flake8==3.5.0',
]

setup(
    name='pconf',
    version=version,
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pconf = pconf.__main__:main'
        ]
    }
)
