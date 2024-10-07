from pydantic import BaseModel # this is needed for data validation and auto json 

class URLBase(BaseModel): # used when user submits a form to shorten url, only target url is reqd 
    target_url: str

class URL(URLBase): # when db stores additional data
    is_active: bool
    clicks: int

    class Config: # important
        orm_mode = True # needed for these models to integrate with orms

class URLInfo(URL): # when returning result to user
    url: str
    admin_url: str