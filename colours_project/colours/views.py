from django.views.generic import TemplateView, DetailView, ListView

from colours.models import Palette

from random import randint

class IndexView(TemplateView):
    template_name = 'colours/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tmp = Palette.objects.all()
        colour_palettes = []
        if len(tmp) > 6:
            used_indexes = []
            tmp_len = len(tmp)
            while len(colour_palettes) < 6:
                ran = randint(0, tmp_len - 1)
                if used_indexes.count(ran) == 0:
                    used_indexes.append(ran)
                    colour_palettes.append(tmp[ran])
                if len(colour_palettes) == 6:
                    break
        else:
            colour_palettes = tmp
        context["colour_palettes"] = colour_palettes
        return context


class PaletteDetailsView(DetailView):
    model = Palette
    template_name = 'colours/palette_details.html'


class PaletteListView(ListView):
    model = Palette
    paginate_by = 8
    template_name = 'colours/palette_list.html'
    context_object_name = 'palette_list'
