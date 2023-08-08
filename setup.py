from ScreenshotsParseTool import NAME, VERSION
from setuptools import setup


setup(
    name=NAME,
    version=VERSION,
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
