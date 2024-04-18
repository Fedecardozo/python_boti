def ObtenerScroll(producto):
    prd = str.lower(producto)
    if(prd == "termotanques" or prd == "tanques"):
        return 780
    elif(prd == "cocinas"):
        return 910
    elif(prd == "aires" or prd == "heladeras" or prd == "secarropas"):
        return 820
    elif(prd == "microondas"):
        return 922
    elif(prd == "semiautomaticos" or prd == "combo_codini"):
        return 874
    
def ObtenerNameCarpeta(producto):
   return str.upper(producto)