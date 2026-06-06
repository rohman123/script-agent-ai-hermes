# Technical Architecture: WhatsApp AI Integration

## The Bridge-Adapter Pattern

To bridge the gap between a Node.js-based WhatsApp library (Baileys) and a Python-based AI Gateway, we utilize a decoupled architecture.

### 1. The Bridge (Node.js)
The Bridge runs a local HTTP server (Express) and maintains the WhatsApp connection. It acts as a "dumb" data provider.

**Core Endpoints:**
- `GET /messages`: Long-polling for new inbound messages.
- `POST /send`: Sending text or media back to the user.

### 2. The Adapter (Python)
The Adapter lives within the Hermes Gateway. It acts as the "glue" code.

**Responsibilities:**
- **Polling:** Periodically checks the Bridge for new messages.
- **Normalization:** Converts WhatsApp-specific JSON structures into a standardized `MessageEvent` that the AI understands.
- **Identity Management:** Handles LID/JID normalization for reliable sender identification.

### 3. The Gateway (AI Core)
The Gateway is the orchestration layer. It treats the WhatsApp platform just like any other (Telegram, Discord, etc.).

**Intelligence Loop:**
1. Receive `MessageEvent`.
2. Pass to `AIAgent.run_conversation()`.
3. Agent calls tools (e.g., `github_repo_list`).
4. Result is formatted and passed back to the Adapter.
