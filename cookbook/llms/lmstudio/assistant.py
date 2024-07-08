from phi.assistant import Assistant
from phi.llm.openai.like import OpenAILike

assistant = Assistant(llm=OpenAILike(base_url="http://localhost:1234/v1"))
msg = "আকাশ কেন নীল?"
assistant.print_response(msg, markdown=True)

