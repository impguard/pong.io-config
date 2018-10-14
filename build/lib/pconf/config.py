import arrow
import json
import copy
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    JSONAttribute,
    UTCDateTimeAttribute,
)


class ConfigModel(Model):
    class Meta:
        table_name = "PongConfiguration"
        region = "us-west-2"

    Id = UnicodeAttribute(hash_key=True)
    Config = JSONAttribute()
    UpdatedAt = UTCDateTimeAttribute()
    CreatedAt = UTCDateTimeAttribute()


def get(id_):
    try:
        row = ConfigModel.get(id_)
    except Model.DoesNotExist:
        row = None

    return row


def push(id_, config):
    current_row = get(id_)

    now = arrow.utcnow()
    created_at = current_row.CreatedAt if current_row else now

    row = ConfigModel(
        Id=id_,
        Config=config,
        UpdatedAt=now,
        CreatedAt=created_at
    )

    row.save()

    return row


def delete(id_):
    row = get(id_)

    if not row:
        return None

    row.delete()
    return row


def scan():
    return [row for row in ConfigModel.scan()]


def pretty(row):
    attributes = copy.deepcopy(row.attribute_values)

    attributes['UpdatedAt'] = arrow.get(attributes['UpdatedAt']).isoformat()
    attributes['CreatedAt'] = arrow.get(attributes['CreatedAt']).isoformat()

    return json.dumps(attributes, sort_keys=True)
