from fastapi import FastAPI # type: ignore
from pydantic import BaseModel

from agent.planner import Planner
from agent.executor import Executor
from agent.agent_loop import AgentLoop
from agent.reflector import Reflector
from evaluation.metrics import AnswerEvaluator
from tools.rag_tool import RAGTool
from generation.rag_chain import ask_rag
from rag_pipeline import run_rag_pipeline

from utils.logger import logger

# ---------- FastAPI app ----------
app = FastAPI(
    title="Agentic RAG API",
    description="Agentic RAG system with reasoning, reflection, and evaluation",
    version="1.0"
)

# ---------- GLOBAL AGENT----------
_agent = None


def get_agent() -> AgentLoop:
    global _agent

    if _agent is None:
        logger.info("Initializing Agent components (lazy)")

        rag_tool = RAGTool(ask_rag)
        planner = Planner()
        executor = Executor(rag_tool)
        reflector = Reflector()
        evaluator = AnswerEvaluator()

        _agent = AgentLoop(
            planner=planner,
            executor=executor,
            reflector=reflector,
            evaluator=evaluator,
            max_retries=2
        )

    return _agent


# ---------- Request / Response Schemas ----------
class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    evaluation: dict


# ---------- API Endpoint ----------
@app.post("/query", response_model=QueryResponse)
def query_agent(request: QueryRequest):
    logger.info(f"API | query_received='{request.question}'")

    agent = get_agent()
    result = agent.run(request.question)

    return result


# ---------- Health Check ----------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------- Run pipeline ----------
@app.post("/pipeline/run")
def run_pipeline():
    global _agent

    logger.info("Running RAG pipeline via API")
    run_rag_pipeline()

    #reset agent after rebuilding vector DB
    _agent = None
    logger.info("Agent reset after pipeline run")

    return {"status": "success"}
