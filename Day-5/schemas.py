from enum import Enum
from pydantic import BaseModel, validator                  # type: ignore

# Enum for component types
class ComponentEnum(Enum):
    CPU = "cpu"
    GPU = "gpu"
    RAM = "ram"

# Schema for components (standard Pydantic model)
class Component(BaseModel):
    id: int
    name: str
    type: ComponentEnum

# Schema for creating a component
class CreateComp(BaseModel):
    @validator('type', pre=True)            # Pre validator for lowercase the 'type'
    def typeToLower(cls, value):
        return value.lower()
    
    name: str
    type: ComponentEnum



# Example of shared properties for user and userCreate
class User(BaseModel):
    username: str
    isActive: bool

class CreateUser(User):     # The CreateUser class inherits all the fields of User
    email: str
    password: str