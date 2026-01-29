from fastapi import FastAPI # type: ignore
from pydantic import BaseModel

from agent.planner import Planner
from agent.executor import Executor
from agent.agent_loop import AgentLoop
from agent.reflector import Reflector
from evaluation.metrics import AnswerEvaluator
from tools.rag_tool import RAGTool
from generation.rag_chain import ask_rag

from utils.logger import logger

# ---------- FastAPI app ----------
app = FastAPI(
    title="Agentic RAG API",
    description="Agentic RAG system with reasoning, reflection, and evaluation",
    version="1.0"
)

# ---------- Agent Initialization (ONCE) ----------
logger.info("Initializing Agent components")

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
    result = agent.run(request.question)
    return result


# ---------- Health Check ----------
@app.get("/health")
def health():
    return {"status": "ok"}
