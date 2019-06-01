from distutils.core import setup

setup(name='app_test',
      py_modules=['ftr_classifier'],
      url = 'https://github.com/cbjrobertson/ftr_classifier.git',
      author = 'cole robertson',
      author_email = 'cbjrobertson@gmail.com',
      version = '1.0.0',
      license = 'MIT',
      description = "classifies english, dutch and german sentence  in terms of how they refer to the future.",
      install_requires=['spacy==2.1.4',
                        'pandas==0.24.2'],
        python_requires='3.6.0'
      )
