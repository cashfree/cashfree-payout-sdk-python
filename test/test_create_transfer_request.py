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
from cashfree_payout.models.create_transfer_request import CreateTransferRequest  # noqa: E501
from cashfree_payout.rest import ApiException

class TestCreateTransferRequest(unittest.TestCase):
    """CreateTransferRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTransferRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTransferRequest`
        """
        model = cashfree_payout.models.create_transfer_request.CreateTransferRequest()  # noqa: E501
        if include_optional :
            return CreateTransferRequest(
                transfer_id = '', 
                transfer_amount = 1.337, 
                transfer_currency = '', 
                transfer_mode = 'banktransfer', 
                beneficiary_details = cashfree_payout.models.create_transfer_request_beneficiary_details.CreateTransferRequest_beneficiary_details(
                    beneficiary_id = '', 
                    beneficiary_name = '', 
                    beneficiary_instrument_details = cashfree_payout.models.create_transfer_request_beneficiary_details_beneficiary_instrument_details.CreateTransferRequest_beneficiary_details_beneficiary_instrument_details(
                        bank_account_number = '', 
                        bank_ifsc = '', 
                        vpa = '', 
                        card_details = cashfree_payout.models.create_transfer_request_beneficiary_details_beneficiary_instrument_details_card_details.CreateTransferRequest_beneficiary_details_beneficiary_instrument_details_card_details(
                            card_token = '', 
                            card_network_type = 'VISA', 
                            card_cryptogram = '', 
                            card_token_expiry = '', 
                            card_type = '', 
                            card_token_pan_sequence_number = '', ), ), 
                    beneficiary_contact_details = cashfree_payout.models.create_transfer_request_beneficiary_details_beneficiary_contact_details.CreateTransferRequest_beneficiary_details_beneficiary_contact_details(
                        beneficiary_email = '', 
                        beneficiary_phone = '', 
                        beneficiary_country_code = '', 
                        beneficiary_address = '', 
                        beneficiary_city = '', 
                        beneficiary_state = '', 
                        beneficiary_postal_code = '', ), ), 
                transfer_remarks = '', 
                fundsource_id = ''
            )
        else :
            return CreateTransferRequest(
                transfer_id = '',
                transfer_amount = 1.337,
        )
        """

    def testCreateTransferRequest(self):
        """Test CreateTransferRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
