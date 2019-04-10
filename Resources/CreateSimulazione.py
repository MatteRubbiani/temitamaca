from flask_restful import Resource, request
from Models.GaraModel import GaraModel
from Models.ProblemaModel import ProblemaModel
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel

class CreateSimulazione(Resource):

    def post (self):
        garaNome=request.args.get('gara')
        simulazioneNome=request.args.get('nome')
        durata=request.args.get('durata')
        password=request.args.get('password')

        gara=GaraModel.find_by_nome(garaNome)
        if gara is None:
            return "gara non esiste", 400

        simulazione1=SimulazioneModel.find_by_nome(simulazioneNome)
        if simulazione1:
            return "una simulazione con questo nome esiste gia", 401
        simulazione=SimulazioneModel(None, gara.id, None, int(durata), 0, simulazioneNome, False, password)
        simulazione.save_to_db()
        simulazione.create_problemi_simulazione()
        return "la simulazione e'stata creata"


    def put (self):
        ex_nome=request.args.get('oldNome')
        nome=request.args.get('nome')
        descrizione=request.args.get('descrizione')
        password=request.args.get('password')
        errore=int(request.args.get('errore'))

        ex_gara=GaraModel.find_by_nome(ex_nome)
        test=GaraModel.find_by_nome(nome)


        if ex_gara==None:
            return "non esiste", 400
        if password!=ex_gara.password:
            return "password no"
        if test is not None:
            return "name already taken"

        if errore<0:
            errore=-errore

        ex_gara.nome=nome
        ex_gara.descrizione=descrizione
        ex_gara.errore=errore
        ex_gara.save_to_db()
        return "la gara e' stata modificata", 200
