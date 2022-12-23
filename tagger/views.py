from django.shortcuts import render

from .models import Emoji, EmojiSequence, Tag

from random import choices

# Create your views here.


def tag_mode(request, length=3):
    context = {}
    if request.method == 'GET':
        all_emoji = Emoji.objects.all()
        context['emoji'] = choices(all_emoji, k=length)

    elif request.method == 'POST':
        pass
    return render(request, 'tagger/tag-mode.html', context)
