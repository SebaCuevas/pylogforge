from setuptools import setup

setup(
    name='PyLogForge',
    version='1.0.1',
    description='Custom Logger Module',
    author='Sebastián M. Cuevas',
    author_email='sebastian.cuevas@greatgeek.net',
    url='https://github.com/krash0n/pylogforge',
    py_modules=['pylogforge'],
    long_description= open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],  # Add any dependencies here
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)