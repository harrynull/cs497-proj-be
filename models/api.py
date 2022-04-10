# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: protos/api.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class Stage(betterproto.Enum):
    APPLIED = 0
    ONLINE_ASSESSMENT = 1
    INTERVIEW = 2
    OFFER = 3


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
    BELOW_HIGH_SCHOOL = 0
    HIGH_SCHOOL = 1
    ASSOCIATES = 2
    BACHELORS = 3
    MASTERS = 4
    DOCTORATE = 5
    OTHER_EDUCATION = 6


class BooleanAnswer(betterproto.Enum):
    YES = 0
    NO = 1
    PREFER_NOT_TO_ANSWER = 2


@dataclass
class SubmitApplicationStatus(betterproto.Message):
    # next 22
    company_name: str = betterproto.string_field(1)
    company_domain: str = betterproto.string_field(21)
    stage: "Stage" = betterproto.enum_field(2)
    job_title: str = betterproto.string_field(3)
    hourly_compensation: int = betterproto.int32_field(4)
    date_of_decision: int = betterproto.int64_field(5)
    gender: "Gender" = betterproto.enum_field(6)
    sexual_orientation: "SexualOrientation" = betterproto.enum_field(7)
    racial_origin: "RacialOrigin" = betterproto.enum_field(8)
    visa_status: "VisaStatus" = betterproto.enum_field(9)
    nationality: str = betterproto.string_field(10)
    disability: "BooleanAnswer" = betterproto.enum_field(11)
    veteran_status: "BooleanAnswer" = betterproto.enum_field(12)
    criminal_background: "BooleanAnswer" = betterproto.enum_field(13)
    indigenous: "BooleanAnswer" = betterproto.enum_field(14)
    marriage_status: "MarriageStatus" = betterproto.enum_field(15)
    education_level: "EducationLevel" = betterproto.enum_field(16)
    year_of_graduation: str = betterproto.string_field(17)
    years_of_experience: int = betterproto.int32_field(18)
    co_op_term: int = betterproto.int32_field(19)
    gpa: float = betterproto.double_field(20)


@dataclass
class CompanyStatsRequest(betterproto.Message):
    interested_attributes: List[str] = betterproto.string_field(1)
    job_title_filter: str = betterproto.string_field(2)


@dataclass
class Company(betterproto.Message):
    name: str = betterproto.string_field(1)
    domain: str = betterproto.string_field(2)
