class Planner:
    def decide(self, query: str) -> str:
        """
        Decide what action to take based on user query.
        Returns: 'use_rag' or 'direct_answer'
        """

        # Simple but explainable logic (very interview-friendly)
        if len(query.split()) < 4:
            return "direct_answer"

        return "use_rag"
