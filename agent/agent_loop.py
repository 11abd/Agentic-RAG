from utils.logger import logger

class AgentLoop:
    def __init__(self, planner, executor, reflector, evaluator, max_retries=2):
        self.planner = planner
        self.executor = executor
        self.reflector = reflector
        self.evaluator = evaluator
        self.max_retries = max_retries

    def run(self, query: str) -> dict:
        logger.info(f"AgentLoop | query_received='{query}'")
        attempt = 0
        final_answer = ""

        while attempt <= self.max_retries:
            logger.info(f"AgentLoop | attempt={attempt}")
            action = self.planner.decide(query)
            answer = self.executor.execute(action, query)
            final_answer = answer

            if self.reflector.is_answer_acceptable(answer):
                break

            attempt += 1
            logger.info("AgentLoop | retry_triggered")

        scores = self.evaluator.evaluate(final_answer)

        logger.info("AgentLoop | completed")
        return {
            "answer": final_answer,
            "evaluation": scores
        }
