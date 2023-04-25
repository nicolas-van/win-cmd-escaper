from setuptools import setup, find_packages
import os.path

here = os.path.dirname(__file__)
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='win-cmd-escaper',
    version='0.0.0',
    license='MIT',
    author="Nicolas Vanhoren",
    description='A Python library to properly handle escaping of command line arguments in Windows\' CMD.exe and Powershell.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["win_cmd_escaper"],
    url='https://github.com/nicolas-van/win-cmd-escaper',
    keywords='windows cmd powershell',
    install_requires=[],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/nicolas-van/win-cmd-escaper/issues',
        #'Funding': 'https://donate.pypi.org',
        #'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/nicolas-van/win-cmd-escaper',
    },
    
    python_requires='>=3.6',
)