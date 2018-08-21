#!/usr/bin/env python3

class Link():
	'''
	Constructor
	Parameters: owner (owner object), properties (list of properties associated with that owner)
	'''
	def __init__(self, owner, properties):
		self.owner = owner
		self.properties = properties