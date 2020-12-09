from django.shortcuts import render
import os

def UserGuideView(request):
    module_dir = os.path.dirname(__file__)
    doc_path = os.path.join(module_dir, 'user_guide.md')

    return render(request, 'user_guide.html',
        context={"user_guide": open(doc_path, "r",encoding="utf-8").read()})