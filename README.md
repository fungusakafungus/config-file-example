This is an example of using multiple configuration files in python.
Developer install (a git checkout) can use the configuration file from current directory or in $HOME.
When the package is installed via `setup.py install`, it will install the configuration file from current directory into /etc

Debian
======

To make a debian package, install `stdeb` and run:

    $ python setup.py --command-packages=stdeb.command debianize
    $ debuild
