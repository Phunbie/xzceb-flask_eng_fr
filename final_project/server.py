from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=["POST", "GET"])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translate = translator.englishToFrench(textToTranslate)
    return translate

@app.route("/frenchToEnglish", methods=["POST", "GET"])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translate = translator.frenchToEnglish(textToTranslate)
    return translate

@app.route("/")
def renderIndexPage():
    # Write the code to rende
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
