# AquaSafe Monitor

## Descripción

Esta es una aplicación web simple desarrollada con Flask que permite a los usuarios analizar datos de monitoreo de agua superficial. Los usuarios ingresan información sobre la ubicación, el parámetro detectado (como metales pesados) y la concentración, y reciben un análisis con posibles causas y soluciones generado por la API de OpenAI. El resultado se guarda en un archivo de texto.

## Tecnologías Utilizadas

- **Flask**: Un framework web para Python.
- **OpenAI**: API para generar análisis de calidad de agua.
- **HTML/CSS**: Para diseñar la interfaz de usuario.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Instala las dependencias**:

   Asegúrate de tener Python y pip instalados. Luego, instala Flask y OpenAI:

   ```bash
   pip install Flask openai
   ```

3. **Configura la clave de API**:

   Reemplaza `YOUR_API_KEY` en el código con tu clave de API de OpenAI.

4. **Ejecuta la aplicación**:

   ```bash
   python app.py
   ```

   La aplicación estará disponible en `http://127.0.0.1:5000`.

## Uso

1. Abre tu navegador y ve a `http://127.0.0.1:5000`.
2. Completa el formulario con los datos de monitoreo de agua:
   - Ubicación (ej. Cajamarca, Cajamarca, Encañada)
   - Parámetro Detectado (ej. Cesio)
   - Concentración (mg/L) (ej. 2.023)
3. Haz clic en "Analizar Datos".
4. Se generará y guardará un archivo de texto con el análisis de posibles causas y soluciones en el directorio actual.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar la aplicación, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes preguntas o comentarios, no dudes en contactarme en nitram767@gmail.com.