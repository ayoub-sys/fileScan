
from flask import Flask,request,render_template
from flask_ipban import IpBan


app = Flask(__name__)
if app.config['ENV']=='production':
	app.config.from_object('config.ProductionConfig')
ip_ban=IpBan(ban_seconds=12,ban_count=11)
ip_ban.init_app(app)
@app.route('/example', methods=['GET','POST'])
def example():
	
	if 1==1:
		ip_ban.add(ip=request.remote_addr)
		print(app.config)
	return "hello"


if __name__ == "__main__":
	print(app.config)
	app.run(host='0.0.0.0')

