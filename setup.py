import os
from setuptools import setup

path = os.path.dirname(__file__)
with open(path + '/ScreenshotsParseTool/__init__.py', 'r') as metadata:
    content = metadata.read()
result = content.split()
__version__ = result[-1][1:-1]


setup(
    name='Screenshots-Parse-Tool',
    version=__version__,
    description='Lightshot screenshots parser',
    author='Lao',
    url='https://github.com/codelao/Screenshots-Parse-Tool',
    license='MIT',
    install_requires=[
        'PyQt6', 'lxml>=4.9.2', 'requests>=2.28.2', 'setproctitle>=1.3.2'
    ],
    packages=[
        'ScreenshotsParseTool'
    ],
    package_data={
        'ScreenshotsParseTool': [
            'scripts/*', 'images/*', 'fonts/*', 'database/*'
        ]
    },
    entry_points={
        'console_scripts': [
            'spt=ScreenshotsParseTool.scripts.menu:entry_point'
        ]
    }
)
