# coding: utf-8

"""
    Cashfree Payout APIs

    Cashfree's Payout APIs provide developers with a streamlined pathway to integrate advanced payout capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2024-01-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_payout
from cashfree_payout.models.beneficiary_beneficiary_contact_details import BeneficiaryBeneficiaryContactDetails  # noqa: E501
from cashfree_payout.rest import ApiException

class TestBeneficiaryBeneficiaryContactDetails(unittest.TestCase):
    """BeneficiaryBeneficiaryContactDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BeneficiaryBeneficiaryContactDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BeneficiaryBeneficiaryContactDetails`
        """
        model = cashfree_payout.models.beneficiary_beneficiary_contact_details.BeneficiaryBeneficiaryContactDetails()  # noqa: E501
        if include_optional :
            return BeneficiaryBeneficiaryContactDetails(
                beneficiary_email = 'johndoe_1@cashfree.com', 
                beneficiary_phone = '9876543210', 
                beneficiary_country_code = '+91', 
                beneficiary_address = '177A Bleecker Street', 
                beneficiary_city = 'New York City', 
                beneficiary_state = 'New York', 
                beneficiary_postal_code = '560001'
            )
        else :
            return BeneficiaryBeneficiaryContactDetails(
        )
        """

    def testBeneficiaryBeneficiaryContactDetails(self):
        """Test BeneficiaryBeneficiaryContactDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()