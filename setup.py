from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main('')
        sys.exit(errno)


description = 'petl extension to work with RDF.'

setup(
    name = 'petl-ld',
    version = '0.0.1',
    url = 'http://github.com/lawlesst',
    author = 'Ted Lawless',
    author_email = 'lawlesst@gmail.com',
    py_modules = ['petlld',],
    packages = ['petlld',],
    description = description,
    cmdclass = {'test': PyTest},
    tests_require=['pytest'],
    install_requires=[
        'petl',
        'rdflib>=4.1',
        'rdflib-jsonld>=0.3'
    ],
)