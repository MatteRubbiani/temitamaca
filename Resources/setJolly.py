from flask_restful import Resource, request
from Models.GaraModel import GaraModel
from Models.ProblemaModel import ProblemaModel
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel

class SetJolly(Resource):

    def post (self):
        simulazione1=request.args.get('simulazione')
        problema=request.args.get('problema')
        simulazione=SimulazioneModel.find_by_nome(simulazione1)
        problemi=ProblemiSimulazioneModel.find_by_simulazione_id(simulazione.id)
        for i in problemi:
            if i.jolly:
                return i.numero, 200

        for k in problemi:
            if k.numero == int(problema):
                k.jolly=True
                return 0, 200
        return "il problema non esiste", 400
