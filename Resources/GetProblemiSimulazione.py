from Resources.CheckEnd import CheckEnd, CheckStatus
from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time

class GetProblemiSimulazione(Resource):

    def get (self):
        sim=request.args.get('simulazione')
        a=CheckStatus(sim)

        #0__non esiste, 1__e' finita, 2__e' in corso, 3__non e' ancora iniziata
        if a==0:
            return "la simulazione non esiste", 400


        if a==1:

            return "metti risulatati", 201


        if a==2:
            simulazione=SimulazioneModel.find_by_nome(sim)
            problemi1=ProblemiSimulazioneModel.find_by_simulazione_id(simulazione.id)

            if problemi1 is None:
                return "non ci sono problemi in questa simulazione"
            d=[]

            for i in problemi1:
                d.append(i)
            f = sorted(d, key=lambda x: x.numero)
        
            #problemi=d.sort(key=lambda x: ProblemaModel.find_id(x.problema_id).numero)
            erroreGara=GaraModel.find_by_id(simulazione.gara_id).errore
            array=[]
            for i in f:
                valore=ProblemaModel.find_by_id(i.problema_id).valore
                if i.risolto:
                    errori=i.tentativi-1
                    totalScore=valore-(errori*erroreGara)

                else:
                    errori=i.tentativi
                    totalScore=-(errori*erroreGara)
                pb=ProblemaModel.find_by_id(i.problema_id)
                array.append({"risolto":i.risolto,
                            "valore":totalScore,
                            "errori":errori,
                            "valoreEffettivo":pb.valore})
            return array, 202


        if a==3:
            return "non ancora iniziata", 203
