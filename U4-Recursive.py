lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3",]
    ]
]

def recorrer_lista(item, nivel=0):
    for x  in item:
        if isinstance(x,list): ## SE fija si el elemento es de tipo lista
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)
recorrer_lista(lista)