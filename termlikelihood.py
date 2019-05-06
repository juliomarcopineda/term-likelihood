class TermLikelihood:
    def __init__(self, corpus):
        self.corpus = corpus
        self.reverse_index = {}

        self.compute_reverse_index()

    def compute_reverse_index(self):
        for doc_id, index in self.corpus.items():
            for term in index.keys():
                if term not in self.reverse_index:
                    ids = set(doc_id)
                    self.reverse_index[term] = ids
                else:
                    self.reverse_index[term].add(doc_id)
