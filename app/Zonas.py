Zonas1 = ["Adrog",
          "Acassu",
          "Aldo bonz",
          "Almagro, bu",
          "Abasto, bu",
          "Glew, bu",
          "Arturo Segui",
          "Rafael calzada",
          "Paternal",
          "Guernica"]

Zonas2 = ["La lucila, bu",
          "Alejandro korn",
          "Beccar, bu",
          "Caseros, bue",
          "Balvanera, bue",
          "Berisso, bu",
          "Hudson, bu",          
          "San Andres, bueno",
          "Ranelagh, bu",
          "Puerto Madero, bue"]

Zonas3 = ["Recoleta, bue",
          "Bella Vista, bu",
          "Castelar, bueno",
          "Barracas, bue",
          "Bosques, bu",
          "Budge, bue",
          "Tortuguitas",
          "San José, bu",
          "Retiro, buenos",
          "Solano, bue"]

Zonas4 = [ "Lanus, bu",
           "Villa de mayo, bu",
           "Turdera",
           "Versalles, bu",
           "Pontevedr",
           "Carlos Spe",
           "Colegiales",
           "Campana",
           "Ciudadela, buenos",
           "Chacarita, bue"]

Zonas5 = ["Marcos Paz, bue",
          "Maquinista Sav",
          "General Rodriguez",
          "Los Polvori",
          "Banfield, bu",
          "Benavidez, Bu",
          "Burzaco",
          "Belgrano, bueno",
          "City Bell, bu",
          "Juan Allan"]

Zonas6 = ["El Talar, b",
          "San Vicente, Buenos",
          "Saavedra, bue",
          "Hurlingham, bu",
          "Villa Adelina",
          "Berazategui",
          "Billinghur",
          "Ciudad Evi",
          "Boedo, bue"
          "San Nicolas, buenos",]

Zonas7 = ["Jose marmol, Buenos",
          "Victoria, Buenos",
          "Sarandi, Buen",
          "San Cristobal, Bueno",
          "Ituzaingo, B",
          "Manzanares, Bueno",
          "Bernal, Bueno",
          "Boulogne, Bue",
          "Caballito, Bue",
          "Ensenada, Bueno"]

Zonas8 = ["San Isidro, Bue",
           "Claypole, b",
           "Don Torcu",
           "Gonzalez Cat",
           "Floresta, bue",
           "Melchor Rom",
           "Longchamps, bu",
           "Parque Patri",
           "Villa devot",
           "Mariano acosta, bu"]

Zonas9 = ["El pato",
          "Manuel B. Gonn",
          "Lomas de Zamora",
          "Temperley",
          "Villa riac",
          "Merlo, bu",
          "Luj",
          "Canning, bue",
          "Villa del parque, bu",
          "Ramos Mejia, Bu"]

Zonas10 = ["Cogh",
           "Etcheve",
           "La union",
           "Villa Balles",
           "Tristan Sua",
           "Velez Sarsfield, bu",
           "Paso del rey",
           "Muñiz, bue",
           "Cañuelas",
           "Campo de mayo, bu"]

Zonas11 = ["Saenz Peña, bu",
           "General San Martin, bu",
           "Flores, Distrito",
           "Escobar, bu",
           "Gregorio de Lafer",
           "La Boca, bu",
           "Ringuelet",
           "Luis Guillon",
           "Villa Rosa, bue",
           "Parque Chacabuco, Di"]

Zonas12 = ["Del viso, bu",
           "El palomar, bu",
           "Constitu",
           "Los Hornos, bu",
           "San telmo, bu",
           "Villa Lynch",
           "Valentin Alsi",
           "Villa Crespo",
           "Rafael Castillo, bu",
           "Olivos, bue"]

Zonas13 = ["Villa Dominico",
           "Villa Lugano, bu",
           "San Justo, bu",
           "Pilar, bue",
           "Domse",
           "Florida, bueno",
           "Isidro Casano",
           "Mataderos, bu",
           "Tigre, bue",
           "Maximo Paz, bu"]

Zonas14 = ["Zelaya, bu",
           "Villa España",
           "Villa Lur",
           "Santa Rosa, Buenos",
           "San Fernando, Bue",
           "Don Bosco, Bu",
           "Garin, Bue",
           "Tapiales",
           "monte castro, di",
           "Villa Elisa, bu"]

Zonas15 = ["Ministro Rivad",
           "Villa Madero, bu",
           "Villa Fiori",
           "Villa Ortu",
           "Santos Lugares, bu",
           "San Miguel, buenos",
           "Don Orio",
           "General Pacheco, bu",
           "La reja, bu",
           "Monte Chingolo"]

Zonas16 = ["Villa General Mitre, Di",
           "San Antonio de Padua, Bu",
           "Jose C. Paz, bu",
           "Dock Sud",
           "Fatima, bue",
           "Haedo, buenos aire",
           "Liniers, Di",
           "Tolosa, Bu",
           "Malvinas Argentinas, bu",
           "Virreyes, bu"]

Zonas17 = ["Nueva Pompeya, Di",
           "Villa Garibaldi, B",
           "Monte Grande, bu",
           "Villa Sarmiento, bu",
           "Libertad (Buenos Aires)",
           "Villa Real, bue",
           "Pereyra, bu",
           "Vicente Lopez, b",
           "Ezeiza, buenos aires",
           "Ingeniero Masch",
           "Grand Bourg, bu"]

Zonas18 = ["Jose Leon Sua",
           "Palermo, bu",
           "Platanos, bu",
           "Lomas del Mirador, bu",
           "Parque Avella",
           "Villa Santa Rita, bu",
           "Villa Bosch",
           "Presidente Derq",
           "Nuñez, bu",
           "Ezpe",
           "La tablada, bu"]

Zonas19 = ["Parque Chas",
           "Villa Pueyr",
           "Villa Urquiza, bu",
           "Quilmes",
           "Wilde, bu",
           "Dique Luj",
           "joaquin gor"
           "Florencio Varel",
           "Villa Solda",
           "Villa Luzu",
           "Gerli, bueno"]


def ObtenerZona(zona):
    retorno = "No existe esa zona"
    if(zona == 1):
        retorno = Zonas1
    elif(zona == 2):
        retorno = Zonas2
    elif(zona == 3):
        retorno = Zonas3
    elif(zona == 4):
        retorno = Zonas4
    elif(zona == 5):
        retorno = Zonas5
    elif(zona == 6):
        retorno = Zonas6
    elif(zona == 7):
        retorno = Zonas7
    elif(zona == 8):
        retorno = Zonas8
    elif(zona == 9):
        retorno = Zonas9
    elif(zona == 10):
        retorno = Zonas10
    elif(zona == 11):
        retorno = Zonas11
    elif(zona == 12):
        retorno = Zonas12
    elif(zona == 13):
        retorno = Zonas13
    elif(zona == 14):
        retorno = Zonas14
    elif(zona == 15):
        retorno = Zonas15
    elif(zona == 16):
        retorno = Zonas16
    elif(zona == 17):
        retorno = Zonas17
    elif(zona == 18):
        retorno = Zonas18
    elif(zona == 19):
        retorno = Zonas19
    else:
        print("No existe esa zona")
        exit()          

    return retorno
