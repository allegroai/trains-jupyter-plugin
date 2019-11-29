from setuptools import setup, find_packages
from pathlib2 import Path


here = Path(__file__).resolve().parent

# Get the long description from the README file
long_description = (here / 'README.md').read_text()

requirements = (here / 'requirements.txt').read_text().splitlines()

setup(
    name="trains-jupyter-plugin",
    version='0.2.1',
    url="https://github.com/allegroai/trains-jupyter-plugin",
    author="Allegro.ai",
    description="Jupyter extension to enable users to commit & push notebooks to a git repo",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords='trains jupyer notebook development machine deep learning version control machine-learning machinelearning '
             'deeplearning deep-learning experiment-manager experimentmanager',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=requirements,
    package_data={'trains-jupyter-plugin': ['static/*']},
    include_package_data=True,
)
