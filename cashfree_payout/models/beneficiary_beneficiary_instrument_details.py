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

class BeneficiaryBeneficiaryInstrumentDetails(BaseModel):
    """
    It displays the payment instrument details of the beneficiary.
    """
    bank_account_number: Optional[StrictStr] = Field(None, description="It displays the bank account of the beneficiary.")
    bank_ifsc: Optional[StrictStr] = Field(None, description="It displays the IFSC information of the beneficiary's bank account.")
    vpa: Optional[StrictStr] = Field(None, description="It displays the UPI VPA information of the beneficiary.")
    __properties = ["bank_account_number", "bank_ifsc", "vpa"]

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
    def from_json(cls, json_str: str) -> BeneficiaryBeneficiaryInstrumentDetails:
        """Create an instance of BeneficiaryBeneficiaryInstrumentDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> BeneficiaryBeneficiaryInstrumentDetails:
        """Create an instance of BeneficiaryBeneficiaryInstrumentDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "bank_account_number, bank_ifsc, vpa" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> BeneficiaryBeneficiaryInstrumentDetails:
        """Create an instance of BeneficiaryBeneficiaryInstrumentDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BeneficiaryBeneficiaryInstrumentDetails.parse_obj(obj)

        _obj = BeneficiaryBeneficiaryInstrumentDetails.parse_obj({
            "bank_account_number": obj.get("bank_account_number"),
            "bank_ifsc": obj.get("bank_ifsc"),
            "vpa": obj.get("vpa")
        })
        return _obj

