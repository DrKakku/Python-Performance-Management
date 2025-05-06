import time
from fastapi import APIRouter

# Create the main API router for version 1
api_router = APIRouter()

# Example: Include other routers or define endpoints here
# from app.api.api_v1.endpoints import example_router
# api_router.include_router(example_router, prefix="/example", tags=["example"])

@api_router.get("/health-check", tags=["health"])
async def health_check():
    return {"status": "ok"}

@api_router.get("/cpu-intensive", tags=["cpu"])
def cpu_intensive(n: int):
    """A CPU-intensive endpoint that calculates the nth Fibonacci number."""
    def fibonacci(num: int) -> int:
        if num <= 1:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)

    start_time = time.time()
    result = fibonacci(n)
    duration = time.time() - start_time
    output = {
        "input": n,
        "result": result,
        "time_taken": f"{duration:.2f} seconds"
    }
    print(output)
    return output