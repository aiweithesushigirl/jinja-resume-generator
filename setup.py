

from setuptools import setup

setup(
    name='resumegenerator',
    version='0.1.0',
    packages=['resumegenerator'],
    include_package_data=True,
    install_requires=[
        "jinja2==2.9.6",
        "sh==1.12.14",
        "pylint==2.1.1"
    ],
    entry_points={
        'console_scripts': [
            'resumegenerator = resumegenerator.__main__:main'
        ]
    },
)
