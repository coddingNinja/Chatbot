# api="AIzaSyC6vD28X7L8RJVVeVW-NRsCvjt8IQse34A"

import google.generativeai as g
g.configure(api_key="AIzaSyC6vD28X7L8RJVVeVW-NRsCvjt8IQse34A")

model=g.GenerativeModel("gemini-1.5-flash")

result=model.generate_content("give me a one line answer on the futer of the ai ")


print(f"the response from the api :  {result.text}")
