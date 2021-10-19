import setuptools
setuptools.setup(
    name='libspwn',
    version='1.0',
    scripts=['./scripts/libspwn'],
    author='Jeffrey Huang',
    description='CLI for creating a SPWN library',
    packages=['libspwn'],
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.5'
)