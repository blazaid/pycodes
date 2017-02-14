import setuptools.command.test

import pycodes

print(pycodes.__name__)

setuptools.setup(
    name=pycodes.__name__,
    version=pycodes.__version__,
    url=pycodes.__url__,
    license='Apache License 2.0',
    author=pycodes.__author__,
    tests_require=[],
    install_requires=[],
    author_email='alberto.da@gmail.com',
    description='A library with utils to validate product codes',
    long_description=open('README.rst').read(),
    packages=pycodes.__name__,
    include_package_data=True,
    platforms='any',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ),
)
