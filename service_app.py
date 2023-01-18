import os
import connexion

app = connexion.FlaskApp(__name__, specification_dir="./")
app.add_api("service_api_spec.yml", strict_validation=True)

@app.route('/')
def index():
    return '<body>Checkout <a  href=http://localhost:8000/api/ui/>/api/ui</a></body>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
