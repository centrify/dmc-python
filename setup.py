
from distutils.core import setup
setup(
  name = 'centrify.dmc',         # How you named your package folder (MyLib)
  packages = ['dmc'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Library to retrieve an access token to Centrify PAS from an enrolled machine',
  author = 'Harvey Kwok',
  author_email = 'harvey.kwok@centrify.com',
  url = 'https://github.com/centrify/dmc-python',
  download_url = 'https://github.com/centrify/dmc-python/archive/v0.2-alpha.tar.gz',
  keywords = ['Centrify', 'DMC'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache 2.0 License',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)