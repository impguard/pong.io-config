from pynamodb.models import Model
from pyanmodb.attributes import


class ConfigModel(Model):
    class Meta:
        table_name = "PongConfiguration"


def push_config(id_, filepath):

