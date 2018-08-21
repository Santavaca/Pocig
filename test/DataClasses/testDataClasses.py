#!/usr/bin/env python3

import unittest, sys
sys.path.append('../../src/DataClasses')

class TestDataClasses(unittest.TestCase):
	def test_owner(self):
		testfirstName = 'John'
		testlastName = 'Doe'
		testemail = 'john@doe.com'
		testphone = 5555555555
		testsocialMedia = {
			'Facebook': 'facebook_url',
			'LinkedIn': 'linkedIn_url',
			'Instagram': 'instagram_url',
			'Twitter': 'twitter_url'
		}
		testOwner = Owner(testfirstName, testlastName, testemail, testphone, testsocialMedia)
		self.assertEquals(testOwner.firstName, testfirstName)
		self.assertEquals(testOwner.lastName, testlastName)
		self.assertEquals(testOwner.email, testemail)
		self.assertEquals(testOwner.phone, testphone)
		self.assertEquals(testOwner.socialMedia['Facebook'], 'facebook_url')
		self.assertEquals(testOwner.socialMedia, testsocialMedia)

	def test_property(self):
		testAddress = {
			'number': '926',
			'street': 'NW 13th Ave',
			'line2': '',
			'city': 'Portland',
			'state': 'OR',
			'zip': '97209'
		}
		testResidenceType = 'Vacasa'
		testProperty = Property(testAddress, testResidenceType)
		self.assertEquals(testProperty.address, testAddress)
		self.assertEquals(testProperty.residenceType, testResidenceType)

	def test_link(self):
		testfirstName = 'John'
		testlastName = 'Doe'
		testemail = 'john@doe.com'
		testphone = 5555555555
		testsocialMedia = {
			'Facebook': 'facebook_url',
			'LinkedIn': 'linkedIn_url',
			'Instagram': 'instagram_url',
			'Twitter': 'twitter_url'
		}
		testOwner = Owner(testfirstName, testlastName, testemail, testphone, testsocialMedia)

		testAddress = {
			'number': '926',
			'street': 'NW 13th Ave',
			'line2': '',
			'city': 'Portland',
			'state': 'OR',
			'zip': '97209'
		}
		testResidenceType = 'Vacasa'
		testProperty = Property(testAddress, testResidenceType)

		testLink = Link(testOwner, testProperty)
		self.assertEquals(testLink.owner, testOwner)
		self.assertEquals(testLink.property, testProperty)

	if __name__ == '__main__':
		unittest.main()












