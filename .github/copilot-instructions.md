```instructions
# Copilot Instructions — Buenas prácticas del proyecto

Estas instrucciones resumen las reglas y convenciones que seguimos en este repositorio para mantener la calidad, reproducibilidad y seguridad.

1) Datos y artefactos pesados
- No incluyas archivos de datos grandes (CSV, Parquet, HDF5, imágenes pesadas, etc.) en el repositorio.
- Usa `.gitignore` para excluir carpetas `data/` u otras fuentes de datos locales.
- Para archivos binarios grandes necesarios, usa Git LFS y documenta su uso en `README.md`.

2) Entorno y dependencias
- Mantén el entorno virtual fuera del control de versiones (ej: `.venv/`, `venv/` deben estar en `.gitignore`).
- Versiona dependencias en `requirements.txt` o `pyproject.toml` con versiones mínimas/compatibles.
- Documenta cómo crear el entorno en el README (ej. `python -m venv .venv` y `pip install -r requirements.txt`).

3) Notebooks
- Evita commitear salidas (outputs) en los notebooks; limpia salidas antes de commit usando `nbstripout` o `jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace`.
- Para diffs legibles y control de cambios, considera usar `jupytext` para mantener una versión `.py` (formato light) sincronizada con cada notebook.
- Protege notebooks de secretos y credenciales: usa variables de entorno o un archivo de configuración local que esté en `.gitignore`.

4) Calidad y revisión
- Añade `nbdime` para mejores diffs de notebooks si colaboras con otros.
- Usa `pre-commit` con `nbstripout` para automatizar la limpieza de salidas al hacer commits.

5) Visualizaciones y herramientas
- Usa Polars para manipulación de datos y Plotnine/Altair/Matplotlib para visualización según convenga.
- Para gráficos complejos generados por código (p. ej. grafos DOT), documenta las dependencias del sistema (Graphviz) en el README.

6) Seguridad
- No subas claves, tokens o credenciales. Revísalos con herramientas como `git-secrets` antes de push.

7) Reproducibilidad
- Incluye ejemplos reproducibles y, cuando sea posible, pequeñas muestras de datos en `data/sample/` (muy ligeras) para que los notebooks se puedan ejecutar localmente.
- Documenta los pasos para reproducir los resultados (comandos, versión de Python, variables de entorno).

8) Meta
- Estas reglas están pensadas para mantener el repositorio ligero, seguro y útil como portafolio técnico. Adáptalas según necesidades del proyecto, pero documenta cualquier excepción.

```# Copilot Instructions

- No incluyas archivos de datos como CSV, Parquet, etc. en el repositorio.
- Usa Polars para manipulación de datos y Plotnine para visualización.
- Mantén el entorno virtual fuera del control de versiones.
- Los notebooks deben ser claros y contener ejemplos reproducibles.
