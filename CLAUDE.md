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
- Diagnoseum (empresa de analíticas de la que Paula es cofundadora): se menciona para quien vive en España, también en las páginas en inglés (hay muchos extranjeros en España que buscan en inglés). Fórmula aprobada: «eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins». En inglés: «you choose exactly what you want to test, no doctor's referral needed, backed by Eurofins». Nunca «tu médico no sabe/no mide esto». Los enlaces a diagnoseum.com llevan parámetros `utm_`. Diagnoseum es intermediario y no tiene dirección propia: quien compra puede sacarse la sangre en **cualquier centro Eurofins** de España y, en Madrid, también en los de **Abolab**. En la web no se ponen direcciones concretas de centros (cambian y no se pueden comprobar desde aquí): se dice «en cualquier centro Eurofins de {ciudad}».

## Estructura

- `index.html`, `en/index.html`: portada en castellano y en inglés.
- `planes/`, `recetas/`: planes y recetas (los generan `tools/planes/` y `tools/recetas/`).
- `tripulaciones/` y `en/cabin-crew/`: páginas de la guía gratuita para tripulaciones, con formulario. Se generan con `python3 tools/crew/build.py` (textos en `tools/crew/content.py`).
- `turnos/`: bloque de trabajo a turnos (página general y dos artículos). Se genera con `python3 tools/turnos/build.py` (textos y fuentes en `tools/turnos/content.py`; los artículos en inglés, en `tools/turnos/content_en.py`, con `lang`, y `alt` para la página gemela). El mismo generador hace los artículos de viajes, como `/jet-lag/` (textos en `tools/turnos/content_viajes.py`); con `trail` y `cta` se cambian las migas y el recuadro final de cada página. Las citas se escriben `[clave]` en el texto y se convierten en notas numeradas.
- Las páginas generadas copian la cabecera y el pie de `planes/glow/index.html` (castellano) o de `en/index.html` (inglés). Si cambias el pie, cámbialo en todas las páginas y vuelve a generar.
- `guias/` y `en/guides/`: índice de guías y recursos (lleva a él «Guías» del menú y el botón del banner de la portada). Se genera con `python3 tools/guias/build.py`. **Cada página nueva que se publique se añade a su lista** y se vuelve a generar.
- `nutricionista-online/{ciudad}/` y `en/nutritionist/{ciudad}/`: páginas de consulta online por ciudad (ES y EN, gemelas). Se generan con `python3 tools/ciudades/build.py`; para añadir una ciudad, se añade a `CIUDADES`, al índice de guías y al sitemap.
- El menú de arriba está copiado en cada página: si se cambia, hay que cambiarlo en todas y volver a generar.
- `tools/crew/emails.py`: genera el HTML de los correos de Brevo (en `tools/crew/emails/`). Si se cambian, hay que pegarlos también en Brevo.

## Lo que dicen las guías (leer antes de escribir de viajes o tripulaciones)

Los PDF no están en el repositorio, así que aquí van sus reglas. **Antes de escribir cualquier artículo de viajes, jet lag o tripulaciones, comprueba que no las contradice** (y si hace falta, pide a Paula los PDF).

- Escalas de **menos de 48 horas**: no adaptarse a la hora local. Dormir lo más cerca posible de la noche de casa y comer en horario de casa (en línea con lo que recomienda la OACI para tripulaciones).
- Escalas de **más de 48 horas**: dormir en la noche local, haciendo que al menos 4 horas de sueño coincidan con la noche de casa; luz natural de día; comer en horario local (si se come en la noche biológica, algo ligero).
- Entre las 00:00 y las 6:00 de casa es la noche biológica: si se come, algo ligero y fácil de digerir.
- Volar al oeste se lleva mejor que al este: el reloj se retrasa unos 92 minutos al día tras volar al oeste y solo se adelanta unos 57 tras volar al este (Eastman y Burgess, 2009).
- Vuelo nocturno al este con 8 husos o más: gafas de sol a primera hora al llegar.
- Cafeína en la primera mitad de la jornada, poco a poco, y nada en las 6 horas antes de dormir.
- Alcohol: la guía dice «empeora el sueño y la deshidratación; si bebes, que sea poco, con comida y lejos de la hora de dormir». En la web Paula prefiere: «el alcohol, en realidad, no ayuda a dormir». Paula no bebe: no ponerle en boca que toma alcohol.
- No poner en primera persona prácticas de Paula que no estén en las guías o que ella no haya confirmado.
- Corto radio (confirmado por Paula): empezó su carrera con cuatro años en corto radio, rotaciones de 4 a 6 saltos con escalas de 25 minutos, semanas de madrugones y semanas de tardes, comida traída de casa (sin comida de tripulación a bordo) y calentada en el horno del avión; comían en la escala si aterrizaban antes o en vuelo después del servicio de venta. No recomienda el agua caliente del avión. **No todas las compañías de corto radio vuelven a base: algunas pernoctan**; no decir que en corto radio no se hace noche fuera.

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
3. Turnos en inglés: `/en/what-to-eat-on-night-shift/` y `/en/how-to-sleep-after-night-shift/` (gemelas de los artículos en castellano). Falta una página general de turnos en inglés.
4a. Jet lag: `/jet-lag/` y `/en/jet-lag/` (para viajeros; aviso para TCP con escalas cortas y la regla de las 48 horas).
4b. «Qué comer antes de un vuelo largo»: `/que-comer-antes-de-un-vuelo-largo/` (líquidos en el control: depende de cada aeropuerto, remitir a confirmarlo con su seguridad).
4c. «Cabin crew meal prep»: `/en/cabin-crew-meal-prep/` (a partir de la guía en inglés).
4d. TCP de corto radio: `/tcp-corto-radio-que-comer/` y `/en/short-haul-cabin-crew-food/` (madrugones, varios saltos, electrolitos, agua del avión). Enlazado desde las páginas de Madrid y Barcelona.
5a. Ciudades, primera tanda: Madrid, Barcelona, Vigo y Santander, en castellano y en inglés. Esperar a ver en Search Console si funcionan antes de hacer más.

Siguiente, por orden:
5. **Ciudades**: «nutricionista integrativa online en {ciudad}» (Madrid, Barcelona, Valencia, Sevilla, Bilbao, Zaragoza, Málaga, Alicante, Granada, Valladolid, Oviedo, Gijón). Cada una con contenido local real (los laboratorios de Diagnoseum de esa ciudad) para que no sean páginas copiadas.
6. Escalada, si Paula quiere esos clientes.

Descartado: «dieta azafata 4 días» (busca dietas exprés para perder peso; no es su clienta).

Pendiente de indexación: `/planes/` y las cuatro recetas están «descubiertas, sin indexar». Hay que enlazarlas más desde otras páginas (artículos y portada) y pedir su indexación.
