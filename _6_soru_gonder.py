from imports import *

def oyunbitir(name,score,sorular):
    dicte = {}
    for z,i in enumerate(sorular):
        dicte[z] = i   
    modifiedname = name.replace("@","_at_").replace(".","_dot_")

    user_ref = db.reference(f"/users/{modifiedname}")
    dicte["tarih"] = {".sv":"timestamp"}
    dicte["puan"] = score
    user_ref.push(dicte)
    return True

