from flask import request, jsonify, make_response, Response
from flask_restful import Resource
from gensim.models import Word2Vec

def load_model():
    print("Loading model...")
    return Word2Vec.load("./static/model/word2vec_NP.bin")

model = load_model()

class SimilarWords(Resource):
    def post(self):
        body = request.get_json()
        word = body.get("word", None)
        topn = body.get("topn", 3)
        if word:
            try:
                similar_words = model.wv.most_similar(word, topn=topn)
                return make_response(jsonify(similar_words), 200)
            except BaseException as error:
                return make_response({"error": str(error)}, 400)
        else:
            return make_response({"error": "No word present"}, 400)

class SimilarityMeasure(Resource):
    def post(self):
        body = request.get_json()
        word1 = body.get("word1", None)
        word2 = body.get("word2", None)
        if word1 and word2:
            try:
                similarity_measure = model.wv.similarity(word1, word2)
                return make_response({"similarityMeasure": float(similarity_measure)}, 200)
            except BaseException as error:
                return make_response({"error": str(error)}, 400)
        elif not word1 and not word2:
            return make_response({"error": "Both words missing"}, 400)
        elif not word1:
            return make_response({"error": "word1 missing"}, 400)
        else:
            return make_response({"error": "word2 missing"}, 400)

class OddOneOut(Resource):
    def post(self):
        body = request.get_json()
        words = body.get("words", None)
        if words:
            try:
                words = [word.strip() for word in words.split(",")]
                if len(words) < 3:
                    return make_response({"error": "Atleast 3 words are required"}, 400)
                odd_one = model.wv.doesnt_match(words)
                return make_response({"oddOne": odd_one}, 200)
            except BaseException as error:
                return make_response({"error": str(error)}, 400)
        else:
            return make_response({"error": "words missing"}, 400)

class AnalogyDifference(Resource):
    def post(self):
        body = request.get_json()
        word1 = body.get("word1", None)
        word2 = body.get("word2", None)
        word3 = body.get("word3", None)
        if word1 and word2 and word3:
            similar_words = model.wv.most_similar(positive=[word1, word2], negative=[word3])
            return make_response(jsonify(similar_words), 200)
        else:
            return make_response({"error": "words missing"}, 400)