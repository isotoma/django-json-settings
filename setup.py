import os
from setuptools import setup

README=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-json-settings",
    version='0.2',
    packages=["json_settings"],
    include_package_data=True,
    license="Apache Software License",
    description="A Django application to let you provide local settings in json format",
    long_description=README,
    url="http://github.com/isotoma/django-json-settings",
    author="Doug Winter",
    author_email="doug.winter@isotoma.com",
)
