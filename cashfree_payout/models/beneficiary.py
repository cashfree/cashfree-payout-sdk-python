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
from pydantic import BaseModel, Field, StrictStr, validator
from cashfree_payout.models.beneficiary_beneficiary_contact_details import BeneficiaryBeneficiaryContactDetails
from cashfree_payout.models.beneficiary_beneficiary_instrument_details import BeneficiaryBeneficiaryInstrumentDetails

class Beneficiary(BaseModel):
    """
    Contains the information of the created beneficiary
    """
    beneficiary_id: Optional[StrictStr] = Field(None, description="It displays the unique ID you created to identify the beneficiary.")
    beneficiary_name: Optional[StrictStr] = Field(None, description="It displays the name of the beneficiary.")
    beneficiary_instrument_details: Optional[BeneficiaryBeneficiaryInstrumentDetails] = None
    beneficiary_contact_details: Optional[BeneficiaryBeneficiaryContactDetails] = None
    beneficiary_status: Optional[StrictStr] = Field(None, description="It displays the current status of the beneficiary. Possible values are as follows - `VERIFIED`: Beneficiary is verified and is available for payouts - `INVALID`: Beneficiary is invalid - `INITIATED`: Beneficiary verification initiated - `CANCELLED`: Beneficiary verification cancelled - `FAILED`: Failed to verify beneficiary - `DELETED`: Beneficiary is deleted")
    added_on: Optional[StrictStr] = Field(None, description="It displays the time of the addition of the beneficiary in UTC.")
    __properties = ["beneficiary_id", "beneficiary_name", "beneficiary_instrument_details", "beneficiary_contact_details", "beneficiary_status", "added_on"]

    @validator('beneficiary_status')
    def beneficiary_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('VERIFIED', 'INVALID', 'INITIATED', 'CANCELLED', 'FAILED', 'DELETED'):
            raise ValueError("must be one of enum values ('VERIFIED', 'INVALID', 'INITIATED', 'CANCELLED', 'FAILED', 'DELETED')")
        return value

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
    def from_json(cls, json_str: str) -> Beneficiary:
        """Create an instance of Beneficiary from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> Beneficiary:
        """Create an instance of Beneficiary from a JSON string"""
        temp_dict = json.loads(json_str)
        if "beneficiary_id, beneficiary_name, beneficiary_instrument_details, beneficiary_contact_details, beneficiary_status, added_on" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> Beneficiary:
        """Create an instance of Beneficiary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Beneficiary.parse_obj(obj)

        _obj = Beneficiary.parse_obj({
            "beneficiary_id": obj.get("beneficiary_id"),
            "beneficiary_name": obj.get("beneficiary_name"),
            "beneficiary_instrument_details": BeneficiaryBeneficiaryInstrumentDetails.from_dict(obj.get("beneficiary_instrument_details")) if obj.get("beneficiary_instrument_details") is not None else None,
            "beneficiary_contact_details": BeneficiaryBeneficiaryContactDetails.from_dict(obj.get("beneficiary_contact_details")) if obj.get("beneficiary_contact_details") is not None else None,
            "beneficiary_status": obj.get("beneficiary_status"),
            "added_on": obj.get("added_on")
        })
        return _obj


