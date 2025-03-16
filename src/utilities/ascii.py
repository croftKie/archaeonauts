from art import text2art

def generate_title_art(line = None, type = "standard", space=0):
    if line == None:
        return
    
    return text2art(line, font=type, space=space, chr_ignore=True)