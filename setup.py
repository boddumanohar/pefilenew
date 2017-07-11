import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
name = 'pefilenew',
packages = ['pefilenew', 'ordlookup'], # this must be the same as the name above
version = '2.1',
description = 'Parses a PE file and reports information on all properties of PE File',
author = 'boddu',
author_email = 'b.manu199@gmail.com',
#url = 'https://github.com/boddumanohar/pdfparse', # use the URL to the github repo
#download_url = 'https://github.com/boddumanohar/pdfparse/archive/0.1.tar.gz', # I'll explain this in a second
keywords = ['pefile', 'malicious', 'analysis'], # arbitrary keywords
classifiers = [],
include_package_data = True,

)
