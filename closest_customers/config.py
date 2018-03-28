# -*- coding: utf-8 -*-

import os

class Config(object):
	''' Class to keep the constant variables'''
	dir_path = os.path.dirname(os.path.realpath(__file__))

class Production(Config):
	data_file_path = os.path.join(Config.dir_path, 'data.json')
	distance_limit = 100


class Staging(Config):
	data_file_path = os.path.join(Config.dir_path, 'test_data.json')
	distance_limit = 10
