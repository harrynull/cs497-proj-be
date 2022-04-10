import datetime
import random

import requests

from models import api


def randbool(percent_true):
    return bool(random.randint(0, 100) < percent_true)


def randchoice(percents, choices):
    rand = random.randint(0, 100)
    for i in range(len(percents)):
        if rand < percents[i]:
            return choices[i]
        else:
            rand -= percents[i]
    return choices[-1]


def randenum(percents, enum):
    return randchoice(percents, list(enum))


def uniformenum(enum):
    return random.choice(list(enum))


ENDPOINT = 'http://localhost:8080/apps/'
if __name__ == '__main__':
    for i in range(250):
        print(requests.post(ENDPOINT, json=api.SubmitApplicationStatus(
            company_name=random.choice(['Google', 'Shopify', 'Spotify', 'Meta', 'Twitter', 'Instagram', 'Facebook',
                                        'Amazon', 'Netflix', 'Microsoft', 'Apple']),
            stage=uniformenum(api.Stage),
            job_title=randchoice([30, 50, 20], ['Software Engineer', 'Software Engineer Intern', 'QA Engineer']),
            hourly_compensation=30,
            date_of_decision=int(datetime.datetime.now().timestamp()),
            gender=randenum([40, 40, 5, 5, 3, 3, 3, 1], api.Gender),
            sexual_orientation=randenum([94, 3, 1, 1, 1], api.SexualOrientation),
            racial_origin=uniformenum(api.RacialOrigin),
            visa_status=randenum([80, 15, 5], api.VisaStatus),
            nationality=randchoice([55, 10, 10, 20, 5], ['Canada', 'India', 'China', 'US', 'UK']),
            disability=randbool(5),
            veteran_status=randbool(1),
            criminal_background=randbool(5),
            indigenous=randbool(5),
            marriage_status=randenum([75, 10, 5, 5, 5], api.MarriageStatus),
            education_level=randenum([5, 10, 15, 50, 10, 5, 5], api.EducationLevel),
            graduated=randbool(15),
            years_of_experience=random.randint(0, 3),
            co_op_term=random.randint(1, 6),
            gpa=random.normalvariate(50, 5),
        ).to_dict()).text)
