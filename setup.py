try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='dummy project',
      version='0.1',
      description='Galaxy evolution utility code snippets',
      url='',
      author='Prajwal R. Kafle',
      author_email='pkafauthor@gmail.com',
      license='MIT',
      packages=["package", "docs"],
      zip_safe=False)