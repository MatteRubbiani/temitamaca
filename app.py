import os
from flask import Flask
from flask_restful import Api
from datetime import timedelta
from flask import Flask, jsonify, request



from Resources.CreateProblema import CreateProblema
from Resources.CreateGara import CreateGara
from Resources.CreateSimulazione import CreateSimulazione
from Resources.StartSimulazione import StartSimulazione
from Resources.ConsegnaProblema import ConsegnaProblema
from Resources.GetGare import GetGare
from Resources.GetProblemiSimulazione import GetProblemiSimulazione


from Resources.GetProblemi import GetSoluzioneProblemi

from Resources.AutorizzaGara import AutorizzaGara
from Resources.AutorizzaSimulazione import AutorizzaSimulazione




app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.config["PROPAGATE_EXCEPTIONS"]=True
app.secret_key="Matteo"
api=Api(app)


"""
@app.before_first_request
def create_table():
    db.create_all()
"""



api.add_resource(CreateGara, "/gara/create")

api.add_resource(CreateProblema, "/problema/create")
api.add_resource(ConsegnaProblema, "/problema/consegna")

api.add_resource(GetSoluzioneProblemi, "/problemi/all")
api.add_resource(GetGare, "/gara/all")

api.add_resource(CreateSimulazione, "/simulazione/create")
api.add_resource(StartSimulazione, "/simulazione/start")
api.add_resource(GetProblemiSimulazione, "/simulazione/get")

api.add_resource(AutorizzaGara, "/autorizza/gara")
api.add_resource(AutorizzaSimulazione, "/autorizza/simulazione")







if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
