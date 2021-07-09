from setuptools import setup, find_packages
import os
import sys

directory = os.path.abspath(os.path.dirname(__file__))
if sys.version_info >= (3, 0):
    with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
else:
    with open(os.path.join(directory, 'README.md')) as f:
        long_description = f.read()

setup(name='419a',
      packages=find_packages(),
      include_package_data=True,
      setup_requires=['setuptools_scm'],
      use_scm_version=True,
      description='GEO 419A Homework',
      classifiers=[
          'License :: FSF Approved :: WTFPL License',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
      ],
      install_requires=['rasterio',
                        'numpy',
                        'zipfile',
                        'requests',
                        'datetime',
                        'matplotlib',
                        'PIL',
                        'glob'],
      python_requires='>=3.6.0',
      url='https://github.com/FelixBach/419a.git',
      author='Felix Bachmann',  # 'Maximilian Nestler'  # how to add second author?
      author_email='Felix.Bachmann@uni-jena.de',  # 'Maximilian.Nestler@uni-jena.de'
      license='WTFPL',
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown')