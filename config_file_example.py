#!/usr/bin/env python
import os
from ConfigParser import RawConfigParser

def main():
    config_parser = RawConfigParser()
    config_parser.read(['/etc/config-file-example.conf', os.path.expanduser('~/.config-file-example.conf'), 'config-file-example.conf'])
    print config_parser.get('section', 'key')

if __name__ == '__main__':
    main()
