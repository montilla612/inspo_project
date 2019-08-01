

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
        user_data = request.form
        print(user_data)
        user_mood = user_data ["mood"]
        print(user_mood)
        mood_quote = model.find_quote(user_mood)
        user_color = model.color(user_mood)
        print(user_color)
        print(mood_quote)
        return render_template("results.html", user_mood = user_mood, mood_quote = mood_quote, user_color = user_color) 

@app.route('/quiz', methods = ["GET", "POST"])
def quiz():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("quiz.html")
        
# @app.route('/quizresults', methods = ["GET", "POST"])

# def quizresults():
#     if request.method == "GET":
#         return render_template("quiz.html")
        
        

@app.route('/quizresults', methods = ["GET", "POST"])

def quizresults():
    if request.method == "GET":
        return render_template("quiz.html")
    else:
        return render_template("quizresults.html")




    # else:
    #     user_data = request.form
    #     print(user_data)
    #     user_answer1 = user_data("q1")
    #     print(user_answer1)
    #     user_answer2 = user_data("q2")
        
    #     user_answer3 = user_data("q3")
        
    #     user_answer4 = user_data("q4")
        
    #     user_answer5 = user_data("q5")
        
    #     user_answer6 = user_data("q6")
        
    #     user_answer7 = user_data("q7")
        
    #     user_answer8 = user_data("q8")
        
    #     user_answer9 = user_data("q9")
        
    #     user_answer10 = user_data("q10")
        
    #     total_points = model.find_pointsq1(user_answer1) + model.find_pointsq2(user_answer2) + model.find_pointsq3(user_answer3) + model.find_pointsq4(user_answer4) + model.find_pointsq5(user_answer5) + model.find_pointsq6(user_answer6) + model.find_pointsq7(user_answer7) + model.find_pointsq8(user_answer8) + model.find_pointsq9(user_answer9) + model.find_pointsq10(user_answer10) 
    #     if total_points > 15:
    #         return("You are depressed")
    #     elif total_points > 8 and total_points <= 14:
    #         return("You are ok")
    #     else:
    #         return("You are happy")
            
    #     return render_template("quizresults.html", user_answer1 = user_answer1, user_answer2 = user_answer2, user_answer3 = user_answer3, user_answer4 = user_answer4, user_answer5 = user_answer5, user_answer6 = user_answer6, user_answer7 = user_answer7, user_answer8 = user_answer8, user_answer9 = user_answer9, user_answer10 = user_answer10, total_points = total_points)
        
       
               
        
        
        
        
        
        
       


# @app.route('/happy', methods = ["GET", "POST"])
# def happy_result():
#     if request.method == "GET":
#         # user_data = request.form
#         # user_mood = ...
#         quote = model.find_quote("Happy")
#         gif = model.find_gif("Happy")
#         image = model.find_image("Happy")
#         return render_template("results.html", quote = quote, gif = gif, image = image)

# @app.route('/sad', methods = ["GET", "POST"])
# def sad_result():
#     if request.method == "GET":
#         quote = model.find_quote("Sad")
#         gif = model.find_gif("Sad")
#         image = model.find_image("Sad")
#         return render_template("results.html", quote = quote, gif = gif, image = image)
# @app.route('/angry', methods = ["GET", "POST"])
# def angry_result():
#     if request.method == "GET":
#         quote = model.find_quote("Angry")
#         gif = model.find_gif("Angry")
#         image = model.find_image("Angry")
#         return render_template("results.html", quote = quote, gif = gif, image = image)

# @app.route('/ambitious', methods = ["GET", "POST"])
# def ambitious_result():
#     if request.method == "GET":
#         quote = model.find_quote("Ambitious")
#         gif = model.find_gif("Ambitious")
#         image = model.find_image("Ambitious")
#         return render_template("results.html", quote = quote, gif = gif, image = image)

   
    # else:
        
    #     return render_template("results.html")
