# Textos de los artículos de viajes y jet lag (castellano). Se generan con tools/turnos/build.py.

SRC_VIAJES = {
    "hobson": ("Hobson RM, Maughan RJ. Hydration status and the diuretic action of a small dose of alcohol. Alcohol and Alcoholism, 2010.", "https://doi.org/10.1093/alcalc/agq029"),
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
                "Bebe agua durante todo el vuelo. Y el alcohol, en realidad, no ayuda a dormir.[ebrahim] Además, te hace orinar más y concentra la sangre, así que con el aire seco de cabina te deshidrata todavía más.[hobson]",
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
    "sources": ["herxbmj", "burgess", "ebrahim", "hobson", "wehrens", "drake", "cochrane"],
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
                "Drink water throughout the flight. And alcohol doesn't actually help you sleep.[ebrahim] It also makes you pee more and concentrates your blood, so in dry cabin air it dehydrates you even more.[hobson]",
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
    "sources": ["herxbmj", "travel", "burgess", "wehrens", "ebrahim", "hobson", "drake", "cochrane"],
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
                "Y el alcohol, en realidad, no ayuda a dormir.[ebrahim] Además, te hace orinar más y concentra la sangre, así que con un aire tan seco te deshidrata todavía más.[hobson]",
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
    "sources": ["hinning", "martingill", "ebrahim", "hobson", "mitter", "medias", "kiwi"],
}

VUELO["cta"] = JETLAG["cta"]

_LINK = "style='color:#5e1a24;border-bottom:1px solid #c9b578'"

MEALPREP_EN = {
    "lang": "en",
    "path": "/en/cabin-crew-meal-prep/",
    "trail": [("Cabin crew guide", "/en/cabin-crew/")],
    "title": "Cabin crew meal prep: what flight attendants eat on long haul flights",
    "desc": "Cabin crew meal prep ideas from a long haul Inflight Manager and nutritionist: what to cook before a trip, what to pack, and what to eat on a night flight.",
    "eyebrow": "Cabin crew · Food",
    "h1": "Cabin crew meal prep",
    "lead": "What to cook before a trip, what to pack, and what to eat on a long haul night flight.",
    "intro": [
        "I'm a nutritionist and a long haul Inflight Manager. I fly the same trips you do, and I know what it's like to sleep in crew rest, do back-to-back 24 hour layovers and eat dinner at odd hours after the service.",
        "Most crew meal prep tips are on social media. Here is how I sort it out, with the research behind it.",
    ],
    "sections": [
        {
            "h2": "The rule behind it: eat by your home clock",
            "ps": [
                "On layovers under 48 hours, eat on home time, not local time. Midnight to 6:00 home time is your biological night, wherever you are.",
                "Eating during your biological night is harder on your body: in a Harvard study of simulated night work, eating at night made blood sugar control worse.[chellappa] So if you eat during those hours, keep it light and easy to digest: broth, eggs, yoghurt, cooked vegetables, rice or potato.",
                "Something small works better than a big meal. In an Australian study, people who had a snack in the early hours performed better at 4am than those who had a full meal or nothing at all.[gupta]",
            ],
        },
        {
            "h2": "Before you leave",
            "ps": [
                "If you're flying overnight, have a 2 to 3 hour nap beforehand. Have a proper meal, with carbs, before you head to the airport. If dinner is more than 6 hours away, pack a snack.",
            ],
        },
        {
            "h2": "Dinner on a night flight",
            "ps": [
                "You take off at 8 or 9 in the evening and dinner comes after the service. It's your main meal, but keep it easy to digest: protein, cooked vegetables and a small portion of carbs.",
            ],
            "list_h": "Three ways to sort it out",
            "list": [
                "<strong>From home:</strong> a container with chicken, fish or eggs, roasted or boiled vegetables and your portion of carbs. Heat it up in the aircraft oven and carry it in a cool bag, in glass or steel. Don't use foil trays.",
                "<strong>From the airport:</strong> a salad or vegetables you can heat up, roast chicken or salmon, boiled eggs or plain yoghurt. Watch out for ready-made rice and potatoes: your carbs are best brought from home.",
                "<strong>On board:</strong> take protein and vegetables from the crew meal, add your own carbs if you've brought them, start with the protein and keep sauces on the side. Skip the white bread, pastries and desserts.",
            ],
        },
        {
            "h2": "Batch cook on your days off",
            "ps": [
                "One cooking session at home covers the trip: roast a tray of vegetables, cook some sweet potato or quinoa, boil a few eggs and portion out the protein.",
            ],
            "list_h": "Carbs that travel well",
            "list": [
                "Sourdough bread.",
                "Corn cakes.",
                "Boiled potato.",
                "Roast sweet potato or cooked quinoa.",
                "Oats, for breakfast down route.",
            ],
        },
        {
            "h2": "What I pack",
            "ps": [
                "A small cool bag covers the flight and your first meal down route. This is the list I use.",
            ],
            "list_h": "In my cool bag",
            "list": [
                "Boiled eggs and small tins of sardines or mackerel.",
                "Greek yoghurt or kefir for the flight.",
                "Carrot, cucumber and pepper sticks.",
                "Roasted vegetables in a container: they're the hardest thing to find on a layover.",
                "Nuts, seeds and an avocado.",
                "Whole fruit.",
                "Chamomile, rooibos or ginger tea, and powdered stock or bone broth for when you land late.",
                "A glass or steel container, cutlery and a large bottle.",
            ],
            "after": "Watch out at customs: the US, Australia and Japan restrict fresh fruit, vegetables and meat. Eat whatever's left before landing or bin it on the aircraft. And what you can take through security depends on the airport, so check with them if you're carrying liquids like yoghurt or broth.",
        },
        {
            "h2": "On board",
            "ps": [
                "On flying days, cut down on pulses and raw cruciferous vegetables, and avoid fizzy drinks and chewing gum. At cabin altitude gas expands and digestion slows down: in studies at in-flight cabin pressure, a fibre-rich meal emptied from the stomach more slowly and left people feeling heavy.[hinning]",
                "Cabin air is very dry.[martingill] Sip water regularly; don't wait until you're thirsty. Use spices, herbs, lemon and tomato to add flavour instead of reaching for sugar.",
                "In the galley, do calf raises, short squats and hip stretches every hour. Sitting is what makes your legs swell: in a study of 10 hours in aircraft seats, lower leg volume had already gone up after 4 hours.[mitter]",
            ],
        },
        {
            "h2": "Eating out down route",
            "ps": [
                "The plate is the same everywhere: protein, vegetables and a small portion of carbs. Wherever you are, order grilled protein, a double portion of vegetables and the sauce on the side.",
                "In the US and Canada, make the most of the supermarket: rotisserie chicken, salads, Greek yoghurt, eggs and berries. In Europe, watch out for late dinners: they fall in your biological night.",
                "There's much more on sleep, jet lag, caffeine and blood tests in my <a href='/en/cabin-crew/' " + _LINK + ">free guide for long haul crew</a>.",
            ],
        },
    ],
    "faq": [
        ("What do flight attendants eat on long haul flights?", "Many bring their own food. On a night flight, the main meal after the service should be easy to digest: protein, cooked vegetables and a small portion of carbs, with something light during your biological night."),
        ("Can cabin crew bring their own food on board?", "Most do. Carry it in a cool bag, in a glass or steel container, and check your airline's rules for heating it up and the customs rules at your destination."),
        ("What are good cabin crew meal prep ideas?", "Roasted vegetables, boiled eggs, chicken or fish, and carbs that travel well, like sourdough bread, boiled potato, roast sweet potato or quinoa. Add nuts, whole fruit and Greek yoghurt for the flight."),
        ("What should I eat on a night flight as crew?", "Have a proper meal before you leave, keep dinner after the service easy to digest, and between midnight and 6:00 home time only eat something light, like broth, eggs or yoghurt."),
    ],
    "sources": ["chellappa", "gupta", "hinning", "martingill", "mitter"],
    "cta": {
        "cta_h": "Want a meal plan built around your roster?",
        "cta_p": "I'll put together a meal plan for home, the airport and on board, with your real schedules and the food you like. Online, in English or Spanish.",
        "cta_b2": ("Cabin crew guide", "/en/cabin-crew/"),
        "cta_note": JETLAG_EN["cta"]["cta_note"].replace("web-jet-lag-en", "web-crew-meal-prep").replace("diagnoseum-jet-lag-en", "diagnoseum-crew-meal-prep"),
    },
}

# Tripulaciones de corto radio (madrugones, varios saltos, sin escala).
SRC_VIAJES.update({
    "arsintescu": ("Arsintescu L y cols. Early starts and late finishes both reduce alertness and performance among short-haul airline pilots. Journal of Sleep Research, 2021.", "https://doi.org/10.1111/jsr.13521"),
    "akerstedt": ("Åkerstedt T y cols. Acute and cumulative effects of scheduling on aircrew fatigue in ultra-short-haul operations. Journal of Sleep Research, 2021.", "https://doi.org/10.1111/jsr.13305"),
    "steven": ("Steven D y cols. Additive effects of time awake and number of flights on fatigue in short-haul pilots. Journal of Sleep Research, 2026.", "https://doi.org/10.1111/jsr.70473"),
    "bhi": ("Maughan RJ y cols. A randomized trial to assess the potential of different beverages to affect hydration status: development of a beverage hydration index. American Journal of Clinical Nutrition, 2016.", "https://doi.org/10.3945/ajcn.115.114769"),
    "aguavion": ("Handschuh H y cols. Bacteria that travel: the quality of aircraft water. International Journal of Environmental Research and Public Health, 2015.", "https://doi.org/10.3390/ijerph121113938"),
    "vejvoda": ("Vejvoda M y cols. Significance of time awake for predicting pilots' fatigue on short-haul flights. Journal of Sleep Research, 2014.", "https://doi.org/10.1111/jsr.12186"),
})

CORTO = {
    "path": "/tcp-corto-radio-que-comer/",
    "alt": "/en/short-haul-cabin-crew-food/",
    "trail": [],
    "title": "TCP de corto radio: qué comer con madrugones y varios saltos",
    "desc": "Qué comer si eres TCP de corto radio: el desayuno cuando firmas a las 5:00, qué llevar para cuatro o seis saltos, cómo reponer líquidos y electrolitos y cómo encadenar madrugones. De una sobrecargo nutricionista.",
    "eyebrow": "Tripulaciones · Corto radio",
    "h1": "TCP de corto radio: qué comer con madrugones y varios saltos",
    "lead": "Firmas de madrugada, cuatro o seis saltos con 25 minutos de escala y, muchas veces, vuelta a base. Así se organiza la comida para llegar entero al último tramo.",
    "intro": [
        "Soy nutricionista y sobrecargo. Empecé en corto radio: cuatro años de rotaciones de cuatro y hasta seis saltos, con escalas de 25 minutos, semanas de madrugones y semanas de tardes.",
        "La comida la llevábamos de casa: a bordo no había nada para la tripulación. A veces comíamos en la escala, si aterrizábamos antes de hora, y si no, en vuelo, después del servicio de venta. Dependía mucho del destino.",
        "No todas las compañías trabajan igual: en unas se pernocta fuera y en otras se vuelve siempre a base. Este artículo es sobre todo para los días de ida y vuelta, con varios saltos seguidos.",
        "Esto es lo que me habría gustado que me contaran entonces, con lo que dicen los estudios con tripulaciones de corto radio.",
    ],
    "sections": [
        {
            "h2": "Por qué los madrugones pasan factura",
            "ps": [
                "En un estudio con 95 pilotos de corto radio, la noche antes de una firma temprana dormían de media una hora y media menos que antes de una salida de tarde, y empezaban el día más cansados.[arsintescu]",
                "Y se acumula. En otro estudio con tripulaciones (entre ellos, TCP), cuantas más firmas muy tempranas había en la semana, más cansancio arrastraban, y cada hora de sueño de más lo reducía.[akerstedt]",
                "Los saltos también suman: con cuatro vuelos en el día, el cansancio llegaba a su punto crítico más de dos horas antes que con uno solo.[steven]",
            ],
        },
        {
            "h2": "Organízate en tus libres",
            "ps": [
                "Con cinco días seguidos de rotaciones, si no llevas la comida hecha, acabas tirando de sándwich o de fideos instantáneos. Lo que mejor funciona es cocinar una o dos veces en los libres y dejarlo en raciones.",
                "Prepara cada noche la bolsa del día siguiente: el desayuno, lo que vas a picar entre saltos y la comida principal. A las 3:30 nadie decide bien qué llevarse.",
                "Si la comida la vas a calentar en el horno del avión, llévala en un recipiente apto para horno.",
            ],
        },
        {
            "h2": "Antes de firmar: un desayuno ligero",
            "ps": [
                "Si firmas a las 5:00, para tu cuerpo sigue siendo de noche: entre las 00:00 y las 6:00 toca algo pequeño y fácil de digerir. En un estudio de turnos de noche, a esas horas rendían mejor quienes tomaban algo ligero que quienes hacían una comida completa o no comían nada.[gupta]",
                "Lo importante es no salir de casa en ayunas y con el estómago lleno de café.",
            ],
            "list_h": "Ideas para ese primer desayuno",
            "list": [
                "Un yogur natural o kéfir con fruta.",
                "Una tostada de pan de masa madre con aceite de oliva y tomate.",
                "Un vaso de leche o de bebida vegetal con unos frutos secos.",
                "Un huevo cocido, preparado la noche antes.",
            ],
        },
        {
            "h2": "Entre saltos: comida que se come en cinco minutos",
            "ps": [
                "Con 25 minutos de escala nunca sabes si vas a poder sentarte. Lleva cosas que se coman rápido y sin cubiertos, y repártelas entre los saltos en lugar de llegar al último tramo sin haber comido.",
                "La comida principal, cuando haya hueco: en una escala en la que aterrices antes de hora o en vuelo, después del servicio.",
            ],
            "list_h": "Lo que cabe en la bolsa",
            "list": [
                "Huevos cocidos.",
                "Bastones de zanahoria, pepino y pimiento, con hummus.",
                "Fruta entera: plátano, manzana, mandarinas.",
                "Un puñado de frutos secos.",
                "Queso curado o latas pequeñas de atún o sardinas.",
                "Para la comida principal: arroz o patata, verdura y proteína (pollo, pescado, legumbre o tortilla).",
            ],
        },
        {
            "h2": "Líquidos y electrolitos durante el día",
            "ps": [
                "El aire de cabina es muy seco[martingill] y en las rotaciones es fácil pasar horas sin beber. Lleva tu botella y bebe un poco en cada tramo, sin esperar a tener sed.",
                "Para que el líquido se quede en el cuerpo, ayuda que lleve electrolitos. En un ensayo que comparó trece bebidas, la leche y las soluciones de rehidratación oral se retenían bastante más que el agua; las bebidas para deportistas, en cambio, no se diferenciaron del agua.[bhi]",
                "En la práctica: acompaña el agua con comida (fruta, verdura, algo salado como el queso o las conservas), un caldo con sal en el termo o un vaso de leche o kéfir. En días de mucho calor o mucho trabajo, una solución de rehidratación oral de farmacia es una opción; consulta cómo tomarla con un profesional.",
            ],
        },
        {
            "h2": "El agua caliente del avión",
            "ps": [
                "Es lo que hay a mano para un té, unos fideos o algo calentito, pero el agua de los depósitos no siempre está en buenas condiciones. En un estudio que analizó el agua de a bordo, se encontraron bacterias de 37 especies distintas, y el camión que rellena los depósitos era una de las principales fuentes.[aguavion]",
                "Si te gusta tomar algo caliente en la rotación, lleva un termo desde casa con agua caliente o caldo.",
            ],
        },
        {
            "h2": "Cafeína: al principio del día",
            "ps": [
                "El café ayuda en la primera mitad de la jornada, pero tarda horas en irse: tomado incluso 6 horas antes de dormir, ya recorta el sueño.[drake]",
                "Si mañana vuelves a madrugar, el café de media tarde te va a quitar justo las horas que necesitas. Tómalo pronto, poco a poco, y nada en las 6 horas antes de acostarte.",
            ],
        },
        {
            "h2": "Al llegar a casa: comida normal y a por la noche siguiente",
            "ps": [
                "Si terminas a mediodía, haz una comida completa, como un día cualquiera. Así no llegas a la noche picando.",
                "Si al día siguiente vuelves a firmar temprano, adelanta la cena y la hora de acostarte. Lo que más protege de los madrugones encadenados es sumar horas de sueño.[akerstedt]",
            ],
        },
        {
            "h2": "Semanas de tardes: cuando acabas de madrugada",
            "ps": [
                "Las salidas de tarde parecen más fáciles, pero al final de la jornada se acumulan muchas horas despierto, y el cansancio al aterrizar es mayor que en las firmas tempranas.[vejvoda]",
                "Haz la comida principal antes de firmar, algo ligero en los saltos de la noche y, al llegar a casa, solo algo pequeño antes de dormir.",
            ],
        },
    ],
    "faq": [
        ("¿Qué desayunar si entro a trabajar a las 5 de la mañana?", "Algo ligero y fácil de digerir: un yogur o kéfir con fruta, una tostada con aceite de oliva o un vaso de leche con frutos secos. A esa hora tu cuerpo sigue en su noche biológica."),
        ("¿Qué comer en un día de cuatro o seis saltos?", "Cosas que se comen en cinco minutos y sin cubiertos, como huevos cocidos, fruta, frutos secos o verdura en bastones con hummus, repartidas entre los saltos. La comida principal, cuando haya hueco en una escala o después del servicio."),
        ("¿Cómo reponer electrolitos durante la rotación?", "Acompaña el agua con comida (fruta, verdura y algo salado), un caldo en el termo o un vaso de leche o kéfir. En un ensayo, la leche y las soluciones de rehidratación oral se retenían más que el agua."),
        ("¿Es seguro el agua caliente del avión?", "El agua de los depósitos no siempre está en buenas condiciones: en un estudio se encontraron bacterias de muchas especies. Para algo caliente, mejor un termo traído de casa."),
        ("¿Cuándo dejar el café si madrugo al día siguiente?", "Tómalo en la primera mitad de la jornada y deja al menos 6 horas sin cafeína antes de acostarte."),
    ],
    "sources": ["arsintescu", "akerstedt", "steven", "gupta", "martingill", "bhi", "aguavion", "drake", "vejvoda"],
    "cta": {
        "cta_h": "¿Vuelas en corto radio?",
        "cta_p": "En consulta preparamos tu plan según tu programación: qué comer en cada tipo de firma, cómo encadenar madrugones y cómo recuperar en tus libres. Online, en castellano o en inglés.",
        "cta_b2": ("Ver todas las guías", "/guias/"),
        "cta_note": JETLAG["cta"]["cta_note"].replace("web-jet-lag", "web-corto-radio").replace("diagnoseum-jet-lag", "diagnoseum-corto-radio"),
    },
}

CORTO_EN = {
    "lang": "en",
    "path": "/en/short-haul-cabin-crew-food/",
    "alt": "/tcp-corto-radio-que-comer/",
    "trail": [],
    "title": "Short haul cabin crew: what to eat on earlies and multi sector days",
    "desc": "What to eat as short haul cabin crew: breakfast before a 5am report, what to pack for four to six sectors, how to stay hydrated and replace electrolytes, and how to cope with a week of earlies. From an Inflight Manager and nutritionist.",
    "eyebrow": "Cabin crew · Short haul",
    "h1": "Short haul cabin crew: what to eat on earlies and multi sector days",
    "lead": "Reports in the middle of the night, four to six sectors with 25 minute turnarounds and, often, back to base. Here's how to plan your food so you still have energy on the last sector.",
    "intro": [
        "I'm a nutritionist and an Inflight Manager. I started on short haul: four years of four and up to six sectors a day, 25 minute turnarounds, weeks of earlies and weeks of lates.",
        "We brought our food from home: there was nothing on board for the crew. Sometimes we ate on the ground if we landed early, and if not, in the air after the onboard sales. It depended a lot on the destination.",
        "Not every airline works the same way: some short haul crews night stop and others always return to base. This article is mainly for those there and back days with several sectors in a row.",
        "This is what I wish someone had told me back then, together with what the research on short haul crew says.",
    ],
    "sections": [
        {
            "h2": "Why earlies take their toll",
            "ps": [
                "In a study of 95 short haul pilots, the night before an early report they slept about an hour and a half less than before a late start, and they began the day more tired.[arsintescu]",
                "And it adds up. In another study of aircrew (cabin crew included), the more very early duties in a week, the more tired they became, and every extra hour of sleep helped.[akerstedt]",
                "Sectors count too: with four flights in a day, fatigue hit its critical point more than two hours earlier than with just one.[steven]",
            ],
        },
        {
            "h2": "Get organised on your days off",
            "ps": [
                "With five days of flying in a row, if your food isn't ready you end up living on sandwiches or instant noodles. What works best is cooking once or twice on your days off and portioning it out.",
                "Pack the next day's bag the night before: breakfast, something to snack on between sectors and your main meal. Nobody makes good food choices at 3:30am.",
                "If you're going to heat your meal in the aircraft oven, pack it in an ovenproof container.",
            ],
        },
        {
            "h2": "Before you report: a light breakfast",
            "ps": [
                "If you report at 5am, your body still thinks it's night: between midnight and 6am, keep it small and easy to digest. In a night shift study, people who had a light snack in the early hours performed better than those who had a full meal or ate nothing.[gupta]",
                "The key is not to leave home on an empty stomach and a lot of coffee.",
            ],
            "list_h": "Ideas for that first breakfast",
            "list": [
                "Natural yoghurt or kefir with fruit.",
                "Sourdough toast with olive oil and tomato.",
                "A glass of milk or a plant drink with a few nuts.",
                "A boiled egg, made the night before.",
            ],
        },
        {
            "h2": "Between sectors: food you can eat in five minutes",
            "ps": [
                "With a 25 minute turnaround you never know if you'll get to sit down. Pack things you can eat quickly without cutlery, and spread them across the sectors so you don't reach the last one without having eaten.",
                "Have your main meal whenever there's a gap: on a turnaround when you land early, or in the air after the service.",
            ],
            "list_h": "What fits in your bag",
            "list": [
                "Boiled eggs.",
                "Carrot, cucumber and pepper sticks with hummus.",
                "Whole fruit: bananas, apples, satsumas.",
                "A handful of nuts.",
                "Hard cheese or small tins of tuna or sardines.",
                "For your main meal: rice or potatoes, vegetables and protein (chicken, fish, beans or a Spanish omelette).",
            ],
        },
        {
            "h2": "Fluids and electrolytes through the day",
            "ps": [
                "Cabin air is very dry[martingill] and on a busy day it's easy to go hours without drinking. Bring your own bottle and have a little on every sector, without waiting until you're thirsty.",
                "Electrolytes help your body hold on to what you drink. A trial comparing thirteen drinks found that milk and oral rehydration solutions were retained much better than water, while sports drinks were no different from water.[bhi]",
                "In practice: have your water with food (fruit, vegetables and something salty, like cheese or tinned fish), a salted broth in a flask or a glass of milk or kefir. On very hot or very busy days, an oral rehydration solution from the pharmacy is an option; ask a professional how to take it.",
            ],
        },
        {
            "h2": "The hot water on board",
            "ps": [
                "It's what's at hand for a tea, some noodles or something warm, but the water in the aircraft tanks isn't always in good condition. A study that tested water on board found 37 different species of bacteria, and the truck that fills the tanks was one of the main sources.[aguavion]",
                "If you like something hot during the day, bring a flask from home with hot water or broth.",
            ],
        },
        {
            "h2": "Caffeine: early in the day",
            "ps": [
                "Coffee helps in the first half of your duty, but it takes hours to clear: even 6 hours before bed, it cuts your sleep short.[drake]",
                "If you're on another early tomorrow, that mid afternoon coffee will take away exactly the hours you need. Have it early, a little at a time, and nothing in the 6 hours before bed.",
            ],
        },
        {
            "h2": "Back home: a normal meal and an early night",
            "ps": [
                "If you finish around midday, have a proper meal, like on any other day. That way you won't spend the evening snacking.",
                "If you're reporting early again tomorrow, bring dinner and bedtime forward. Adding up hours of sleep is what protects you most from a run of earlies.[akerstedt]",
            ],
        },
        {
            "h2": "Weeks of lates: when you finish after midnight",
            "ps": [
                "Late starts look easier, but by the end of the duty you've been awake for a long time, and fatigue on landing is higher than on earlies.[vejvoda]",
                "Have your main meal before you report, something light on the evening sectors and, once home, only something small before bed.",
            ],
        },
    ],
    "faq": [
        ("What should I eat before a 5am report?", "Something light and easy to digest: yoghurt or kefir with fruit, toast with olive oil or a glass of milk with a few nuts. At that hour your body is still in its biological night."),
        ("What should cabin crew eat on a four or six sector day?", "Food you can eat in five minutes without cutlery, like boiled eggs, fruit, nuts or vegetable sticks with hummus, spread across the sectors. Have your main meal when there's a gap on a turnaround or after the service."),
        ("How can I replace electrolytes on a busy duty?", "Have your water with food (fruit, vegetables and something salty), a broth in a flask or a glass of milk or kefir. In one trial, milk and oral rehydration solutions were retained better than water."),
        ("Is the hot water on a plane safe to drink?", "The water in aircraft tanks isn't always in good condition: one study found many species of bacteria. For something hot, a flask from home is a better option."),
        ("When should I stop caffeine if I have an early tomorrow?", "Have it in the first half of your duty and leave at least 6 hours without caffeine before bed."),
    ],
    "sources": CORTO["sources"],
    "cta": {
        "cta_h": "Flying short haul?",
        "cta_p": "In my consultations we build a plan around your roster: what to eat on each type of duty, how to handle a run of earlies and how to recover on your days off. Online, in English or Spanish.",
        "cta_b2": ("See all guides", "/en/guides/"),
        "cta_note": JETLAG_EN["cta"]["cta_note"].replace("web-jet-lag-en", "web-short-haul-en").replace("diagnoseum-jet-lag-en", "diagnoseum-short-haul-en"),
    },
}
