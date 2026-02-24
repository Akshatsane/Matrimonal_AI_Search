from models.user_details import UserDetails
from models.user_query import UserQuery
from repositories.sample_repository import SampleRepository
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

class MatrimonialService:
    def __init__(self, repository: SampleRepository):
        self.repository = repository
        self.llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key="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")  # Securely load key

    def process_query(self, user_details: UserDetails, user_query: UserQuery):
        data_str = self.repository.get_data()
        #covert user_details to to json string
        user_str = user_details.model_dump_json()      
        # Use LangChain messages
    
        messages = [
            SystemMessage(
                content="You are a highly intelligent AI for matchmaking. Your goal is to find the best possible matches based on user profile you will be provided with."
            ),
            HumanMessage(
                content=f"""
                 ## **User Details**
                 {user_str}

                 ## **Matrimonial Database**
                 Below is the available matrimonial data:

                 {data_str}

                 ## **Matching Criteria**
                 - match according to the user details 
                 - additionally here is the user prompt for further matching:
                 {user_query}
                 
                 

                 ## **Required Output**
                 Return only the **some most relevant matches** in the format given below and If **no perfect match is found**, ask the user to suggest **the next best alternatives** instead.

                 1. **Name:** <Match Name>
                    - **Age:** <Match Age>
                    - **Profession:** <Match Profession>
                    - **Reason for selection:** <Explain why this match fits the user’s preferences>

                    
                 """
            ),
        ]

        # Generate AI response
        response = self.llm(messages)
        return {"matches": response.content.split("\n")}  # Cleaned responseIf **no perfect match is found**, ask the user to suggest **the next best alternatives** instead.