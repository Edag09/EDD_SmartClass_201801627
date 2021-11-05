from ArbolB.ListCurseDouble import ListCurse

curse = ListCurse()


def pri():
    curse.addListCurse("101", "Matematica Basica 1", "7", "Ninguno", "True")
    curse.addListCurse("102", "Matematica Basica 2", "7", "101", "True")
    curse.addListCurse("103", "Matematica Intermedia 1", "10", "102, 33Crts", "True")
    curse.addListCurse("104", "Matematica Intermedia 2", "7", "103", "True")
    curse.addListCurse("105", "Matematica Intermedia 3", "7", "104", "True")

    print("Si")
    curse.showList()


pri()
