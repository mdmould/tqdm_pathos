from distutils.core import setup

setup(name='tqdm_pathos',
      packages = ['tqdm_pathos'],
      version='0.1',
      description='tqdm progress bar for pathos multiprocessing with additional arguments',
      url='https://github.com/mdmould/tqdm_pathos',
      download_url = 'https://github.com/mdmould/tqdm_pathos/archive/0.1.tar.gz',
      author='Matthew Mould',
      author_email='mattdmould@gmail.com',
      keywords = ['multiprocessing'],
      license='MIT',

      install_requires=['pathos','tqdm',],  #YOUR DEPENDENCIES HERE
  

      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        ],
)

