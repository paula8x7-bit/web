# Textos del bloque de trabajo a turnos (castellano). Cada dato lleva su fuente al final de la página.

SRC = {
    "chellappa": ("Chellappa SL y cols. Daytime eating prevents internal circadian misalignment and glucose intolerance in night work. Science Advances, 2021.", "https://doi.org/10.1126/sciadv.abg9910"),
    "gupta": ("Gupta CC y cols. Altering meal timing to improve cognitive performance during simulated nightshifts. Chronobiology International, 2019.", "https://doi.org/10.1080/07420528.2019.1676256"),
    "grant": ("Grant CL y cols. Timing of food intake during simulated night shift impacts glucose metabolism. Chronobiology International, 2017.", "https://doi.org/10.1080/07420528.2017.1335318"),
    "grosser": ("Grosser L y cols. Exploring circadian and meal timing impacts on cortisol during simulated night shifts. Sleep, 2026.", "https://doi.org/10.1093/sleep/zsaf249"),
    "phoi": ("Phoi YY y cols. Understanding chrononutrition for managing shift workers' health: a narrative review. Medical Journal of Australia, 2026.", "https://doi.org/10.5694/mja2.70324"),
    "drake": ("Drake C y cols. Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed. Journal of Clinical Sleep Medicine, 2013.", "https://doi.org/10.5664/jcsm.3170"),
    "eastman": ("Eastman CI y cols. Dark goggles and bright light improve circadian rhythm adaptation to night-shift work. Sleep, 1994.", "https://doi.org/10.1093/sleep/17.6.535"),
    "smith": ("Smith MR, Fogg LF, Eastman CI. Practical interventions to promote circadian adaptation to permanent night shift work. Journal of Biological Rhythms, 2009.", "https://doi.org/10.1177/0748730409332068"),
    "jackson": ("Jackson EJ, Moreton A. Safety during night shifts: a cross-sectional survey of junior doctors' preparation and practice. BMJ Open, 2013.", "https://doi.org/10.1136/bmjopen-2013-003567"),
    "ebrahim": ("Ebrahim IO y cols. Alcohol and sleep I: effects on normal sleep. Alcoholism: Clinical and Experimental Research, 2013.", "https://doi.org/10.1111/acer.12006"),
    "ine": ("Redacción Médica, con datos del INE: más de 2,4 millones de personas trabajaron en turno de noche en España en 2022.", "https://www.redaccionmedica.com/ultimas-noticias/20240310/trabajar-de-noche-turnos-perjudica-gravemente-la-salud-acorta-vida-un-empeora-su-calidad/116394_0.amp.html"),
}

COMER = {
    "path": "/turnos/que-comer-en-el-turno-de-noche/",
    "title": "Qué comer en el turno de noche: antes, durante y al salir",
    "desc": "Qué comer antes, durante y después del turno de noche según los estudios, con horarios e ideas para el táper. De una nutricionista que también trabaja de noche.",
    "eyebrow": "Trabajo a turnos · Alimentación",
    "h1": "Qué comer en el turno de noche",
    "lead": "Antes, durante y al salir. Con horarios y con ideas que caben en un táper.",
    "intro": [
        "Soy nutricionista y sobrecargo de largo radio, así que paso muchas noches trabajando. Sé lo que es tener hambre a las tres de la mañana y no saber si comer o aguantar.",
        "Aquí tienes lo que dicen los estudios sobre comer de noche y cómo lo aplico yo. Vale igual si trabajas en planta, en urgencias, en una central o en un almacén.",
    ],
    "sections": [
        {
            "h2": "Por qué de noche no es lo mismo",
            "ps": [
                "Tu cuerpo tiene un reloj interno que espera comida de día y descanso de noche. Aunque estés despierto y trabajando, por dentro sigue siendo de noche.",
                "En un estudio de Harvard simularon dos semanas de trabajo nocturno. Las personas que comían de noche empeoraron su tolerancia a la glucosa; las que concentraron las comidas en horas de día, con el mismo turno, no.[chellappa] Otro equipo vio lo mismo en Australia,[grant] y también que comer de madrugada eleva el cortisol.[grosser]",
                "No hace falta pasar la noche en ayunas: basta con mover lo grande al día y dejar la noche para algo pequeño.",
            ],
        },
        {
            "h2": "Antes del turno: tu comida grande",
            "ps": [
                "Haz la comida principal antes de entrar. Si empiezas a las 22:00, cena a las 19:00 o a las 20:00, como una persona con horario normal.",
                "Que sea un plato completo: proteína (pescado, huevos, carne, legumbre o tofu), verdura en cantidad, un hidrato (arroz, patata, boniato, pasta o pan) y grasa de calidad, como el aceite de oliva o el aguacate. Es lo que te sostiene la primera mitad de la noche.",
            ],
            "list_h": "Ideas para esa comida",
            "list": [
                "Salmón al horno con patata y judías verdes.",
                "Lentejas guisadas con verduras y un huevo duro.",
                "Pollo al curri con arroz y brócoli.",
                "Tortilla de patata con una ensalada grande.",
            ],
        },
        {
            "h2": "Durante el turno: algo ligero",
            "ps": [
                "Un equipo de la Universidad de Australia del Sur comparó tres opciones durante cuatro noches seguidas: una comida completa a medianoche, un tentempié pequeño o nada. A las cuatro de la mañana, el grupo del tentempié rendía mejor que los otros dos, y el de la comida completa tenía más sueño.[gupta]",
                "Así que, hacia la mitad del turno, toma algo ligero y fácil de digerir. Cuanto más cerca del amanecer, más pequeño.",
            ],
            "list_h": "Lo que yo meto en el táper",
            "list": [
                "Un caldo o una crema de verduras en un termo.",
                "Yogur natural o kéfir con fruta.",
                "Huevos cocidos con unos tomatitos.",
                "Hummus con zanahoria y pepino.",
                "Un puñado de frutos secos.",
                "Un poco de arroz o patata con verdura, si la noche es larga.",
            ],
            "after": "Ve bebiendo agua toda la noche. El cansancio y la sed se parecen mucho, y muchas veces lo que pide el cuerpo es agua.",
        },
        {
            "h2": "El café, en la primera mitad",
            "ps": [
                "La cafeína te ayuda en la primera mitad del turno, pero tarda horas en irse. En un estudio, tomarla incluso 6 horas antes de acostarse acortaba el sueño.[drake]",
                "Mi regla: café o té en la primera mitad de la noche, en tomas pequeñas, y nada en las 6 horas antes de irte a dormir.",
            ],
        },
        {
            "h2": "Al salir: un desayuno ligero y a dormir",
            "ps": [
                "Si llegas con hambre, toma algo pequeño para que no te despierte a media mañana: un yogur, un kéfir o una tostada con aceite. Deja la comida fuerte para cuando te levantes.",
                "Y el alcohol, en realidad, no ayuda a dormir.[ebrahim]",
            ],
        },
        {
            "h2": "Los días libres",
            "ps": [
                "Cuando libras, vuelve a comer a horas de día y aprovecha para hacer la compra y dejar cosas preparadas. Las revisiones sobre crononutrición coinciden en lo mismo: reducir lo que se come de noche y cuidar qué se elige.[phoi]",
                "Si quieres saber cómo dormir mejor después del turno, aquí tienes la otra parte: <a href=\"/turnos/como-dormir-despues-del-turno-de-noche/\">cómo dormir después de un turno de noche</a>.",
            ],
        },
    ],
    "faq": [
        ("¿Trabajar de noche engorda?", "Trabajar de noche se asocia a más riesgo de sobrepeso y diabetes, y una parte tiene que ver con comer a horas en las que el cuerpo gestiona peor la comida. Mover la comida grande a antes del turno y tomar solo algo ligero de madrugada ayuda."),
        ("¿Es mejor no comer nada en toda la noche?", "No necesariamente. En el estudio australiano, el grupo que tomó un tentempié pequeño rindió mejor de madrugada que el que no comió nada. Algo ligero a mitad de turno suele ser el punto medio."),
        ("¿Qué llevo en el táper para el turno de noche?", "Para la mitad del turno, cosas ligeras: un caldo o una crema en termo, yogur con fruta, huevos cocidos, hummus con verdura cruda o un puñado de frutos secos."),
        ("¿Hasta qué hora puedo tomar café si trabajo de noche?", "Tómalo en la primera mitad del turno y deja al menos 6 horas sin cafeína antes de irte a dormir."),
    ],
    "sources": ["chellappa", "grant", "grosser", "gupta", "drake", "ebrahim", "phoi"],
}

DORMIR = {
    "path": "/turnos/como-dormir-despues-del-turno-de-noche/",
    "title": "Cómo dormir después de un turno de noche (y dormir de verdad)",
    "desc": "Qué hacer al salir del turno de noche para dormir de día: luz, oscuridad, horarios, café y comida. Basado en estudios, de una nutricionista que trabaja de noche.",
    "eyebrow": "Trabajo a turnos · Sueño",
    "h1": "Cómo dormir después de un turno de noche",
    "lead": "Lo que haces entre que sales del trabajo y te metes en la cama cuenta tanto como las horas que duermes.",
    "intro": [
        "Llegas a casa agotado y, aun así, te cuesta dormir o te despiertas a las tres horas. A mí me pasa en destino: después de un vuelo de noche, me suelo despertar a la hora de casa.",
        "La luz de la mañana le dice a tu reloj interno que es hora de estar despierto. Casi todo lo que funciona va de proteger tu sueño de esa señal.",
    ],
    "sections": [
        {
            "h2": "De camino a casa: gafas de sol",
            "ps": [
                "En un estudio clásico con trabajadores de noche, llevar gafas muy oscuras al volver a casa por la mañana ayudó a que el reloj interno se adaptara, y quienes se adaptaron más durmieron mejor de día y tuvieron menos fatiga.[eastman]",
                "Ponte unas gafas de sol oscuras en cuanto salgas, aunque esté nublado. Y si puedes, evita hacer recados por el camino.",
            ],
        },
        {
            "h2": "El dormitorio, como una cueva",
            "ps": [
                "Oscuridad total: persianas bajadas, cortinas opacas o un antifaz. En los estudios que mejor funcionaron, los participantes dormían en habitaciones completamente a oscuras.[smith]",
                "Fresco, silencioso y con el móvil lejos. Si hay ruido en casa, unos tapones o ruido blanco ayudan mucho.",
            ],
        },
        {
            "h2": "Un horario fijo para dormir de día",
            "ps": [
                "Intenta acostarte siempre a la misma hora después de cada turno de noche y dormir de una vez, en lugar de en trozos. Al cuerpo le cuesta menos si sabe cuándo toca.",
                "Al levantarte, sal a la calle un rato por la tarde. Esa luz ayuda a que el reloj no se te vaya demasiado lejos y puedas dormir de noche en tus días libres.[smith]",
            ],
        },
        {
            "h2": "Café y comida antes de acostarte",
            "ps": [
                "Nada de cafeína en las 6 horas antes de dormir.[drake] Si tomas café a las cinco de la mañana y te acuestas a las nueve, te va a costar.",
                "Llega a la cama sin hambre, pero sin una comida pesada: un yogur o una tostada bastan. Te lo explico con detalle en <a href=\"/turnos/que-comer-en-el-turno-de-noche/\">qué comer en el turno de noche</a>.",
                "Y el alcohol, en realidad, no ayuda a dormir.[ebrahim]",
            ],
        },
        {
            "h2": "Antes de la primera noche: una siesta",
            "ps": [
                "Una siesta por la tarde antes del primer turno de noche reduce el sueño acumulado con el que empiezas. Es una de las recomendaciones habituales para el personal sanitario, aunque en una encuesta a médicos residentes la mayoría no la hacía.[jackson]",
            ],
        },
        {
            "h2": "Los días libres",
            "ps": [
                "No hace falta volver de golpe al horario de día. Acostarte tarde y levantarte tarde los primeros días libres te deja a medio camino, y la vuelta al siguiente turno de noche cuesta menos.[smith]",
            ],
        },
    ],
    "faq": [
        ("¿Cuántas horas tengo que dormir después del turno de noche?", "Las mismas que necesitas cualquier otro día. Si no llegas de una vez, completa con una siesta por la tarde."),
        ("¿Por qué me despierto a las pocas horas de acostarme?", "Porque a media mañana tu reloj interno empuja hacia la vigilia. La oscuridad total, el silencio y no tomar cafeína en las 6 horas anteriores ayudan a mantener el sueño."),
        ("¿Es malo dormir de día?", "Dormir de día cuesta más porque va contra el reloj interno, pero se puede dormir bien si cuidas la luz al volver, la oscuridad del cuarto y un horario fijo."),
        ("¿Me conviene una siesta antes del turno de noche?", "Sí, sobre todo antes de la primera noche. Una siesta por la tarde reduce el cansancio con el que empiezas el turno."),
    ],
    "sources": ["eastman", "smith", "drake", "ebrahim", "jackson"],
}

HUB = {
    "path": "/turnos/",
    "title": "Nutricionista para trabajo a turnos y turno de noche",
    "desc": "Nutrición y sueño para quien trabaja a turnos: enfermería, medicina, tripulaciones, policía y más. Consulta online con una nutricionista que también trabaja de noche.",
    "eyebrow": "Trabajo a turnos",
    "h1": "Nutricionista para quien trabaja a turnos",
    "lead": "Para quien come a deshora, duerme de día y cambia de turno cada pocas semanas.",
    "intro": [
        "En España, más de 2,4 millones de personas trabajaron en turno de noche en 2022.[ine] Yo también trabajo de noche: soy nutricionista y sobrecargo de largo radio, y mi cuadrante cambia cada mes.",
        "Mi consulta está pensada para quien trabaja en enfermería, medicina, tripulaciones, policía, emergencias o cualquier puesto con turnos. Ajustamos qué comes, a qué hora y cómo duermes a tu cuadrante.",
    ],
    "who_h2": "Con quién trabajo",
    "who": [
        ("Enfermería y medicina", "Guardias de 24 horas, noches seguidas y comidas en la sala de descanso."),
        ("Tripulaciones y pilotos", "Jet lag, escalas cortas y comida a bordo. Tienes una guía gratuita para ti."),
        ("Policía, bomberos y emergencias", "Turnos rotativos y noches imprevisibles."),
        ("Logística, industria y atención 24 horas", "Turnos fijos de noche y descanso de día."),
    ],
    "articles_h2": "Para empezar",
    "articles": [
        ("Qué comer en el turno de noche", "Antes, durante y al salir, con ideas para el táper.", "/turnos/que-comer-en-el-turno-de-noche/"),
        ("Cómo dormir después de un turno de noche", "Luz, oscuridad, horarios y café para dormir de día.", "/turnos/como-dormir-despues-del-turno-de-noche/"),
        ("Guía gratuita para tripulaciones", "Jet lag, comida a bordo, sueño y analíticas para escalas de 24 a 72 horas.", "/tripulaciones/"),
    ],
    "steps_h2": "Cómo trabajamos",
    "steps": [
        ("Primera consulta", "Repasamos tu historia, tus síntomas, tu cuadrante y tus analíticas, y vemos por dónde empezar."),
        ("Tu protocolo", "Te llevas tu hoja de ruta de alimentación y hábitos adaptada a cada tipo de turno, y tu plan de comidas en una app."),
        ("Seguimiento", "Cada mes vemos cómo te han ido los turnos y ajustamos. Puedes hacerlo mes a mes o en un pack de 3 meses."),
    ],
    "faq": [
        ("¿La consulta es online?", "Sí, por videollamada, en castellano o en inglés. Da igual dónde vivas o qué turno tengas, buscamos una hora que te encaje."),
        ("¿Qué pasa si mis turnos cambian cada semana?", "Es lo más habitual. Preparamos pautas para cada tipo de turno (mañana, tarde, noche y libranza) y las vas usando según toque."),
        ("¿Necesito analíticas?", "No es imprescindible para empezar, pero ayudan mucho. Si vives en España, puedes hacértelas en Diagnoseum sin volante."),
    ],
    "sources": ["ine"],
}
