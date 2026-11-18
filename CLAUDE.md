# Web de Paula Rubio Nutricionista

Web estática (HTML y CSS a mano, sin framework) publicada con GitHub Pages en https://paularubionutricionista.com. Lo que se sube a `main` sale en la web en uno o dos minutos. El repositorio es **público**: aquí no va nada privado (direcciones, datos de clientes, contraseñas, claves).

Paula es nutricionista integrativa y sobrecargo de largo radio. No es programadora: explícale las cosas sin jerga y avísale si algo puede poner en riesgo sus datos.

## Reglas de trabajo

- **Nunca publiques sin su OK.** Enseña antes capturas (ordenador y móvil) o una vista previa, y espera a que diga que sí. Después de publicar, comprueba que la página responde en la web real.
- Los commits, en castellano y describiendo el cambio.
- Si añades una página: enlázala desde el pie o desde otra página, añádela a `sitemap.xml` y recuérdale pedir la indexación en Search Console.
- Analítica con Umami. Añadiendo `?soy-paula` a cualquier URL, sus propias visitas no cuentan. Las acciones importantes llevan `data-umami-event`.

## Cómo escribir (textos de cara al público)

- En primera persona, con la voz de Paula: frases cortas y concretas, cercana y profesional. Se permite algún diminutivo («tomatitos», «cositas»).
- Nada de «modo Claude»: ni frases hechas, ni antítesis del tipo «no es X, es Y», ni cierres con moraleja, ni grandilocuencia.
- **Sin guiones** en la prosa: usa puntos, comas, dos puntos o paréntesis.
- Revisa tildes, puntuación y gramática antes de entregar nada.
- Masculino genérico para el público general; nada de fórmulas inclusivas.
- Terminología de aviación en castellano: «sobrecargo» (nunca «Inflight Manager»), «sala de firmas», «TCP» o «tripulaciones» (no «crew»). En inglés, «Inflight Manager» sí vale.
- **No nombres a British Airways** ni a ninguna aerolínea concreta como su empresa.
- Nunca enlaces a productos (Amazon, tiendas, marcas). El nombre del producto puede ir como texto.
- **Nunca se publican dosis** de suplementos ni medicamentos (melatonina, etc.): se dice qué dice la evidencia y se remite a consultarlo con un profesional.
- Todo dato de salud se contrasta con fuentes (PubMed, con su DOI) y las fuentes van listadas al final de la página. Nada de memoria.
- Diagnoseum (empresa de analíticas de la que Paula es cofundadora): se menciona para quien vive en España, también en las páginas en inglés (hay muchos extranjeros en España que buscan en inglés). Fórmula aprobada: «eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins». En inglés: «you choose exactly what you want to test, no doctor's referral needed, backed by Eurofins». Nunca «tu médico no sabe/no mide esto». Los enlaces a diagnoseum.com llevan parámetros `utm_`.

## Estructura

- `index.html`, `en/index.html`: portada en castellano y en inglés.
- `planes/`, `recetas/`: planes y recetas (los generan `tools/planes/` y `tools/recetas/`).
- `tripulaciones/` y `en/cabin-crew/`: páginas de la guía gratuita para tripulaciones, con formulario. Se generan con `python3 tools/crew/build.py` (textos en `tools/crew/content.py`).
- `turnos/`: bloque de trabajo a turnos (página general y dos artículos). Se genera con `python3 tools/turnos/build.py` (textos y fuentes en `tools/turnos/content.py`; los artículos en inglés, en `tools/turnos/content_en.py`, con `lang`, y `alt` para la página gemela). El mismo generador hace los artículos de viajes, como `/jet-lag/` (textos en `tools/turnos/content_viajes.py`); con `trail` y `cta` se cambian las migas y el recuadro final de cada página. Las citas se escriben `[clave]` en el texto y se convierten en notas numeradas.
- Las páginas generadas copian la cabecera y el pie de `planes/glow/index.html` (castellano) o de `en/index.html` (inglés). Si cambias el pie, cámbialo en todas las páginas y vuelve a generar.
- `guias/` y `en/guides/`: índice de guías y recursos (lleva a él «Guías» del menú y el botón del banner de la portada). Se genera con `python3 tools/guias/build.py`. **Cada página nueva que se publique se añade a su lista** y se vuelve a generar.
- El menú de arriba está copiado en cada página: si se cambia, hay que cambiarlo en todas y volver a generar.
- `tools/crew/emails.py`: genera el HTML de los correos de Brevo (en `tools/crew/emails/`). Si se cambian, hay que pegarlos también en Brevo.

## Guía gratuita y correos (Brevo)

- El formulario de la web envía el correo a Brevo (casilla de consentimiento obligatoria). Listas: «Guía tripulaciones ES» y «Crew guide EN».
- Cada lista dispara una automatización: correo con el enlace a la guía al momento y correo de seguimiento a los 6 días. Remitente: hola@paularubionutricionista.com.
- Los PDF de las guías **no** van en este repositorio (es público). Están en el Drive de la cuenta de la marca y se enlazan solo desde los correos.
- La política de privacidad ya explica el envío de guías con Brevo. Si se añade otro formulario u otra herramienta, hay que actualizarla (castellano e inglés).

## Plan SEO

Búsquedas reales (autocompletado de Google, noviembre de 2026). Nadie busca «nutricionista para tripulaciones»: se busca el problema concreto. Cada página de entrada responde a uno y lleva a la guía o a la consulta.

Hecho:
1. Páginas de la guía de tripulaciones (ES y EN).
2. Bloque de turnos en castellano: `/turnos/`, «qué comer en el turno de noche» y «cómo dormir después de un turno de noche».
3. Turnos en inglés: `/en/what-to-eat-on-night-shift/` (gemela de «qué comer en el turno de noche», enlazada en el pie inglés). Falta una página general de turnos y el artículo de sueño en inglés.

Siguiente, por orden:
4. **Artículos de tripulaciones**:
   - Jet lag en castellano: «jet lag cómo recuperarse», «cómo evitar el jet lag de forma natural», «jet lag comida», «síntomas».
   - Jet lag en inglés: «how to beat jet lag going east / west», «UK to USA», «UK to Australia», «jet lag eating schedule / meal times».
   - «Qué comer antes de un vuelo largo» (qué llevar para comer en el avión, retención de líquidos en el avión, estreñimiento viajero).
   - «Cabin crew meal prep» en inglés (flight attendant meal prep ideas, what do flight attendants eat on long haul flights). Hoy solo hay blogs y redes sociales: hueco claro.
5. **Ciudades**: «nutricionista integrativa online en {ciudad}» (Madrid, Barcelona, Valencia, Sevilla, Bilbao, Zaragoza, Málaga, Alicante, Granada, Valladolid, Oviedo, Gijón). Cada una con contenido local real (los laboratorios de Diagnoseum de esa ciudad) para que no sean páginas copiadas.
6. Escalada, si Paula quiere esos clientes.

Descartado: «dieta azafata 4 días» (busca dietas exprés para perder peso; no es su clienta).

Pendiente de indexación: `/planes/` y las cuatro recetas están «descubiertas, sin indexar». Hay que enlazarlas más desde otras páginas (artículos y portada) y pedir su indexación.
