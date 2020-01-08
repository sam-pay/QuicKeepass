from setuptools import setup, Extension
import sys

if sys.version.startswith("2"):
    print >>sys.stderr, "QuicKeepass is only for python3 => pip3 install quickeepass"
    sys.exit(1)

setup(name='QuicKeepass',
        version='0.1',
        author='@chaignc',
        url='https://github.com/nongiach/QuicKeepass',
        packages=['quickeepass'],
        py_modules=['quickeepass'],
        description = 'Efficiently autotype your password from keepass on i3 using rofi ',
        entry_points = {
            'console_scripts': [
                'quickeepass = quickeepass:main',
                ],
            },
        install_requires=[
            'pykeepass',
            ],
        keywords = ['keepass', 'rofi', 'password', 'quick', 'manager', 'autotype', 'autofill']
        )