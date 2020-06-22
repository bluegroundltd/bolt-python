#!/usr/bin/env python
from glob import glob
from os.path import splitext, basename

import setuptools

__version__ = None
exec(open("src/slack_bolt/version.py").read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slack_bolt",
    version=__version__,
    author="Slack Technologies, Inc.",
    author_email="opensource@slack.com",
    description="The Bolt Framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slackapi/bolt-python",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    setup_requires=["pytest-runner==5.2"],
    tests_require=["pytest==3.8.2"],
    install_requires=[
        "slackclient==2.7.1", # TODO: will be replaced with slack_sdk==3.0.0
    ],
    # used only under src/slack_bolt/adapter
    extra_requires=[
        "aiohttp==3.6.2",
        "bottle==0.12.18",
        "falcon==2.0.0",
        "fastapi==0.54.1",
        "Flask==1.1.2",
        "pyramid==1.10.4",
        "python-lambda==11.7.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)