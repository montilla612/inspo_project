import random

ambitious = [ "Shoutout to the girls who put in major work. Who are up early ass hell for school/work. Girls that study. Grind. Who persevere & prioritize self worth/lov. Who rise above & hold it down even when they're falling apart, to the girls whopush harder.", "I used to think going to sleep late was cool. Till I realized wakin up early was the real boss shit.", "if you look at people in your circle and don't get inspired.then you don't have a circle, you have a cage", "shout out to everyone making progress that no one recognize", "Don't limit your challlenges. Challenge your limits!", "Yes it is going to be hard but it's going to be worth it!"
    ]
angry = [ "Speak when you are angry and you'll make the best speech you'll ever REGRET!!!", "Never let your emotions overpower your intelligence!!!", "Don't do something permanentely stupid just because you're temporarily upset!!", "Anger dosen't solve anything. It builds nothing, but it can destroy everything."]

sad = [ "Be strong because things will get better. It maybe stormy now but it never rains forever! ;)", "You are not allowed to let sadness ruin you. ;)", "It's not about forcing sadness it's about not leting sadness win ;)", "Breathe it's only a bad day not a bad life ;)", "I was sad but then I went beast mode ;)"]






random.shuffle(ambitious)

def find_quote(mood):  
    if mood == "Ambitious":
       return "I WANT MORE SOOOOOO I'M ABOUT TO DO MORE..."
    elif mood == "ambitious":
        return  "I WANT MORE SOOOOOO I'M ABOUT TO DO MORE..."
    elif mood == "Sad":
         return "Sometimes you need to take a break from everyone and spend time alone, to experience, appteciate and love yourself."
    elif mood == "sad":
        return "Sometimes you need to take a break from everyone and spend time alone, to experience, appteciate and love yourself."
    elif mood == "Happy":
        return "Being happy never goes out of style"
    elif mood == "happy":
        return "Being happy never goes out of style"
    elif mood == "Angry":
        return "For every minute you remain angry, you give up sixty seconds of peace of mind"
    elif mood == "angry":
        return  "For every minute you remain angry, you give up sixty seconds of peace of mind"
    else:
        return "Sorry Try Again!"
    return find_quote(mood)

print(ambitious[0])   

