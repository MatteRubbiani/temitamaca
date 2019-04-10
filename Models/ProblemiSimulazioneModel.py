from db import db
class ProblemiSimulazioneModel(db.Model):
    __tablename__="problemiSimulazione"

    id = db.Column(db.Integer, primary_key=True)
    simulazione_id=db.Column(db.Integer)
    problema_id=db.Column(db.Integer)
    tentativi=db.Column(db.Integer)
    risolto=db.Column(db.Boolean)
    tempo_risoluzione=db.Column(db.Integer)#secondi

    def __init__(self, id, simulazione_id, problema_id, tentativi, risolto, tempo_risoluzione):
        self.id=id
        self.simulazione_id=simulazione_id
        self.problema_id=problema_id
        self.tentativi=tentativi
        self.risolto=risolto
        self.tempo_risoluzione=tempo_risoluzione

    @classmethod
    def find_by_simulazione_id(cls, nome):
        a=ProblemiSimulazioneModel.query.filter_by(simulazione_id=nome)
        b=[]
        try:
            for i in a:
                b.append(i)

            return b
        except:
            return None

    @classmethod
    def delete_by_simulazione_id(cls, simulazione_id):
        problemi= ProblemiSimulazioneModel.query.filter_by(simulazione_id=simulazione_id)
        for i in problemi:
            i.delete_from_db()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
