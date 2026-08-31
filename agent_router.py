from pydantic import BaseModel, Field
from typing import Optional

class CheckoutIntent(BaseModel):
    action: str = Field(description="Action to take: add_item, apply_coupon, initiate_payment")
    item_id: Optional[str] = None
    quantity: Optional[int] = 1
    payment_method: Optional[str] = None  # e.g., 'upi', 'card', 'bnpl'

def parse_user_intent(user_prompt: str) -> CheckoutIntent:
    # Simulated deterministic parsing/guardrail
    if "pay" in user_prompt.lower() or "checkout" in user_prompt.lower():
        return CheckoutIntent(action="initiate_payment", payment_method="upi")
    return CheckoutIntent(action="add_item", item_id="SKU_1001", quantity=1)

if __name__ == "__main__":
    test_query = "Proceed to pay with UPI"
    intent = parse_user_intent(test_query)
    print(f"Validated Intent: {intent.model_dump()}")
