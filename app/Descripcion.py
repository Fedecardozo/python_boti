Termotanques = """🏠SAN JORGE HOGAR 🏠
                
TERMOTANQUES eléctricos🔌
TERMOTANQUES a gas 🔥
Envíos a todo el país 🚛🌎
Entrega inmediata 🚚🌪
Garantia escrita de fabrica 📑y garantía de colocación🤝 de 48hs


☎📱💻 TU CONSULTA NO MOLESTA 💫"""


Aires = """🌿San Jorge Hogar 🌿
AIRES ACONDICIONADOS 💨

✔Todas las marcas, variedad de frigorías 
▫Hitachi
▫Surrey
▫Philco
▫Samsung
▫Midea Carrier
🚚Entrega inmediata 
💰Abona cuando recibe, aceptamos todos los medios de pago
🇦🇷Envios a todosel país"""

Tanques = """🌿SAN JORGE HOGAR 🌿

🩵TANQUES DE AGUA ROTOPLAS 🩵

Envíos a todo el país 🚛🌎
Entrega inmediata 🚚🌪
Garantia escrita de fabrica 📑


☎📱💻 SU CONSULTA NO MOLESTA 💫"""

Cocinas = """🏠SAN JORGE HOGAR🏠

Cocinas industriales y convencionales. 
▫ Escorial
▫ Florencia
▫ Morelli
▫ Usman
🎀Gas envasado🎀
🎀Gas natural 🎀
🎀Multigas🎀
Las mejores marcas 🏆 
Los mejores precios 💲 
Entregas inmediatas 🌪 
Envíos a todo el país 🇦🇷 

Su consulta no molesta 🌿"""

Microondas = """🍀SAN JORGE HOGAR🍀
Microondas 

✨Variedad de marcas 
▫Samsung
▫Likon
▫Siam
▫Daewoo
▫BGH 

💲Los mejores precios/varios métodos de pago 
✅Garantía oficial de fábrica 
🚚Entregas inmediatas puerta a puerta 
🇦🇷Entregas a todo el país 

‼Su consulta no molesta"""

Heladeras = """🏠SAN JORGE HOGAR🏠
Heladeras. 

🏆Las mejores marcas
🤍 Bambi 
🤍 Briket
🤍 Patrick
🤍 Drean
💲Los mejores precios 
✅Garantía directa de fábrica 
🌪Entregas inmediatas
🇦🇷Envios a todo el país"""

Secarropas = """🌿SAN JORGE HOGAR🌿

💥SECARROPAS💥

🏆Las mejores marcas
🤍 Kohinoor 
🤍 Drean
🤍 Codini 
💲Los mejores precios 
✅Garantía directa de fábrica 
🌪Entregas inmediatas
🇦🇷Envios a todo el país"""

SemiAutomaticos = """🌿SAN JORGE HOGAR🌿

Lavarropas 
✨Automáticos✨
✨Semiautomáticos✨

🪄Las mejores marcas 
❌Drean 
❌Codini
❌Columbia 
💲Los mejores precios 
✅Garantía directa de fábrica 
🌪Entregas inmediatas 
🇦🇷Envios a todo el país"""

def ObtenerDescripcion(producto):
    prd = str.lower(producto)
    if(prd == "termotanques"):
        return Termotanques
    elif(prd == "tanques"):
        return Tanques
    elif(prd == "cocinas"):
        return Cocinas
    elif(prd == "aires"):
        return Aires
    elif(prd == "microondas"):
        return Microondas
    elif(prd == "heladeras"):
        return Heladeras
    elif(prd == "secarropas"):
        return Secarropas
    elif(prd == "semiautomaticos" or prd == "combo_codini"):
        return SemiAutomaticos