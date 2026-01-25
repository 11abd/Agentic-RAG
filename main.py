from evaluation.metrics import AnswerEvaluator
from agent.reflector import Reflector
from agent.agent_loop import AgentLoop
from agent.planner import Planner
from agent.executor import Executor
from tools.rag_tool import RAGTool
from generation.rag_chain import ask_rag  

def main():
    rag_tool = RAGTool(ask_rag)

    planner = Planner()
    executor = Executor(rag_tool)
    reflector = Reflector()
    evaluator = AnswerEvaluator()

    agent = AgentLoop(
        planner=planner,
        executor=executor,
        reflector=reflector,
        evaluator=evaluator,
        max_retries=2
    )

    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == "exit":
            break

        result = agent.run(query)

        print("\nAgent Answer:\n", result["answer"])
        print("\nEvaluation Scores:")
        for k, v in result["evaluation"].items():
            print(f"  {k}: {v:.2f}")


if __name__ == "__main__":
    main()
