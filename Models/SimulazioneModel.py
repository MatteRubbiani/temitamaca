from db import db
from Models.GaraModel import GaraModel
from Models.ProblemaModel import ProblemaModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
class SimulazioneModel(db.Model):
    __tablename__="simulazione"

    id = db.Column(db.Integer, primary_key=True)
    durata=db.Column(db.Integer) #numero di secondi
    gara_id=db.Column(db.Integer)
    inizio=db.Column(db.Integer)#secondi
    totale_punti=db.Column(db.Integer)
    nome=db.Column(db.String(30))
    started=db.Column(db.Boolean)


    def __init__(self, id, gara_id, inizio, durata, totale_punti, nome, started):
        self.id=id
        self.gara_id=gara_id
        self.inizio=inizio
        self.totale_punti=200
        self.durata=durata
        self.nome=nome
        self.started=started


    def create_problemi_simulazione(self):
        problemi=ProblemaModel.find_all_by_gara_id(self.gara_id)
        for i in problemi:
            a=ProblemiSimulazioneModel(None, self.id, i.id, 0, 0, False)
            a.save_to_db()

    @classmethod
    def find_by_nome(cls, nome):
        return SimulazioneModel.query.filter_by(nome=nome).first()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
