from setuptools import setup, find_packages

setup(
    name='chalice-restful',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Provides a more structured way of writing RESTful APIs ' +
                'with Chalice.',
    long_description=open('README.md').read(),
    install_requires=['chalice'],
    url='https://github.com/JoshuaLight/chalice-restful',
    author='Joshua Light',
    author_email='j.light.developer@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ]
)
