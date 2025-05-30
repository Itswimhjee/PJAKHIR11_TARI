from .. import db

class Tari(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    asal = db.Column(db.String(100), nullable=False)

    @staticmethod
    def get_all():
        return Tari.query.all()

    @staticmethod
    def get_by_id(id):
        return Tari.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
