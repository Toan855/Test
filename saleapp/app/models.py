from sqlalchemy import Column, Integer, String,Boolean,Float,ForeignKey
from app import db,app
from sqlalchemy.orm import relationship
class Category(db.Model):
    id=Column(Integer,primary_key=True, autoincrement= True)
    name= Column(String(50),unique=True)
    products = relationship('Product',backref='category',lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    price = Column(Float, default=0)
    description = Column(String(255),nullable=True)
    image = Column(String(100),nullable=True)
    category_id = Column(Integer,ForeignKey(Category.id),nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Table')
        # c3 = Category(name='Laptop')
        #
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()
