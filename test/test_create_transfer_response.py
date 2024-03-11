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
from cashfree_payout.models.create_transfer_response import CreateTransferResponse  # noqa: E501
from cashfree_payout.rest import ApiException

class TestCreateTransferResponse(unittest.TestCase):
    """CreateTransferResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTransferResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTransferResponse`
        """
        model = cashfree_payout.models.create_transfer_response.CreateTransferResponse()  # noqa: E501
        if include_optional :
            return CreateTransferResponse(
                transfer_id = '', 
                cf_transfer_id = '', 
                status = '', 
                beneficiary_details = cashfree_payout.models.create_transfer_response_beneficiary_details.CreateTransferResponse_beneficiary_details(
                    beneficiary_id = '', 
                    beneficiary_instrument_details = cashfree_payout.models.create_transfer_response_beneficiary_details_beneficiary_instrument_details.CreateTransferResponse_beneficiary_details_beneficiary_instrument_details(
                        bank_account_number = '', 
                        ifsc = '', 
                        vpa = '', ), ), 
                transfer_amount = 1.337, 
                transfer_service_charge = 1.337, 
                transfer_service_tax = 1.337, 
                transfer_mode = '', 
                transfer_utr = '', 
                fundsource_id = '', 
                added_on = '', 
                updated_on = ''
            )
        else :
            return CreateTransferResponse(
        )
        """

    def testCreateTransferResponse(self):
        """Test CreateTransferResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
