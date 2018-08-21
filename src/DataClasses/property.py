#!/usr/bin/env python3

class Property():
	''' 
	Constructor
	Parameters: address (dict), residenceType(string)
	'''
	def __init__(self, address, residenceType):
		self.address = address
		self.residenceType = residenceType
		self.number = address['number']
		self.street = address['street']
		self.line2 = address['line2']
		self.city = address['city']
		self.state = address['state']
		self.zip = address['zip']

	'''
	Function: returns address as a string
	Parameters: none
	'''
	def getAddressAsString():
		if (self.line2 != ''):
			return '' + self.number + ' ' + self.street + ' ' + self.line2 + ' ' + self.city + ', ' self.state + ' ' + self.zip
		return '' + self.number + ' ' + self.street + ' ' + self.city + ', ' self.state + ' ' + self.zip
