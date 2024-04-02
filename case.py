class AlgumaCoisa:
    def __enter__(self):
        print("estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("estou saindo")

with AlgumaCoisa() as ola:
    print("estou no meio")



