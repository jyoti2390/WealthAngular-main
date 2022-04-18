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
    return "jyoti"


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

    return resreturn


@app.route('/user/add', methods=['POST'])
def newusr():
    cur =mysql.connection.cursor()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        usrEmail = json["userEmail"]
        usrPassword = json["userPassword"]
        usrName = json["userName"]
        usrPhoneNumber = json["userPhoneNumber"]
        usrAge = json["userAge"]
        imgsrc = json["imgSrc"]
        cur.execute(
    """INSERT INTO
        users (
            img_src,
            user_age,
            user_email,
            user_name,
            user_password,
            user_phone_number)
    VALUES (%s,%s,%s,%s,%s,%s)""", (imgsrc, usrAge, usrEmail, usrName, usrPassword, usrPhoneNumber))
        mysql.connection.commit()
        cur.execute("""SELECT * FROM users WHERE user_email=%s and user_password=%s""", (usrEmail, usrPassword))
        rv = cur.fetchall()
        for entry in rv:
            Result={}
            Result['userId']=entry[0]
            Result['userName']=entry[4]
            Result['userEmail']=entry[3]
            Result['userPassword']=entry[5]
            Result['userPhoneNumber']=entry[6]
            Result['userAge']=entry[2]
            Result['imgSrc']=entry[1]
            response=Result
        return jsonify(response)
    else:
        return 'Request not valid!'

@app.route('/signin', methods=['POST'])
# @secure.login_required
def signIn():
    cur =mysql.connection.cursor()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        usrEmail = json["userEmail"]
        usrPassword = json["userPassword"]
        cur.execute("""SELECT * FROM users WHERE user_email=%s and user_password=%s""", (usrEmail, usrPassword))
        rv = cur.fetchall()
        for entry in rv:
            Result={}
            Result['userId']=entry[0]
            Result['userName']=entry[4]
            Result['userEmail']=entry[3]
            Result['userPassword']=entry[5]
            Result['userPhoneNumber']=entry[6]
            Result['userAge']=entry[2]
            Result['imgSrc']=entry[1]
            response=Result
        return jsonify(response)
    else:
        return 'Request not valid!'
      #Get all match from history and funds table
     @app.route('/funds/join', methods=['GET'])
        def fundsalljoin():
          cur =mysql.connection.cursor()
          cur.execute("SELECT fund_name, fund_amc, fund_risk, fund_aum, fund_type, fund_nav, fund_mgr, fund_desc, img_src,fh1month, fh1year, fh_total FROM funds f ,fund_history h where f.fund_id = h.fund_id")
          rv = cur.fetchall()
          Results=[]
          for entry in rv: 
              Result={}
              if entry=='fund_name':
                Result['fundName']=rv[entry]
              elif entry=='fund_amc':
                Result['fundAmc']=rv[entry]
              elif entry=='fund_risk':
                Result['fundRisk']=rv[entry]
              elif entry=='fund_aum':
                Result['fundAum']=rv[entry]
              elif entry=='fund_type':
                Result['fundType']=rv[entry]
              elif entry=='fund_nav':
                Result['fundNav']=rv[entry]
              elif entry=='fund_mgr':
                Result['fundMgr']=rv[entry]
              elif entry=='fund_desc':
                Result['fundDesc']=rv[entry]
              elif entry=='img_src':
                Result['imgSrc']=rv[entry]
              elif entry=='fh1month':
                Result['fh1month']=rv[entry]
              elif entry=='fh1year':
                Result['fh1year']=rv[entry]
              elif entry=='fh_total':
                Result['fhTotal']=rv[entry]
                Results.append(Result)
        response=Results
        resreturn=app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )
#Api for find fundRisk Priority
@app.route('/fundsRisk/Priority/<fundrisk>')
def fundsRiskPriority(fundrisk):
  cur =mysql.connection.cursor()
  cur.execute("SELECT * from funds where fund_risk=%s",[fundrisk])
  rv = cur.fetchall()
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
  response=Result
  return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True) 
