import os
from datetime import datetime as dt 
from ratelimit import limits,sleep_and_retry
import subprocess 
import pdfAnalysis
import docAnalysis
import model 
import fileHashing
from flask_httpauth import HTTPBasicAuth,HTTPDigestAuth
from flask import request 
import fileHashing 

from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'AJKRO655RGGPEL'

if app.config['ENV']=='production':
	app.config.from_object('config.ProductionConfig')

elif app.config['ENV']=='development':
	app.config.from_object('config.DevelopmentConfig')

else:
	app.config.from_object('config.TestingConfig')
##basic authentication
auth = HTTPBasicAuth()

#digest authentication
#auth = HTTPDigestAuth()

##alloweed extensions
ALLOWED_EXTENSIONS = set(['txt', 'pdf','docm','docx'])

@auth.verify_password
def authenticate(username, password):
	
	if username and password:
		if username == 'roy' and password == 'roy' :
			return True
		else:
			
			return False
	return False

'''users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None'''
#and request.remote_addr=="30.25.50.20"


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''@app.route('/')

@limits(calls=4,period=15)
@sleep_and_retry 
def helloWorld():
	ip_addr=request.remote_addr
	return ip_addr'''


@app.route('/file-upload', methods=['POST'])
@limits(calls=15,period=15)
@sleep_and_retry 
@auth.login_required
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		now =dt.now().replace(microsecond=0)
		date=dt.isoformat(now)
		NewFilename=filename.rsplit('.',1)[0]+date+'.'+filename.rsplit('.',1)[1]
		path=os.path.join(app.config['UPLOADS'],NewFilename)
		print(type(path))
		file.save(path)

		# ----------------- return pdf scan -----------------

		if filename.rsplit('.',1)[1].lower()=="pdf":
			filehash=fileHashing.hashFile(path)
			database=model.get_db_connection(app.config["DB_NAME"])
			status=model.ifAlreadyFileHash(database,filehash)
			if status!=None:
				os.remove(path)
				return jsonify({'status':status})
			else: 
				state=getPdfStatus(path)
				model.insertHashFile(app.config["DB_NAME"],filehash,state)
				resp= jsonify({"status":state})
				resp.status_code=201
				os.remove(path)
				return resp 

		# ---------------------return docx scan--------------------

		if filename.rsplit('.',1)[1].lower()=="docm" or filename.rsplit('.',1)[1].lower()=="docx":
			filehash=fileHashing.hashFile(path)
			database=model.get_db_connection(app.config["DB_NAME"])
			status=model.ifAlreadyFileHash(database,filehash)
			if status!=None:
				os.remove(path)
				return jsonify({'status':status})
			else: 
				state=getWordStatus(path)
				model.insertHashFile(app.config["DB_NAME"],filehash,state)
				resp= jsonify({"status":state})
				resp.status_code=201
				os.remove(path)
				return resp 
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


def getPdfStatus(file):

	#if file is .pdf
	cmd=subprocess.Popen(["python3","/home/ayoub/devHacking/python/fileScan/pdfScan.py","-s",file],stdout=subprocess.PIPE)
	
	with open('/home/ayoub/devHacking/python/fileScan/jScript.txt',"w") as f:
		for line in cmd.stdout:
			f.write(line.decode("utf-8"))
	resp= pdfAnalysis.scanPDF()
	
	return resp 

def getWordStatus(file):
	#if file is .docx or .docm 
	resp=docAnalysis.docScan(file)
	
	return resp 


if __name__ == "__main__":
	app.run()

#fetchData(get_db_connection())
#print(app.config)
