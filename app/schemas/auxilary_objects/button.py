from pydantic import BaseModel


class ButtonAction(BaseModel):
    type: str
    url: str    


class ButtonAux(BaseModel):
    title: str
    action: ButtonAction
