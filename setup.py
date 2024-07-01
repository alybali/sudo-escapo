from setuptools import setup, find_packages

setup(
    name='escapo',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'escapo=escapo.main:minimize_all_windows',
            'sudo_escapo=escapo.main:minimize_all_windows',
        ],
    },
    install_requires=[
        # List other dependencies here if needed
    ],
    description='A script to minimize all open windows',
    author='Swiss',
    url='https://github.com/alybali/sudo-escapo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)
