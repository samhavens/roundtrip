
from distutils.core import setup

setup(
    name = 'roundtrip',
    packages = ['roundtrip'],
    version = '0.1.1',
    description = 'round trip translation for NLP data augmentation',
    author = 'Sam Havens',
    author_email = 'samhavens@gmail.com',
    url = 'https://github.com/samhavens/roundtrip',
    keywords = ['console', 'translate', 'translator', 'backtranslate', 'roundtrip'],
    classifiers = [],
    install_requires=['mtranslate', 'google.cloud.translate'],
    entry_points={
        'console_scripts': [
            'roundtrip = roundtrip.__main__:main'
        ]
    },
)