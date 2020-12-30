from server.resources.api import SimilarWords, SimilarityMeasure, OddOneOut, AnalogyDifference

def initialize_routes(api):
    api.add_resource(SimilarWords, '/api/v1/similar-words')
    api.add_resource(SimilarityMeasure, '/api/v1/similarity')
    api.add_resource(OddOneOut, '/api/v1/oddoneout')
    api.add_resource(AnalogyDifference, '/api/v1/analogy')