from db import db
class GaraModel(db.Model):
    __tablename__="gara"

    id = db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(30))
    descrizione=db.Column(db.String(200))
    password=db.Column(db.String(30))
    errore=db.Column(db.Integer)
    autore=db.Column(db.String(30))
    date=db.Column(db.Integer)


    def __init__(self, id, nome, descrizione, password, errore, autore, date):
        self.id=id
        self.nome=nome
        self.descrizione=descrizione
        self.password=password
        self.errore=errore
        self.autore=autore
        self.date=date

    @classmethod
    def find_by_id(cls, id):
        return GaraModel.query.filter_by(id=id).first()
    @classmethod
    def find_by_nome(cls, nome):
        return GaraModel.query.filter_by(nome=nome).first()
    @classmethod
    def find_all(cls):
        a=GaraModel.query.filter_by()
        b=[]
        for i in a:
            b.append(i)
        return b






    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
