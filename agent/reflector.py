from utils.logger import logger

class Reflector:
    def __init__(self, min_length: int = 30):
        self.min_length = min_length

    def is_answer_acceptable(self, answer: str) -> bool:
        if answer is None:
            logger.info("Reflector | FAIL | reason=answer_none")
            return False

        text = answer.strip().lower()

        if len(text) < self.min_length:
            logger.info(f"Reflector | FAIL | reason=too_short | length={len(text)}")
            return False

        failure_signals = [
            "i don't know",
            "does not provide",
            "no information",
            "not available in the context"
        ]

        for signal in failure_signals:
            if signal in text:
                logger.info(f"Reflector | FAIL | reason=signal_detected | signal='{signal}'")
                return False

        logger.info("Reflector | PASS")
        return True
