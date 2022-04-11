from flask import Flask, jsonify
from flask import request
from sqlalchemy import func

from db import Session
from db.dbapp import *
from models.api import SubmitApplicationStatus, CompanyStatsRequest, Stage, Company

app = Flask(__name__)


@app.route('/company/', methods=['GET'])
def get_companies():
    return jsonify(list([Company(name=c.company_name, domain=c.company_domain)
                         for c in Session().query(DbApp.company_name, DbApp.company_domain)
                        .distinct().all()]))


@app.route('/company/<name>/jobs/', methods=['GET'])
def get_company_jobs(name: str):
    return jsonify(list(map(lambda x: x.job_title,
                            Session().query(DbApp.job_title).filter(DbApp.company_name == name).distinct().all())))


# req:
# {
#   interested: ["nationality", "indigenous"],
#   job_title_filter: ""
# }
# resp:
# {
#   stages: {
#       "Applied": {
#           "nationality": {
#               "Canada": 0.9,
#               "China": 0.1
#           }
#       }
#   },
#   domain: "xx.com"
# }
@app.route('/company/<name>', methods=['POST'])
def get_company_stats(name: str):
    def count(stg: Stage, attr_of_interest):
        q = session.query(attr_of_interest, func.count(attr_of_interest)).filter(DbApp.company_name == name)
        if req.job_title_filter:
            q = q.filter(DbApp.job_title == req.job_title_filter)
        result = q.filter(DbApp.stage == stg).group_by(attr_of_interest).all()
        return {r[0]: r[1] for r in result}

    # convert attr_name to the corresponding DbApp field
    def str2field(attr_name: str):
        return {
            "gender": DbApp.gender,
            "sexual_orientation": DbApp.sexual_orientation,
            "racial_origin": DbApp.racial_origin,
            "visa_status": DbApp.visa_status,
            "nationality": DbApp.nationality,
            "disability": DbApp.disability,
            "veteran_status": DbApp.veteran_status,
            "criminal_background": DbApp.criminal_background,
            "indigenous": DbApp.indigenous,
            "marriage_status": DbApp.marriage_status,
            "education_level": DbApp.education_level,
            "year_of_graduation": DbApp.graduation_year,
            "years_of_experience": DbApp.years_of_experience,
        }[attr_name]

    req = CompanyStatsRequest().from_dict(request.json)
    resp = {}
    with Session() as session:
        resp['stages'] = {
            stage.name: {attr: count(stage, str2field(attr)) for attr in req.interested_attributes}
            for stage in Stage
        }
    domain = Session().query(DbApp.company_domain).filter(DbApp.company_name == name).distinct().first()
    resp['domain'] = domain[0] if domain else None
    return resp


@app.route('/apps/', methods=['POST'])
def submit_app():
    application = SubmitApplicationStatus().from_dict(request.json)
    with Session() as session:
        session.add(DbApp(
            company_name=application.company_name,
            company_domain=application.company_domain,
            stage=application.stage,
            job_title=application.job_title,
            hourly_compensation=application.hourly_compensation,
            date_of_decision=application.date_of_decision,
            gender=application.gender,
            sexual_orientation=application.sexual_orientation,
            racial_origin=application.racial_origin,
            visa_status=application.visa_status,
            nationality=application.nationality,
            disability=application.disability,
            veteran_status=application.veteran_status,
            criminal_background=application.criminal_background,
            indigenous=application.indigenous,
            marriage_status=application.marriage_status,
            education_level=application.education_level,
            graduation_year=application.year_of_graduation,
            years_of_experience=application.years_of_experience,
            gpa=application.gpa,
        ))
        session.commit()
    return '"OK"'


if __name__ == '__main__':
    app.run()
