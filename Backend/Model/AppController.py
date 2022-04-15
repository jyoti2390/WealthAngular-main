from distutils.log import debug
from flask_cors import CORS
import MySQLdb
# import Funds
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json
from json import loads
from flask import request


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'wealthmanagement'

mysql = MySQL(app)
secure = HTTPBasicAuth()

@secure.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'user' and password == 'admin':
            return True
    else:
      return False
    return False

@app.route('/funds/all')
def ViewFunds():
    cur =mysql.connection.cursor()
    funds=cur.execute("SELECT * FROM `funds`;")
    # fun=Funds.Funds
    if(funds>0):
        Result=cur.fetchall()
        res=[]
        for i in range(len(Result)):
            cur={}
            cur['fundId']=Result[i][0]
            cur['fundName']=Result[i][1]
            cur['fundAmc']=Result[i][2]
            cur['fundRisk']=Result[i][3]
            cur['fundType']=Result[i][4]
            cur['fundAum']=Result[i][5]
            cur['fundNav']=Result[i][6]
            cur['fundMgr']=Result[i][7]
            cur['fundDesc']=Result[i][8]
            cur['imgSrc']=Result[i][9]
            res.append(cur)
        return jsonify(res)
    return "vikas"


@app.route('/fundAmc')
def FundAmc():
    cur =mysql.connection.cursor()
    funds=cur.execute("SELECT distinct fund_amc FROM funds;")
    if(funds>0):
        Result=cur.fetchall()
        return jsonify(Result)

@app.route('/fundsOrder')
def fundsOrder():
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds order by fund_name;")
    rv = cur.fetchall()
    Results=[]
    for entry in rv:
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )

    return resreturn

@app.route('/fundsRisk')
def fundsRisk():
    cur =mysql.connection.cursor()
    cur.execute("SELECT distinct fund_risk FROM funds;")
    rv = cur.fetchall() 
    Results=[]
    for row in rv: 
      Results.append(row[0])
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )

    return resreturn

@app.route('/fundsOrderByAum')
def fundsOrderByAum():
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds order by fund_aum;")
    rv = cur.fetchall() 
    Results=[]
    for entry in rv: 
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )

    return resreturn



@app.route('/funds/<fundname>')
def fundsbyinput(fundname):
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds where fund_amc=%s",[fundname])
    rv = cur.fetchall() 
    Results=[]
    for entry in rv:      
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )

    return resreturn

@app.route('/search/<fundname>')
def fundsbysearch(fundname):
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds where fund_amc like '%%%s%%'" %(fundname))
    rv = cur.fetchall() 
    Results=[]
    for entry in rv: 
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080') 



@app.route('/funds/<fundname>')
def fundsbyinput(fundname):
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds where fund_amc=%s",[fundname])
    rv = cur.fetchall() 
    Results=[]
    for entry in rv:      
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )

    return resreturn

@app.route('/search/<fundname>')
def fundsbysearch(fundname):
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds where fund_amc like '%%%s%%'" %(fundname))
    rv = cur.fetchall() 
    Results=[]
    for entry in rv: 
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080') 
