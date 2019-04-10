from db import db
from Models.GaraModel import GaraModel
class ProblemaModel(db.Model):
    __tablename__="problema"
    id = db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.Integer)
    gara_id=db.Column(db.Integer)
    valore=db.Column(db.Integer)
    soluzione=db.Column(db.Integer)


    def __init__(self, id, gara_id, numero, valore, soluzione):
        self.id=id
        self.numero=numero
        self.gara_id=gara_id
        self.valore=valore
        self.soluzione=soluzione

    @classmethod
    def find_all_by_gara_id(cls, gara_id):
        p=ProblemaModel.query.filter_by(gara_id=gara_id)
        a=[]
        for i in p:
            a.append(i)

        c= sorted(a, key=lambda x: x.numero)
        if c:
            return c
        return []

    @classmethod
    def find_by_id(cls, id):
        a=ProblemaModel.query.filter_by(id=id).first()
        if a:
            return a
        return None


    @classmethod
    def append_problema(cls, gara_id, valore, soluzione):
        gara=GaraModel.find_by_id(gara_id)
        if gara:
            problemi1=ProblemaModel.query.filter_by(gara_id=gara_id)
            problemi=[]
            for i in problemi1:
                problemi.append(i)
            if problemi==[]:
                numero=1
            else:
                problemi.sort(key=lambda x: x.numero)
                max=problemi[-1]
                numero=max.numero+1
            problema=ProblemaModel(None, gara.id, numero, int(valore), int(soluzione))
            problema.save_to_db()
            return problema
        return None
    @classmethod
    def modify_problema(cls, gara_id, numero, valore, soluzione):
        gara=GaraModel.find_by_id(gara_id)
        if gara:
            problema=ProblemaModel.query.filter_by(gara_id=gara_id, numero=numero).first()
            if problema:
                if valore:
                    problema.valore=valore
                if soluzione:
                    problema.soluzione=soluzione
                problema.save_to_db()
                return problema
        return None

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
