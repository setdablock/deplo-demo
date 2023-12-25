from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='custom_templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-rna", methods=["POST"])
def process_rna():
    data = request.json
    rna_sequence = data['rnaSequence']
    reconstructed_rna = rna_sequence[::-1]
    original_rna = ''.join(sorted(rna_sequence.split(',')))
    return jsonify(reversedRNA=reversed_rna, originalRNA=original_rna)

if __name__ == "__main__":
    app.run(debug=True)
