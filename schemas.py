from marshmallow import Schema, fields


class TimeStampSchema(Schema):
    created_at = fields.DateTime(required=True, dump_only=True)
    updated_at = fields.DateTime(required=True, dump_only=True)
    deleted_at = fields.DateTime(required=True, dump_only=True)


class PlainPenggunaSchema(TimeStampSchema):
    id = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    photo = fields.Str(required=True)
    premium = fields.Boolean(required=False)
    token = fields.Str(required=False)
    terakhir_login = fields.DateTime(required=True)


class PlainLahanSchema(TimeStampSchema):
    id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    nama = fields.Str(required=True)
    luas = fields.Float(required=True)
    alamat = fields.Str(required=False)
    lat = fields.Float(required=False)
    lon = fields.Float(required=False)


class PenggunaSchema(PlainPenggunaSchema):
    lahan = fields.List(fields.Nested(PlainLahanSchema()), dump_only=True)


class LahanSchema(PlainLahanSchema):
    pengguna = fields.Nested(PlainPenggunaSchema(), dump_only=True)
