from flask_restful import Resource, request
from Models.GaraModel import GaraModel
from Models.ProblemaModel import ProblemaModel
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
import time

class SimulazioneTime(Resource):

    def get(self):
        simulazione1=request.args.get('simulazione')
        simulazione=SimulazioneModel.find_by_nome(simulazione1)
        if simulazione.started:
            time1=int(time.time())
            tempo=simulazione.inizio+simulazione.durata-time1
            return time1
