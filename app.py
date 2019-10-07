from flask import Flask, jsonify, request, json
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user':'postgres',
    'pw':'postgres',
    'db':'hrddatabase',
    'host':'localhost',
    'port':'5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#----------------------------------------------------------------------------------------------------------#
db.init_app(app)
from model.dbhrd import EmployeeData
from model.dbhrd import RequestData
from model.dbhrd import CreateHistory
from model.dbhrd import ComHistory
from model.dbhrd import JobData
#----------------------------------------------------------------------------------------------------------#
@app.route('/employee', methods=['GET'])
def getEmployee():
    try:
        employee = EmployeeData.query.all()
        return jsonify({'data':[emp.serialize() for emp in employee]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()

@app.route('/jobdesc', methods=['GET'])
def getJob():
    try:
        jobs = JobData.query.all()
        return jsonify({'data':[j.serialize() for j in jobs]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()

@app.route('/createreq', methods=['POST'])
def createRequest():
    body = request.json
    try:
        reqdata = RequestData(body['record_id'], body['process_id'], body['req_name'], body['req_npk'],
    body['req_position'], body['ob_name'], body['ob_position'], body['e_id'], body['e_name'], body['e_poscode'],
    body['e_position'], body['e_company'], body['e_costid'], body['e_costname'], body['e_perarea'], body['e_group'], 
    body['e_subgroup'], body['types'], body['poscode'], body['position'], body['costid'], body['costname'], body['dcostid'],
    body['dcostname'], body['company'], body['perarea'], body['persubarea'], body['em_type'], body['receiver'], body['em_date'], body['attach'], body['justif'])
        db.session.add(reqdata)
        db.session.commit()
        return jsonify({
            'message':'add request success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()


@app.route('/reqlist', methods=['GET'])
def requestList():
    try:
        reqlist = RequestData.query.all()
        return jsonify({'data':[rl.serialize() for rl in reqlist]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()


@app.route('/createHistory', methods=['POST'])
def createsHistory():
    body = request.json
    try:
        history = CreateHistory(body['creatorId'], body['creatorName'], body['record_id'], body['process_id'])
        db.session.add(history)
        db.session.commit()
        return jsonify({
            'message':'add history success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()

@app.route('/comHistory', methods=['POST'])
def comsHistory():
    body = request.json
    try:
        comment = ComHistory(body['task_id'], body['record_id'], body['created_at'], body['completed_at'], body['name'], body['position'], body['response'], body['comment'])
        db.session.add(comment)
        db.session.commit()
        return jsonify({
            'message':'add comment history success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()

@app.route('/cHistory/<id_>', methods=['GET'])
def getCHistory(id_):
    try:
        chis = CreateHistory.query.filter_by(creatorId=id_).all()
        return jsonify({
            'data':[ch.serialize() for ch in chis]
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()

@app.route('/comHistory', methods=['GET'])
def getComHistory():
    try:
        comhis = ComHistory.query.all()
        return jsonify({'data':[comh.serialize() for comh in comhis]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()