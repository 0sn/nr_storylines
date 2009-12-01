from django import template
from django.http import Http404
import re

from nr_storylines.models import Storyline
from nr_comics.models import Comic

register = template.Library()

def do_storyline_nav(parser, token):
    return StorylineNav()

class StorylineNav(template.Node):
    def render(self, context):
        storyline = template.Variable("storyline").resolve(context)
        comic = template.Variable("comic").resolve(context)
        t = template.loader.get_template("nr_storylines/storyline_navfragment.html")
        ids = list(storyline.associated_ids())
        try:
            index = ids.index(comic.sequence)
        except ValueError:
            raise Http404
        return t.render(template.Context({
            'storyline':storyline,
            'comic':comic,
            'first': ids[0],
            'prev': ids[index-1],
            'next': ids[(index+1)%len(ids)],
            'last': ids[-1]
        }))

register.tag("storyline_nav", do_storyline_nav)