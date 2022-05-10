from flask import jsonify, request
from config import PORT, HOST, app, db
from models import Game_model, Game_schema, City_schema, Judge_schema, Team_schema, City_model, Team_model, Judge_model, \
    User_model

games_schema = Game_schema(many=True)
citys_schema = City_schema(many=True)
judges_schema = Judge_schema(many=True)
teams_schema = Team_schema(many=True)
game_schema = Game_schema()
city_schema = City_schema()
judge_schema = Judge_schema()
team_schema = Team_schema()


def get_all(schema, model):
    return jsonify(schema.dump(model.query.order_by(model.id.asc()).all())), 200


def create_city(data):
    if data["name"] and data["population"]:
        db.session.add(City_model(id=len(City_model.query.order_by(City_model.id.asc()).all()) + 1, name=data['name'],
                                  population=data['population']))
        db.session.commit()
        return jsonify(201)
    return jsonify({"error_id": 404})


def create_judge(data):
    if data["fio"] and data["city_id"]:
        db.session.add(Judge_model(id=len(Judge_model.query.order_by(Judge_model.id.asc()).all()) + 1, fio=data['fio'],
                                   city_id=data['city_id']))
        db.session.commit()
        return jsonify(201)
    return jsonify({"error_id": 404})


def create_team(data):
    if data["name"] and data["city_id"] and data["line_up"]:
        db.session.add(Team_model(id=len(Team_model.query.order_by(Team_model.id.asc()).all()) + 1, name=data['name'],
                                  city_id=data['city_id'], line_up=data['line_up']))
        db.session.commit()
        return jsonify(201)
    return jsonify({"error_id": 404})


def create_game(data):
    if data['team_owner_id'] and data['team_guest_id'] and data['city_id'] and data["judge_id"] and data["time"] and \
            data['date']:
        db.session.add(Game_model(id=len(Game_model.query.order_by(Game_model.id.asc()).all()) + 1,
                                  team_owner_id=data['team_owner_id'], team_guest_id=data['team_guest_id'],
                                  city_id=data['city_id'], judge_id=data["judge_id"], time=data["time"],
                                  date=data['date']))
        db.session.commit()
        return jsonify(201)
    return jsonify({"error_id": 404})


def change_city(data):
    city = City_model.query.filter_by(id=data["id"]).first()
    city.name = data["name"]
    city.population = data["population"]
    db.session.merge(city)
    db.session.flush()
    db.session.commit()
    return jsonify(202)


def change_judge(data):
    judge = Judge_model.query.filter_by(id=data["id"]).first()
    judge.fio = data["fio"]
    judge.city_id = data["city_id"]
    db.session.merge(judge)
    db.session.flush()
    db.session.commit()
    return jsonify(202)


def change_team(data):
    team = Team_model.query.filter_by(id=data["id"]).first()
    team.name = data["name"]
    team.city_id = data["city_id"]
    team.line_up = data["line_up"]
    db.session.merge(team)
    db.session.flush()
    db.session.commit()
    return jsonify(202)


def change_game(data):
    game = Game_model.query.filter_by(id=data["id"]).first()
    game.team_owner_id = data["team_owner_id"]
    game.team_guest_id = data["team_guest_id"]
    game.city_id = data["city_id"]
    game.judge_id = data["judge_id"]
    game.time = data["time"]
    game.date = data["date"]
    db.session.merge(game)
    db.session.flush()
    db.session.commit()
    return jsonify(202)


@app.route("/City/<int:id>", methods=['DELETE'])
def delete_city(id):
    try:
        data = games_schema.dump(Game_model.query.order_by(Game_model.id.asc()).all())
        for i in data:
            if i.get("city_id") == id:
                i["city_id"] = None
            change_game(i)
        data = judges_schema.dump(Judge_model.query.order_by(Judge_model.id.asc()).all())
        for i in data:
            if i.get("city_id") == id:
                i["city_id"] = None
            change_judge(i)
        data = teams_schema.dump(Team_model.query.order_by(Team_model.id.asc()).all())
        for i in data:
            if i.get("city_id") == id:
                i["city_id"] = None
            change_team(i)
        db.session.delete(db.session.get(City_model, id))
        db.session.commit()
        return jsonify(201)
    except Exception:
        return jsonify({"error_id": 400})


@app.route("/City/<int:id>", methods=['GET'])
def get_city(id):
    city = city_schema.dump(City_model.query.get(id))
    if city:
        return jsonify(city), 200
    return jsonify({"error_id": 404})


@app.route("/Judge/<int:id>", methods=['DELETE'])
def delete_judge(id):
    try:
        data = games_schema.dump(Game_model.query.order_by(Game_model.id.asc()).all())
        for i in data:
            if i.get("judge_id") == id:
                i["judge_id"] = None
            change_game(i)
        db.session.delete(db.session.get(Judge_model, id))
        db.session.commit()
        return jsonify(201)
    except Exception:
        return jsonify({"error_id": 400})


@app.route("/Judge/<int:id>", methods=['GET'])
def get_judge(id):
    judge = judge_schema.dump(Judge_model.query.get(id))
    if judge:
        return jsonify(judge), 200
    return jsonify({"error_id": 404})


@app.route("/Team/<int:id>", methods=['DELETE'])
def delete_team(id):
    try:
        data = games_schema.dump(Game_model.query.order_by(Game_model.id.asc()).all())
        for i in data:
            if i.get("team_owner_id") == id:
                i["team_owner_id"] = None
            if i.get("team_guest_id") == id:
                i["team_guest_id"] = None
            change_game(i)
        db.session.delete(db.session.get(Team_model, id))
        db.session.commit()
        return jsonify(201)
    except Exception:
        return jsonify({"error_id": 400})


@app.route("/Team/<int:id>", methods=['GET'])
def get_team(id):
    team = team_schema.dump(Team_model.query.get(id))
    if team:
        return jsonify(team), 200
    return jsonify({"error_id": 404})


@app.route("/Game/<int:id>", methods=['DELETE'])
def delete_game(id):
    try:
        db.session.delete(db.session.get(Game_model, id))
        db.session.commit()
        return jsonify(201)
    except Exception:
        return jsonify({"error_id": 400})


@app.route("/Game/<int:id>", methods=['GET'])
def get_game(id):
    game = game_schema.dump(Game_model.query.get(id))
    if game:
        return jsonify(game), 200
    return jsonify({"error_id": 404})


@app.route('/Game', methods=['GET', 'POST', 'PUT'])
def game_requests():
    if request.method == "GET":
        return get_all(games_schema, Game_model)
    elif request.method == "POST":
        return create_game(request.get_json())
    elif request.method == "PUT":
        return change_game(request.get_json())


@app.route('/City', methods=['GET', 'POST', 'PUT'])
def city_requests():
    if request.method == "GET":
        return get_all(citys_schema, City_model)
    elif request.method == "POST":
        return create_city(request.get_json())
    elif request.method == "PUT":
        return change_city(request.get_json())


@app.route('/Judge', methods=['GET', 'POST', 'PUT'])
def judge_requests():
    if request.method == "GET":
        return get_all(judges_schema, Judge_model)
    elif request.method == "POST":
        return create_judge(request.get_json())
    elif request.method == "PUT":
        return change_judge(request.get_json())


@app.route('/Team', methods=['GET', 'POST', 'PUT'])
def team_requests():
    if request.method == "GET":
        return get_all(teams_schema, Team_model)
    elif request.method == "POST":
        return create_team(request.get_json())
    elif request.method == "PUT":
        return change_team(request.get_json())


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    res = User_model.query.filter_by(login=data["login"], password=data["password"]).first()
    if res:
        return jsonify(200)
    return jsonify({"error_id": 404})


@app.route('/registration', methods=['POST'])
def create_new_user():
    data = request.get_json()
    db.session.add(User_model(id=len(User_model.query.order_by(User_model.id.asc()).all()) + 1, login=data['login'],
                              password=data['password']))
    db.session.commit()
    return jsonify(201)


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
