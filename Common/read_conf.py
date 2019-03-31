# -*- coding: utf-8 -*-
# user = www

import configparser
from Common import base_path
class ReadConf:
    def __init__(self):
        file_name = base_path.test_path
        self.cf = configparser.ConfigParser()
        self.cf.read(filenames=file_name, encoding='utf-8')
    def get(self, sections, options):
        value = self.cf.get(sections, options)
        return value
    def getboolean(self, sections, options):
        value = self.cf.getboolean(sections, options)
        return value
    def getint(self, sections, options):
        value = self.cf.getint(sections, options)
        return value
