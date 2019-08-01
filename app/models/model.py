import random

Ambitious = [ "Shoutout to the girls who put in major work. Who are up early ass hell for school/work. Girls that study. Grind. Who persevere & prioritize self worth/lov. Who rise above & hold it down even when they're falling apart, to the girls whopush harder.", "I used to think going to sleep late was cool. Till I realized wakin up early was the real boss shit.", "if you look at people in your circle and don't get inspired.then you don't have a circle, you have a cage", "shout out to everyone making progress that no one recognize", "Don't limit your challlenges. Challenge your limits!", "Yes it is going to be hard but it's going to be worth it!"
    ]
Angry = [ "Speak when you are angry and you'll make the best speech you'll ever REGRET!!!", "Never let your emotions overpower your intelligence!!!", "Don't do something permanentely stupid just because you're temporarily upset!!", "Anger dosen't solve anything. It builds nothing, but it can destroy everything.", "You will not be punished for your anger, you will be punished by your anger."]

Sad = [ "Be strong because things will get better. It maybe stormy now but it never rains forever! ;)", "You are not allowed to let sadness ruin you. ;)", "It's not about forcing sadness it's about not leting sadness win. ;)", "Breathe it's only a bad day not a bad life. ;)", "I was sad but then I went beast mode! ;)", ]

Happy = [ "Being happy NEVER goes out of style. :)", "Happiness is letting go of what you think your life is supposed to be. :)", "It's fun to be happy. :)", "People look at you as a role model when you happy. :)","Happiness never decreases by being shared. :)" ]

Woke = [ "It's not the world that's cruel. It's the people in it.", "Life is not a problem to be solved, but a reality to be experienced.", "Dead people receive more flowers than the living ones because regret is stronger than gratitude.", "Listen to your possibilites not your insecurities", "OUTSIDERS know all your business from INSIDERS. ", "Be forgiving, Be understanding, But don't be a fool.", 
    
    
    ]


random.shuffle(Ambitious)
random.shuffle(Sad)
random.shuffle(Angry)
random.shuffle(Happy)
random.shuffle(Woke)


# def submit_emotion(mood):
#     if mood == "Happy":
#         return "Happy quote"
    


def find_quote(mood): 
    if mood.capitalize() == "Ambitious":
        random.shuffle(Ambitious)
        one_quote = Ambitious[0]
        return one_quote
    elif mood.capitalize() == "Sad":
        random.shuffle(Sad)
        one_quote = Sad[0]
        return one_quote
    elif mood.capitalize() == "Happy":
        random.shuffle(Happy)
        one_quote = Happy[0]
        return one_quote
    elif mood.capitalize() == "Angry":
        random.shuffle(Angry)
        one_quote = Angry[0]
        return one_quote
    elif mood.capitalize() == "Woke":
        random.shuffle(Woke)
        one_quote = Woke[0]
        return one_quote
        
        
    else:
        return "Sorry Try Again!"
    return find_quote(mood)


def color(mood):
    if mood.capitalize() == "Happy":
        mood_color = "yellow lighten-4"
        return color(mood)
    
    
        
    
    
    
    
    
# def find_gif(mood):
#     if mood == "Ambitious":
#       return "/static/ambitious-picture.gif"
#     elif mood == "Sad":
#         return "/static/sad-picture.gif"
#     elif mood == "sad":
#          return "/static/sad-picture.gif"
#     elif mood == "Happy":
#         return "/static/happy-picture.gif"
#     elif mood == "Angry":
#         return "/static/angry-picture.gif"
#     else:
#         return "Please type in a real emotion"
#     return find_quote(mood)

# def find_image(mood):
#     if mood == "Ambitious":
#       return "/static/ambitious-photo.jpg"
#     elif mood == "Sad":
#         return "/static/sad-photo.jpg"
#     elif mood == "sad":
#          return "/static/sad-photo.jpg"
#     elif mood == "Happy":
#         return "/static/happy-photo.jpg"
#     elif mood == "Angry":
#         return "/static/angry-photo.jpg"
#     else:
#         return "Please type in a real emotion"
#     return find_image(mood)
    
# print(ambitious[0])   

def find_pointsq1(answer):
    if answer == "q1-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q1-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter

def find_pointsq2(answer):
    if answer == "q2-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q2-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter
        
def find_pointsq3(answer):
    if answer == "q3-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q3-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 0
        return pointcounter

def find_pointsq4(answer):
    if answer == "q4-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q4-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 0
        return pointcounter
 
def find_pointsq5(answer):
    if answer == "q5-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q5-a2":
        pointcounter = 0
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter  
 
def find_pointsq6(answer):
    if answer == "q6-a1":
        pointcounter = 2
        return pointcounter
    if answer == "q6-a2":
        pointcounter = 0
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter   

def find_pointsq7(answer):
    if answer == "q7-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q7-a2":
        pointcounter = 2
        return pointcounter
    else:
        pointcounter = 1
        return pointcounter   
  
def find_pointsq8(answer):
    if answer == "q8-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q8-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter  

def find_pointsq9(answer):
    if answer == "q9-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q9-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter  

def find_pointsq10(answer):
    if answer == "q10-a1":
        pointcounter = 0
        return pointcounter
    if answer == "q10-a2":
        pointcounter = 1
        return pointcounter
    else:
        pointcounter = 2
        return pointcounter  

from app import app
from flask import render_template, request
from app.models import model, formopener

def depression_suggestion(total_points):
    if total_points >= 15: 
        return ("You may be depressed")
      
    elif total_points > 8 and total_points <= 14:
        return("You are doing ok")
    else:
        return("You are very happy")
    return 



