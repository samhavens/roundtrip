
from distutils.core import setup

setup(
    name = 'roundtrip',
    packages = ['roundtrip'],
    version = '0.0.1a1',
    description = 'round trip translation for NLP data augmentation',
    author = 'Sam Havens',
    author_email = 'samhavens@gmail.com',
    url = 'https://github.com/samhavens/roundtrip',
    download_url = 'https://github.com/samhavens/roundtrip/tarball/0.0.1a1',
    keywords = ['console', 'translate', 'translator', 'backtranslate', 'roundtrip'],
    classifiers = [],
    install_requires=['mtranslate'],
    entry_points={
        'console_scripts': [
            'roundtrip = roundtrip.__main__:main'
        ]
    },
)