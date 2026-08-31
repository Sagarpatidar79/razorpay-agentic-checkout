from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_router import parse_user_intent, CheckoutIntent
from razorpay_gateway import PaymentService

app = FastAPI(title="Autonomous Agentic Checkout Engine", version="1.0.0")
payment_service = PaymentService()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "Razorpay Agentic Engine"}

@app.post("/chat/checkout")
def handle_checkout_chat(payload: ChatRequest):
    try:
        # Step 1: Parse intent deterministically
        intent: CheckoutIntent = parse_user_intent(payload.message)
        
        # Step 2: Route payment if checkout triggered
        order_details = None
        if intent.action == "initiate_payment":
            order_details = payment_service.create_order(
                amount_paise=49900, 
                session_id=payload.session_id
            )
            
        return {
            "session_id": payload.session_id,
            "parsed_intent": intent.model_dump(),
            "razorpay_order": order_details,
            "reply": "Order initiated successfully. Redirecting to secure Razorpay checkout." if order_details else "Cart updated."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
