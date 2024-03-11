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
from cashfree_payout.models.beneficiary_beneficiary_instrument_details import BeneficiaryBeneficiaryInstrumentDetails  # noqa: E501
from cashfree_payout.rest import ApiException

class TestBeneficiaryBeneficiaryInstrumentDetails(unittest.TestCase):
    """BeneficiaryBeneficiaryInstrumentDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BeneficiaryBeneficiaryInstrumentDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BeneficiaryBeneficiaryInstrumentDetails`
        """
        model = cashfree_payout.models.beneficiary_beneficiary_instrument_details.BeneficiaryBeneficiaryInstrumentDetails()  # noqa: E501
        if include_optional :
            return BeneficiaryBeneficiaryInstrumentDetails(
                bank_account_number = '00111122233', 
                bank_ifsc = 'HDFC0000001', 
                vpa = 'test@upi'
            )
        else :
            return BeneficiaryBeneficiaryInstrumentDetails(
        )
        """

    def testBeneficiaryBeneficiaryInstrumentDetails(self):
        """Test BeneficiaryBeneficiaryInstrumentDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
