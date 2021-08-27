import justpy as jp

from webapp.about import About
from webapp.home import Home

jp.Route(path=Home.path, func_to_run=Home.serve)
jp.Route(path=About.path, func_to_run=About.serve)

jp.justpy(port=8001)