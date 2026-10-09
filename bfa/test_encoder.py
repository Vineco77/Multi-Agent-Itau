from fastapi.encoders import jsonable_encoder
import asyncio
from app import lifespan
from fastapi import FastAPI
from registry import resolve_agent, AGENT_REGISTRY

async def main():
    app = FastAPI()
    async with lifespan(app):
        result = resolve_agent("cartao de credito", filter_type="agent")
        print("\n\n--- Result ---")
        # print Registry Keys and their types
        for k, v in AGENT_REGISTRY.items():
            print(k, type(k))
            for k2, v2 in v.items():
                print("  ", k2, type(v2))
                if isinstance(v2, list):
                    if len(v2) > 0:
                        print("    [0]", type(v2[0]))
        
        # Test jsonable_encoder
        try:
            print("Trying jsonable_encoder(result)...")
            jsonable_encoder(result)
            print("jsonable_encoder succeeded!")
        except Exception as e:
            print(f"Exception: {e}")

asyncio.run(main())
