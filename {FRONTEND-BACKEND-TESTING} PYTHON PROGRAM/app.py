from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows frontend to connect

@app.route('/button-click', methods=['GET'])
def button_click():
    MESSAGE = " MY NAME: SAAD ALAM SHAIKH \n MY FEILD: MASTER OF SCIENCE IN INFROMATION TECHNOLOGY MANAGEMENT \n MY UNIVERSITY: BERLIN SCHOOL OF BUSINESS AND INNOVATION. \n MY MOBILE NUMBER: +49 15732985578 \n MY E-MAIL ADDRESS: saad_alam9522@yahoo.com."
    return jsonify({"message": MESSAGE})
    
if __name__ == "__main__":
    app.run(debug=True)