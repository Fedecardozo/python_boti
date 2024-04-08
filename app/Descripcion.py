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