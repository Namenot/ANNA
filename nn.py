'''
in this library, there will just be the simple task
of executing a networkprocess
'''

def mxm():
    print("multiplying matrixes")

def net(l1: list, vs: list):
    l2 = []




mxm()


'''
l1 = {n1   size = 1 * n
      n2}

l2 = {n1   size = 1 * n
      n2
      n3}

v = {c1 c4 size = l1n * l2n
     c2 c5
     c3 c6}

l2 = v * l1

Haupt-Probleme :

- config:
    Ansatz :
        laedt die verschiedenen infos (L1, infos, verbindungen)

- organisation der Layer (zwischenspeichern der temporaeren layer + exec queue):
    Ansatz :
        Zwischenspeicher:
            jedes Layer wird zunaechst mit "None" belegt
            sollte ein None-layer abgefragt werden, wird der..... (pfad abfragen zur erschaffung des layers)
            layer werden waehrend der ausfuehrung etabliert und belegen nun nicht mehr None
        exec queue:
            wird on the go erschaffen
            heisst :
                es gibt ein verzeichnis mit der Info welches Layer mit welchem verknuepft ist (multiDimensional)
                dieses verzeichnis wird jedes mal angefordert, wenn ein layer ausgefuehrt wird
                darauf basierend wird jedes layer in die neue command-queue gepackt
                die cmd-queue ist multiDimensional um die activierten layer dem Ursprung zuordnen zu koenneq

- implementation von lernregeln:
    Ansatz:
        Logging:
            es muss ein Log funktion geben, welche mitschreibt, was alles wann passiert ist
        Abgleich:
            natuerlich muss der Output mit dem gewuenschten Output abgeglichen werden\
            und darauf ein Fitness lvl erstellt werden

- input stream :
    Ansatz:
        der Input muss streambar sein
        heisst, dass das ann haeufiger ausgefuehrt werden muss, mit einem sich aendernen L1
        dabei muss der Status der layer bestehen bleiben (!= None)

- laufzeit effizienz:
    Ansatz :
        im laufe des Projekts wird die MxM Multiplikation durch openCL ersetzt
