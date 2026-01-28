from utils.logger import logger

class Planner:
    def decide(self, query: str) -> str:
        decision = "use_rag" if len(query.split()) >= 3 else "direct_answer"
        logger.info(f"Planner | decision={decision} | query='{query}'")
        return decision
