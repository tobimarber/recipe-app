from flask import Flask, render_template, request, redirect
from deep_translator import GoogleTranslator

app = Flask(__name__)

recipes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_text = request.form["recipe"]

        try:
            translated = GoogleTranslator(source='auto', target='en').translate(original_text)
        except:
            translated = "Translation failed"

        recipes.append({
            "original": original_text,
            "translated": translated
        })

        return redirect("/")

    return render_template("index.html", recipes=recipes)

app.run(host="0.0.0.0", port=5000)
