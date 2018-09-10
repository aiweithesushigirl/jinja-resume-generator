"""
Aiwei's resume generator.
"""

from setuptools import setup

setup(
    name='resumegenerator',
    version='0.1.0',
    packages=['resumegenerator'],
    include_package_data=True,
    install_requires=[
        "click==6.7",
        "jinja2==2.9.6",
        "sh==1.12.14",
        "html5validator==0.2.7",
        "pycodestyle==2.3.1",
        "pydocstyle==2.0.0",
        "pylint==2.1.1"
    ],
    entry_points={
        'console_scripts': [
            'resumegenerator = resumegenerator.__main__:main'
        ]
    },
)
