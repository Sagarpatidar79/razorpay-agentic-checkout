# Autonomous Agentic Checkout & Conversational Commerce Engine

An intelligent, LLM-driven commerce copilot designed to eliminate checkout friction, automate cart interactions, and dynamically route payments using Razorpay APIs.

---

## 📌 Problem Statement
Over 65% of online e-commerce checkouts are abandoned due to multi-step checkout friction, static forms, and lack of real-time payment personalization.

## 🚀 Key Features
- **Conversational Checkout:** Natural language cart updates, product queries, and address parsing via WebSocket streaming.
- **Dynamic Payment Routing:** Auto-detects optimal payment methods (UPI, Cards, pre-approved BNPL) based on order context.
- **Deterministic Guardrails:** Strict Pydantic schema validation preventing LLM hallucinations during order calculation.
- **Zero-PII Architecture:** All sensitive payment collection is securely offloaded directly to hosted Razorpay SDKs.

## 🛠️ Tech Stack
- **Agent Orchestration:** Python, Lang Chain / Llama Index, Open AI/Claude APIs
- **Backend & Services:** Java (Spring Boot) / Fast API, AWS Lambda, REST APIs
- **Database & State:** Redis (Session caching & idempotency), PostgreSQL
- **Payments:** Razorpay Custom & Standard Checkout APIs

## 📐 System Architecture
1. **Client Layer:** Web SDK / Chat UI with bidirectional WebSocket connection.
2. **Agentic Layer:** Intent recognition, tool execution, and session state tracking.
3. **Backend Engine:** Deterministic price/tax calculations and Razorpay order generation.
