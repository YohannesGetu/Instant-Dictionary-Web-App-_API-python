import inspect

import justpy as jp

from webapp import page
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(path=obj.path, func_to_run=obj.serve)

# jp.Route(path=Home.path, func_to_run=Home.serve)
# jp.Route(path=About.path, func_to_run=About.serve)
# jp.Route(path=Dictionary.path, func_to_run=Dictionary.serve)

jp.justpy(port=8001)