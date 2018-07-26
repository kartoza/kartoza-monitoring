import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='Kartoza Monitoring',
        version='0.1',
        packages=find_packages(exclude=['tests', ]),
        include_package_data=True,
        license='MIT License',
        description='Dockerised System Monitoring service',
        long_description=README,
        url='http://bims.kartoza.com',
        author='Alison Mukoma',
        author_email='alison@kartoza.com',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: 1.11',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',  # example license
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
        install_requires=[
            'Django==1.11',
            'django-prometheus==1.0.14',
            'prometheus_client==0.2.0',
        ],
        dependency_links=[
            'git+https://github.com/soynatan/django-easy-audit.git',
        ]
)
