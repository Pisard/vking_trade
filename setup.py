from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vking_trade/__init__.py
from vking_trade import __version__ as version

setup(
	name="vking_trade",
	version=version,
	description="Vking Trade Customizations",
	author="Abraham Kalungi",
	author_email="abrahamskalungi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
