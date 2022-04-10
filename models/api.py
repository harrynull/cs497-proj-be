# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: protos/api.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class Stage(betterproto.Enum):
    Applied = 0
    OnlineAssessment = 1
    Interview = 2
    Interview2 = 3
    Interview3 = 4
    Offer = 5


class Gender(betterproto.Enum):
    CIS_FEMALE = 0
    CIS_MALE = 1
    TRANS_FEMALE = 2
    TRANS_MALE = 3
    AGENDER = 4
    GENDER_FLUID = 5
    BIGENDER = 6
    OTHER_GENDER = 7


class SexualOrientation(betterproto.Enum):
    HETEROSEXUAL = 0
    HOMOSEXUAL = 1
    BISEXUAL = 2
    ASEXUAL = 3
    OTHER_SEXUAL_ORIENTATION = 4


class RacialOrigin(betterproto.Enum):
    AMERICAN_INDIAN = 0
    ASIAN = 1
    AFRICAN_AMERICAN = 2
    HISPANIC = 3
    WHITE = 4
    OTHER_RACIAL_ORIGIN = 5


class VisaStatus(betterproto.Enum):
    NATIONAL = 0
    VISA_HOLDER = 1
    NO_STATUS = 2


class MarriageStatus(betterproto.Enum):
    SINGLE = 0
    MARRIED = 1
    DIVORCED = 2
    WIDOWED = 3
    OTHER_MARITAL_STATUS = 4


class EducationLevel(betterproto.Enum):
    NO_EDUCATION = 0
    HIGH_SCHOOL = 1
    ASSOCIATES = 2
    BACHELORS = 3
    MASTERS = 4
    DOCTORATE = 5
    OTHER_EDUCATION = 6


@dataclass
class SubmitApplicationStatus(betterproto.Message):
    company_name: str = betterproto.string_field(1)
    stage: "Stage" = betterproto.enum_field(2)
    job_title: str = betterproto.string_field(3)
    hourly_compensation: int = betterproto.int32_field(4)
    date_of_decision: int = betterproto.int64_field(5)
    gender: "Gender" = betterproto.enum_field(6)
    sexual_orientation: "SexualOrientation" = betterproto.enum_field(7)
    racial_origin: "RacialOrigin" = betterproto.enum_field(8)
    visa_status: "VisaStatus" = betterproto.enum_field(9)
    nationality: str = betterproto.string_field(10)
    disability: bool = betterproto.bool_field(11)
    veteran_status: bool = betterproto.bool_field(12)
    criminal_background: bool = betterproto.bool_field(13)
    indigenous: bool = betterproto.bool_field(14)
    marriage_status: "MarriageStatus" = betterproto.enum_field(15)
    education_level: "EducationLevel" = betterproto.enum_field(16)
    graduated: bool = betterproto.bool_field(17)
    years_of_experience: int = betterproto.int32_field(18)
    co_op_term: int = betterproto.int32_field(19)
    gpa: float = betterproto.double_field(20)


@dataclass
class CompanyStatsRequest(betterproto.Message):
    interested_attributes: List[str] = betterproto.string_field(1)
    job_title_filter: str = betterproto.string_field(2)
