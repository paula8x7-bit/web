# Textos de los artículos de viajes y jet lag (castellano). Se generan con tools/turnos/build.py.

SRC_VIAJES = {
    "martingill": ("Martin-Gill C y cols. In-flight medical emergencies: a review. JAMA, 2018.", "https://doi.org/10.1001/jama.2018.19842"),
    "hinning": ("Hinninghofen H, Enck P. Passenger well-being in airplanes. Autonomic Neuroscience, 2006.", "https://doi.org/10.1016/j.autneu.2006.07.018"),
    "mitter": ("Mittermayr M y cols. Leg edema formation and venous blood flow velocity during a simulated long-haul flight. Thrombosis Research, 2007.", "https://doi.org/10.1016/j.thromres.2006.12.012"),
    "medias": ("Clarke MJ y cols. Compression stockings for preventing deep vein thrombosis in airline passengers. Cochrane Database of Systematic Reviews, 2021.", "https://doi.org/10.1002/14651858.CD004002.pub4"),
    "kiwi": ("Chey SW y cols. Exploratory comparative effectiveness trial of green kiwifruit, psyllium, or prunes in US patients with chronic constipation. American Journal of Gastroenterology, 2021.", "https://doi.org/10.14309/ajg.0000000000001149"),
    "travel": ("Eastman CI, Burgess HJ. How to travel the world without jet lag. Sleep Medicine Clinics, 2009.", "https://doi.org/10.1016/j.jsmc.2009.02.006"),
    "herxbmj": ("Herxheimer A. Jet lag. BMJ Clinical Evidence, 2014 (revisión sistemática).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4006102/"),
    "burgess": ("Burgess HJ y cols. Preflight adjustment to eastward travel: 3 days of advancing sleep with and without morning bright light. Journal of Biological Rhythms, 2003.", "https://doi.org/10.1177/0748730403253585"),
    "wehrens": ("Wehrens SMT y cols. Meal timing regulates the human circadian system. Current Biology, 2017.", "https://doi.org/10.1016/j.cub.2017.04.059"),
    "cochrane": ("Herxheimer A, Petrie KJ. Melatonin for the prevention and treatment of jet lag. Cochrane Database of Systematic Reviews, 2002.", "https://doi.org/10.1002/14651858.CD001520"),
}

JETLAG = {
    "path": "/jet-lag/",
    "alt": "/en/jet-lag/",
    "trail": [],
    "title": "Jet lag: cómo recuperarte antes y qué comer",
    "desc": "Síntomas del jet lag, por qué cuesta más volar al este y cómo recuperarte de forma natural: horarios, luz, comida, café y melatonina. De una sobrecargo de largo radio.",
    "eyebrow": "Viajes · Jet lag",
    "h1": "Jet lag: cómo recuperarte",
    "lead": "Qué hacer antes, durante y después del vuelo para que tu cuerpo llegue cuanto antes a la hora del destino.",
    "intro": [
        "Soy nutricionista y sobrecargo de largo radio. Cruzo husos horarios varias veces al mes, así que el jet lag forma parte de mi trabajo.",
        "Aquí tienes lo que dicen los estudios para cuando vas a quedarte varios días en el destino: unas vacaciones en Nueva York o un viaje de trabajo a Tokio.",
        "<strong>Si eres TCP o piloto</strong> con escalas de menos de 48 horas, esto no es para ti: en escalas cortas, lo mejor es quedarte en la hora de casa. Lo tienes explicado en mi <a href=\"/tripulaciones/\" style=\"color:#5e1a24;border-bottom:1px solid #c9b578\">guía gratuita para tripulaciones de largo radio</a>.",
    ],
    "sections": [
        {
            "h2": "Qué es y qué síntomas da",
            "ps": [
                "Tu cuerpo tiene un reloj interno que sigue en la hora de casa aunque tú ya estés en otro continente. El jet lag es el desajuste entre ese reloj y la hora del sitio donde estás.",
                "Suele notarse a partir de unos cinco husos horarios. Los síntomas más habituales son dormir mal, cansancio durante el día, rendir menos, problemas de digestión y una sensación general de malestar.[herxbmj]",
            ],
        },
        {
            "h2": "Por qué volar al este cuesta más",
            "ps": [
                "Al reloj interno le cuesta más adelantarse que retrasarse. Por eso volar hacia el este, donde tienes que acostarte antes de lo que te pide el cuerpo, suele ser más duro que volar hacia el oeste.[burgess]",
                "Si vuelas de Madrid a Nueva York, lo vas a llevar mejor que a la vuelta.",
            ],
        },
        {
            "h2": "Antes del vuelo: empieza a moverte",
            "ps": [
                "Puedes llegar con parte del camino hecho. En un estudio, adelantar la hora de acostarse una hora cada día durante tres días, con luz intensa por la mañana al levantarse, adelantó el reloj interno unas dos horas antes de viajar.[burgess]",
                "Si vas hacia el este, acuéstate y levántate un poco antes los días previos y busca luz por la mañana. Si vas hacia el oeste, al revés: acuéstate un poco más tarde.",
            ],
        },
        {
            "h2": "En el avión: vive ya en la hora de destino",
            "ps": [
                "En cuanto subas, pon el reloj en la hora del destino y organízate según esa hora. Si allí es de noche, intenta dormir: antifaz, tapones y nada de pantallas. Si allí es de día, aguanta despierto, aunque sea con alguna siesta corta.",
                "Bebe agua durante todo el vuelo. Y el alcohol, en realidad, no ayuda a dormir.[ebrahim]",
                "Qué comer antes de salir y qué llevar te lo cuento en <a href=\"/que-comer-antes-de-un-vuelo-largo/\">qué comer antes de un vuelo largo</a>.",
            ],
        },
        {
            "h2": "La comida: a la hora del destino",
            "ps": [
                "El horario de las comidas también mueve relojes del cuerpo. En un estudio de la Universidad de Surrey, retrasar las comidas cinco horas retrasó casi seis horas el ritmo de la glucosa en sangre.[wehrens]",
                "No hay estudios buenos sobre alimentos concretos contra el jet lag.[herxbmj] Lo que sí puedes hacer es comer a las horas del sitio donde estás desde el primer día, aunque no tengas hambre.",
            ],
            "list_h": "Si vas a quedarte varios días",
            "list": [
                "Si llegas por la mañana, un desayuno de verdad: huevos, fruta, pan, yogur.",
                "Comida y cena a la hora local, aunque sea algo pequeño.",
                "Cenas ligeras las primeras noches, para dormir mejor.",
                "Agua durante todo el día.",
            ],
        },
        {
            "h2": "Al llegar: luz y café en su momento",
            "ps": [
                "La luz es una de las señales que más mueven tu reloj: en el estudio de antes, quienes tuvieron luz intensa por la mañana adelantaron su reloj más del triple que quienes estuvieron en penumbra.[burgess] Busca luz de día en el destino: sal a la calle y evita quedarte a oscuras en el hotel.",
                "El café te ayuda a aguantar despierto de día, pero tómalo pronto: incluso 6 horas antes de acostarse, la cafeína acortaba el sueño.[drake]",
            ],
        },
        {
            "h2": "¿Y la melatonina?",
            "ps": [
                "Es lo que más evidencia tiene. En la revisión Cochrane, nueve de diez ensayos encontraron que tomar melatonina cerca de la hora de acostarse en el destino (entre las 22:00 y las 24:00) reducía el jet lag en vuelos de cinco o más husos horarios, sobre todo hacia el este.[cochrane]",
                "Eso sí, la hora importa: tomada temprano por el día, puede retrasar la adaptación. Si te la planteas, consúltalo antes con un profesional, sobre todo si tienes epilepsia o tomas anticoagulantes como la warfarina.[cochrane]",
            ],
        },
        {
            "h2": "Escalas cortas: quédate en la hora de casa",
            "ps": [
                "Si vas a estar menos de 48 horas, no intentes adaptarte a la hora local. Duerme lo más cerca posible de la noche de casa y come en horario de casa: así la vuelta cuesta mucho menos. Es lo que hago yo en mis escalas.",
                "Si la escala es de más de 48 horas, duerme en la noche local, pero haz que al menos 4 horas de sueño coincidan con la noche de casa.",
                "Lo explico con detalle en la <a href=\"/tripulaciones/\">guía gratuita para tripulaciones de largo radio</a>, pensada para escalas de 24 a 72 horas.",
            ],
        },
    ],
    "faq": [
        ("¿Cuánto dura el jet lag?", "Depende de cuántos husos horarios cruces y de la dirección. Hacia el este suele durar más que hacia el oeste, y cuantos más husos, más días tarda el cuerpo en ponerse en hora."),
        ("¿Cómo evitar el jet lag de forma natural?", "Empieza a mover tu horario unos días antes, vive en la hora de destino desde que subes al avión, come y duerme a la hora local, busca luz de día y deja el café para la primera parte del día."),
        ("¿Qué comer para el jet lag?", "No hay alimentos milagro, pero sí importa el horario: come a las horas del destino desde el primer día, con cenas ligeras las primeras noches, agua de sobra."),
        ("¿Y si soy TCP o piloto?", "En escalas de menos de 48 horas, no te adaptes a la hora local: duerme lo más cerca posible de la noche de casa y come en horario de casa. Así la vuelta cuesta mucho menos."),
        ("¿Qué síntomas tiene el jet lag?", "Dormir mal, cansancio durante el día, rendir menos, problemas de digestión y malestar general."),
        ("¿Funciona la melatonina para el jet lag?", "Es lo que más evidencia tiene, sobre todo en vuelos de cinco o más husos hacia el este, tomada cerca de la hora de acostarse en el destino. Antes de tomarla, consúltalo con un profesional."),
    ],
    "sources": ["herxbmj", "burgess", "ebrahim", "wehrens", "drake", "cochrane"],
    "cta": {
        "cta_h": "¿Viajas mucho por trabajo?",
        "cta_p": "En consulta preparamos tu plan para cada viaje: horarios de sueño, luz y comidas según tus rutas, con tus síntomas y tus analíticas delante. Online, en castellano o en inglés.",
        "cta_b2": ("Guía para tripulaciones", "/tripulaciones/"),
        "cta_note": 'Si vives en España, puedes hacerte las analíticas en <a href="https://diagnoseum.com/?utm_source=web-jet-lag&amp;utm_medium=referral" target="_blank" rel="noopener" data-umami-event="diagnoseum-jet-lag" style="color:#5e1a24;border-bottom:1px solid #c9b578">Diagnoseum</a>: eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins.',
    },
}


JETLAG_EN = {
    "lang": "en",
    "path": "/en/jet-lag/",
    "alt": "/jet-lag/",
    "trail": [],
    "title": "How to beat jet lag going east or west (and what to eat)",
    "desc": "How to beat jet lag flying east or west, from the UK to the USA or Australia: a jet lag eating schedule, light, caffeine and melatonin. From a long haul Inflight Manager.",
    "eyebrow": "Travel · Jet lag",
    "h1": "How to beat jet lag",
    "lead": "What to do before, during and after your flight so your body catches up with destination time as soon as possible.",
    "intro": [
        "I'm a nutritionist and a long haul Inflight Manager. I cross time zones several times a month, so jet lag is part of my job.",
        "Here is what the research says for when you're staying several days at your destination: a holiday in New York or a work trip to Sydney.",
        "<strong>If you're cabin crew or a pilot</strong> on layovers under 48 hours, this isn't for you: on short layovers, you're better off staying on home time. It's all in my <a href=\"/en/cabin-crew/\" style=\"color:#5e1a24;border-bottom:1px solid #c9b578\">free guide for long haul crew</a>.",
    ],
    "sections": [
        {
            "h2": "What jet lag is",
            "ps": [
                "Your body has an internal clock that stays on home time even when you're on another continent. Jet lag is the mismatch between that clock and the time where you are.",
                "It usually kicks in from about five time zones. The most common symptoms are poor sleep, daytime tiredness, lower performance, digestive problems and feeling generally unwell.[herxbmj]",
            ],
        },
        {
            "h2": "Why flying east is harder than flying west",
            "ps": [
                "Your body clock finds it easier to run later than earlier. In real travellers, it moved back by about 92 minutes a day after flying west, but forward by only about 57 a day after flying east.[travel]",
                "So a trip to New York is usually easier than the flight home.",
            ],
        },
        {
            "h2": "UK to USA: flying west",
            "ps": [
                "New York is 5 hours behind the UK and Los Angeles 8. Your clock has to run later, which is the easy direction.",
                "On arrival, stay awake until a normal local bedtime and get outside in the afternoon. A few days before you fly, you can go to bed a little later each night to get a head start.[travel]",
            ],
        },
        {
            "h2": "UK to Australia: flying east",
            "ps": [
                "Sydney is 9 to 11 hours ahead of the UK, depending on the time of year. It's the hardest trip there is.",
                "With 8 or more time zones east, the body clock often shifts the wrong way, later instead of earlier. That's why, for trips this long, many experts suggest shifting your clock later, as if you were flying west.[travel]",
                "If you land in the morning, wear sunglasses first thing and get your daylight later in the morning and in the afternoon: early morning light can push your clock the wrong way.[travel]",
            ],
        },
        {
            "h2": "Before you fly: get a head start",
            "ps": [
                "You can arrive with part of the work done. In one study, going to bed an hour earlier each day for three days, with bright light in the morning, moved the body clock about two hours earlier before the trip.[burgess]",
                "Even one or two days helps, but don't shift by more than about an hour a day.[travel]",
            ],
        },
        {
            "h2": "A jet lag eating schedule",
            "ps": [
                "Meal times also move clocks in your body. In a University of Surrey study, eating five hours later shifted the blood glucose rhythm by almost six hours.[wehrens]",
                "There are no good studies on specific foods for jet lag.[herxbmj] What you can do is move your meals along with your sleep.[travel]",
            ],
            "list_h": "If you're staying several days",
            "list": [
                "In the days before you fly, move your meals along with your bedtime.",
                "On the plane, eat at destination meal times. If it's night there, eat little or nothing.",
                "From day one, breakfast, lunch and dinner on local time, even if they're small.",
                "Light dinners for the first few nights, so you sleep better.",
                "Water throughout the day.",
            ],
        },
        {
            "h2": "On the plane",
            "ps": [
                "If you're staying several days, set your watch to destination time as soon as you board. If it's night there, try to sleep: eye mask, earplugs and no screens.",
                "Drink water throughout the flight. And alcohol doesn't actually help you sleep.[ebrahim]",
            ],
        },
        {
            "h2": "Caffeine at the right time",
            "ps": [
                "Coffee helps you stay awake during the day, but have it early: even 6 hours before bed, caffeine cut sleep short.[drake]",
            ],
        },
        {
            "h2": "What about melatonin?",
            "ps": [
                "It's what has the most evidence. In the Cochrane review, nine out of ten trials found that melatonin taken close to bedtime at the destination reduced jet lag on flights across five or more time zones, especially flying east.[cochrane]",
                "Timing matters, though: taken early in the day, it can slow down adjustment. If you're thinking about it, check with a professional first, especially if you have epilepsy or take blood thinners like warfarin.[cochrane]",
            ],
        },
        {
            "h2": "Short layovers: stay on home time",
            "ps": [
                "If you're there for less than 48 hours, don't try to adjust to local time. Sleep as close as you can to your home night and eat on home time: getting back home is much easier. It's what I do on my layovers.",
                "If the layover is longer than 48 hours, sleep at night local time, but make sure at least 4 hours of your sleep fall within your home night.",
                "I go into detail in my <a href=\"/en/cabin-crew/\">free guide for long haul crew</a>, written for 24 to 72 hour layovers.",
            ],
        },
    ],
    "faq": [
        ("How long does jet lag last?", "It depends on how many time zones you cross and in which direction. Flying west, your body clock catches up by about an hour and a half a day; flying east, by about one hour a day."),
        ("Is jet lag worse going east or west?", "East. Your body clock finds it harder to run earlier than later, so the trip home from the USA is usually harder than the trip out."),
        ("How do I beat jet lag from the UK to Australia?", "It's a trip of 9 to 11 hours east, where the clock often shifts the wrong way. Many experts suggest shifting your clock later, as if flying west, and on arrival wearing sunglasses early in the morning and getting daylight later in the day."),
        ("What should I eat for jet lag?", "There are no miracle foods, but timing matters: move your meals along with your sleep, eat on local time from day one and keep dinners light for the first few nights."),
        ("Does melatonin work for jet lag?", "It has the most evidence, especially on flights across five or more time zones going east, taken close to bedtime at the destination. Check with a professional before taking it."),
        ("What if I'm cabin crew or a pilot?", "On layovers under 48 hours, don't adjust to local time: sleep as close as you can to your home night and eat on home time. Getting back home is much easier."),
    ],
    "sources": ["herxbmj", "travel", "burgess", "wehrens", "ebrahim", "drake", "cochrane"],
    "cta": {
        "cta_h": "Do you travel a lot for work?",
        "cta_p": "In my consultations we plan each trip with you: sleep, light and meal times for your routes, with your symptoms and blood tests in front of us. Online, in English or Spanish.",
        "cta_b2": ("Cabin crew guide", "/en/cabin-crew/"),
        "cta_note": 'Living in Spain? You can get your blood tests done at <a href="https://diagnoseum.com/?utm_source=web-jet-lag-en&amp;utm_medium=referral" target="_blank" rel="noopener" data-umami-event="diagnoseum-jet-lag-en" style="color:#5e1a24;border-bottom:1px solid #c9b578">Diagnoseum</a>: you choose exactly what you want to test, no doctor\'s referral needed, backed by Eurofins.',
    },
}


VUELO = {
    "path": "/que-comer-antes-de-un-vuelo-largo/",
    "trail": [],
    "title": "Qué comer antes de un vuelo largo (y qué llevar al avión)",
    "desc": "Qué comer antes de un vuelo largo, qué llevar para comer en el avión y cómo evitar la hinchazón, la retención de líquidos y el estreñimiento al viajar. De una sobrecargo nutricionista.",
    "eyebrow": "Viajes · Comida",
    "h1": "Qué comer antes de un vuelo largo",
    "lead": "Qué comer antes de salir, qué llevar en la bolsa y cómo llegar sin hinchazón, sin piernas pesadas y sin estreñimiento.",
    "intro": [
        "Soy nutricionista y sobrecargo de largo radio. Es muy habitual subir al avión con hambre, comer lo primero que encuentras en el aeropuerto y aterrizar hinchado.",
        "Con un poco de organización, el vuelo se lleva mucho mejor. Esto es lo que te recomiendo.",
        "<strong>Si eres TCP o piloto</strong>, en mi <a href=\"/tripulaciones/\" style=\"color:#5e1a24;border-bottom:1px solid #c9b578\">guía gratuita para tripulaciones de largo radio</a> tienes cómo organizar la comida a bordo y en la escala.",
    ],
    "sections": [
        {
            "h2": "Antes de salir: una comida completa",
            "ps": [
                "Haz una comida completa antes de ir al aeropuerto: proteína, verdura cocinada y una ración de hidrato. Así no llegas con hambre a la puerta de embarque.",
                "Si hasta la siguiente comida van a pasar más de 6 horas, lleva algo para el camino.",
            ],
            "list_h": "Ideas para esa comida",
            "list": [
                "Pescado a la plancha con patata cocida y judías verdes.",
                "Pollo asado con boniato y calabacín.",
                "Tortilla con verdura salteada y pan de masa madre.",
            ],
        },
        {
            "h2": "El día del vuelo: lo que mejor evitar",
            "ps": [
                "En cabina la presión es más baja que en tierra. Los gases del intestino ocupan más y la digestión se vuelve más lenta: en estudios con la presión de un avión en vuelo, las comidas con mucha fibra vaciaban el estómago más despacio y daban sensación de pesadez.[hinning]",
                "Por eso, el día del vuelo, reduce las legumbres y las crucíferas crudas (brócoli, coliflor, col) y evita las bebidas con gas y el chicle.",
            ],
        },
        {
            "h2": "Qué llevar para comer en el avión",
            "ps": [
                "Con una bolsa térmica pequeña resuelves el vuelo y la primera comida en destino.",
            ],
            "list_h": "Lo que cabe en la bolsa",
            "list": [
                "Huevos cocidos y latas pequeñas de sardinas o caballa.",
                "Zanahoria, pepino y pimiento en bastones.",
                "Verdura asada con boniato o quinoa en un táper.",
                "Frutos secos y un aguacate.",
                "Pan de centeno de masa madre.",
                "Fruta entera.",
                "Bolsitas de manzanilla, rooibos o jengibre, para pedir agua caliente a bordo.",
            ],
            "after": "Ojo con dos cosas. Lo que se puede pasar por el control de seguridad depende de cada aeropuerto: algunos, como varios de Londres, ya permiten llevar más líquido. Si llevas yogur, kéfir o caldo, confírmalo antes con la seguridad del aeropuerto. Y Estados Unidos, Australia o Japón restringen la fruta, la verdura y la carne frescas: lo que sobre, cómelo antes de aterrizar o tíralo en el avión.",
        },
        {
            "h2": "Agua, a sorbos",
            "ps": [
                "El aire de cabina es muy seco.[martingill] Bebe agua a sorbos y de forma regular, sin esperar a tener sed. Las infusiones también cuentan.",
                "Y el alcohol, en realidad, no ayuda a dormir.[ebrahim]",
            ],
        },
        {
            "h2": "Retención de líquidos y piernas hinchadas",
            "ps": [
                "La hinchazón de piernas en un vuelo largo viene sobre todo de estar sentado. En un estudio que simuló diez horas en asientos de avión, el volumen de la parte baja de las piernas ya había subido a las cuatro horas, y volvió a la normalidad al día siguiente.[mitter]",
                "Levántate y pasea por el pasillo cuando puedas. Sentado, mueve los tobillos y haz elevaciones de talones cada hora.",
                "Las medias de compresión reducen los trombos sin síntomas en vuelos de más de cuatro horas, y probablemente también la hinchazón.[medias] Si tienes más riesgo de trombosis, consúltalo con tu médico antes de volar.",
            ],
        },
        {
            "h2": "El estreñimiento del viajero",
            "ps": [
                "Cambiar de horarios, beber menos, pasar horas sentado y comer distinto: el intestino lo nota.",
                "Lo que mejor funciona es lo de siempre: agua, verdura, fruta y moverte. En un ensayo, dos kiwis verdes al día mejoraron el estreñimiento igual que las ciruelas pasas o el psyllium, y fueron lo que menos molestias dio.[kiwi] Llévatelos para el primer día, pero cómetelos antes de aterrizar si vas a un país que no deja entrar fruta.",
                "Y cuando tengas ganas de ir al baño, no lo dejes para luego.",
            ],
        },
    ],
    "faq": [
        ("¿Qué es mejor comer antes de un vuelo largo?", "Una comida completa y fácil de digerir antes de ir al aeropuerto: proteína, verdura cocinada y una ración de hidrato, como pescado con patata y judías verdes."),
        ("¿Qué no comer antes de volar?", "El día del vuelo, mejor reducir las legumbres y las crucíferas crudas, y evitar las bebidas con gas y el chicle: en cabina los gases ocupan más y la digestión es más lenta."),
        ("¿Qué llevar para comer en el avión?", "Huevos cocidos, latas pequeñas de sardinas o caballa, verdura en bastones o asada en un táper, frutos secos, pan de masa madre y fruta entera. Para los líquidos, como el yogur o el caldo, confirma antes las normas de seguridad de tu aeropuerto."),
        ("¿Por qué se me hinchan las piernas en el avión?", "Sobre todo por pasar muchas horas sentado. Levantarte, pasear y mover los tobillos ayuda, y las medias de compresión también pueden ayudar."),
        ("¿Por qué me estriño cuando viajo?", "Por el cambio de horarios, beber menos, estar sentado y comer distinto. Agua, fruta como el kiwi, verdura y movimiento son lo que mejor funciona."),
    ],
    "sources": ["hinning", "martingill", "ebrahim", "mitter", "medias", "kiwi"],
}

VUELO["cta"] = JETLAG["cta"]
