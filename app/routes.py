

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
        quote = model.find_quote("Happy")
        gif = model.find_gif("happy")
        image = model.find_image("happy")
        return render_template("results.html", quote = quote, gif = gif, image = image)

@app.route('/sad', methods = ["GET", "POST"])
def sad_result():
    if request.method == "GET":
        quote = model.find_quote("Sad")
        gif = model.find_gif("sad")
        image = model.find_image("sad")
        return render_template("results.html", quote = quote, gif = gif, image = image)
@app.route('/angry', methods = ["GET", "POST"])
def angry_result():
    if request.method == "GET":
        quote = model.find_quote("Angry")
        gif = model.find_gif("angry")
        image = model.find_image("angry")
        return render_template("results.html", quote = quote, gif = gif, image = image)

@app.route('/ambitious', methods = ["GET", "POST"])
def ambitious_result():
    if request.method == "GET":
        quote = model.find_quote("Ambitious")
        gif = model.find_gif("ambitious")
        image = model.find_image("ambitious")
        return render_template("results.html", quote = quote, gif = gif, image = image)

   
    # else:
        
    #     return render_template("results.html")
