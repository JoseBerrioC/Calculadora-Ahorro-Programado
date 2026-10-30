import sys
sys.path.append("src")

from flask import Flask

from view.web import vista_planes_ahorro

app = Flask(__name__)

app.register_blueprint(vista_planes_ahorro.vista)

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__ == '__main__':
    app.run(debug=True)