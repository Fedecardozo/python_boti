import random

titulos_termotanques = [
    "⚾Mega liquidación de termotanque Señorial y Escorial⚽",
    "🌐Los mejores precios en termotanques electricos y a gas🌐",
    "🕌Ultimo stock en termotanques señorial y Escorial de fábrica en rebaja🕌",
    "🗺Stock exclusivo en termotanques electricos y a gas con garantía 🗺",
    "💈Precios accesibles en termotanques señorial y Escorial💈",
    "🧨Mega ofertas en termotanques señorial y Escorial 🧨",
    "✨stock limitado de termotanque eléctrico y a gas en rebaja✨",
    "🍞Ofertas imperdible en termotanques entrada superior e inferior 🍞",
    "🧊termotanques señorial y Escorial,  todos los litrajes🧊",
    "♣Liquidamos ultimos termotanques electricos y a gas♣",
    "🎰Super precios en termotanques señorial y Escorial de fabrica🎰",
    "⚾MEGA LIQUIDACIÓN DE TERMOTANQUE SEÑORIAL Y ESCORIAL⚽",
    "🌐LOS MEJORES PRECIOS EN TERMOTANQUES ELECTRICOS Y A GAS🌐",   
    "🕌ULTIMO STOCK EN TERMOTANQUES SEÑORIAL Y ESCORIAL DE FÁBRICA EN REBAJA🕌",
    "🗺STOCK EXCLUSIVO EN TERMOTANQUES ELECTRICOS Y A GAS CON GARANTÍA 🗺",
    "💈PRECIOS ACCESIBLES EN TERMOTANQUES SEÑORIAL Y ESCORIAL💈",
    "🧨MEGA OFERTAS EN TERMOTANQUES SEÑORIAL Y ESCORIAL 🧨",
    "✨STOCK LIMITADO DE TERMOTANQUE ELÉCTRICO Y A GAS EN REBAJA✨",
    "🍞OFERTAS IMPERDIBLE EN TERMOTANQUES ENTRADA SUPERIOR E INFERIOR 🍞",
    "🧊TERMOTANQUES SEÑORIAL Y ESCORIAL, TODOS LOS LITRAJES🧊",
    "♣LIQUIDAMOS ULTIMOS TERMOTANQUES ELECTRICOS Y A GAS♣",
    "🎰SUPER PRECIOS EN TERMOTANQUES SEÑORIAL Y ESCORIAL DE FABRICA🎰",
    "🏆TERMOTANQUES SEÑORIAL Y ESCORIAL DE FÁBRICA EN OFERTA 🏆",
    "🌈🌈 súper oferta termotanque eléctrico y a gas natural 🌈🌈",
    "‼‼ Liquidación termotanques eléctricos y multigas‼‼",
    "💥💥 LOQUIDAMOS TERMOTANQUES ELÉCTRICOS Y MULTIGAS💥💥",
    "🍄❤ termotanque eléctrico y a gas natural en Oferta❤🍄",
    "✨✨ TERMOTANQUES ELÉCTRICOS Y MULTIGAS A BUEN PRECIO CONSULTAR✨✨",
    "🌈🌈 SÚPER OFERTA TERMOTANQUE ELÉCTRICO Y A GAS NATURAL 🌈🌈",
    "‼‼ LIQUIDACIÓN TERMOTANQUES ELÉCTRICOS Y MULTIGAS ‼‼",
    "🍄❤ TERMOTANQUE ELÉCTRICO Y A GAS NATURAL EN OFERTA ❤🍄",
    "🕌ultimo stock en termotanques señorial y escorial de fábrica en rebaja🕌",
    "🎰super precios en termotanques señorial y escorial de fabrica🎰",
    "🏆termotanques señorial y escorial de fábrica en oferta 🏆",
    # "❎❎TERMOTANQUES VENTAS POR MAYOR Y MENOR  Escorial señorial❎❎",
    # "🌀🌀TERMOTANQUES VENTAS POR MAYOR Y MENOR ESCORIAL SEÑORIAL🌀🌀",
    # "🌐🌐termotanques señorial escorial Ventas por mayor y menor🌐🌐",
    # "👻👻TERMOTANQUES señorial escorial electronico multigas VENTA POR MAYOR Y MENOR👻👻",
    # "🌊🌐LIQUIDAMOS TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO Y MULTIGAS 🌐🌊",
    # "🔱🌀APROVECHE OFERTA LIMITADA termotanques señorial escorial 🌀⚜",
    # "🌀🔱APROVECHE OFERTAS LIMITADAS termotanques señorial escorial electronico multigas 🔱🌀",
    # "🌀🌀liquidamos termotanques señorial escorial electronico y multigas 🌀🌀",
    # "🌀🌀últimas unidades termotanques señorial escorial electronico multiga 🌀🌀",
    # "🔱🔱termotanques señorial escorial precios por mayor y menor 🔱🔱",
    # "❇🌐señorial escorial liquidamos termotanques electronico y multigas 🌐❇",
    # "👻🔱precios imperdibles Termotanques señorial escorial electronico multigas NUEVOS 👻🔱",
    # "💫💫OFERTAS EXCLUSIVAS TERMOTANQUES ESCORIAL SEÑORIAL PRECIOS IMPERDIBLES💫💫",
    # "🚿🚿PROMOCIONES TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO Y MULTIGASS🚿🚿",
    # "💧💧OPORTUNIDAD IMPERDIBLE TERMOTANQUES ESCORIAL SEÑORIAL 💧💧",
    # "🚿💧HASTA AGOTAR STOCK TERMOTANQUES ESCORIAL SEÑORIAL 💧🚿",
    # "🌊🌊TERMOTANQUES ESCORIAL Y SEÑORIAL OPORTUNIDAD UNICA🌊🌊",
    # "🌊🌊termotanques escorial y señorial oportunidad única🌊🌊",
    # "🚿💧hasta agotar stock termotanques escorial señorial 💧🚿",
    # "💧💧oportunidad imperdible termotanques escorial señorial 💧💧",
    # "🚿🚿promociones termotanques señorial escorial electronico y a gas🚿🚿",
    # "💫💫ofertas exclusivas termotanques escorial señorial precios imperdibles💫💫",
    # "💫💫Ofertas EXCLUSIVAS TERMOTANQUES ESCORIAL SEÑORIAL PRECIOS IMPERDIBLES💫💫",
    # "🚿🚿Promociones TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO Y MULTIGAS🚿🚿",
    # "💧💧Oportunidad IMPERDIBLE TERMOTANQUES ESCORIAL SEÑORIAL 💧💧",
    # "🚿💧Hasta Agotar STOCK TERMOTANQUES ESCORIAL SEÑORIAL 💧🚿",
    # "🌊🌊Termontanques ESCORIAL Y SEÑORIAL OPORTUNIDAD UNICA🌊🌊",
    # "🌊🌊Termotanques escorial y señorial oportunidad única🌊🌊",
    # "🚿💧Hasta Agotar stock termotanques escorial señorial 💧🚿",
    # "💧💧Oportunidad!! imperdible termotanques escorial señorial 💧💧",
    # "🚿🚿Promociones!! termotanques señorial escorial electronico y a gas🚿🚿",
    # "💫💫Ofertas!! exclusivas termotanques escorial señorial precios imperdibles💫💫",
    # "🍁💫TERMOTANQUES Eléctricos Multigas Señorial Escorial NUEVOS CON garantía LIQUIDAMOS 🍁✨️",
    # "👻🔱PRECIOS IMPERDIBLES TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO MULTIGAS NUEVOS 👻🔱",
    # "❇🌐señorial escorial liquidamos termotanques electronico y multigas 🌐❇",
    # "❇🌐SEÑORIAL ESCORIAL LIQUIDAMOS TERMOTANQUES ELECTRONICO Y MULTIGAS 🌐❇",
    # "🔱🔱TERMOTANQUES SEÑORIAL ESCORIAL PRECIOS POR MAYOR Y MENOR 🔱🔱",
    # "🌀🌀ÚLTIMAS UNIDADES TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO MULTIGA 🌀🌀",
    # "🌀🌀LIQUIDAMOS TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO Y MULTIGAS 🌀🌀",
    # "🌀🔱APROVECHE OFERTAS LIMITADAS TERMOTANQUES SEÑORIAL ESCORIAL ELECTRONICO MULTIGAS 🔱🌀",
    # "☀☀LIQUIDAMOS TERMOTANQUES SEÑORIAL ESCORIAL NUEVOS OFERTA!!☀☀",
    # "🔥🔥TERMOTANQUES ELECTRONICO MULTIGAS SEÑORIAL ESCORIAL NUEVOS VENTA POR MAYOR Y MENOR🔥🔥",
    # "🌎🌎VENTA MINORISTA Y MAYORISTA TERMOTANQUES ELECTRONICO MULTIGAS 🌎🌎",
    # "💥💥VENTA POR MAYOR Y MENOR TERMOTANQUES ELECTRONICO MULTIGAS 💥💥",
    # "🌟🌟TERMOTANQUES ELECTRONICO MULTIGAS SEÑORIAL ESCORIAL NUEVOS CON GARANTIA 🌟🌟",
    # "☀☀liquidamos termotanques señorial escorial nuevos oferta!!☀☀",
    # "🔥🔥termotanques electronico multigas señorial escorial nuevos venta por mayor y menor🔥🔥",
    # "🌎🌎venta minorista y mayorista termotanques electronico multigas 🌎🌎",
    # "💥💥venta por mayor y menor termotanques electronico multigas 💥💥",
    # "🌟🌟termotanques electricos multigas señorial escorial nuevos con garantia 🌟🌟",
    # "❎❎TERMOTANQUES VENTAS POR MAYOR Y MENOR  Escorial señorial❎❎",
    # "🌀🌀TERMOTANQUES VENTAS POR MAYOR Y MENOR ESCORIAL SEÑORIAL🌀🌀",
    # "🌐🌐termotanques señorial escorial Ventas por mayor y menor🌐🌐",
    # "👻👻TERMOTANQUES señorial escorial electricos multigas VENTA POR MAYOR Y MENOR👻👻",
    # "🌊🌐LIQUIDAMOS TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO Y MULTIGAS 🌐🌊",
    # "🔱🌀APROVECHE OFERTA LIMITADA termotanques señorial escorial 🌀⚜",
    # "🌀🔱APROVECHE OFERTAS LIMITADAS termotanques señorial escorial electricos multigas 🔱🌀",
    # "🌀🌀liquidamos termotanques señorial escorial electricos y multigas 🌀🌀",
    # "🌀🌀últimas unidades termotanques señorial escorial electricos multiga 🌀🌀",
    # "🔱🔱termotanques señorial escorial precios por mayor y menor 🔱🔱",
    # "❇🌐señorial escorial liquidamos termotanques electricos y multigas 🌐❇",
    # "👻🔱precios imperdibles Termotanques señorial escorial electricos multigas NUEVOS 👻🔱",
    # "💫💫OFERTAS EXCLUSIVAS TERMOTANQUES ESCORIAL SEÑORIAL PRECIOS IMPERDIBLES💫💫",
    # "🚿🚿PROMOCIONES TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO Y MULTIGASS🚿🚿",
    # "💧💧OPORTUNIDAD IMPERDIBLE TERMOTANQUES ESCORIAL SEÑORIAL 💧💧",
    # "🚿💧HASTA AGOTAR STOCK TERMOTANQUES ESCORIAL SEÑORIAL 💧🚿",
    # "🌊🌊TERMOTANQUES ESCORIAL Y SEÑORIAL OPORTUNIDAD UNICA🌊🌊",
    # "🌊🌊termotanques escorial y señorial oportunidad única🌊🌊",
    # "🚿💧hasta agotar stock termotanques escorial señorial 💧🚿",
    # "💧💧oportunidad imperdible termotanques escorial señorial 💧💧",
    # "🚿🚿promociones termotanques señorial escorial electricos y a gas🚿🚿",
    # "💫💫ofertas exclusivas termotanques escorial señorial precios imperdibles💫💫",
    # "💫💫Ofertas EXCLUSIVAS TERMOTANQUES ESCORIAL SEÑORIAL PRECIOS IMPERDIBLES💫💫",
    # "🚿🚿Promociones TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO Y MULTIGAS🚿🚿",
    # "💧💧Oportunidad IMPERDIBLE TERMOTANQUES ESCORIAL SEÑORIAL 💧💧",
    # "🚿💧Hasta Agotar STOCK TERMOTANQUES ESCORIAL SEÑORIAL 💧🚿",
    # "🌊🌊Termontanques ESCORIAL Y SEÑORIAL OPORTUNIDAD UNICA🌊🌊",
    # "🌊🌊Termotanques escorial y señorial oportunidad única🌊🌊",
    # "🚿💧Hasta Agotar stock termotanques escorial señorial 💧🚿",
    # "💧💧Oportunidad!! imperdible termotanques escorial señorial 💧💧",
    # "🚿🚿Promociones!! termotanques señorial escorial electricos y a gas🚿🚿",
    # "💫💫Ofertas!! exclusivas termotanques escorial señorial precios imperdibles💫💫",
    # "🍁💫TERMOTANQUES Eléctricos Multigas Señorial Escorial NUEVOS CON garantía LIQUIDAMOS 🍁✨️",
    # "👻🔱PRECIOS IMPERDIBLES TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO MULTIGAS NUEVOS 👻🔱",
    # "❇🌐señorial escorial liquidamos termotanques electricos y multigas 🌐❇",
    # "❇🌐SEÑORIAL ESCORIAL LIQUIDAMOS TERMOTANQUES ELECTRICO Y MULTIGAS 🌐❇",
    # "🔱🔱TERMOTANQUES SEÑORIAL ESCORIAL PRECIOS POR MAYOR Y MENOR 🔱🔱",
    # "🌀🌀ÚLTIMAS UNIDADES TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO MULTIGA 🌀🌀",
    # "🌀🌀LIQUIDAMOS TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO Y MULTIGAS 🌀🌀",
    # "🌀🔱APROVECHE OFERTAS LIMITADAS TERMOTANQUES SEÑORIAL ESCORIAL ELECTRICO MULTIGAS 🔱🌀",
    # "☀☀LIQUIDAMOS TERMOTANQUES SEÑORIAL ESCORIAL NUEVOS OFERTA!!☀☀",
    # "🔥🔥TERMOTANQUES ELECTRICO MULTIGAS SEÑORIAL ESCORIAL NUEVOS VENTA POR MAYOR Y MENOR🔥🔥",
    # "🌎🌎VENTA MINORISTA Y MAYORISTA TERMOTANQUES ELECTRICO MULTIGAS 🌎🌎",
    # "💥💥VENTA POR MAYOR Y MENOR TERMOTANQUES ELECTRICO MULTIGAS 💥💥",
    # "🌟🌟TERMOTANQUES ELECTRICO MULTIGAS SEÑORIAL ESCORIAL NUEVOS CON GARANTIA 🌟🌟",
    # "☀☀liquidamos termotanques señorial escorial nuevos oferta!!☀☀",
    # "🔥🔥termotanques electricos multigas señorial escorial nuevos venta por mayor y menor🔥🔥",
    # "🌎🌎venta minorista y mayorista termotanques electricos multigas 🌎🌎",
    # "💥💥venta por mayor y menor termotanques electricos multigas 💥💥",
    # "🌟🌟termotanques electricos multigas señorial escorial nuevos con garantia 🌟🌟"
    ]

titulos_aires = ["🌀🌀LIQUIDAMOS AIRES ACONDICIONADOS SAMSUNG HITACHI TCL ENOVA PHILCO 🌀🌀",
                "❎❎AIRES ACONDICIONADOS OFERTAS!! HASTA AGOTAR STOCK❎❎",
                "🌀🌀AIRES ACONDICIONADOS LIQUIDAMOS HASTA AGOTAR STOCK🌀🌀",
                "🌐🌐ULTIMAS UNIDADES AIRES ACONDICIONADOS SAMSUNG HITACHI TCL ENOVA PHILCO...🌐🌐",
                "👻👻AIRES ACONDICIONADOS SAMSUNG HITACHI TCL ENOVA PHILCO OFERTA IMPERDIBLE👻👻",
                "🌊🌐LIQUIDAMOS AIRES ACONDICIONADOS LAS MEJORES MARCAS AL MEJOR PRECIO 🌐🌊",
                "🔱🌀APROVECHE OFERTA LIMITADA AIRES ACONDICIONADOS 🌀⚜",
                "🌀🌀liquidamos aires acondicionados samsung hitachi tcl enova philco 🌀🌀",
                "❎❎aires acondicionados ofertas!! hasta agotar stock❎❎",
                "🌀🌀aires acondicionados liquidamos hasta agotar stock🌀🌀",
                "🌐🌐ultimas unidades aires acondicionados samsung hitachi tcl enova philco...🌐🌐",
                "👻👻aires acondicionados samsung hitachi tcl enova philco oferta imperdible👻👻",
                "🌊🌐liquidamos aires acondicionados las mejores marcas al mejor precio 🌐🌊",
                "🔱🌀aproveche oferta limitada aires acondicionados 🌀⚜",
                "🔱🔱AIRES ACONDICIONADOS OFERTAS EXCLUSIVAS🔱🔱",
                "💫💫Ofertas Exclusivas Aires Acondicionados Eco Invert Split Portatil💫💫",
                "💫💫Aproveche Liquidacion de Aires Acondicionados Eco Invert 💫💫",
                "💫💫ofertas exclusivas aires acondicionados eco invert split portatil💫💫",
                "💫💫aproveche liquidacion de aires acondicionados eco invert 💫💫",
                "💫💫OFERTAS EXCLUSIVAS AIRES ACONDICIONADOS ECO INVERT SPLIT PORTATIL💫💫",
                "💫💫APROVECHE LIQUIDACION DE AIRES ACONDICIONADOS ECO INVERT 💫💫",
                "💫💫OFERTAS EXCLUSIVAS AIRES ACONDICIONADOS ECO INVERT SPLIT PORTATIL💫💫",
                "💫💫APROVECHE LIQUIDACION DE AIRES ACONDICIONADOS ECO INVERT 💫💫"]

titulos_tanques = [
    "❎❎COMBOS TANQUES DE AGUA VENTAS POR MAYOR Y MENOR  Rotoplas forteplas❎❎",
    "🌀🌀COMBOS TANQUES DE AGUA VENTAS POR MAYOR Y MENOR ROTOPLAS FORTEPLAS🌀🌀",
    "🌐🌐combo tanques de agua forteplas rotoplas Ventas por mayor y menor🌐🌐",
    "👻👻COMBOS TANQUES DE AGUA forteplas rotoplas 2, 3 y 4 capas VENTA POR MAYOR Y MENOR👻👻",
    "🌊🌐LIQUIDAMOS COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS Y 🌐🌊",
    "🔱🌀APROVECHE OFERTA LIMITADA combo tanques de agua forteplas rotoplas 🌀⚜",
    "🌀🔱APROVECHE OFERTAS LIMITADAS combo tanques de agua forteplas rotoplas 2, 3 y 4 capas 🔱🌀",
    "🌀🌀liquidamos combo tanques de agua forteplas rotoplas 2, 3 y 4 capas y 🌀🌀",
    "🌀🌀últimas unidades combo tanques de agua forteplas rotoplas 2, 3 y 4 capas🌀🌀",
    "🔱🔱combo tanques de agua forteplas rotoplas precios por mayor y menor 🔱🔱",
    "❇🌐forteplas rotoplas liquidamos combo tanques de agua 2, 3 y 4 capas y 🌐❇",
    "👻🔱precios imperdibles Termotanques forteplas rotoplas 2, 3 y 4 capas NUEVOS 👻🔱",
    "💫💫OFERTAS EXCLUSIVAS COMBOS TANQUES DE AGUA ROTOPLAS FORTEPLAS PRECIOS IMPERDIBLES💫💫",
    "🚿🚿PROMOCIONES COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS YS🚿🚿",
    "💧💧OPORTUNIDAD IMPERDIBLE COMBOS TANQUES DE AGUA ROTOPLAS FORTEPLAS 💧💧",
    "🚿💧HASTA AGOTAR STOCK COMBOS TANQUES DE AGUA ROTOPLAS FORTEPLAS 💧🚿",
    "🌊🌊COMBOS TANQUES DE AGUA ROTOPLAS Y FORTEPLAS OPORTUNIDAD UNICA🌊🌊",
    "🌊🌊combo tanques de agua rotoplas y forteplas oportunidad única🌊🌊",
    "🚿💧hasta agotar stock combo tanques de agua rotoplas forteplas 💧🚿",
    "💧💧oportunidad imperdible combo tanques de agua rotoplas forteplas 💧💧",
    "🚿🚿promociones combo tanques de agua forteplas rotoplas 2, 3 y 4 capas y a gas🚿🚿",
    "💫💫ofertas exclusivas combo tanques de agua rotoplas forteplas precios imperdibles💫💫",
    "💫💫Ofertas EXCLUSIVAS COMBOS TANQUES DE AGUA ROTOPLAS FORTEPLAS PRECIOS IMPERDIBLES💫💫",
    "🚿🚿Promociones COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS Y🚿🚿",
    "💧💧Oportunidad IMPERDIBLE COMBOS TANQUES DE AGUA ROTOPLAS FORTEPLAS 💧💧",
    "🚿💧Hasta Agotar STOCK COMBOS TANQUES DE AGUA ROTOPLAS FORTEPLAS 💧🚿",
    "🌊🌊Termontanques ROTOPLAS Y FORTEPLAS OPORTUNIDAD UNICA🌊🌊",
    "🌊🌊Termotanques rotoplas y forteplas oportunidad única🌊🌊",
    "🚿💧Hasta Agotar stock combo tanques de agua rotoplas forteplas 💧🚿",
    "💧💧Oportunidad!! imperdible combo tanques de agua rotoplas forteplas 💧💧",
    "🚿🚿Promociones!! combo tanques de agua forteplas rotoplas 2, 3 y 4 capas y a gas🚿🚿",
    "💫💫Ofertas!! exclusivas combo tanques de agua rotoplas forteplas precios imperdibles💫💫",
    "🍁💫COMBOS TANQUES DE AGUA Rotoplas NUEVOS CON garantía LIQUIDAMOS 🍁✨️",
    "👻🔱PRECIOS IMPERDIBLES COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS NUEVOS 👻🔱",
    "❇🌐forteplas rotoplas liquidamos combo tanques de agua 2, 3 y 4 capas y 🌐❇",
    "❇🌐FORTEPLAS ROTOPLAS LIQUIDAMOS COMBOS TANQUES DE AGUA 2, 3 y 4 CAPAS Y 🌐❇",
    "🔱🔱COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS PRECIOS POR MAYOR Y MENOR 🔱🔱",
    "🌀🌀ÚLTIMAS UNIDADES COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS🌀🌀",
    "🌀🌀LIQUIDAMOS COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS Y 🌀🌀",
    "🌀🔱APROVECHE OFERTAS LIMITADAS COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS 2, 3 y 4 CAPAS 🔱🌀",
    "☀☀LIQUIDAMOS COMBOS TANQUES DE AGUA FORTEPLAS ROTOPLAS NUEVOS OFERTA!!☀☀",
    "🔥🔥COMBOS TANQUES DE AGUA 2, 3 y 4 CAPAS FORTEPLAS ROTOPLAS NUEVOS VENTA POR MAYOR Y MENOR🔥🔥",
    "🌎🌎VENTA MINORISTA Y MAYORISTA COMBOS TANQUES DE AGUA 2, 3 y 4 CAPAS🌎🌎",
    "💥💥VENTA POR MAYOR Y MENOR COMBOS TANQUES DE AGUA 2, 3 y 4 CAPAS 💥💥",
    "🌟🌟COMBOS TANQUES DE AGUA 2, 3 y 4 CAPAS FORTEPLAS ROTOPLAS NUEVOS CON GARANTIA 🌟🌟",
    "☀☀liquidamos combo tanques de agua forteplas rotoplas nuevos oferta!!☀☀",
    "🔥🔥combo tanques de agua 2, 3 y 4 capas forteplas rotoplas nuevos venta por mayor y menor🔥🔥",
    "🌎🌎venta minorista y mayorista combo tanques de agua 2, 3 y 4 capas 🌎🌎",
    "💥💥venta por mayor y menor combo tanques de agua 2, 3 y 4 capas 💥💥",
    "🌟🌟combo tanques de agua 2, 3 y 4 capas forteplas rotoplas nuevos con garantia 🌟🌟"]

titulos_cocinas = ["🌀🌀LIQUIDAMOS COCINAS CONVENCIONALES 🌀🌀",
                "❎❎COCINAS DE HOGAR OFERTAS!! HASTA AGOTAR STOCK❎❎",
                "🌀🌀COCINAS DE HOGAR LIQUIDAMOS HASTA AGOTAR STOCK🌀🌀",
                "🌐🌐ULTIMAS UNIDADES COCINAS CONVENCIONALES🌐🌐",
                "👻👻COCINAS CONVENCIONALES OFERTA IMPERDIBLE👻👻",
                "🌊🌐LIQUIDAMOS COCINAS CONVENCIONALES LAS MEJORES MARCAS AL MEJOR PRECIO 🌐🌊",
                "🔱🌀APROVECHE OFERTA LIMITADA COCINAS CONVENCIONALES 🌀⚜",
                "🌀🌀liquidamos cocinas convencionales 🌀🌀",
                "❎❎cocinas convencionales ofertas!! hasta agotar stock❎❎",
                "🌀🌀cocinas convencionales liquidamos hasta agotar stock🌀🌀",
                "🌐🌐ultimas unidades cocinas de hogar🌐🌐",
                "👻👻cocinas de hogar oferta imperdible👻👻",
                "🌊🌐liquidamos cocinas de hogar las mejores marcas al mejor precio 🌐🌊",
                "🔱🌀aproveche oferta limitada cocinas convencionales 🌀⚜",
                "🔱🔱COCINAS CONVENCIONALES OFERTAS EXCLUSIVAS🔱🔱",
                "💫💫Ofertas Exclusivas Cocinas Convencionales 💫💫",
                "💫💫Aproveche Liquidacion de Cocinas Convencionales 💫💫",
                "💫💫ofertas exclusivas cocinas convencionales💫💫",
                "💫💫aproveche liquidacion de cocinas convencionales💫💫",
                "💫💫OFERTAS EXCLUSIVAS COCINAS CONVENCIONALES 💫💫",
                "💫💫APROVECHE LIQUIDACION DE COCINAS CONVENCIONALES💫💫",
                "💫💫OFERTAS EXCLUSIVAS COCINAS CONVENCIONALES 💫💫",
                "💫💫APROVECHE LIQUIDACION DE COCINAS CONVENCIONALES 💫💫"]

titulos_microondas = ["🌀🌀LIQUIDAMOS MICROONDAS SAMSUNG BGH 🌀🌀",
                "❎❎MICROONDAS DE HOGAR OFERTAS!! HASTA AGOTAR STOCK❎❎",
                "🌀🌀MICROONDAS DE HOGAR LIQUIDAMOS HASTA AGOTAR STOCK🌀🌀",
                "🌐🌐ULTIMAS UNIDADES MICROONDAS SAMSUNG BGH🌐🌐",
                "👻👻MICROONDAS OFERTA IMPERDIBLE👻👻",
                "🌊🌐LIQUIDAMOS MICROONDAS LAS MEJORES MARCAS AL MEJOR PRECIO 🌐🌊",
                "🔱🌀APROVECHE OFERTA LIMITADA MICROONDAS 🌀⚜",
                "🌀🌀liquidamos microondas samsung bgh 🌀🌀",
                "❎❎microondas samsung bgh ofertas!! hasta agotar stock❎❎",
                "🌀🌀microondas samsung bgh liquidamos hasta agotar stock🌀🌀",
                "🌐🌐ultimas unidades microondas de hogar🌐🌐",
                "👻👻microondas de hogar oferta imperdible👻👻",
                "🌊🌐liquidamos microondas de hogar las mejores marcas al mejor precio 🌐🌊",
                "🔱🌀aproveche oferta limitada microondas samsung bgh 🌀⚜",
                "🔱🔱MICROONDAS OFERTAS EXCLUSIVAS🔱🔱",
                "🔥🔥Ofertas Exclusivas Microoondas Samsung Bhg 🔥🔥",
                "🔥🔥Aproveche Liquidacion de Microoondas Samsung Bhg 🔥🔥",
                "💫💫ofertas exclusivas microondas samsung bgh💫💫",
                "👻👻aproveche liquidacion de microondas samsung bgh👻👻",
                "👻👻OFERTAS EXCLUSIVAS MICROONDAS 👻👻",
                "💥💥APROVECHE LIQUIDACION DE MICROONDAS💥💥",
                "💥💥OFERTAS EXCLUSIVAS MICROONDAS 💥💥",
                "💫💫APROVECHE LIQUIDACION DE MICROONDAS 💫💫"]

def ObtenerTitulo(titulos):
    num = len(titulos) - 1
    indice = random.randint(0,num)
    return titulos[indice]

def GetTitulo(producto):
    prd = str.lower(producto)
    if(prd == "termotanques"):
        return titulos_termotanques
    elif(prd == "cocinas"):
        return titulos_cocinas
    elif(prd == "tanques"):
        return titulos_tanques
    elif(prd == "aires"):
        return titulos_aires
    elif(prd == "microondas"):
        return titulos_microondas
