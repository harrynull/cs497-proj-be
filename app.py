import json

from flask import Flask
from flask import request

from db import Session
from db.dbapp import *
from models.api import SubmitApplicationStatus

app = Flask(__name__)


@app.route('/company/', methods=['GET'])
def get_companies():
    return json.dumps(list(map(lambda x: x.company_name,
                               Session().query(DbApp.company_name).distinct().all())))


@app.route('/apps/', methods=['POST'])
def submit_app():
    application = SubmitApplicationStatus().from_dict(request.json)
    with Session() as session:
        session.add(DbApp(**application.to_dict()))
        session.commit()
    return "OK"


if __name__ == '__main__':
    app.run()
