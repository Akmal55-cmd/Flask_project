from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Ahfaz"
    age = 20
    return render_template("home.html",name=name,age=age)
       
@app.route("/about")
def about():
    data = ["Bob","James","Jack","Ymir","Saif"]
    s = [{'name': "Ahfaz", 'age': 20, 'address':"Bhopal", 'marks': 83},{'name': "Mayur", 'age': 19, 'address':"Bhopal", 'marks': 85},{'name': "Neymar", 'age': 21, 'address':"Bhopal", 'marks': 90},{'name': "Allu", 'age': 24, 'address':"Bhopal", 'marks': 82}]
    return render_template("about.html",data=data, s=s)

@app.route("/contact")
def Contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)