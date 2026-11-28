# Registro PuntoBEC LinkedIn

## 2026-11-24 · configuración inicial (sesión interactiva)
- Acceso de administrador a PuntoBEC verificado en Chrome. Antes de empezar: 0 publicaciones programadas y 0 publicadas. 0 seguidores.
- Buffer: la cola del canal 6b058f8d8541f09ecb89b010 estaba vacía a las 14:31 (comprobado antes de abandonar Buffer). El conector de Buffer se desconectó después y no se ha vuelto a comprobar. Buffer no se usa ni se modifica.
- Investigación: ~25 publicaciones (búsqueda en LinkedIn, semana o mes pasado). Se leyeron las cifras de la tarjeta de resultados, sin abrir cada publicación ni obtener enlaces → investigacion/2026-11-24.md
- Programadas y VERIFICADAS en la lista de programadas de LinkedIn (solo texto):
  - mar 24/11 22:31 · "Hoy, antes de dormir, haz una prueba de 5 minutos con tu día."
  - mié 25/11 14:33 · "\"Se necesitan 21 días para crear un hábito.\""
  - jue 26/11 15:03 · "¿Cuántas horas de tu vida cuesta lo último que compraste?"
  - vie 27/11 15:38 · "Cada \"sí\" tiene un precio que no viene escrito."
  - sáb 28/11 11:00 · "Opinión: la libertad de tiempo no consiste en trabajar menos."
  - dom 29/11 19:00 · "Domingo por la tarde. Antes de planificar la semana, prueba a quitar algo."
  - lun 30/11 09:00 · "Lunes, 9 de la mañana. Si te está costando empezar, quizá no te falte motivación."
- Siguiente hueco a cubrir: mar 01/12 22:31 (lo cubre la tarea diaria del 25/11).

## 2026-11-24 · cambio de funcionamiento (sesión interactiva, ~15:10–15:30)
- Nueva regla: cada publicación se basa en la investigación del MISMO día. Se anula el colchón de 7 días.
- Las 7 publicaciones programadas del 24/11 al 30/11 se han ELIMINADO de la programación de LinkedIn (ninguna había salido). Se ha verificado que la lista de programadas de PuntoBEC está vacía ("Aún no hay publicaciones programadas"). Los textos están guardados en reserva-borradores/borradores-2026-11-24.md (no se publicarán automáticamente).
- Tareas: la antigua "diaria 08:25" pasa a ser la del lunes (06:00). Se han creado las de martes a domingo, con inicio 3 h antes de cada publicación. Todas siguen INSTRUCCIONES.md.
- Gráfico obligatorio: scripts/tarjeta.py (PNG 1080x1350, estilos titular, lista, comparación y dato). Se ha probado la subida con file_upload en el editor de LinkedIn: funciona desde la carpeta de trabajo de la sesión, pero NO desde datos/ (Chrome no tiene permiso para leer esa carpeta). Se ha probado también el texto alternativo. El borrador de prueba se ha descartado sin publicar.
- PENDIENTE: ninguna ejecución automática ha usado Chrome todavía. La primera prueba real será la del martes 24/11 a las ~19:39.

## 2026-11-24 · migración a la nube (sesión interactiva)
- Verificado desde la nube (sin publicar): Zapier + LinkedIn conectados (conexión "Ciprian Corneliu Bec"); PuntoBEC (145510157) seleccionable; lectura de publicaciones y estadísticas de PuntoBEC por API GET funciona (0 publicaciones); raw.githubusercontent.com accesible; www.linkedin.com NO accesible desde la nube (falta permitirlo en la red del entorno).
- Las 7 publicaciones programadas en LinkedIn ya se habían cancelado. Instrucciones v3 (nube) en INSTRUCCIONES.md.
- 24/11 ~17:10: LinkedIn devuelve 403 a la nube. El usuario elige el MODO GRATUITO: investigación con noticias y estudios verificados y conversación pública (HN, Reddit…), sin análisis de publicaciones de LinkedIn de terceros. Instrucciones actualizadas.

## 2026-11-24 (martes) · inicio 19:31 → publicación 22:31 · NUBE · SIN PUBLICAR
- Causas: (1) la rutina no pudo escribir en GitHub (403: la app Claude de GitHub no tiene permiso de escritura en el repositorio), así que no había URL pública para la imagen; (2) declaró la investigación insuficiente en 98 s, con 1 fuente verificada (HN "burnout from agentic coding", 7 puntos y 9 comentarios), sin abrir otras candidatas de noviembre de 2026 que tenía en el buscador.
- Corrección (25/11, sesión interactiva): investigación mínima obligatoria (30 min, 12 consultas, 10 fuentes abiertas) antes de declararla insuficiente, y comprobación de escritura en GitHub al empezar. Pendiente: instalar la app Claude de GitHub en el repositorio.
- Zapier: 0 tareas usadas.

## 2026-11-25 (miércoles) · inicio 11:34 → publicación 14:33 (Madrid) · NUBE
- Fuentes consultadas: ~30 consultas de búsqueda; ~24 fuentes abiertas (detalle en investigacion/2026-11-25.md). Originales: Adecco Group GWoF 19/11 (comunicado, Fortune, healthnews.pt), Rest of World 19/11 (Hacker News 152 puntos y 84 comentarios, captura 25/11 ~10:36 UTC), Lyra Health 2026 con noticia diario.mx 21/11; Gallup 16/11 como contexto. Reddit y varios medios bloqueados (403). Sin análisis de publicaciones de LinkedIn de terceros (modo gratuito).
- Ventana: ampliada a 7 días (18-25/11) por falta de estudios en 24-48 h.
- Tema: quién decide cómo cambia tu trabajo cuando la IA te ahorra tiempo. Puntuación 23/25 (frente a 17, 13 y 12).
- Enfoque original de PuntoBEC: pauta de decidir por escrito qué hacer con el tiempo recuperado; sin experiencias inventadas.
- Conversación que se busca provocar: qué pasa con la hora ahorrada (más trabajo, salir antes u otra cosa).
- Imagen: estilo dato, tema claro, https://raw.githubusercontent.com/InstalacionesBEC/puntobec-linkedin/main/datos/graficos/2026-11-25.png. Corregido scripts/tarjeta.py (glob recursivo; antes no encontraba fuentes y fallaban los acentos).
- Publicación: VERIFICADA por la respuesta de Zapier (id urn:li:share:7531349357762310144, 14:33 Madrid, imagen sí). No se abrió LinkedIn.
- Tareas de Zapier usadas hoy: 2.
- Intervención manual necesaria: no. Nota: push directo a main funcionó.

## 2026-11-25 · cambio: investigación y publicación separadas (sesión interactiva, ~14:45)
- Motivo: el 25/11 la rutina esperó 3 h en segundo plano hasta las 14:33; la espera se cortó una vez a las ~13:38 y solo se recuperó porque la sesión se reactivó. Publicó bien (14:33:32), pero el método era frágil.
- Ahora cada día hay dos rutinas: INVESTIGAR (hora de inicio; termina en estado LISTA, sin esperar) y PUBLICAR (hora exacta de publicación; solo publica lo que esté LISTA). Ver INSTRUCCIONES.md v3.1.
- Primera prueba real del nuevo sistema: jueves 26/11 (investigación 12:03, publicación 15:03).

## 2026-11-26 (jueves) · inicio 12:03 → publicación 15:03 (Madrid) · NUBE
- Fuentes consultadas: 19 consultas de búsqueda; ~30 fuentes abiertas (detalle en investigacion/2026-11-26.md). Verificadas: Deloitte Encuesta Global 2026 Gen Z y millennials (PDF original; noticia El Economista 26/11), Anthropic "Working with AI" 23/11 (original), Lyra Health 2026 con noticia diario.mx 21/11. Conversación: Hacker News "Why aren't we working 2-days a week?" 62 puntos y 84 comentarios, "Working with AI" 89 puntos y 76 comentarios (captura 26/11 ~11:05 UTC). Reddit y fastcompany bloqueados. Sin análisis de publicaciones de LinkedIn de terceros (modo gratuito).
- Ventana: ampliada a 7 días (19-26/11): el buscador devuelve poco material de 24-48 h; se aceptan informes anteriores con noticia nueva en la ventana.
- Tema: necesitar parar vs poder parar (Deloitte 71% vs 41%). Puntuación 21/25 (frente a 19, 19 y 15).
- Enfoque original de PuntoBEC: definir antes de la crisis una señal de parada y un plan de cobertura, sobre todo para quien trabaja por su cuenta; sin experiencias inventadas.
- Conversación que se busca provocar: qué permitió o habría permitido parar a tiempo sin culpa.
- Imagen: estilo comparacion, tema oscuro, https://raw.githubusercontent.com/InstalacionesBEC/puntobec-linkedin/main/datos/graficos/2026-11-26.png (URL comprobada).
- Publicación: VERIFICADA por respuesta de Zapier (lifecycleState PUBLISHED, autor organización 145510157, imagen sí, texto íntegro), urn:li:share:7531719758694666240, hacia las 15:05 Madrid. Primer intento falló con "Could not find entity"; el reintento (único) funcionó.
- Tareas de Zapier usadas hoy: 2 (la llamada fallida no debería consumir).
- Intervención manual necesaria: no. Limitación: debate observable de una sola fuente (HN); el reloj del entorno marcó solo unos minutos de investigación.

## 2026-11-26 · incidencia: publicación DUPLICADA (revisión en sesión interactiva)
- La rutina de publicación (15:04) llamó a Zapier; la primera llamada devolvió el error "Could not find entity" pero la publicación SÍ salió. El reintento (15:05) creó una segunda publicación idéntica (urn:li:share:7531719758694666240). La rutina de investigación no publicó nada.
- Corrección: tras un error de Zapier ya no se reintenta a ciegas; primero se comprueba con un GET si la publicación existe (INSTRUCCIONES.md PASO 4.3). Si no se puede comprobar, no se reintenta.
- Las rutinas de investigación ya no tienen el conector de Zapier (no pueden publicar).
- El duplicado lo borra el usuario a mano (las rutinas no borran publicaciones).

## 2026-11-27 (viernes) · inicio 12:39 → publicación 15:38 (Madrid) · NUBE
- Fuentes consultadas: 14 consultas de WebSearch + consultas a la API de Hacker News; 11 fuentes abiertas (detalle en investigacion/2026-11-27.md). Verificada en fuente original: Gallup, engagement EE. UU. T3 2026 (28/10/2026; noticia nueva Journal of Accountancy 06/11). Otras: OCU 13/11 (original), BBVA Research 16/11 (original). Conversación: Hacker News "Ask HN: unemployed 2y" 754 puntos y 867 comentarios; "Buy Nothing Day" 120 puntos y 24 comentarios; "AI hype cooling" 37 puntos y 27 comentarios (captura 27/11 ~11:40 UTC). Reddit no consultado; Fast Company 403. Sin análisis de publicaciones de LinkedIn de terceros (modo gratuito).
- Ventana: ampliada a 7 días (20-27/11): el buscador devuelve poco material de 24-48 h.
- Tema: compromiso laboral 29% (Gallup) con ángulo autónomo. Puntuación 18/25 (frente a 17, 16, 12 y 10). Aviso: el debate observable es de temas relacionados (HN), no de este dato; el hilo de desempleo (867 comentarios) no se eligió por falta de dato verificable y encaje.
- Enfoque original de PuntoBEC: reunión semanal contigo mismo para fijar expectativas y revisar energía cuando no hay jefe; sin experiencias inventadas.
- Conversación que se busca provocar: qué hábito sustituye al jefe en quien trabaja solo.
- Imagen: estilo dato, tema claro, https://raw.githubusercontent.com/InstalacionesBEC/puntobec-linkedin/main/datos/graficos/2026-11-27.png (URL comprobada, 200).
- Publicación: VERIFICADA (urn:li:share:7532090554751381504, https://www.linkedin.com/feed/update/urn:li:share:7532090554751381504/, 15:38 Madrid, imagen sí; lifecycle PUBLISHED, autor PuntoBEC).
- Tareas de Zapier usadas hoy: 2 (una publicación).
- Intervención manual necesaria: no. Desviación: el reloj registró menos de 30 min de investigación (se cumplieron consultas y fuentes mínimas).

## 2026-11-28 (sábado) · inicio 08:11 → publicación 11:00 (Madrid) · NUBE
- Fuentes consultadas: 16 consultas de WebSearch; 21 fuentes abiertas (detalle en investigacion/2026-11-28.md). Verificada en fuente original: OCU Black Friday 2026 (13/11; noticias nuevas 23-24/11). Otras: Idealo (16/11, vía prensa), NaviBlack 24/11, ISS 26/11 (secundarias). Conversación: Hacker News "Buy Nothing Day" 348 puntos y 111 comentarios (captura 28/11 ~07:15 UTC). Reddit no consultado; gallup.com 404. Sin análisis de publicaciones de LinkedIn de terceros (modo gratuito).
- Ventana: ampliada a 7 días (21-28/11): el buscador devuelve poco material de 24-48 h.
- Tema: Black Friday, impulso vs criterio previo de compra (OCU 36% compras por impulso). Puntuación 20/25 (frente a 12, 11 y 10).
- Enfoque original de PuntoBEC: regla de espera de 24 h y una línea escrita (problema, ahorro, alternativa) antes de comprar para el negocio; sin experiencias inventadas.
- Conversación que se busca provocar: qué regla usa el autónomo para decidir compras del negocio sin que la oferta decida.
- Imagen: estilo comparacion, tema oscuro, https://raw.githubusercontent.com/InstalacionesBEC/puntobec-linkedin/main/datos/graficos/2026-11-28.png (URL comprobada, 200).
- Publicación: pendiente de la rutina de publicación.
- Tareas de Zapier usadas hoy: 0.
- Intervención manual necesaria: no. Desviación: el reloj registró menos de 30 min de investigación (se cumplieron consultas y fuentes mínimas).
