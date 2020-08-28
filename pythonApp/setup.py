#! /usr/bin/python3
import glob
import json
import shutil
import re
import setuptools
import os
import sys

packageData = json.load(open('package.json'))
templateFolder = packageData['flaskConfig']['templatePath']
staticFolder = packageData['flaskConfig']['staticPath']
packageName = packageData['name']
staticPrefix = f'/static/{packageName}'
version = packageData['version']
distPath = glob.glob('dist/*')[0]
index = f"{distPath}/index.html"
flaskIndexPath = f'{templateFolder}/index.html'
flaskStaticPath = f'{staticFolder}/'


def index_reshape(src: str, dst: str):
    with open(src, 'r') as f:
        indexData = '\n'.join(f.readlines())
    hrefContents = re.findall(r'(?<!base )href=\"(.+?)\"', indexData)
    srcContents = re.findall(r'src=\"(.+?)\"', indexData)
    for r in hrefContents + srcContents:
        indexData = indexData.replace(r, f'{staticPrefix}/{r}')

    with open(dst, 'w') as f:
        f.write(indexData)


def move_files(src: str, dst: str):
    if os.path.exists(dst):
        shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('index.html', '.DS_Store'))


index_reshape(index, flaskIndexPath)
move_files(distPath, flaskStaticPath)

setuptools.setup(
    name=packageName,
    version=version,
    author="NutShellBox",
    author_email="nutshellbox.public@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "Flask",
        "pymongo",
        "gevent",
        "Flask-Login",
    ],
)
