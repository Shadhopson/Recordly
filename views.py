from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def redirect():
    return "redirecting..."

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "Toggle Favorite, or delete!"
    else:
        return render_template("main.html")

@app.route('/favorite', methods=['GET','POST'])
def favorite():
    if request.method == 'POST':
        return "Toggle Favorite"
    else:
        return render_template("favorite.html") 

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login')
def login():
    return render_template("login.html",my_string="Wheee!", my_list = [0,1,2,3,4,5]) 

if __name__ =='__main__':
    app.run(debug=True)
