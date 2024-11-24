from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, _, line):
        # Emitir cada palabra en la línea
        for word in line.split():
            yield word.lower(), 1

    def reducer(self, word, counts):
        # Sumar todas las ocurrencias de una palabra
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()
