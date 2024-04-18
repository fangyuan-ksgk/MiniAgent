from miniagent import *
from system_prompt import *

queries = load_queries()

import pandas as pd
import os
from tqdm import tqdm as tqdm

group_id = "1743503684043542894"
api_key ="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJhc2FjaG9pIiwiVXNlck5hbWUiOiJhc2FjaG9pIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE3NDM1MDM2ODQwNTE5MzE1MDIiLCJQaG9uZSI6IjE3MTUyMTY2NzI5IiwiR3JvdXBJRCI6IjE3NDM1MDM2ODQwNDM1NDI4OTQiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJhc2EuY2hvaUBnbWFpbC5jb20iLCJDcmVhdGVUaW1lIjoiMjAyNC0wNC0xNyAwOTo0NTo0MSIsImlzcyI6Im1pbmltYXgifQ.YGWqWHr68X7_KbvqWRuq8YvahtOCoyk9p5F59BQSsvYMkJNGj0E_wE-T9Fq_WIuhoFNz2wiq-HEl3Y8jf4xJxmzr-3l_I8RosiBWMD67X2b410jLg8ARi_P-9OzQcbjW_T47ZS1kisifQdKXzKx3giQqNxfARNsxIZ88Z3pqx7sJ1JJ-goE5klMvGFH1nIl7hwxw51h3Hrq2O1YFj1fx_qhPq5m0LeDdfe6BZbh2EXtt_658wpMZWx-LTogfSfHiDKUOF8BJbPhHoPNoiWMXoEClQtqdNOzbuT6iB5-xgAIqfyhEwgWcNeQJKlNWUzFVPltzW2WM-332tNDjxXyd3A"

system_prompt = system_prompt_2

datasets = []
for query in tqdm(queries):
    agent = MiniAgent(group_id, api_key, "客户", system_prompt)
    message = query
    agent.chat(message)
    reply = agent.get_conversation()[-1]
    datasets.append({"query": query, "reply": reply})  # Accessing the 'text' key from the reply dictionary
df = pd.DataFrame(datasets)    

df.to_csv("data/minimax-completion-v2.csv", index=False)