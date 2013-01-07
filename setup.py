from setuptools import setup, find_packages

setup(
    name='config-file-example',
    version='0.1',
    py_modules=['config_file_example'],
    entry_points = {
        'console_scripts': [
            'config_file_example = config_file_example:main',
        ]
    },
    data_files=[('/etc/', ['config-file-example.conf'])]
)
