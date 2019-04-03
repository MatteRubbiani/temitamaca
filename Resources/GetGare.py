from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time
class GetGare(Resource):

    def get (self):

        gare=GaraModel.find_all()
        a=[]

        c=[]

        for gara in gare:
            numeroProblemi=len(ProblemaModel.find_all_by_gara_id(gara.id))
            o=time.strftime('%d-%m-%Y', time.localtime(gara.date))
            b={
                "nome":gara.nome,
                "descrizione":gara.descrizione,
                "autore":gara.autore,
                "numeroProblemi":numeroProblemi,
                "data":o
            }
            a.append(b)
        if a:
            return a
        return []
