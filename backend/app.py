# Aplicativo básico para cadastro e gerenciamento de biblioteca em Python

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos de dados
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer)

@app.route('/')
def home():
    return "API da Biblioteca funcionando"

@app.route('/livros', methods=['GET'])
def get_livros():
    livros = Livro.query.all()
    return jsonify([{'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor, 'ano': livro.ano} for livro in livros])

@app.route('/livros', methods=['POST'])
def add_livro():
    data = request.json
    novo_livro = Livro(titulo=data['titulo'], autor=data['autor'], ano=data.get('ano'))
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify({'id': novo_livro.id, 'titulo': novo_livro.titulo, 'autor': novo_livro.autor, 'ano': novo_livro.ano}), 201

@app.route('/livros/<int:livro_id>', methods=['GET'])
def get_livro(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    return jsonify({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor, 'ano': livro.ano})

@app.route('/livros/<int:livro_id>', methods=['PUT'])
def update_livro(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    data = request.json
    livro.titulo = data['titulo']
    livro.autor = data['autor']
    livro.ano = data.get('ano')
    db.session.commit()
    return jsonify({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor, 'ano': livro.ano})

@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    db.session.delete(livro)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)