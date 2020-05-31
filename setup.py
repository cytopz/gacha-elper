import setuptools

with open('docs/README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gacha-elper',
    version='0.0.1',
    author='cytopz',
    author_email='cytopz@protonmail.com',
    description='A small utility to help automate mobile (Android) video games',
    long_description=long_description,
    url='https://github.com/cytopz/gacha-elper',
    packages=setuptools.find_packages(),
    install_requires=['opencv-python', 'scipy', 'numpy']
    license='GPLv3',
    python_requires='>=3.6'
)