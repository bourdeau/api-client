from setuptools import setup

setup(name='api-client',
      version='0.1',
      description='A simple tool to make Oauth2 request',
      url='https://github.com/bourdeau/oauth2-request.git',
      author='Pierre-Henri Bourdeau',
      author_email='phbasic@gmail.com',
      license='MIT',
      packages=['api-client'],
      install_requires=[
          'strictyaml',
      ],
      zip_safe=False)
