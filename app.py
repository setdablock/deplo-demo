from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# Create a Flask application instance
# Set 'template_folder' to the name of your folder containing the HTML files.
app = Flask(__name__, template_folder='custom_templates')

@app.route("/")
def index():
    # Serve the HTML page
    return render_template("index.html")

@app.route("/process-rna", methods=["POST"])
def process_rna():
    # Get JSON data sent with the POST request
    data = request.json
    rna_sequence = data['rnaSequence']
    
    # Here, you would call your actual RNA reconstruction algorithm.
    # For demonstration purposes, this example simply reverses the input.
    reconstructed_rna = rna_sequence[::-1]
    
    # Return the result as JSON
    return jsonify(reconstructedRNA=reconstructed_rna)

# Check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.run(debug=True)