import json
from collections import OrderedDict

import pandas as pd
from flask import Flask, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    studios = db.Column(db.String(255), nullable=True)
    producers = db.Column(db.String(255), nullable=False)
    winner = db.Column(db.Boolean, default=False)

def populate_database(data):
    for _, row in data.iterrows():
        movie = Movie(
            year=row['year'],
            title=row['title'],
            studios=row['studios'],
            producers=row['producers'],
            winner=True if row['winner'] == 'yes' else False
        )
        db.session.add(movie)
    db.session.commit()

@app.route('/producers/intervals', methods=['GET'])
def get_producer_intervals():
    # Recuperar os vencedores do banco de dados
    winners = Movie.query.filter_by(winner=True).all()
    if not winners:
        return jsonify({"error": "No winners found"}), 404

    # Criar um dicionário para armazenar intervalos de prêmios por produtor
    producer_intervals = {}
    for movie in winners:
        producers = [p.strip() for p in movie.producers.split(",")]
        for producer in producers:
            if producer not in producer_intervals:
                producer_intervals[producer] = []
            producer_intervals[producer].append(movie.year)

    # Calcular os intervalos
    intervals = []
    for producer, years in producer_intervals.items():
        if len(years) > 1:
            years.sort()
            for i in range(len(years) - 1):
                intervals.append(OrderedDict({
                    "producer": producer,
                    "interval": years[i + 1] - years[i],
                    "previousWin": years[i],
                    "followingWin": years[i + 1]
                }))

    if not intervals:
        return jsonify({"error": "No producers with multiple wins found"}), 404

    # Ordenar os intervalos em ordem crescente
    sorted_intervals = sorted(intervals, key=lambda x: x['interval'])

    # Separar dois menores e dois maiores intervalos
    min_producers = sorted_intervals[:2]  # Dois menores intervalos
    max_producers = sorted(intervals, key=lambda x: x['interval'], reverse=True)[:2]  # Dois maiores intervalos

    # Garantir a saída com campos ordenados usando JSON puro
    result = OrderedDict({
        "min": min_producers,
        "max": max_producers
    })

    return Response(
        json.dumps(result, indent=4),
        content_type="application/json"
    )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        data = pd.read_csv('movies.csv', delimiter=';')
        populate_database(data)
    app.run(debug=True)
