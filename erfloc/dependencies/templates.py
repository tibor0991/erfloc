from fastapi.templating import Jinja2Templates
from jinja2 import PackageLoader, Environment
from functools import cache
from fastapi import Depends
from typing import Annotated

@cache
def get_template_engine():
    return Jinja2Templates(env=Environment(loader=PackageLoader('erfloc')))

TemplateDep = Annotated[Jinja2Templates, Depends(get_template_engine)]