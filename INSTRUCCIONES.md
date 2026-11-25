# PuntoBEC · Publicación diaria en LinkedIn (versión NUBE)
Versión 3.1 · 25/11/2026 (investigación y publicación en rutinas separadas). Lo ejecutan las rutinas en la nube de Claude, sin el ordenador del usuario, sin Chrome y sin archivos locales. Idioma de trabajo: español de España.

- **Página:** PuntoBEC, https://www.linkedin.com/company/145510157 (organización 145510157).
- **Repositorio (esta carpeta):** InstalacionesBEC/puntobec-linkedin. Es público, así que **nunca guardes en él datos personales, tokens ni nada privado**.
- **Para publicar y leer datos de PuntoBEC:** conector **Zapier** (app LinkedIn) con
  - `connection_id` = `02637f23-81cb-8957-a74b-c88e37d4a469` (siempre explícito);
  - `company_id` = `145510157`.
- **No uses Buffer nunca.**

## REGLA PRINCIPAL
Cada ejecución investiga, selecciona, redacta, diseña, publica y verifica ÚNICAMENTE la publicación de HOY, a la hora fijada de hoy. Nunca prepares publicaciones de otros días ni muevas una publicación a otro día.

| Día | Inicio (Madrid) | Publicación (Madrid) |
|---|---|---|
| Lunes | 06:00 | 09:00 |
| Martes | 19:31 | 22:31 |
| Miércoles | 11:33 | 14:33 |
| Jueves | 12:03 | 15:03 |
| Viernes | 12:38 | 15:38 |
| Sábado | 08:00 | 11:00 |
| Domingo | 16:00 | 19:00 |

LinkedIn no tiene programación nativa a través de la API. Por eso cada día hay **DOS rutinas** (desde el 25/11/2026; antes una sola rutina esperaba 3 h con `sleep` y la espera podía cortarse):

- **Rutina de INVESTIGACIÓN** (se activa a la hora de "Inicio"): hace los PASOS 0, 1, 2 y 3 y **termina** con `estado: LISTA`. **No espera y no publica.**
- **Rutina de PUBLICACIÓN** (se activa a la hora de "Publicación"): hace solo el apartado "RUTINA DE PUBLICACIÓN" (PASOS 4 y 5) con lo que dejó lista la de investigación.

**Nunca uses `sleep` largos ni bucles de espera.** Si tu rutina es la de investigación, termina al dejar la publicación LISTA.

## PASO 0 · Comprobaciones (rutina de INVESTIGACIÓN)
1. Ejecuta `TZ=Europe/Madrid date '+%F %u %H:%M'`. Cada rutina se activa dos veces, en las dos horas UTC posibles, para cubrir el horario de verano y el de invierno. **Continúa solo si el día coincide con el de la rutina y la hora de Madrid está a ±20 min del "Inicio".** Si no, termina en silencio, sin registrar nada.
2. Con `git checkout -B main origin/main && git pull origin main`, comprueba si existe `datos/publicaciones/AAAA-MM-DD.md` con estado PUBLICADA, LISTA, PUBLICANDO o EN CURSO. Si existe, termina, para evitar duplicados.
3. Crea ese archivo con `estado: EN CURSO` y la hora de inicio. Haz commit y push (ver "Guardar en el repositorio").
4. Si la hora de publicación de hoy ya ha pasado o faltan menos de 20 min, registra "EJECUCIÓN TARDÍA: hueco sin publicar" y termina.

## PASO 1 · Investigación del día (máximo 60 min)
Temas:
- mentalidad y hábitos;
- concentración, foco y productividad;
- negocios y emprendimiento;
- toma de decisiones;
- paz mental y gestión de la sobrecarga;
- libertad de tiempo y relación entre trabajo, dinero y bienestar.

**MODO GRATUITO (decisión del usuario, 24/11/2026).** LinkedIn rechaza con error 403 las conexiones desde la nube cuando no hay sesión iniciada. Por eso **no se analizan publicaciones de terceros en LinkedIn**.
- No intentes saltar ese bloqueo: nada de cambiar el user-agent, usar proxies, scrapers ni servicios de terceros.
- La investigación se basa en actualidad verificable y en conversaciones públicas accesibles.
- Cada registro debe decir literalmente: "Sin análisis de publicaciones de LinkedIn de terceros (modo gratuito)".

**A) Noticias y estudios de actualidad (obligatorio)**
- Con WebSearch, haz al menos 8 consultas en español y en inglés sobre los temas, con prioridad a las últimas 24–48 h y ampliando hasta 7 días si hace falta (déjalo escrito). Ejemplos:
  - "estudio productividad noviembre 2026";
  - "burnout encuesta trabajadores";
  - "decision fatigue study";
  - "emprendedores España informe";
  - "semana laboral 4 días";
  - "salud mental trabajo datos".
- Abre las candidatas con WebFetch y verifícalas en su **fuente original**: el estudio, el organismo o el medio que publicó primero.
- Si WebFetch no puede abrir la fuente (dominio no permitido o bloqueo), confirma el dato con al menos 2 resultados independientes de WebSearch. Márcalo como "verificado solo por buscador" y sé prudente al citarlo.

**B) Conversación pública e interacción observable**
Busca señales de que el tema genera debate ahora mismo y anota las cifras **visibles**, con la hora UTC de la captura:
- Hacker News: `https://hn.algolia.com/api/v1/search_by_date?query=<tema>&tags=story` (puntos y comentarios).
- Reddit, si es accesible: `https://www.reddit.com/r/<sub>/search.json?q=<tema>&sort=top&t=week` (votos y comentarios).
- Comentarios en los medios.
- Cualquier otra fuente pública que se abra sin sesión.

Si una fuente no es accesible, anótalo y sigue sin ella. No inventes cifras. Las fuentes en inglés valen como señal de tendencia, pero el post se escribe para la audiencia hispanohablante.

**C) Regla de mínimos (obligatoria)**
- Para publicar hacen falta **al menos 3 fuentes de actualidad de los últimos 7 días, verificadas** (fuente original o 2 resultados independientes).
- Al menos una debe tener **interacción o debate observable** (cifras o comentarios visibles).
- **Antes de declarar la investigación insuficiente es obligatorio:**
  - haber dedicado **al menos 30 minutos** a investigar;
  - haber hecho **al menos 12 consultas** de WebSearch;
  - haber abierto con WebFetch **al menos 10 candidatas**. Que una fuente aparezca solo en el buscador no basta para descartarla: ábrela.

  La red del entorno tiene acceso completo, así que los medios y los estudios se pueden abrir. Si algún dominio concreto falla (por ejemplo, reddit.com), sigue con otros.
- Una fuente cuenta como "de los últimos 7 días" si su fecha de publicación está en esa ventana. También cuenta un informe más antiguo si se ha publicado sobre él una noticia nueva dentro de la ventana.
- Si no se cumple, NO publiques: registra "INVESTIGACIÓN INSUFICIENTE" con el motivo y con el número de consultas, de fuentes abiertas y de minutos. Deja el hueco sin publicar.
- Nunca uses los borradores de reserva para llenar el hueco.

**D) Selección**
- Puntúa cada finalista de 1 a 5 en:
  - actualidad;
  - interacción relativa a la antigüedad y a la audiencia del autor;
  - calidad de la conversación;
  - relevancia para PuntoBEC;
  - margen para una perspectiva propia.
- Elige el tema con **mayor interacción y conversación demostrables en la muestra**.
- Reglas:
  - Una cuenta grande no hace excepcional un tema.
  - No digas que algo "crece rápido" si lo has observado una sola vez.
  - No presentes la muestra como ranking de LinkedIn.
  - No inventes métricas.

Guarda `datos/investigacion/AAAA-MM-DD.md` con:
- consultas y fuentes;
- tabla de finalistas;
- puntuaciones;
- tema elegido y motivo;
- limitaciones.

## PASO 2 · Redacción
Contenido **original**: no copies ni parafrasees la publicación elegida.

Estructura:
- Un comienzo concreto que despierte interés sin engañar (las 2 primeras líneas son decisivas).
- Una idea útil y bien desarrollada.
- Un ejemplo o una aplicación práctica.
- Un cierre con una pregunta concreta o un punto de debate que se pueda responder con experiencia.

Formato:
- Entre 150 y 260 palabras, en párrafos cortos.
- Si citas una noticia o un estudio, indica la fuente sin exagerar.

Prohibido:
- motivación genérica;
- polémica artificial;
- culpabilizar al lector;
- "comenta X", "dale like" o "etiqueta a…";
- inventar experiencias, testimonios, cifras o resultados de PuntoBEC o de Cipri;
- prometer riqueza o viralidad.

Antes de elegir, lee `datos/aprendizajes.md` y las 3 últimas publicaciones de `datos/publicaciones/` para no repetir tema, comienzo, pregunta ni estilo.

**Formato de texto de LinkedIn (campo `comment`):**
- Máximo 3000 caracteres.
- Escapa con `\` los caracteres reservados: `| { } @ [ ] ( ) < > # * _ ~ \`. Por ejemplo, `\(texto\)`.
- Lo más sencillo es evitarlos y no usar hashtags.
- Deja `allow_reserved_characters` en su valor por defecto.

## PASO 3 · Imagen (obligatoria)
1. Escribe `datos/graficos/AAAA-MM-DD.json` para `scripts/tarjeta.py`, adaptado a ESTA publicación.
   - Estilos disponibles: "titular", "lista", "comparacion" (bloques "Título|texto") y "dato" (cifra verificable con fuente en `dato_texto`).
   - Campos: etiqueta, titular (resume el aprendizaje en 4–14 palabras, no la primera frase), pregunta y tema "claro" u "oscuro".
   - Alterna estilo y tema respecto al día anterior.
2. Genera la imagen: `python3.13 scripts/tarjeta.py datos/graficos/AAAA-MM-DD.json datos/graficos/AAAA-MM-DD.png`. Usa `python3.13`, porque con `python3` Pillow falla.
3. Ábrela con Read y revísala: texto cortado, solapes, erratas y legibilidad. Si algo falla, corrígelo y vuelve a generarla.
4. Haz commit y push de la imagen.
5. Comprueba con WebFetch que la URL pública responde: `https://raw.githubusercontent.com/InstalacionesBEC/puntobec-linkedin/<rama>/datos/graficos/AAAA-MM-DD.png`.
6. Guarda en `datos/publicaciones/AAAA-MM-DD.md`, con `estado: LISTA`:
   - el texto final, ya escapado, bajo el encabezado exacto `## Texto final` (y nada más hasta el siguiente encabezado `## `);
   - el JSON;
   - la línea `imagen: <URL raw>`.
   Haz commit y push.
   - Si al terminar faltan menos de 10 min para la hora de publicación (o ya ha pasado), no pongas LISTA: pon `estado: SIN PUBLICAR` con el motivo "investigación no terminada a tiempo".
7. Añade a `datos/registro.md` la entrada del PASO 5 con todo lo de la investigación y "Publicación: pendiente de la rutina de publicación". **Termina aquí. No esperes ni publiques.**

## RUTINA DE PUBLICACIÓN (PASOS 4 y 5)
Solo para la rutina de PUBLICACIÓN. No investigues ni reescribas el texto.

### PASO 4.0 · Comprobaciones
1. Ejecuta `TZ=Europe/Madrid date '+%F %u %H:%M'`. **Continúa solo si el día coincide y la hora de Madrid está entre la hora de "Publicación" y 15 min después.** Si es antes de la hora o más de 60 min después, termina en silencio (es la activación de la otra hora UTC). Si han pasado entre 15 y 60 min, registra la INCIDENCIA "rutina de publicación activada tarde: hueco sin publicar", pon `estado: SIN PUBLICAR` y termina.
2. `git config user.name "Claude"`, `git config user.email "noreply@anthropic.com"`, `git checkout -B main origin/main && git pull origin main`.
3. Lee `datos/publicaciones/AAAA-MM-DD.md` (fecha de HOY).
   - Si está PUBLICADA o PUBLICANDO: termina (evita duplicados).
   - Si no existe o está EN CURSO: la investigación no terminó. Pon `estado: SIN PUBLICAR` con el motivo "la investigación no dejó la publicación lista", añádelo al registro, haz push y termina. **Nunca publiques un borrador de reserva para cubrir el hueco.**
   - Si está SIN PUBLICAR o INCIDENCIA: termina.
   - Solo si está **LISTA**, continúa.
4. Comprueba con WebFetch que la URL de la imagen (línea `imagen:`) responde. Si no responde, INCIDENCIA y no publiques.
5. Cambia el estado a `PUBLICANDO`, haz commit y push. Si el push falla por conflicto, vuelve a hacer pull y repite la comprobación 3.

### PASO 4 · Publicar
1. Publica ya (no esperes: la rutina ya se activa a la hora).
2. Publica con Zapier: `execute_zapier_write_action` → `linkedin_create_company_update`. Parámetros:
   - `connection_id` = `02637f23-81cb-8957-a74b-c88e37d4a469`;
   - `company_id` = `145510157`;
   - `comment` = el texto de `## Texto final`, exactamente como está guardado;
   - `image` = URL pública raw de la imagen;
   - `image_type` = `post_media`.
3. Llama UNA sola vez. Si falla, revisa el error, corrige y reintenta **una vez como máximo**.
   - Si vuelve a fallar, NO publiques sin imagen: registra la INCIDENCIA y deja el hueco.
   - Nunca publiques fuera de la hora (más de 15 min tarde): registra la incidencia.
4. **Verifica:**
   - Guarda el id o la URL que devuelva Zapier.
   - Si linkedin.com es accesible, abre la publicación o la página con WebFetch y comprueba el texto y la imagen.
   - Si no lo es, usa como máximo una vez `linkedin_make_api_get_request` GET `https://api.linkedin.com/rest/posts?q=author&author=urn%3Ali%3Aorganization%3A145510157&count=3` con la cabecera `LinkedIn-Version: 202610` (consume 2 tareas de Zapier).
   - Confirma: PuntoBEC, fecha y hora, primeras palabras e imagen. Solo entonces el estado es PUBLICADA.
5. **Presupuesto de Zapier:** el plan gratuito da 100 tareas al mes y cada acción correcta consume 2. Evita llamadas innecesarias. Si Zapier indica que se ha agotado el límite, registra la INCIDENCIA.

Autorización del usuario: publicar la publicación de HOY sin aprobación individual, dentro de estas reglas. No publiques respuestas a comentarios, no edites ni borres publicaciones y no cambies ajustes de la página.

## PASO 5 · Registro (commit y push al final)
La rutina de investigación escribe la entrada completa (ver PASO 3.7). La rutina de publicación solo completa las líneas "Publicación" y "Tareas de Zapier usadas hoy" de la entrada de hoy.

Actualiza `datos/publicaciones/AAAA-MM-DD.md` con el estado final: PUBLICADA, SIN PUBLICAR con motivo, o INCIDENCIA.

Añade a `datos/registro.md`:
```
## AAAA-MM-DD (día) · inicio HH:MM → publicación HH:MM (Madrid) · NUBE
- Fuentes consultadas: consultas de búsqueda, noticias y estudios (enlaces; fuente original o "verificado solo por buscador") y señales de conversación (fuente, cifras visibles y hora UTC). Incluye: "Sin análisis de publicaciones de LinkedIn de terceros (modo gratuito)".
- Ventana: 24-48 h o ampliada a 7 días (motivo).
- Tema seleccionado y motivo, con las puntuaciones.
- Enfoque original de PuntoBEC:
- Conversación que se busca provocar:
- Imagen: estilo y URL.
- Publicación: VERIFICADA (id o URL, hora real, imagen sí o no) o INCIDENCIA (detalle).
- Tareas de Zapier usadas hoy:
- Intervención manual necesaria: sí o no (cuál).
```

## Guardar en el repositorio
- Al empezar, configura `git config user.name "Claude"` y `git config user.email "noreply@anthropic.com"`.
- Comprueba **al principio** que puedes escribir en el repositorio: haz el commit del estado EN CURSO y el push.
  - Si el push devuelve 403, la app de Claude en GitHub no tiene permiso de escritura. Sin repositorio no hay URL pública para la imagen, así que no se puede publicar.
  - En ese caso, registra la INCIDENCIA "GitHub sin permiso de escritura: instalar la app Claude de GitHub en el repositorio", envía una notificación y termina sin investigar, para no gastar recursos.
- Intenta `git push origin HEAD:main`.
- Si el push a `main` está prohibido, usa la rama `claude/puntobec-datos`. En ese caso:
  - haz pull y push siempre en esa rama;
  - usa esa rama en las URL raw;
  - anótalo en el registro.
- Haz commit al menos en estos momentos:
  - al crear el estado EN CURSO;
  - después de generar la imagen;
  - al terminar.
