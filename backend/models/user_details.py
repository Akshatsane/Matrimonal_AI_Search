from pydantic import BaseModel

class UserDetails(BaseModel):
    name: str
    age: int
    profession: str
    gender: str
    qualifications: str
    location: str
    preferences: str

   
# class UserDetails:
#     def __init__(self, name, age, profession, gender, qualifications, location, preferences):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.gender = gender
#         self.qualifications = qualifications
#         self.location = location
#         self.preferences = preferences
