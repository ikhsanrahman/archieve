from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

app.config['SECRET_KEY'] = 'thisissupposedtobesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///credit_score.db"

db=SQLAlchemy(app)




home=[{'hello': 'selamat datang'}]

class User(db.Model):
	__tablename__='user'
	user_id = db.Column(db.Integer, primary_key=True)
	Full_Name = db.Column(db.String(100))
	KTP_No = db.Column(db.Integer)
	Place_of_Birth = db.Column(db.String(100))
	Date_of_Birth = db.Column(db.Integer)
	Age = db.Column(db.Integer)
	Gender = db.Column(db.String(100))
	Address = db.Column(db.String(100))
	Province = db.Column(db.String(100))
	City = db.Column (db.String(100))
	Kecamatan = db.Column(db.String(100))
	Kelurahan = db.Column(db.String(100))
	Education = db.Column(db.String(100))
	Marital_Status = db.Column(db.String(100))
	Number_of_Children = db.Column(db.Integer)
	Religion = db.Column(db.String(100))
	Phone_Number = db.Column(db.Integer)

class Work_Information(db.Model):
	__tablename__ = 'workinformation'
	id=db.Column(db.Integer, primary_key=True)
	Position = db.Column(db.String(100))
	Employement_Status = db.Column(db.String(100))
	End_of_Contract = db.Column(db.String)

class Emergency_Contact(db.Model):
	__tablename__ = 'emergencycontact'
	id = db.Column(db.Integer, primary_key=True)
	Emergency_Contact_01 = db.Column(db.Integer, primary_key=True)
	Emergency_Contact_02 = db.Column(db.Integer, primary_key=True)
	Relationship_with_econ_01 = db.Column(db.String(100))

class Score :
	__tablename__='score'
	user_id = db.Column(db.Integer, primary_key=True)
	SFull_Name = db.Column(db.Integer)
	SKTP_No = db.Column(db.Integer)
	SPlace_of_Birth = db.Column(db.Integer)
	SDate_of_Birth = db.Column(db.Integer)
	SAge = db.Column(db.Integer)
	SGender = db.Column(db.Integer)
	SAddress = db.Column(db.Integer)
	SProvince = db.Column(db.Integer)
	SCity = db.Column (db.Integer)
	SKecamatan = db.Column(db.Integer)
	SKelurahan = db.Column(db.Integer)
	SEducation = db.Column(db.Integer)
	SMarital_Status = db.Column(db.Integer)
	SNumber_of_Children = db.Column(db.Integer)
	SReligion = db.Column(db.Integer)
	SPhone_Number = db.Column(db.Integer)


home=[{'hello': 'selamat datang'}]


class credit_score:
	pass



@app.route('/', methods = ['GET'])
def home_page():
	if request.method=='GET':
		import json
		return json.dumps(home)


@app.route('/fields', methods = ["POST"])
def addField():
	pass
	

@app.route('/input', methods = ["POST"])
def input():
	print ("test")
	try:
		print ("testlagi")
		if request.method == 'POST':
			print ("testlagi")
		#user=request.get_json()
			Full_Name = request.form['Full_Name']
			print ("test_2")
			if Full_Name:
				SFull_Name=10
			else :
				SFull_Name=0

			print ("ok")

			KTP_No = request.form['KTP_No']
			if KTP_No:
				SKTP_No=10
			else :
				SKTP_No=0
			print ("ok")
			Place_of_Birth = request.form ['Place_of_Birth']
			if Place_of_Birth:
				SPlace_of_Birth=10
			else :
				SPlace_of_Birth=0

			Date_of_Birth = request.form ['Date_of_Birth']
			if Date_of_Birth:
				SDate_of_Birth=10
			else :
				SDate_of_Birth=0

			print ("apa")
			Age = int(request.form.get ['Age'])
			if 21<Age<45 :
				SAge=10
			elif 18 < Age < 20 :
				SAge = 5
			elif Age >46 and Age <18 :
				SAge=0
			else :
				SAge=0
			print ("po")
			Gender = request.form [ 'Gender']
			if Gender:
				SGender=10
			else :
				SGender=0

			Address = request.form [ 'Address']
			if Address:
				SAddress=10
			else :
				SAddress=0

			Province = request.form [ 'Province']
			if Province:
				SProvince=10
			else :
				SProvince=0

			City = request.form [ 'City']
			if City:
				SCity=10
			else :
				SCity=0

			Kecamatan = request.form ['Kecamatan']
			if Kecamatan:
				SKecamatan=10
			else :
				SKecamatan=0

			Kelurahan = request.form['Kelurahan']
			if Kelurahan:
				SKelurahan=10
			else :
				SKelurahan=0

			print ("apa")
			Marital_Status = request.form [ 'Marital_Status']
			if Marital_Status:
				SMarital_Status=10
			elif Marital_Status=="Married":
				SMarital_Status=5
			elif Marital_Status=="single":
				SMarital_Status=5
			elif Marital_Status=="Divorce":
				SMarital_Status==0
			else :
				SMarital_Status=0

			print ("apa")
			Number_of_Children = int(request.form [ 'Number_of_Children'])
			if Number_of_Children==0:
				SNumber_of_Children=10
			elif Number_of_Children==1 :
				SNumber_of_Children=5
			elif Number_of_Children >1 :
				SNumber_of_Children=2.5
			else:
				SNumber_of_Children=0


			Religion = request.form [ 'Religion']
			if Religion:
				SReligion=10
			else :
				SReligion=0

			Phone_Number = request.form ['Phone_Number']
			if Phone_Number:
				SPhone_Number=10
			else :
				SPhone_Number=0

			print ("yes")


		#if not User.filter_by(Full_Name=Full_Name).first():
			new_user = User (Full_Name=Full_Name, KTP_No=KTP_No, Place_of_Birth=Place_of_Birth, Date_of_Birth=Date_of_Birth,
						 Age=Age, Gender=Gender, Address=Address, Province=Province, City=City, Kecamatan=Kecamatan,
						 Kelurahan=Kelurahan, Marital_Status=Marital_Status, Number_of_Children=Number_of_Children, 
						 Religion=Religion, Phone_Number=Phone_Number)
			db.session.add(new_user)
			db.session.commit()

			print("wew")

			new_score = Score (SFull_Name=SFull_Name, SKTP_No=SKTP_No, SPlace_of_Birth=SPlace_of_Birth, SDate_of_Birth=SDate_of_Birth,
						 SAge=SAge, SGender=SGender, SAddress=SAddress, SProvince=SProvince, SCity=SCity, SKecamatan=SKecamatan,
						 SKelurahan=SKelurahan, SMarital_Status=SMarital_Status, SNumber_of_Children=SNumber_of_Children, 
						 SReligion=Religion, SPhone_Number=Phone_Number)

			db.session.add(new_score)
			db.session.commit()

			
			

		#print (" you are success")
			return jsonify ({'messages ' : ' new user has been created and available'})
	except:
		return jsonify(msg="you have something wrong")




if __name__ == '__main__':
	app.run(port=0000, debug=True)