# coding: utf-8

"""
    Cashfree Payout APIs

    Cashfree's Payout APIs provide developers with a streamlined pathway to integrate advanced payout capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2024-01-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from cashfree_payout.models.create_transfer_request_beneficiary_details_beneficiary_contact_details import CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails
from cashfree_payout.models.create_transfer_request_beneficiary_details_beneficiary_instrument_details import CreateTransferRequestBeneficiaryDetailsBeneficiaryInstrumentDetails

class CreateTransferRequestBeneficiaryDetails(BaseModel):
    """
    It should contain the details of the beneficiary who receives the transfer amount.
    """
    beneficiary_id: Optional[StrictStr] = Field(None, description="It is the unique ID you created to identify the beneficiary. Alphanumeric characters are allowed.")
    beneficiary_name: Optional[StrictStr] = Field(None, description="It is the name of the beneficiary. The maximum character limit is 100.  Only alphabets and whitespaces are allowed. It is required if beneficiary_id is not present.")
    beneficiary_instrument_details: Optional[CreateTransferRequestBeneficiaryDetailsBeneficiaryInstrumentDetails] = None
    beneficiary_contact_details: Optional[CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails] = None
    __properties = ["beneficiary_id", "beneficiary_name", "beneficiary_instrument_details", "beneficiary_contact_details"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateTransferRequestBeneficiaryDetails:
        """Create an instance of CreateTransferRequestBeneficiaryDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateTransferRequestBeneficiaryDetails:
        """Create an instance of CreateTransferRequestBeneficiaryDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "beneficiary_id, beneficiary_name, beneficiary_instrument_details, beneficiary_contact_details" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of beneficiary_instrument_details
        if self.beneficiary_instrument_details:
            _dict['beneficiary_instrument_details'] = self.beneficiary_instrument_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beneficiary_contact_details
        if self.beneficiary_contact_details:
            _dict['beneficiary_contact_details'] = self.beneficiary_contact_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTransferRequestBeneficiaryDetails:
        """Create an instance of CreateTransferRequestBeneficiaryDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTransferRequestBeneficiaryDetails.parse_obj(obj)

        _obj = CreateTransferRequestBeneficiaryDetails.parse_obj({
            "beneficiary_id": obj.get("beneficiary_id"),
            "beneficiary_name": obj.get("beneficiary_name"),
            "beneficiary_instrument_details": CreateTransferRequestBeneficiaryDetailsBeneficiaryInstrumentDetails.from_dict(obj.get("beneficiary_instrument_details")) if obj.get("beneficiary_instrument_details") is not None else None,
            "beneficiary_contact_details": CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails.from_dict(obj.get("beneficiary_contact_details")) if obj.get("beneficiary_contact_details") is not None else None
        })
        return _obj


