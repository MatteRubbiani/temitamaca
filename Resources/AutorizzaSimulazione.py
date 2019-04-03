from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel

class AutorizzaSimulazione(Resource):

    def post(self):
        simul=request.args.get('simulazione')
        simulazione=SimulazioneModel.find_by_nome(simul)
        if simulazione:
            return True, 200
        return False, 400
