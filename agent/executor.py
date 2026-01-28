from utils.logger import logger

class Executor:
    def __init__(self, rag_tool):
        self.rag_tool = rag_tool

    def execute(self, action: str, query: str) -> str:
        logger.info(f"Executor | action={action}")

        if action == "use_rag":
            return self.rag_tool.run(query)

        logger.info("Executor | direct_answer_path")
        return "This question does not require document retrieval."
