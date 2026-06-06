# Script Agent AI Hermes - WhatsApp Integration

This repository contains the core components to integrate WhatsApp as an AI-powered agent using Hermes Agent.

## Architecture
1. **WhatsApp Bridge (The Hands):** `bridge.js` (Node.js + Baileys) - Connects WhatsApp to the system via HTTP.
2. **WhatsApp Adapter (The Translator):** `whatsapp_adapter.py` - Translates WhatsApp messages into Hermes-compatible events.
3. **Hermes Gateway (The Brain):** The main Hermes Agent process that interprets messages and executes tools.

## Deployment Prompt
When setting this up with an AI Agent, use this prompt:
> "Integrasikan WhatsApp ke Hermes Agent AI menggunakan pattern Bridge. Gunakan Node.js (Baileys) sebagai bridge di port 3000, dan hubungkan ke WhatsAppAdapter di gateway/platforms/whatsapp.py. Pastikan environment variabel untuk port, script path, dan session path sudah disetel."

## Installation & Setup
1. **Install Dependencies:**
   - Node.js (for the bridge)
   - Python 3.x (for the gateway and adapter)
   - `npm install @whiskeysockets/baileys express pino qrcode-terminal` inside the bridge directory.

2. **Run the Bridge:**
   ```bash
   node bridge.js --port 3000 --session ./whatsapp_session
   ```

3. **Run the Hermes Gateway:**
   Set the following environment variables and run the gateway:
   ```bash
   export WHATSAPP_BRIDGE_PORT=3000
   export WHATSAPP_BRIDGE_SCRIPT=$(pwd)/bridge.js
   export WHATSAPP_SESSION_PATH=$(pwd)/whatsapp_session
   export WHATSAPP_DM_POLICY=open
   export WHATSAPP_GROUP_POLICY=open
   python3 -m gateway.run
   ```
