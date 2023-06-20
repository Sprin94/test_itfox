from django.shortcuts import get_object_or_404

from news.models import News


class NewsDefault:
    requires_context = True
    model = News

    def __call__(self, serializer_field):
        view = serializer_field.context['view']
        object_pk = view.kwargs.get('pk')
        return get_object_or_404(self.model, pk=object_pk)
