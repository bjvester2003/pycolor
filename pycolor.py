def set_foreground_color_code(fgc):
    foreground_color_codes = {
        "black"	         :30,
        "red"	         :31,
        "green"	         :32,
        "yellow"	     :33,
        "blue"	         :34,
        "magenta"	     :35,
        "cyan"	         :36,
        "white"	         :37,
        "default"	     :39,
        "bright_black"	 :90,
        "bright_red"	 :91,
        "bright_green"	 :92,
        "bright_yellow"	 :93,
        "bright_blue"	 :94,
        "bright_magenta" :95,
        "bright_cyan"	 :96,
        "bright_white"	 :97,
    }
    
    return foreground_color_codes[fgc]
    
def set_background_color_code(bgc):
    background_color_codes = {
        "black"	         :40,
        "red"	         :41,
        "green"	         :42,
        "yellow"	     :43,
        "blue"	         :44,
        "magenta"	     :45,
        "cyan"	         :46,
        "white"	         :47,
        "default"	     :49,
        "bright_black"	 :100,
        "bright_red"	 :101,
        "bright_green"	 :102,
        "bright_yellow"	 :103,
        "bright_blue"	 :104,
        "bright_magenta" :105,
        "bright_cyan"	 :106,
        "bright_white"	 :107,
    }

    return background_color_codes[bgc]

def color_text(fgc="default", bgc="default", underline=False, msg="filler text"):
    reset_code = f"\033[0m"
    
    fgc = set_foreground_color_code(fgc)
    bgc = set_background_color_code(bgc)
    
    if underline == True:
        color_code = f"\033[4;{fgc};{bgc}m"
    elif underline == False:
        color_code = f"\033[{fgc};{bgc}m"
        
    modified_message = f"{color_code}{msg}{reset_code}"
    
    return modified_message