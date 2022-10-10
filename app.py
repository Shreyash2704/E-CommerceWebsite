from flask import Flask, session,render_template,request,session,redirect,url_for
#from flask_session import Session
#from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import db,User,New_Seller,Add_Product
from flask_migrate import Migrate
from datetime import timedelta
from base64 import b64encode, b64decode
import base64
app = Flask(__name__)
app.secret_key = "12344"
app.permanent_session_lifetime = timedelta(minutes=3)
#DATABASE_URL = postgres://ipdmmnuwjfvnjr:9c1d35df332b87bfc994a4487df6b118dfbc4d27b1f7e9615ca218ccae3aaf0b@ec2-52-72-34-184.compute-1.amazonaws.com:5432/d8limipiuuth3p
# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ipdmmnuwjfvnjr:9c1d35df332b87bfc994a4487df6b118dfbc4d27b1f7e9615ca218ccae3aaf0b@ec2-52-72-34-184.compute-1.amazonaws.com:5432/d8limipiuuth3p"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
#Session(app)
migrate = Migrate(app, db)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine("postgresql://postgres:Sahilm@123@localhost:5432/postgres")
#db = scoped_session(sessionmaker(bind=engine))

#model
'''

'''      

@app.route("/")
def index():
    if "user" in session:
       users = session["user"]
       return redirect(url_for("home"))
    return render_template("loginPage.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
       user = request.form['user']
       password = request.form['password']
       new_user = User.query.filter_by(UserName=user).first()
       if new_user is not None:
          if new_user.Password == password:
             session.permanent = True
             session["user"] = user
             users = session["user"]
             return render_template("homePage.html",Users=users)
          else:
             return "Worng password"
       else:
          return "user doesnt exist"
    if request.method == 'GET':
       if "user" in session:
          return redirect(url_for("home"))
       return render_template("loginPage.html")
@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":
       user = request.form['user']
       email = request.form['email']
       password = request.form['password'] 
       newuser = User(user,email,password)
       db.session.add(newuser)
       db.session.commit()
       return render_template("loginPage.html")
       
    if request.method == "GET":
       return render_template("signupPage.html")       
@app.route("/home",methods=['GET'])
def home():
    if request.method == "GET":
        if "user" in session:
           users = session["user"]
           product = Add_Product.query.all()
           seller = New_Seller.query.all()
           return render_template("homepage.html",Users = users,Product=product,Seller=seller)
        else:
           return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
@app.route("/purchase")
def purchase():
    user = session["user"]
    seller = New_Seller.query.all()
    products = Add_Product.query.all()
    return render_template("purchasePage.html",User = user,Product_info=products,Seller=seller) 
@app.route("/seller",methods=['GET','POST'])
def seller():
    if request.method=="GET":
       user = session["user"]
       seller = New_Seller.query.filter_by(seller_username=user).first()
       if seller is None:
          return render_template("sellerPage.html",User = user)  
       else:
          fname = seller.fname
          lname = seller.lname
          p_id = seller.seller_id
          product_info = Add_Product.query.filter_by(product_owner_id=p_id).all()
          return render_template("valid_Sellers_Page.html",FirstName=fname,LastName=lname,Product_info=product_info)       

    if request.method == "POST":
       id = New_Seller.query.all()
       nos_of_id = len(id)
       seller_id = int(nos_of_id) + 1
       seller_username = session["user"]
       fname = request.form['fname'] 
       lname = request.form['lname'] 
       email = request.form['email'] 
       ph_no = request.form['ph_no'] 
       adhaar_no = request.form['adhaar_no'] 
       pan_no = request.form['pan_no'] 
       address = request.form['address'] 
     
       new_seller = New_Seller(seller_id,seller_username,fname,lname,email,ph_no,adhaar_no,pan_no,address) 
       db.session.add(new_seller)
       db.session.commit()
       return redirect("/seller") 
@app.route("/add_product",methods=['GET','POST'])    
def add_product():
    if request.method == "POST":
       User = session["user"]
       seller = New_Seller.query.filter_by(seller_username = User).first()
       product_owner_id = seller.seller_id
       product_name = request.form["product_name"]
       product_price = request.form["price"]
       product_quantity = request.form["quantity_left"]
       product_img = request.files["img"]
       if product_img.filename == "":
                with open("default_bookcover.png" , "rb" ) as f:
                    data = f.read()
                    product_img = b64encode(data).decode("utf-8")
       else:        
                product_img = b64encode(product_img.read()).decode("utf-8")
       new_product = Add_Product(product_owner_id,product_name,product_price,product_quantity,product_img)
       db.session.add(new_product)
       db.session.commit()
       return redirect("/seller")
 
@app.route("/cart_page/<int:product_owner_id>",methods=['GET','POST']) 
def cart_page(product_owner_id):
    if "user" in session:
       if request.method == "POST":
       
          p_owner = New_Seller.query.filter_by(seller_id = product_owner_id).first()
          product = Add_Product.query.filter_by(product_owner_id = product_owner_id).first()
          return render_template('CartPage.html',Owner = p_owner,Product = product)
          
       if request.method == "GET":
          p_owner = New_Seller.query.filter_by(seller_id = product_owner_id).first()
          product = Add_Product.query.filter_by(product_owner_id = product_owner_id).first()
          return render_template('CartPage.html',Owner = p_owner,Product = product)
if __name__ == "__main__":
   app.run('host' == localhost, debug = True)

