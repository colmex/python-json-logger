from setuptools import setup

setup(
    name = "python-json-logger",
    version = "0.0.6",
    url = "http://github.com/madzak/python-json-logger",
    license = "BSD",
    description = "A python library adding a json log formatter",
    author = "Zakaria Zajac",
    author_email = "zak@madzak.com",
    package_dir = {'': 'src'},
    packages = [''],
    test_suite = "tests.tests",
    install_requires = ['setuptools'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Logging',
    ]
)
