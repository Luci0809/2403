 #Import
 from fastapi import FastAPI

 #Define an API object
 app = FastAPI()

 #Map HTTP method and path to python function
 @app.get("\")
 async def root ():
  return {"message": "Hello KEA student. Welcome to the FastAPI page."}

 @app.get("/newpoints")
async def function_demo_get():
 return ("message": "This is /newpoints endpoint"):


