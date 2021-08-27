import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home

jp.Route(path=Home.path, func_to_run=Home.serve)
jp.Route(path=About.path, func_to_run=About.serve)
jp.Route(path=Dictionary.path, func_to_run=Dictionary.serve)

jp.justpy(port=8001)