import datetime
import random

import requests

from models import api


def randbool(percent_true):
    return api.BooleanAnswer.YES if bool(random.randint(0, 100) < percent_true) else api.BooleanAnswer.NO


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
COMPANIES = [
    ('Google', 'google.com'),
    ('Faire', 'faire.com'),
    ('Spotify', 'spotify.com'),
    ('Meta', 'facebook.com'),
    ('Twitter', 'twitter.com'),
    ('Amazon', 'amazon.com'),
    ('Netflix', 'netflix.com'),
    ('Microsoft', 'microsoft.com'),
    ('Apple', 'apple.com'),
]

if __name__ == '__main__':
    for i in range(15):
        company = random.choice(COMPANIES)
        print(requests.post(ENDPOINT, json=api.SubmitApplicationStatus(
            company_name=company[0],
            company_domain=company[1],
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
            year_of_graduation=random.randint(2020, 2026),
            years_of_experience=random.randint(0, 3),
            gpa=random.normalvariate(50, 5),
        ).to_dict(include_default_values=True)).text)
