import uuid

class PaymentService:
    def __init__(self, api_key: str = "rzp_test_mock"):
        self.api_key = api_key

    def create_order(self, amount_paise: int, currency: str = "INR", session_id: str = None) -> dict:
        # Enforcing idempotency key via session_id
        idempotency_key = session_id or str(uuid.uuid4())
        
        # Mock Razorpay Order API Response
        return {
            "id": f"order_{uuid.uuid4().hex[:14]}",
            "entity": "order",
            "amount": amount_paise,
            "currency": currency,
            "status": "created",
            "idempotency_key": idempotency_key
        }

if __name__ == "__main__":
    service = PaymentService()
    order = service.create_order(amount_paise=49900, session_id="sess_user_123")
    print(f"Created Razorpay Order: {order}")
