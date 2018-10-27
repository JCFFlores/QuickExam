class ParserException(Exception):
    pass


class ParserSyntaxError(ParserException):
    pass


class ParserVariableNotFound(ParserException):
    pass
