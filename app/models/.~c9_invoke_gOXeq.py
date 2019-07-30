import random

ambitious = [ "Shoutout to the girls who put in major work. Who are up early ass hell for school/work. Girls that study. Grind. Who persevere & prioritize self worth/lov. Who rise above & hold it down even when they're falling apart, to the girls whopush harder.", "I used to think going to sleep late was cool. Till I realized wakin up early was the real boss shit.", "if you look at people in your circle and don't get inspired.then you don't have a circle, you have a cage", "shout out to everyone making progress that no one recognize", "Don't limit your challlenges. Challenge your limits!", "Yes it is going to be hard but it's going to be worth it!"
    ]
angry = [ "Speak when you are angry and you'll make the best speech you'll ever REGRET!!!", "Never let your emotions overpower your intelligence!!!", "Don't do something permanentely stupid just because you're temporarily upset!!", "Anger dosen't solve anything. It builds nothing, but it can destroy everything."]

sad = [ "Be strong because things will get better. It maybe stormy now but it never rains forever! ;)", "You are not allowed to let sadness ruin you. ;)", "It's not about forcing sadness it's about not leting sadness win. ;)", "Breathe it's only a bad day not a bad life. ;)", "I was sad but then I went beast mode! ;)", ]

happy = [ "Being NEVER goes out of style. :)", "Happiness is letting go of what you think your life is supposed to be. :)", 


]



random.shuffle(ambitious)
random.shuffle(sad)
random.shuffle(angry)
random.shuffle(happy)


def find_quote(mood):  
    if mood == "Ambitious":
        random.shuffle(ambitious)
        one_quote = ambitious[0]
        return one_quote
    elif mood == "Sad":
        random.shuffle(sad)
        one_quote = sad[0]
        return one_quote
    elif mood == "Happy":
        random.shuffle(happy)
        one_quote = happy[0]
        return one_quote
    elif mood == "Angry":
        random.shuffle(angry)
        one_quote = angry[0]
        return one_quote
    else:
        return "Sorry Try Again!"
    return find_quote(mood)
p
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
    
# print(ambitious[0])   

