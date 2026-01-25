class Reflector:
    def __init__(self, min_length: int = 30):
        self.min_length = min_length

    def is_answer_acceptable(self, answer: str) -> bool:
        """
        Generic quality checks.
        No topic-specific logic.
        """

        if answer is None:
            return False

        text = answer.strip().lower()

        # Empty or extremely short answers
        if len(text) < self.min_length:
            return False

        # Typical RAG failure phrases
        failure_signals = [
            "i don't know",
            "does not provide",
            "no information",
            "not available in the context"
        ]

        for signal in failure_signals:
            if signal in text:
                return False

        return True
