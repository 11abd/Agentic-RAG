class AnswerEvaluator:
    def __init__(self, min_length=50):
        self.min_length = min_length

    def evaluate(self, answer: str) -> dict:
        scores = {
            "length_score": 0.0,
            "clarity_score": 0.0,
            "grounding_score": 0.0
        }

        if not answer:
            return scores

        text = answer.strip().lower()
        length = len(text)

        # 1. Length score (is the answer substantial?)
        scores["length_score"] = min(length / self.min_length, 1.0)

        # 2. Clarity score (penalize uncertainty phrases)
        unclear_phrases = [
            "i don't know",
            "not sure",
            "does not provide",
            "no information"
        ]

        clarity_penalty = any(p in text for p in unclear_phrases)
        scores["clarity_score"] = 0.0 if clarity_penalty else 1.0

        # 3. Grounding score (very simple heuristic)
        grounding_penalty = "context" in text and "not" in text
        scores["grounding_score"] = 0.0 if grounding_penalty else 1.0

        return scores
