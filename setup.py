from setuptools import setup

#imposto i requisiti
with open('requirements.txt') as f:
	requirements = f.read().splitlines()

setup(name='mydice',
	version='1.0.1',
	description='OpenShift App for launching dices',
	author='Daniele Rapetti',
	author_email='iximie@gmail.com',
	url='http://www.python.org/sigs/distutils-sig/',
	install_requires=requirements,
	)
