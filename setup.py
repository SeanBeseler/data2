from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov', 'tox']
}

setup(
    name='Data structures',
    desctription='Contains the implementation of various data structures.',
    version='0.0',
    author='Sean Besler, Carlos',
    author_email='Seanwbeseler@gmail.com',
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)
