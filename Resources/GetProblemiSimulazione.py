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
                        if i.jolly:
                            totalScore=totalScore*2
                        tempo=i.tempo_risoluzione-simulazione.inizio

                    else:
                        errori=i.tentativi
                        totalScore=-(errori*erroreGara)
                        if i.jolly:
                            totalScore=totalScore*2
                        tempo=0

                    pb=ProblemaModel.find_by_id(i.problema_id)
                    array.append(

                         {"risolto":i.risolto,
                        "punteggio":totalScore,
                        "errori":errori,
                        "tempo":tempo,
                        "jolly":i.jolly}
                        )
                return array, 201



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
                    if i.jolly:
                        totalScore=totalScore*2

                else:
                    errori=i.tentativi
                    totalScore=-(errori*erroreGara)
                    if i.jolly:
                        totalScore=totalScore*2
                pb=ProblemaModel.find_by_id(i.problema_id)
                array.append({"risolto":i.risolto,
                            "valore":totalScore,
                            "errori":errori,
                            "valoreEffettivo":pb.valore,
                            "jolly":i.jolly})
            return array, 202


        if a==3:
            simulazione=SimulazioneModel.find_by_nome(sim)
            gara=GaraModel.find_by_id(simulazione.gara_id)
            o={
                "durata":simulazione.durata,
                "gara": gara.nome
            }
            return o, 203
