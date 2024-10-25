from setuptools import setup, find_packages

setup(
    name='project_name',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'Flask==2.0.1',
        'numpy==1.21.0',
    ],
    entry_points={
        'console_scripts': [
            'start-project=src.main:main'
        ]
    },
)