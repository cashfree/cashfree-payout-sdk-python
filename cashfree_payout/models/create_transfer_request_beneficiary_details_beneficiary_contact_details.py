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

class CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails(BaseModel):
    """
    It should contain the contact details of the beneficiary.
    """
    beneficiary_email: Optional[StrictStr] = Field(None, description="It is the email address of the beneficiary. The maximum character limit is 200. It should contain dot (.) and at the rate of (@).")
    beneficiary_phone: Optional[StrictStr] = Field(None, description="It is the phone number of the beneficiary. Only registered Indian phone numbers are allowed. The value should be between 8 and 12 characters after stripping +91.")
    beneficiary_country_code: Optional[StrictStr] = Field(None, description="It is the country code (+91) of the beneficiary's phone number.")
    beneficiary_address: Optional[StrictStr] = Field(None, description="It should contain the address of the beneficiary. The maximum character limit is 150. Alphanumeric characters and whitespaces are allowed.")
    beneficiary_city: Optional[StrictStr] = Field(None, description="It is the name of the city as present in the beneficiary address. The maximum character limit is 50. Alphanumeric characters and whitespaces are allowed.")
    beneficiary_state: Optional[StrictStr] = Field(None, description="It is the name of the state as present in the beneficiary address. The maximum character limit is 50. Alphanumeric characters and whitespaces are allowed.")
    beneficiary_postal_code: Optional[StrictStr] = Field(None, description="It is the PIN code as present in the address. It should be a 6 character numeric value.")
    __properties = ["beneficiary_email", "beneficiary_phone", "beneficiary_country_code", "beneficiary_address", "beneficiary_city", "beneficiary_state", "beneficiary_postal_code"]

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
    def from_json(cls, json_str: str) -> CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails:
        """Create an instance of CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails:
        """Create an instance of CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "beneficiary_email, beneficiary_phone, beneficiary_country_code, beneficiary_address, beneficiary_city, beneficiary_state, beneficiary_postal_code" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails:
        """Create an instance of CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails.parse_obj(obj)

        _obj = CreateTransferRequestBeneficiaryDetailsBeneficiaryContactDetails.parse_obj({
            "beneficiary_email": obj.get("beneficiary_email"),
            "beneficiary_phone": obj.get("beneficiary_phone"),
            "beneficiary_country_code": obj.get("beneficiary_country_code"),
            "beneficiary_address": obj.get("beneficiary_address"),
            "beneficiary_city": obj.get("beneficiary_city"),
            "beneficiary_state": obj.get("beneficiary_state"),
            "beneficiary_postal_code": obj.get("beneficiary_postal_code")
        })
        return _obj

