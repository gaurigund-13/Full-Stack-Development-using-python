# Q2. Create a Flask application displaying system information using routes.

from flask import Flask
import platform

app = Flask(__name__)

@app.route("/system_info")
def system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    return str(system_info)

app.run(debug=True)