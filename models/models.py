from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy( ) #objeto de la clase SQLAlchemy

class Radionovela(db.Model):
    __tablename__="Radionovelas"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    archivo=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(200),nullable=True)
    serie=db.Column(db.String(100),nullable=True)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "archivo": self.archivo,
        "description": self.description,
        "serie": self.serie,
        "date_created": self.date_created.strftime("%Y-%m-%d") if self.date_created else None
    }

class Visitas(db.Model):
    __tablename__="visitas"
    id=db.Column(db.Integer,primary_key=True)
    fecha=db.Column(db.DateTime,default=lambda: datetime.utcnow().date())
