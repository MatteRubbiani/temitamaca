from flask_restful import Resource, request
from Models.GaraModel import GaraModel
from Models.ProblemaModel import ProblemaModel


class CreateProblema(Resource):

    def post (self):
        gara1=request.args.get('gara')
        risposta=request.args.get('risposta')
        valore=request.args.get('valore')
        if risposta:
            if gara1:
                gara=GaraModel.find_by_nome(gara1)
                if gara:
                    prob=ProblemaModel.append_problema(gara.id, valore, risposta)
                    return prob.numero
                return "gara non esiste"
            return "mancano dati"
        return "mancano dati"



    def put(self):
        gara1=request.args.get('gara')
        numero=request.args.get('numero')
        risposta=request.args.get('risposta')
        valore=request.args.get('valore')
        if gara1 and numero:
            gara=GaraModel.find_by_nome(gara1)
            if gara:
                prob=ProblemaModel.modify_problema(gara.id, numero, valore, risposta)
                return prob.soluzione
            return "gara non esiste"

        return "mancano dati"
