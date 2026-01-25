class AgentLoop:
    def __init__(self, planner, executor, reflector, max_retries=2):
        self.planner = planner
        self.executor = executor
        self.reflector = reflector
        self.max_retries = max_retries

    def run(self, query: str) -> str:
        attempt = 0

        while attempt <= self.max_retries:
            action = self.planner.decide(query)
            answer = self.executor.execute(action, query)

            if self.reflector.is_answer_acceptable(answer):
                return answer

            attempt += 1

        # If all retries fail, return last answer with transparency
        return answer + "\n\n[Note: Answer quality may be limited based on available data.]"
