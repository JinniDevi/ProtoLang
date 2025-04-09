# app.py

from fastapi import FastAPI
from langserve import add_routes
from chains.simple_chain import simple_chain, SimpleInput, SimpleOutput

# ✅ FastAPI 앱 생성
app = FastAPI()
# ✅ docs_url, redoc_url 끄기
# app = FastAPI(docs_url=None, redoc_url=None)

# ✅ LangServe 체인 등록
add_routes(
    app,
    runnable=simple_chain,
    path="/simple",
    input_type=SimpleInput,   # ✅ 입력 타입 명시
    output_type=SimpleOutput, # ✅ 출력 타입 명시
)
