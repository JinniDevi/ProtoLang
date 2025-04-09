from pydantic import BaseModel
from langchain_core.runnables import RunnableLambda

# ✅ 입력 모델
class SimpleInput(BaseModel):
    name: str

# ✅ 출력 모델
class SimpleOutput(BaseModel):
    greeting: str

# ✅ 체인 함수 수정 (dict → 모델 변환 추가)
def greet_user(input: dict) -> SimpleOutput:
    parsed_input = SimpleInput(**input)  # dict를 SimpleInput 모델로 파싱
    return SimpleOutput(greeting=f"Hello, {parsed_input.name}!")

# ✅ Runnable 체인 등록
simple_chain = RunnableLambda(greet_user)
