#!/usr/bin/env python3

class Owner():
	'''
	Constructor
	Parameters: firstName (string), lastName (string), email (string), phone (int), socialMedia (dict)
	'''
	def __init__(self, firstName, lastName, email, phone, socialMedia):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.phone = phone
		self.socialMedia = socialMedia