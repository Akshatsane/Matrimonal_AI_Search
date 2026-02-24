
# from backend.models import user_details
# class SampleRepository:
#     def __init__(self):
#         self.data = self.create_sample_data()

#     def create_sample_data(self):
       
#         data= [ 
#             user_details("john Doe", 33,),
            
            
#         ]
#         # Sample matrimonial data
#         # data = {
#         #     "Name": [
        
#         #         "John Doe", "Alice Smith", "Bob Johnson", "Eve Brown", "Mike Davis", "Sarah Taylor", "Tom White", "Emily Lee", "David Kim", "Jessica Martin"
#         #     ],
#         #     "Fathers Name": [
#         #         "Mr. Doe", "Mr. Smith", "Mr. Johnson", "Mr. Brown", "Mr. Davis", "Mr. Taylor", "Mr. White", "Mr. Lee", "Mr. Kim", "Mr. Martin"
#         #     ],
#         #     "Address": [
#         #         "123 Main St", "456 Elm St", "789 Oak St", "321 Maple St", "901 Pine St", "234 Cedar St", "567 Walnut St", "890 Cherry St", "345 Orange St", "678 Grape St"
#         #     ],
#         #     "City": [
#         #         "New York", "Los Angeles", "Chicago", "Houston", "New York", "Los Angeles", "Chicago", "Houston", "New York", "Los Angeles"
#         #     ],
#         #     "Working City": [
#         #         "New York", "Los Angeles", "Chicago", "Houston", "New York", "Los Angeles", "Chicago", "Houston", "New York", "Los Angeles"
#         #     ],
#         #     "DOB": [
#         #         "1990-01-01", "1992-01-01", "1991-01-01", "1993-01-01", "1990-02-01", "1992-02-01", "1991-02-01", "1993-02-01", "1990-03-01", "1992-03-01"
#         #     ],
#         #     "Height (Inch)": [
#         #         68, 65, 70, 67, 69, 66, 71, 68, 70, 65
#         #     ],
#         #     "Contact": [
#         #         "1234567890", "9876543210", "5551234567", "9998887777", "1112223333", "4445556666", "7778889999", "6665554444", "8887776666", "3332221111"
#         #     ],
#         #     "AGE": [
#         #         33, 31, 32, 30, 33, 31, 32, 30, 33, 67
#         #     ],
#         #     "Education": [
#         #         "Bachelor", "Master", "Bachelor", "Master", "Bachelor", "Master", "Bachelor", "Master", "Bachelor", "Master"
#         #     ],
#         #     "Business / Service": [
#         #         "Tech", "Tech", "Finance", "Tech", "Finance", "Tech", "Finance", "Tech", "Finance", "Tech"
#         #     ],
#         #     "MARRIAGE": [
#         #         "Unmarried", "Unmarried", "Unmarried", "Unmarried", "Unmarried", "Unmarried", "Unmarried", "Unmarried", "Unmarried", "Unmarried"
#         #     ],
#         #     "Gender": [
#         #         "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"
#         #     ]
#         # }
#         # return pd.DataFrame(data)
     
#     def get_data(self):
#         # convert self.data to json string
#         return self.data.to_json(orient="records")
from models.user_details import UserDetails

class SampleRepository:
    def __init__(self):
        self.data = self.create_sample_data()  # ✅ Calls create_sample_data() method

    def create_sample_data(self):  # ✅ Method is properly indented inside the class
        data = [
            UserDetails(
                name="John Doe", age=33, profession="Engineer", gender="Male",
                qualifications="B.Tech", location="New York", preferences="Remote"
            ),
            UserDetails(
                name="Jane Smith", age=29, profession="Doctor", gender="Female",
                qualifications="MBBS", location="Los Angeles", preferences="On-site"
            ),
             UserDetails(
            name="Mike Johnson", age=40, profession="Architect", gender="Male",
            qualifications="M.Arch", location="Chicago", preferences="Hybrid"
        ),
        UserDetails(
            name="Emily Davis", age=35, profession="Data Scientist", gender="Female",
            qualifications="PhD in AI", location="San Francisco", preferences="Remote"
        ),
        UserDetails(
            name="Robert Brown", age=42, profession="Lawyer", gender="Male",
            qualifications="LLB", location="Houston", preferences="On-site"
        ),
        UserDetails(
            name="Sophia Wilson", age=27, profession="Graphic Designer", gender="Female",
            qualifications="BFA", location="Seattle", preferences="Remote"
        ),
        UserDetails(
            name="William Anderson", age=31, profession="Software Developer", gender="Male",
            qualifications="M.Tech", location="Austin", preferences="Hybrid"
        ),
        UserDetails(
            name="Olivia Martinez", age=26, profession="Marketing Manager", gender="Female",
            qualifications="MBA", location="Boston", preferences="On-site"
        ),
        UserDetails(
            name="James Lee", age=37, profession="Mechanical Engineer", gender="Male",
            qualifications="B.E", location="Denver", preferences="Hybrid"
        ),
        UserDetails(
            name="Emma Thomas", age=30, profession="HR Manager", gender="Female",
            qualifications="MBA in HR", location="Phoenix", preferences="Remote"
        )
        ]
        return data

    def get_data(self):
        return [user.model_dump() for user in self.data]
