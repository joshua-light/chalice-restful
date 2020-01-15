from setuptools import setup, find_packages

setup(
    name='chalice-restful',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Provides a more structured way of writing RESTful APIs ' +
                'with Chalice.',
    long_description=open('README.md').read(),
    install_requires=['chalice'],
    url='https://github.com/JoshuaLight/chalice-restful',
    author='Joshua Light',
    author_email='j.light.developer@gmail.com'
)
