# from app import apps
# from flask import render_template, request
# from app.models import model, formopener

# @app.route('/')
# @app.route('/index')
# # def index():
# #     return "hello world!"
# def index():
#     return render_template("index.html")
    
    
# @app.route('/results', methods = ["GET", "POST"])
# def results():
#     if request.method == "GET":
#         return render_template("index.html")
#     else:
       
#         return render_template("results.html")

from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/results', methods = ["GET", "POST"])
def results():
    if request.method == "GET":
        return render_template("index.html")
    else:
        output = request.form['mood']
        print(output)
        emotion_output = model.find_quote(output)
        return render_template("results.html", output = output, emotion_output = emotion_output)


@app.route('/happy', methods = ["GET", "POST"])
def happy_result():
    if request.method == "GET":
        quote = model.find_quote("happy")
        picture = model.find_image("happy")
        return render_template("results.html",  quote= quote, picture = picture )

@app.route('/sad', methods = ["GET", "POST"])
def sad_result():
    if request.method == "GET":
        quote = model.find_quote("sad")
        return render_template("results.html", quote = quote )

@app.route('/angry', methods = ["GET", "POST"])
def angry_result():
    if request.method == "GET":
        quote = model.find_quote("angry")
        return render_template("results.html", quote = quote )

@app.route('/ambitious', methods = ["GET", "POST"])
def ambitious_result():
    if request.method == "GET":
        quote = model.find_quote("ambitious")
        return render_template("results.html", quote = quote )

   
    # else:
        
    #     return render_template("results.html")
        
        
        
# words = request.form['string']re
#         print(words)
#         reversed_word = model.reverse(words)
#         print(reversed_word)
#         return render_template("results.html", words=words, reversed_word = reversed_word)