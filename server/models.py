from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80) )
    create_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime )
    serialized_rules = "-baked_goods.bakery" 
    
    # Define a one-to-many relationship with BakedGood
    baked_goods = db.relationship('BakedGood', backref='bakery')


    def __repr__(self):
        return f'<Bakery {self.name}>'

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float )
    Bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    create_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<BakedGood {self.name}>'