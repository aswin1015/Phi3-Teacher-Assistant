from langchain.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.chains import SequentialChain

import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

repo_id = "microsoft/Phi-3-mini-4k-instruct"


llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=1000, temperature=0.5, token='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'
) 

def generate_response(System_message):

    template = """You are the teacher and you must grade the answer according to {Sytem_message}"""

    prompt = PromptTemplate.from_template(template)

    llm_chain= LLMChain(prompt=prompt, llm=llm)

    response= llm_chain.run(System_message)

    return response
