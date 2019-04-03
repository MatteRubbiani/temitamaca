from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time
class GetSoluzioneProblemi(Resource):

    def get (self):
        gara1=request.args.get('gara')
        if gara1 is None:
            return "mancano dati", 400
        gara=GaraModel.find_by_nome(gara1)
        if gara is None:
            return "la gara non esiste", 400
        problemi=ProblemaModel.find_all_by_gara_id(gara.id)
        a=[]
        for i in problemi:
            a.append(i.soluzione)
        return a
