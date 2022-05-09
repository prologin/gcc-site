class MultipleSerializerViewSetMixin:
    """
    Mixin allowing to specify multiple serializers for a ViewSet. Useful when
    you need to have a specific serializer for a specific action.

    Implements the get_serializer_class and lookup the
    actions_serializer_classes dict to find the serializer to use. Will
    fallback to the base get_serializer_class if actions_serializer_classes
    is not defined or no serializer is found.

    e.g.:

    class ExampleViewSet(MultipleSerializerViewSetMixin, ViewSet):
        serializer_class = ExampleSerializer
        actions_serializer_classes = {
            "list": ExampleListSerializer
            "retrieve": ExampleRetrieveSerializer
        }
    """

    def get_serializer_class(self):
        try:
            return self.actions_serializer_classes[self.action]
        except (AttributeError, KeyError):
            return super(
                MultipleSerializerViewSetMixin, self
            ).get_serializer_class()
