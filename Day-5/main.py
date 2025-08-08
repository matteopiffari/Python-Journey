from fastapi import FastAPI, Query, HTTPException                      # type: ignore
from typing import Annotated

from schemas import *

app = FastAPI()

componentsList = [
    {"id": 1, "name": "Component 1", "type": (ComponentEnum.CPU).value},
    {"id": 2, "name": "Component 2", "type": (ComponentEnum.GPU).value},
    {"id": 3, "name": "Component 3", "type": (ComponentEnum.RAM).value},
]


# -----------------------------------
#                GET:
# -----------------------------------

@app.get("/")
async def read_root():
    return {"Hello World!"}

@app.get("/components")
async def readComponents(id: int | None = None) -> list[Component]:             # type: ignore
    # If query is present (/components/?id=1)
    if id:
        return [
            Component(**comp) for comp in componentsList if comp['id'] == id
        ]
    
    # Normal endpoint
    return [Component(**comp) for comp in componentsList]                       # Convert dict to Component by using the ** (unpacking) operator that pass each key-value pair as arguments

@app.get("/components/{component_id}", status_code=200)
async def readComponent(component_id: int) -> Component:
    for comp in componentsList:
        if comp.get("id") == component_id:
            return Component(**comp)
    raise HTTPException(status_code=404, detail="Component not found")          # Raise HTTP 404 error if component not found



@app.get("/components/type/")
async def readComponentQuery(component_type: Annotated[str | None, Query(max_length=10)] = None):    # type: ignore
    # Added the metadata (using Annotated) for the type length that must be smaller than or equal to 10
    try:
        compEnum = ComponentEnum(component_type.lower()) if component_type != None else None
    except:
        raise HTTPException(status_code=400, detail="Type not valid")
    
    if(compEnum == None):
         raise HTTPException(status_code=400, detail="Insert a type")
    
    return[
        Component(**comp) for comp in componentsList if ComponentEnum(comp['type']).value == component_type.lower()     # type: ignore
    ]

@app.get("/components/type/{component_type}")
async def readComponentsFromType(component_type) -> list[Component]:            # type: ignore
    try:
        component_type = ComponentEnum(component_type.lower())
    except:
        raise HTTPException(status_code=400, detail="Type not valid")
    
    return[
        Component(**comp) for comp in componentsList if ComponentEnum(comp['type']).value == component_type.value.lower()
    ]
# -----------------------------------
#               POST:
# -----------------------------------

@app.post("/components")
async def createComponent(data: CreateComp) -> Component:
    comp = Component(id=componentsList[-1]['id'] + 1, **data.model_dump()).model_dump()
    componentsList.append(comp)

    return comp


# -----------------------------------
#               PUT:
# -----------------------------------
@app.put("/components/{id}")
async def modifyComp(id: int, data: CreateComp) -> Component:
    comp = Component(id=id, **data.model_dump()).model_dump()
    componentsList[id-1] = comp

    return comp

# -----------------------------------
#               DELETE:
# -----------------------------------
@app.delete("/components/{id}")
async def deleteComp(id: int):
    for comp in componentsList:
        if comp['id'] == id:
            componentsList.remove(comp)
            return "component deleted"

    raise HTTPException(status_code=404)