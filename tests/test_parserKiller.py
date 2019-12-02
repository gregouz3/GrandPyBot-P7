from Classes.parserKiller import Parser

def test_parser():
    my_parser = Parser("salut, quelle est la rue de la tour Eiffel ")
    assert my_parser.parsed_string == "rue tour eiffel"