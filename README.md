# Polars — Guía y notebooks en Polars

Este repositorio contiene notebooks y material de apoyo para aprender y aplicar Polars en Python.

Resumen del contenido
- Capítulos organizados en carpetas `Chapter_1`, `Chapter_2`, `Chapter_3`, `Chapter_4`, cada una con su notebook y datos de ejemplo.
- Carpeta `python-polars-the-definitive-guide` (proyecto original del libro) está excluida del control de versiones y no forma parte del repositorio principal.
- Archivos de configuración: `requirements.txt`, `.gitignore`, y configuración de VS Code en `.vscode/`.

Cómo usar
1. Crea/activa un entorno virtual para el proyecto (recomendado `.venv` o similar).
2. Instala dependencias:
   - `pip install -r requirements.txt`
3. Selecciona el intérprete del proyecto en VS Code o registra el kernel con `ipykernel` para Jupyter.
4. Abre cualquier `Notebook_X.ipynb` y selecciona el kernel del proyecto.

Notas sobre la carpeta ignorada
- La carpeta `python-polars-the-definitive-guide` está añadida a `.gitignore` por petición; contiene una copia local del libro que no debe versionarse aquí.

Instrucciones de Copilot (resumen)
- Revisa `.github/copilot-instructions.md` para las reglas internas usadas por el asistente: evita incluir archivos de datos en el repo, usa Polars para manipulación y Plotnine para visualización, y mantén ambientes virtuales fuera del control de versiones.

Contribuir
- Si añades capítulos o ejercicios, crea una carpeta `Chapter_N` con su notebook y un `README.md` en español describiendo el contenido.
- Evita subir datos grandes o binarios; agrega rutas de ejemplo y scripts para reproducir resultados.

Contacto y licencia
- Revisa `LICENSE` para información de licencia del contenido.

---

(README generado/actualizado automáticamente)
