from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time
from CheckEnd import CheckEnd
class ConsegnaProblema(Resource):

    def post (self):

        nome=request.args.get('nome')
        numero=request.args.get('numero')
        risposta=request.args.get('risposta')


        simulazione=SimulazioneModel.find_by_nome(nome)
        if simulazione is None:
            return "non esite simulazione"



        if not simulazione.started:
            return "gara non ancora iniziata"

        if CheckEnd(nome):
            return "gara finit"
