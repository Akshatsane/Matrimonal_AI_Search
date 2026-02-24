
from models.user_details import UserDetails

class SampleRepository:
    def __init__(self):
        self.data = self.create_sample_data()  #  Calls create_sample_data() method

    def create_sample_data(self):  # Method is properly indented inside the class
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
