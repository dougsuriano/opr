from setuptools import setup

setup(
    name='opr',
    version='0.1',
    py_modules=['opr'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        opr=opr:opr
    ''',
)