from setuptools import setup

#imposto i requisiti
with open('requirements.txt') as f:
		requirements = f.read().splitlines()

setup(name='tiraDadi',
      version='0.1',
      description='OpenShift App',
      author='iximiel',
      author_email='iximiel@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
	  install_requires=requirements,
     )
