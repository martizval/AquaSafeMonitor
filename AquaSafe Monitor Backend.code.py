from flask import Flask, render_template, request, redirect, url_for
import os
import datetime
import openai

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

# Crear el cliente OpenAI
client = openai.Client()

app = Flask(__name__)

def analyze_water_monitoring_data(monitoring_data, model):
    # Realizar la solicitud de autocompletado
    response = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "assistant",
            "content": "You are an expert in environmental science and water quality analysis."
        },
            {
                "role": "user",
                "content": f"Analyze the following water monitoring data and provide a possible cause and a practical solution for the detected parameter: {monitoring_data}"
            }
        ],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Devolver el texto generado
    return response.choices[0].message.content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    location = request.form["location"]
    parameter = request.form["parameter"]
    concentration = request.form["concentration"]

    monitoring_data = f"Location: {location}, Parameter Detected: {parameter}, Concentration: {concentration} mg/L"

    analysis_result = analyze_water_monitoring_data(monitoring_data, "gpt-3.5-turbo-1106")

    # Crear un nombre de archivo único basado en la fecha y hora actuales
    now = datetime.datetime.now()
    file_name = f"analysis_{now.strftime('%Y-%m-%d-%H-%M-%S')}.txt"

    # Escribir el resultado en un archivo txt
    with open(file_name, "w") as f:
        f.write(analysis_result)

    # Redirigir al usuario a la página principal
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
