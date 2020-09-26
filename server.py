from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)

def write_to_csv(data):
	with open('database.csv', mode = 'a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message1 = data["message1"]
		message2 = data["message2"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message1,message2])

def write_to_file(data):
	with open('database.txt', mode = 'a') as database1:
		email = data["email"]
		subject = data["subject"]
		message1 = data["message1"]
		message2 = data["message2"]
		database1.write(f'\n{email}, {subject}, {message1}, {message2}')

@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			write_to_file(data)
			return redirect("/thankyou.html")
		except:
			return "Didn't save to Database."
	else:
		return "Something went wrong, try again!!"