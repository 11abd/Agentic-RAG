class Executor:
    def __init__(self, rag_tool):
        self.rag_tool = rag_tool

    def execute(self, action: str, query: str) -> str:
        if action == "use_rag":
            return self.rag_tool.run(query)

        # Direct answer fallback (agent chose not to use RAG)
        return "This question does not require document retrieval."
