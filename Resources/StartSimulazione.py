from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
import time

class StartSimulazione(Resource):

    def post (self):
        simulazioneNome=request.args.get('nome')
        password=request.args.get('password')
        time1= int(time.time())
        simulazione=SimulazioneModel.find_by_nome(simulazioneNome)
        if simulazione is None or simulazione.password != password or simulazione.started is True:
            return "nope", 400
        simulazione.inizio=time1
        simulazione.started=True
        simulazione.save_to_db()
        return simulazione.inizio
