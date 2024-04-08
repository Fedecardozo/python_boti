def ObtenerScroll(producto):
    prd = str.lower(producto)
    if(prd == "termotanques" or prd == "tanques"):
        return 780
    elif(prd == "cocinas"):
        return 910
    elif(prd == "aires"):
        return 820
    
def ObtenerNameCarpeta(producto):
   return str.upper(producto)