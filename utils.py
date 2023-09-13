from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format


def logging_queries(queries: list):
    for qs in queries:
        sql_formatted = format(str(qs["sql"]), reindent=True)
        print(highlight(sql_formatted, SqlLexer(), TerminalFormatter()))
    print(len(queries))

