from flask_restful import Resource, request
from Models.GaraModel import GaraModel

class CreateGara(Resource):

    def post (self):
        nome=request.args.get('nome')
        descrizione=request.args.get('descrizione')
        password=request.args.get('password')
        errore=int(request.args.get('errore'))

        ex_gara=GaraModel.find_by_nome(nome)

        if ex_gara:
            return "nome non disponibile", 400

        if errore<0:
            errore=-errore

        gara=GaraModel(None, nome, descrizione, password, errore)
        gara.save_to_db()
        return "la gara e' stata creata", 200

    def put (self):
        ex_nome=request.args.get("nome")
        nome=request.args.get('newNome')
        descrizione=request.args.get('descrizione')
        password=request.args.get('password')
        errore=request.args.get('errore')

        if ex_nome:
            ex_gara=GaraModel.find_by_nome(ex_nome)
            test=GaraModel.find_by_nome(nome)
        else:
            return "manca nome della classe", 400

        if ex_gara==None:
            return "non esiste", 400
        if password!=ex_gara.password:
            return "password no", 400
        if test is not None:
            return "name already taken", 400

        if nome:
            ex_gara.nome=nome
        if descrizione:
            ex_gara.descrizione=descrizione
        if errore:
            if errore<0:
                errore=-errore
            ex_gara.errore=int(errore)
        ex_gara.save_to_db()
        return "la gara e' stata modificata", 200


    def get (self):
        gara=request.args.get('nome')
        ex_gara=GaraModel.find_by_nome(gara)
        return ex_gara.errore
