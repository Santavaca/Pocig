#!/usr/bin/env python3

#import unittest
#sys.path.insert(0, '/')
#import owner
import unittest, sys
sys.path.append('../../')
from src.DataClasses.owner import Owner
from src.DataClasses.property import Property
from src.DataClasses.link import Link

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
		testAddress2 = {
			'number': '927',
			'street': 'NW 14th Ave',
			'line2': '',
			'city': 'Portland',
			'state': 'OR',
			'zip': '97210'
		}

		testResidenceType = 'Vacasa'
		testProperty = Property(testAddress, testResidenceType)
		testProperty2 = Property(testAddress2, testResidenceType)
		testProperties = [testProperty, testProperty2]

		testLink = Link(testOwner, testProperties)
		self.assertEquals(testLink.owner, testOwner)
		self.assertEquals(testLink.properties[0], testProperty)
		self.assertEquals(testLink.properties, testProperties)

	if __name__ == '__main__':
		unittest.main()












