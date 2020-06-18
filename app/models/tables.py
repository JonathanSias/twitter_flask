# importando variavel db
from app import db

# criando tabela
# classe user
# herda de db.Model um modelo padrão
class User(db.Model):
    # nome da tabela no banco de dados
    # passa o nome no plural
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    # construtor com campos obrigatorios
    # quando o usuario for criado precisa conter todos os campos abaixo
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    
    # representaçao
    # forma como será visualizada a informaçao quando for feita busca no banco de dados
    def __repr__(self):
        return "<User %r>" % self.username

# classe post(tweet)
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    # id_user é um inteiro que referencia um id existente na tabela users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relacionamento para ver as informaçoes do usuario que fez o post
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)