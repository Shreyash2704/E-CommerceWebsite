from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
   __tablename__ = "user"
   id = db.Column(db.Integer, primary_key=True)
   UserName = db.Column(db.String , nullable=False)
   Email = db.Column(db.String, nullable=False)
   Password = db.Column(db.String, nullable=False)
   
   def __init__(self,UserName,Email,Password):
      self.UserName = UserName
      self.Email = Email
      self.Password = Password
      
class New_Seller(db.Model):
   __tablename__ = "seller_db"
   seller_id = db.Column(db.Integer, primary_key=True)
   seller_username = db.Column(db.String(30) , nullable=False)
   fname = db.Column(db.String , nullable=False )
   lname = db.Column(db.String , nullable=False)
   email = db.Column(db.String, nullable=False)
   ph_no = db.Column(db.String, nullable=False)
   adhaar_no = db.Column(db.String, nullable=False)
   pan_no = db.Column(db.String, nullable=False)
   address = db.Column(db.String, nullable=False)
   
   def __init__(self,seller_id,seller_username,fname,lname,email,ph_no,adhaar_no,pan_no,address):
      self.seller_id = seller_id
      self.seller_username = seller_username
      self.fname = fname
      self.lname = lname
      self.email = email
      self.ph_no = ph_no
      self.adhaar_no = adhaar_no
      self.pan_no = pan_no
      self.address = address

class Add_Product(db.Model):
      __tablename__ = "product_db" 
      id = db.Column(db.Integer, primary_key=True)
      product_owner_id = db.Column(db.Integer,nullable=False)
      product_name = db.Column(db.String, nullable=False)
      product_price = db.Column(db.Integer, nullable=False)
      product_quantity = db.Column(db.Integer, nullable=False)
      product_img = db.Column(db.String,nullable=False)
      
      def __init__(self,product_owner_id,product_name,product_price,product_quantity,product_img):
         self.product_owner_id = product_owner_id
         self.product_name = product_name
         self.product_price = product_price
         self.product_quantity = product_quantity
         self.product_img = product_img
    