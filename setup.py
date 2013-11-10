'''
    Tinkerer-Localpost Setup
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Package setup script.

    :copyright: Copyright 2013, Nathan Hawkes
    :license: FreeBSD, see LICENCE file
'''
from distutils.core import setup, find_packages


long_desc = '''
Tinkerer-Localpost is an addon for Tinkerer that makes it easy to see your blog
before you publish it.

Tinkerer-Localpost provides the ability to see your site as it would appear on
the Web from the privacy of your own computer. Use it to review your posts and
pages, check your RSS feed, build custom themes and customize your blog to your
heart's content.

Remember, before you post, always http://localhost.

Tinkerer-Localpost requires Tinkerer to function properly.
'''

requires = ['tinkerer>=1.2.1',]

test_requires = ['nose', 'tox']

setup(
    name = 'Tinkerer-Localpost',
    version = localpost.__version__,
    license = 'FreeBSD',
    author = 'Nathan Hawkes',
    author_email = 'gisraptor@gmail.com',
    description = 'Localhost your Tinkerer blog',
    long_description = long_desc,
    classifiers = [
    ],
    platforms = 'any',
    packages = find_packages(exclude=['localposttest',]),
    entry_points = {
        'console_scripts': [
            'localpost = localpost.cmdline:main'
        ]
    }
    install_requires = ['tinkerer>=1.2.1', ],
    test_requires = test_requires,
    test_suite = 'nose.collector'
)
