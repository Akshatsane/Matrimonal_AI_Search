from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.matrimonial_service import MatrimonialService
from repositories.sample_repository import SampleRepository
from models.user_details import UserDetails
from models.user_query import UserQuery

app = FastAPI()


repository = SampleRepository()
service = MatrimonialService(repository)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/start_matchmaking")
async def start_matchmaking(user_details: UserDetails):
    # Initialize a query to start matchmaking
    user_query = UserQuery(query="Find matches for the user.")
    
    result = service.process_query(user_details, user_query)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
