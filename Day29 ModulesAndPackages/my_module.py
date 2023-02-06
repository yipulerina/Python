data = {"name":"Nobody",
"Class":["Necromancer","Alchemist","Plunderer","Sage"],
"Specialty":["Infinite Magic", "Appraisal","Revive","No Limit"],
"greetings": "Hello, my slaves"
}

def get_specialty():
    """This function will return the characters specialty"""
    return data["Specialty"]

def get_greetings():
    """This function will return the characters intro/greetings"""
    return data["greetings"]