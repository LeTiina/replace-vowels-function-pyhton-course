
def ilman_vokaaleja(merkkijono):
    mjono = merkkijono
    mjono = mjono.replace("a","")
    mjono = mjono.replace("e","")
    mjono = mjono.replace("i","")
    mjono = mjono.replace("o","")
    mjono = mjono.replace("u","")
    mjono = mjono.replace("y","")
    mjono = mjono.replace("ä","")
    mjono = mjono.replace("ö","")
    mjono = mjono.replace("å","")
    return mjono

mmjono = "täma on esimerkki"
print(ilman_vokaaleja(mmjono))