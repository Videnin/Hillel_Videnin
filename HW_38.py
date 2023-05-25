class AttributePrinterMixin:
    def __str__(self):
        class_name = self.__class__.__name__
        fields = self._get_fields()
        formatted_fields = self._format_fields(fields)
        return f"{class_name}: {formatted_fields}"

    def _get_fields(self):
        fields = {}
        for attr_name, attr_value in self.__dict__.items():
            if not attr_name.startswith("_"):
                fields[attr_name] = attr_value
        return fields

    def _format_fields(self, fields, indent_level=1):
        indent = "\t" * indent_level
        formatted_fields = []
        for attr_name, attr_value in fields.items():
            if isinstance(attr_value, dict):
                formatted_value = self._format_fields(attr_value, indent_level + 1)
                formatted_fields.append(f"{indent}{attr_name}: {formatted_value}")
            else:
                formatted_fields.append(f"{indent}{attr_name}: {attr_value}")
        return "\n".join(formatted_fields)
