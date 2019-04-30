from Resources.CheckEnd import CheckEnd, CheckStatus
from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time
def find_valore_effettivo(problema, simulazione, problema_riferimento):
    jolly=1
    if problema.jolly:
        jolly=2
    if problema.risolto:
        tempo=problema.tempo_risoluzione
    else:
        tempo=int(time.time())
    tempo_trascorso = tempo-simulazione.inizio
    bonus = tempo_trascorso//60
    valore_puro = problema_riferimento.valore + bonus
    return valore_puro*jolly

def find_valore(problema, simulazione, problema_riferimento, gara):
    jolly=1
    if problema.jolly:
        jolly=2
    errore=(problema.tentativi-1)*jolly*gara.errore
    if not problema.risolto:
        return  -errore

    valore_effettivo = find_valore_effettivo(problema, simulazione, problema_riferimento)
    totale = valore_effettivo-errore
    return totale

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
            gara=GaraModel.find_by_id(simulazione.gara_id)

            problemi1=ProblemiSimulazioneModel.find_by_simulazione_id(simulazione.id)

            if problemi1 is None:
                return "non ci sono problemi in questa simulazione"
            d=[]
            for i in problemi1:
                d.append(i)
            f = sorted(d, key=lambda x: x.numero)

            array=[]
            for i in f:
                problema_riferimento=ProblemaModel.find_by_id(i.problema_id)
                valoreEffettivo=find_valore_effettivo(i, simulazione, problema_riferimento)
                valore=find_valore(i, simulazione, problema_riferimento, gara)
                array.append({"risolto":i.risolto,
                            "valore":valore,
                            "errori":i.tentativi-1,
                            "valoreEffettivo":valoreEffettivo,#valore che avrebbe senza gli errori
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
