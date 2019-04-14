from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel

class AutorizzaSimulazione(Resource):

    def post(self):
        simul=request.args.get('simulazione')
        password=request.args.get('password')
        simulazione=SimulazioneModel.find_by_nome(simul)
        if simulazione and simulazione.password==password:
            return True, 200
        if simulazione:
            return False, 200
