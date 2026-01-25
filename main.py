from agent.planner import Planner
from agent.executor import Executor
from agent.agent_loop import AgentLoop
from agent.reflector import Reflector
from tools.rag_tool import RAGTool

from generation.rag_chain import ask_rag

def main():
    rag_tool = RAGTool(ask_rag)

    planner = Planner()
    executor = Executor(rag_tool)
    reflector = Reflector()

    agent = AgentLoop(
        planner=planner,
        executor=executor,
        reflector=reflector,
        max_retries=2
    )

    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == "exit":
            break

        response = agent.run(query)
        print("\nAgent Response:\n", response)


if __name__ == "__main__":
    main()
