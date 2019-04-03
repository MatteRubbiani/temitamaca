from flask_restful import Resource, request
from Models.GaraModel import GaraModel
class AutorizzaGara(Resource):

    def post(self):
        gara1=request.args.get('gara')
        password=request.args.get('password')
        gara=GaraModel.find_by_nome(gara1)
        if gara and gara.password==password:
            return True
        return False
