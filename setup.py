from setuptools import setup
from rss_reader.rss_reader import name, version

setup(
    name = name,
    version = version,
    packages = ['rss_reader'],
    entry_points = {
        'console_scripts': [
            'rss_reader = rss_reader.rss_reader:main'
        ]
    })