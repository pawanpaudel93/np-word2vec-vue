from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from gensim.models import Word2Vec

from settings import MODE, ProductionConfig, DevelopmentConfig
from resources.routes import initialize_routes


app = Flask(__name__, 
    static_folder="./static", 
    template_folder="./static/dist"
)
app.config.from_object(ProductionConfig if MODE == "production" else DevelopmentConfig)    
CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

model = Word2Vec.load("./static/model/word2vec_NP.model")

initialize_routes(api)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
