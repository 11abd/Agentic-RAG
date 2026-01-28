from utils.logger import logger
import time

class RAGTool:
    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline

    def run(self, query: str) -> str:
        logger.info(f"RAGTool | start | query='{query}'")
        start = time.time()

        result = self.rag_pipeline(query)

        elapsed = round(time.time() - start, 2)
        logger.info(f"RAGTool | end | time_taken={elapsed}s")

        return result
