from flask import Flask, jsonify
from flask import render_template
import openai

openai.api_key = "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"
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

  @app.route('/generateimages/<prompt>')
  def generate(prompt):
    print("prompt:", prompt)
    response = openai.Image.create(prompt=prompt, n=3, size="104x104")
    print("response", response)
    return jsonify(response)

  return render_template('index.html')


app.run(host='0.0.0.0', port=81)
