def feed_animals(animals):
    """
    Calcula o total de pontos de comida consumidos usando sum()
    e uma expressão geradora conforme a diretriz nº 2.
    """
    return sum(animal.feed() for animal in animals)

if __name__ == "__main__":
    # Seus testes aqui
    pass