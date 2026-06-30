from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
from sse_starlette.sse import EventSourceResponse

app= FastAPI()
connected_clients=[]


@app.get("/")
def home():
    return {"message": "Realtime API is Running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(f"Message: {message}")
                
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

async def counter_generator():
    count= 1
    while True:
        yield {
            "event": "counter",
            "data": f"Count: {count}" 
        }
        count +=1
        await asyncio.sleep(1)

@app.get("/events")
async def events():
    return EventSourceResponse(counter_generator())
