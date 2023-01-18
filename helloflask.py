from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)


app.config.update(
    
    SECRET_KEY='topsecret',
    # SQLAlchemy_DATABASE_URL='db://<username>:<password>@<server>/<database_name>'
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost/catlog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)
app.app_context().push()

@app.route("/")
def login():
    return render_template('login.html')

@app.route('/verify')
def verify():
    name = request.args.get("name")
    age = request.args.get("age")
    sal = request.args.get("sal")
    return render_template('welcome.html',name=name)

@app.route('/data')
def data():
    movie_list = ['autospy','neon demon','ghost in shell','john wick2','spiderman']
    return render_template('data.html',movie_list=movie_list)
    
@app.route('/table')
def table():
    movie_dict = {'autospy':2.14,
                  'neon demon':3.20
                  ,'ghost in shell':1.50
                  ,'john wick2':2.52
                  ,'spiderman':1.48}
    return render_template('table_data.html',movies=movie_dict,film='jatra')


@app.route('/macros')
def macros():
    movie_dict = {'autospy':2.14,
                  'neon demon':3.20
                  ,'ghost in shell':1.50
                  ,'john wick2':2.52
                  ,'spiderman':1.48}
    return render_template('macros.html',movies=movie_dict)




class Publication(db.Model):
    __tablename__='publication'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    
    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        return 'Publisher is {}'.format(self.name)
    
    
class Book(db.Model):
    __tablename__ ='book'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(500),nullable=False,index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format=db.Column(db.String(50))
    image = db.Column(db.String(100),unique=True)
    num_page = db.Column(db.Integer)
    # pub_date = db.Column(db.DateTime,default=datetime())
    
    # Relationship
    pub_id = db.Column(db.Integer,db.ForeignKey('publication.id'))
    
    
    def __init__(self,title,author,avg_rating,format,image,num_page,pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_page = num_page
        self.pub_id = pub_id
        
    def __repr__(self):
        return '{} by {}'.format(self.title,self.author)
    

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)