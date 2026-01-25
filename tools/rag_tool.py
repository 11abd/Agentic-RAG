class RAGTool:
    def __init__(self, rag_pipeline):
        """
        rag_pipeline: your existing RAG object or function
        """
        self.rag_pipeline = rag_pipeline

    def run(self, query: str) -> str:
        """
        Executes RAG retrieval + generation
        """
        return self.rag_pipeline(query)
