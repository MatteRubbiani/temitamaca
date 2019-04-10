from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time
from Resources.CheckEnd import CheckEnd
class ConsegnaProblema(Resource):

    def post (self):

        nome=request.args.get('nome')
        numero=request.args.get('numero')
        risposta=request.args.get('risposta')


        simulazione=SimulazioneModel.find_by_nome(nome)
        if simulazione is None:
            return "non esite simulazione", 400



        if not simulazione.started:
            return "gara non ancora iniziata", 400

        if CheckEnd(nome):
            return "gara finita"
        problemi=ProblemiSimulazioneModel.find_by_simulazione_id(simulazione.id)
        if problemi is None:

            return "non ci sono problemi in questa simulazione", 400
        for i in problemi:

            a=ProblemaModel.find_by_id(i.problema_id)
            if a.numero==int(numero):

                if i.risolto:
                    return "il problema e' gia' stato risolto", 400
                i.tentativi=i.tentativi+1
                if a.soluzione !=int(risposta):
                    gara=GaraModel.find_by_id(simulazione.gara_id)
                    punteggio=gara.errore
                    i.save_to_db()
                    simulazione.totale_punti=simulazione.totale_punti-punteggio
                    simulazione.save_to_db()

                    return False
                else:

                    punteggio=a.valore
                    i.risolto=True
                    i.tempo_risoluzione= int(time.time())
                    i.save_to_db()
                    simulazione.totale_punti=simulazione.totale_punti+punteggio
                    simulazione.save_to_db()

                    return True
                break
        return "il problema non esiste", 400
