from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

HEROKU_DB_URL = ""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///diagnosis"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class DiagnosisCodeModel(db.Model):
    __tablename__ = 'diagnosis'

    id = db.Column(db.Integer, primary_key=True)
    cat_code = db.Column(db.String())
    dg_code = db.Column(db.Integer())
    full_code = db.Column(db.String())
    abb_des = db.Column(db.String())
    full_des = db.Column(db.String())
    title = db.Column(db.String())

    def __init__(self, cat_code, dg_code, full_code, abb_des, full_des, title):
        self.cat_code = cat_code
        self.dg_code = dg_code
        self.full_code = full_code
        self.abb_des = abb_des
        self.full_des = full_des
        self.title = title

    def __repr__(self):
        return f"<Diagnosis Code {self.title}>"


@app.route('/')
def hello_world():
    return render_template('api_docs.html')


@app.route('/dg_code', methods=['POST', 'GET'])
def handle_dg_codes():
    if request.method == 'POST':
        if 'cat_code' in request.args:
            cat_code = request.args['cat_code']
        else:
            return jsonify([
                {'error_message': 'cat_code field not provided'}
            ])
        if 'dg_code' in request.args:
            dg_code = request.args['dg_code']
        else:
            return jsonify([
                {'error_message': 'dg_code field not provided'}
            ])
        if 'full_code' in request.args:
            full_code = request.args['full_code']
        else:
            return jsonify([
                {'error_message': 'full_code field not provided'}
            ])
        if 'abb_des' in request.args:
            abb_des = request.args['abb_des']
        else:
            return jsonify([
                {'error_message': 'abb_des field not provided'}
            ])
        if 'full_des' in request.args:
            full_des = request.args['full_des']
        else:
            return jsonify([
                {'error_message': 'full_des field not provided'}
            ])
        if 'title' in request.args:
            title = request.args['title']
        else:
            return jsonify([
                {'error_message': 'title field not provided'}
            ])

        new_diagnosis = DiagnosisCodeModel(cat_code, dg_code, full_code, abb_des, full_des, title)
        db.session.add(new_diagnosis)
        db.session.commit()
        return {"message": f"Diagnosis record for {new_diagnosis.title} has been created successfully."}

    elif request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        all_diagnosis = DiagnosisCodeModel.query.paginate(page=page, per_page=20)
        results = [
            {
                "cat_code": diagnosis.cat_code,
                "dg_code": diagnosis.dg_code,
                "full_code": diagnosis.full_code,
                "abb_des": diagnosis.abb_des,
                "full_des": diagnosis.full_des,
                "title": diagnosis.title
            }
            for diagnosis in all_diagnosis.items]

        return {"count": len(results), "all_diagnosis": results, "message": "success"}


@app.route('/dg_code/<code_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_dg_code(code_id):
    diagnosis = DiagnosisCodeModel.query.get_or_404(code_id)

    if request.method == 'GET':
        response = {
            "cat_code": diagnosis.cat_code,
            "dg_code": diagnosis.dg_code,
            "full_code": diagnosis.full_code,
            "abb_des": diagnosis.abb_des,
            "full_des": diagnosis.full_des,
            "title": diagnosis.title
        }
        return {"message": "success", "diagnosis": response}

    elif request.method == 'PUT':
        if 'cat_code' in request.args:
            cat_code = request.args['cat_code']
        else:
            return jsonify([
                {'error_message': 'cat_code field not provided'}
            ])
        if 'dg_code' in request.args:
            dg_code = request.args['dg_code']
        else:
            return jsonify([
                {'error_message': 'dg_code field not provided'}
            ])
        if 'full_code' in request.args:
            full_code = request.args['full_code']
        else:
            return jsonify([
                {'error_message': 'full_code field not provided'}
            ])
        if 'abb_des' in request.args:
            abb_des = request.args['abb_des']
        else:
            return jsonify([
                {'error_message': 'abb_des field not provided'}
            ])
        if 'full_des' in request.args:
            full_des = request.args['full_des']
        else:
            return jsonify([
                {'error_message': 'full_des field not provided'}
            ])
        if 'title' in request.args:
            title = request.args['title']
        else:
            return jsonify([
                {'error_message': 'title field not provided'}
            ])

        diagnosis.cat_code = cat_code
        diagnosis.dg_code = dg_code
        diagnosis.full_code = full_code
        diagnosis.abb_des = abb_des
        diagnosis.full_des = full_des
        diagnosis.title = title
        db.session.add(diagnosis)
        db.session.commit()
        return {"message": f"Diagnosis record for {diagnosis.title} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(diagnosis)
        db.session.commit()
        return {"message": f"Diagnosis record for {diagnosis.title} successfully deleted."}


if __name__ == '__main__':
    app.run(debug=True)
