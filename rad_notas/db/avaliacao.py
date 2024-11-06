from peewee import Field, Model


class Avaliacao(Model):
  id = AutoField()



class PrefixedSerial(Field):
  field_type = 'prefixed_serial'

  def db_value(self, value):
    return

  def python_value(self, value):

    if (value not in ["PROVA", "NF"]):
      raise ValueError("Invalid evaluation method")

    field_string = value + str(Avaliacao.select().count() + 1)
    return field_string
