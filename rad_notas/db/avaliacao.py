from peewee import Field, AutoField
from string import Template
import psycopg

from rad_notas.db.base_model import BaseModel

class PrefixedSerial(Field):
    field_type = 'text'

    def get_count(self):
        with psycopg.connect() as conn:
            cur = conn.cursor()
            query_entries = cur.execute("SELECT COUNT(*) FROM avaliacao").fetchone()
        if query_entries == None:
            entry_count = 0
            return str(entry_count)
        else:
            entry_count = query_entries[0] + 1
            return str(entry_count)

    def db_value(self, value):
        return AutoField()

    def python_value(self, value):
        entry_count = self.get_count()
        template_string = Template("$value_$entry_count")
        if (value not in ["PROVA", "NF"]):
            raise ValueError("Invalid evaluation method")
        else:
            concatenated_string = template_string.substitute(value, entry_count=str(entry_count))
            return concatenated_string


class Avaliacao(BaseModel):
    id = PrefixedSerial(null=False, primary_key=True)
