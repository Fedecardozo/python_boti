Zonas1 = ["Acassu",
          "Abasto, bu",
          "Glew, bu",
          "Rafael calzada",
          "Paternal"]

Zonas2 = ["Adrog",
          "Aldo bonz",
          "Almagro, bu",
          "Arturo Segui",
          "Arturo Segui",
          "San Andres, bueno",
          "Ranelagh, bu",
          "Puerto Madero, bue"]

Zonas3 = ["La lucila, bu",
          "Alejandro korn",
          "Beccar, bu",
          "Caseros, bue",
          "Balvanera, bue",
          "Berisso, bu",
          "Hudson, bu",
          "Santa Maria, bueno",
          "Solano, bue"]

Zonas4 = ["Recoleta, bue",
          "Avellaneda",
          "Bella Vista, bu",
          "Castelar, bueno",
          "Barracas, bue",
          "Bosques, bu",
          "Budge, bue",
          "Tortuguitas"]

Zonas5 = ["San José, bu",
          "Retiro, buenos",
          "General Rodriguez",
          "Los Polvori",
          "Banfield, bu",
          "Benavidez, Bu",
          "Belgrano, bueno",
          "City Bell, bu",
          "Juan Allan"]

Zonas6 = ["El Talar, b",
          "San Vicente, Buenos",
          "Saavedra, bue",
          "Hurlingham, bu",
          "Berazategui",
          "Billinghur",
          "Ciudad Evi",
          "Boedo, bue"]

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

Zonas8 = ["Villa Adelina",
          "San Nicolas, buenos",
          "Marcos Paz, bue",
          "Maquinista Sav",
          "Burzaco",
          "Campana",
          "Ciudadela, buenos",
          "Chacarita, bue"]

Zonas9 = ["Etcheve",
          "Temperley",
          "San telmo, bu",
          "Merlo, bu",
          "Canning, bue",
          "Campo de mayo, bu"]

Zonas10 = ["Cogh",
           "La union",
           "Villa Balles",
           "Tristan Sua",
           "Velez Sarsfield, bu",
           "Paso del rey",
           "Mu'ñ'iz, bue",
           "Ca'ñ'uelas"]

Zonas11 = ["Colegiales",
           "Lanus, bu",
           "Villa de mayo, bu",
           "Turdera",
           "Versalles, bu",
           "Pontevedr",
           "Carlos Spe"]

Zonas12 = ["Del viso, bu",
           "El palomar, bu",
           "Constitu",
           "Los Hornos, bu",
           "Villa Lynch",
           "Valentin Alsi",
           "Villa Crespo",
           "Rafael Castillo, bu",
           "Olivos, bue"]

Zonas13 = ["Dique Luj",
           "Flores, Distrito",
           "Manuel B. Gonn",
           "Lomas de Zamora",
           "Villa del parque, bu",
           "Ramos Mejia, Bu",
           "Luj"]

Zonas14 = ["San Isidro, Bue",
           "Claypole, b",
           "Don Torcu",
           "Gonzalez Cat",
           "Floresta, bue",
           "Melchor Rom",
           "Longchamps, bu",
           "Villa devot",
           "Mariano acosta, bu"]

Zonas15 = ["Saenz Pe'ñ'a, bu",
           "General San Martin, bu",
           "Escobar, bu",
           "Gregorio de Lafer",
           "La Boca, bu",
           "Ringuelet",
           "Luis Guillon",
           "Villa Rosa, bue",
           "Parque Chacabuco, Di"]

Zonas16 = ["Villa General Mitre, Di",
           "San Antonio de Padua, Bu",
           "Jose C. Paz, bu",
           "Dock Sud",
           "Fatima, bue",
           "Haedo, buenos aire",
           "Liniers, Di",
           "Tolosa, Bu",
           "Malvinas Argentinas, bu",
           "Virreyes, bu",
           "Parque Chas"]

Zonas17 = ["Villa Dominico",
           "Villa Lugano, bu",
           "San Justo, bu",
           "Pilar, bue",
           "Domse",
           "Florida, bueno",
           "Isidro Casano",
           "Mataderos, bu",
           "Maximo Paz, bu",
           "Parque Patri"]

Zonas18 = ["Zelaya, bu",
           "Villa España",
           "Villa Lur",
           "Santa Rosa, Buenos",
           "San Fernando, Bue",
           "Don Bosco, Bu",
           "Garin, Bue",
           "Villa Elisa, bu",
           "Villa Urquiza, bu"]

Zonas19 = ["Ministro Rivad",
           "Villa Madero, bu",
           "Villa Fiori",
           "Villa Ortu",
           "Santos Lugares, bu",
           "San Miguel, buenos",
           "Don Orio",
           "General Pacheco, bu",
           "La reja, bu"]

Zonas20 = ["Monte Chingolo",
           "Villa Pueyr",
           "Tapiales",
           "Tigre, bue",
           "Grand Bourg, bu",
           "La tablada, bu"]

Zonas21 = ["Nueva Pompeya, Di",
           "Villa Garibaldi, B",
           "Monte Grande, bu",
           "Villa Sarmiento, bu",
           "Villa Real, bue",
           "Vicente Lopez, b",
           "Ezeiza, buenos aires",
           "Ingeniero Masch"]

Zonas22 = ["Libertad (Buenos Aires)",
           "Pereyra, bu",
           "Villa riac",
           "Villa Bosch",
           "Presidente Derq",
           "Nu'ñ'ez, bu",
           "Ezpe"]

Zonas23 = ["Palermo, bu",
           "Platanos, bu",
           "Villa Santa Rita, bu",
           "Florencio Varel"]

Zonas24 = ["Jose Leon Sua",
           "Lomas del Mirador, bu",
           "Parque Avella",
           "Quilmes",
           "Wilde, bu",
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
    elif(zona == 20):
        retorno = Zonas20
    elif(zona == 21):
        retorno = Zonas21
    elif(zona == 22):
        retorno = Zonas22
    elif(zona == 23):
        retorno = Zonas23
    elif(zona == 24):
        retorno = Zonas24 
    else:
        print("No existe esa zona")
        exit()          

    return retorno
