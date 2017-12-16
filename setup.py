"""Setup file for data-structures repo."""
from setuptools import setup

setup(
    name="data-structures",
    description="Implementations of various data structures in Python",
    version=0.1,
    author="Matt Favoino, Allan Liebold",
    licence="MIT",
<<<<<<< HEAD
    py_modules=['linked-list', 'dll', 'stack', 'queue'],
=======
    py_modules=['linked-list', 'stack', 'dll', 'que_'],
>>>>>>> 42be6b3c3e0a24e503aec3d23f1c481867e3d5cd
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}
)
