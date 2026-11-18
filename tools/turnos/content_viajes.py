# Textos de los artículos de viajes y jet lag (castellano). Se generan con tools/turnos/build.py.

SRC_VIAJES = {
    "herxbmj": ("Herxheimer A. Jet lag. BMJ Clinical Evidence, 2014 (revisión sistemática).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4006102/"),
    "burgess": ("Burgess HJ y cols. Preflight adjustment to eastward travel: 3 days of advancing sleep with and without morning bright light. Journal of Biological Rhythms, 2003.", "https://doi.org/10.1177/0748730403253585"),
    "wehrens": ("Wehrens SMT y cols. Meal timing regulates the human circadian system. Current Biology, 2017.", "https://doi.org/10.1016/j.cub.2017.04.059"),
    "cochrane": ("Herxheimer A, Petrie KJ. Melatonin for the prevention and treatment of jet lag. Cochrane Database of Systematic Reviews, 2002.", "https://doi.org/10.1002/14651858.CD001520"),
}

JETLAG = {
    "path": "/jet-lag/",
    "trail": [],
    "title": "Jet lag: cómo recuperarte antes y qué comer",
    "desc": "Síntomas del jet lag, por qué cuesta más volar al este y cómo recuperarte de forma natural: horarios, luz, comida, café y melatonina. De una sobrecargo de largo radio.",
    "eyebrow": "Viajes · Jet lag",
    "h1": "Jet lag: cómo recuperarte",
    "lead": "Qué hacer antes, durante y después del vuelo para que tu cuerpo llegue cuanto antes a la hora del destino.",
    "intro": [
        "Soy nutricionista y sobrecargo de largo radio. Cruzo husos horarios varias veces al mes, así que el jet lag forma parte de mi trabajo.",
        "Aquí tienes lo que dicen los estudios y cómo lo aplico yo. Vale para unas vacaciones en Nueva York y para un viaje de trabajo a Tokio.",
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
                "Si vas hacia el este, acuéstate y levántate un poco antes los días previos y busca luz por la mañana. Si vas hacia el oeste, yo hago lo contrario: me acuesto un poco más tarde.",
            ],
        },
        {
            "h2": "En el avión: vive ya en la hora de destino",
            "ps": [
                "En cuanto subas, pon el reloj en la hora del destino y organízate según esa hora. Si allí es de noche, intenta dormir: antifaz, tapones y nada de pantallas. Si allí es de día, aguanta despierto, aunque sea con alguna siesta corta.",
                "Bebe agua durante todo el vuelo y nada de alcohol. Te ayuda a dormirte, pero rompe la segunda mitad de la noche: más despertares y menos sueño REM.[ebrahim] Incluso en poca cantidad, el cuerpo se recupera peor mientras duermes.[pietila] Y no hay una cantidad saludable: en el mayor análisis mundial, la cantidad de alcohol que menos daño hacía a la salud era cero.[gbd]",
            ],
        },
        {
            "h2": "La comida: a la hora del destino",
            "ps": [
                "El horario de las comidas también mueve relojes del cuerpo. En un estudio de la Universidad de Surrey, retrasar las comidas cinco horas retrasó casi seis horas el ritmo de la glucosa en sangre.[wehrens]",
                "No hay estudios buenos sobre alimentos concretos contra el jet lag.[herxbmj] Lo que sí puedes hacer es comer a las horas del sitio donde estás desde el primer día, aunque no tengas hambre.",
            ],
            "list_h": "Lo que hago yo al llegar",
            "list": [
                "Si llego por la mañana, un desayuno de verdad: huevos, fruta, pan, yogur.",
                "Comida y cena a la hora local, aunque sea algo pequeño.",
                "Cenas ligeras las primeras noches, para dormir mejor.",
                "Agua durante todo el día y nada de alcohol.",
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
            "h2": "Escalas cortas: a veces mejor no adaptarse",
            "ps": [
                "Si vas a estar solo uno o dos días, no siempre compensa cambiar de horario. En muchas escalas yo me quedo en la hora de casa y vuelvo casi sin jet lag.",
                "Lo explico con detalle en la <a href=\"/tripulaciones/\">guía gratuita para tripulaciones de largo radio</a>, pensada para escalas de 24 a 72 horas.",
            ],
        },
    ],
    "faq": [
        ("¿Cuánto dura el jet lag?", "Depende de cuántos husos horarios cruces y de la dirección. Hacia el este suele durar más que hacia el oeste, y cuantos más husos, más días tarda el cuerpo en ponerse en hora."),
        ("¿Cómo evitar el jet lag de forma natural?", "Empieza a mover tu horario unos días antes, vive en la hora de destino desde que subes al avión, come y duerme a la hora local, busca luz de día y deja el café para la primera parte del día."),
        ("¿Qué comer para el jet lag?", "No hay alimentos milagro, pero sí importa el horario: come a las horas del destino desde el primer día, con cenas ligeras las primeras noches, agua de sobra y nada de alcohol."),
        ("¿Qué síntomas tiene el jet lag?", "Dormir mal, cansancio durante el día, rendir menos, problemas de digestión y malestar general."),
        ("¿Funciona la melatonina para el jet lag?", "Es lo que más evidencia tiene, sobre todo en vuelos de cinco o más husos hacia el este, tomada cerca de la hora de acostarse en el destino. Antes de tomarla, consúltalo con un profesional."),
    ],
    "sources": ["herxbmj", "burgess", "ebrahim", "pietila", "gbd", "wehrens", "drake", "cochrane"],
    "cta": {
        "cta_h": "¿Viajas mucho por trabajo?",
        "cta_p": "En consulta preparamos tu plan para cada viaje: horarios de sueño, luz y comidas según tus rutas, con tus síntomas y tus analíticas delante. Online, en castellano o en inglés.",
        "cta_b2": ("Guía para tripulaciones", "/tripulaciones/"),
        "cta_note": 'Si vives en España, puedes hacerte las analíticas en <a href="https://diagnoseum.com/?utm_source=web-jet-lag&amp;utm_medium=referral" target="_blank" rel="noopener" data-umami-event="diagnoseum-jet-lag" style="color:#5e1a24;border-bottom:1px solid #c9b578">Diagnoseum</a>: eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins.',
    },
}
