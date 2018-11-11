from sqlalchemy import types

class EnumColumn(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, engine):
        if value is None:
            return None
        return value.name

    def process_result_value(self, value, engine):
        if value is None:
            return None
        return self.Enum[value]
