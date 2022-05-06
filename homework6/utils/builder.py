from utils.parser import Parser


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_table(self, model):
        builder = None
        params = Parser.parse(model)
        n = 0
        for param in params:
            builder = model(**param)
            self.client.session.add(builder)
            n += 1
        builder.expected_value = n

        self.client.session.commit()
        return builder
