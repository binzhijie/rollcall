def white_txt(name,leirong):
    file = open(name, "w", encoding="ANSI")
    file.write(str(leirong))
    file.close()