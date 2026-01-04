from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
#from google.colab import userdata
import os
from System import SYSTEM_PROMPT

class MessageObject(BaseModel):
  message: str
  final_label: str
  intent: str
  reason: str


class LLMAssistant:
    def __init__(self):
        load_dotenv()  # MUST be called before getenv

        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Check .env file")

        self.model_name = "gemini-2.5-flash"
    

    def send_message(self, user_message):
        self.parser = PydanticOutputParser(pydantic_object=MessageObject)
        self.format_instructions = self.parser.get_format_instructions()
        final_prompt = f"""
        {SYSTEM_PROMPT}
        
        USER_MESSAGE:
        {user_message}

        OUTPUT_FORMAT:
        {self.format_instructions}
        """
        #print ("*" * 100)
        #print ("INPUT PROPMPT")
        #print (final_prompt)
        #print ("*" * 100)
        llm = ChatGoogleGenerativeAI(
            model=self.model_name,
            google_api_key=self.api_key
            )
        print (f"ML choice is not satisfactory, hence invoking LLM")
        response = llm.invoke(final_prompt)

        try:
            structured = self.parser.parse(response.content)
            #print ("*" * 100)
            #print(" Structured Output:")
            #print(structured)
            #print ("*" * 100)
            return structured
        except Exception as e:
            #print(" Validation failed:")
            #print(e)
            return response.text


