# Script Agent AI Hermes 🤖🚀

A professional, all-in-one repository for deploying an AI-powered WhatsApp and Telegram Agent using the Hermes Agent architecture.

## 🌟 Overview

This repository integrates **WhatsApp** and **Telegram** into the **Hermes Agent AI Core**, transforming simple command-line bridges into highly intelligent, natural-language-capable AI assistants.

**⚠️ SECURITY NOTE:** This repository is designed to be secure. It uses environment variables for secrets and is configured to prevent session data from being uploaded. **Never share your .env file or session folders.**

---

## 🏗️ Architecture (WhatsApp Integration)

The WhatsApp integration uses a **Bridge-Adapter-Gateway** pattern:

| Component | File | Role | Technology |
| :--- | :--- | :--- | :--- |
| **WhatsApp Bridge** | `bridge.js` | **The Hands:** Maintains the connection. | Node.js + Baileys |
| **WhatsApp Adapter** | `whatsapp_adapter.py` | **The Translator:** Converts events for Hermes. | Python |
| **Hermes Gateway** | (Core Process) | **The Brain:** Performs reasoning and tool use. | Hermes Agent Core (LLM) |
| **Telegram Controller**| `telegram_controller.py`| **Remote Terminal:** Direct shell command bridge. | Python |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Node.js** (for the WhatsApp Bridge)
- **Python 3.x** (for the Gateway & Adapters)
- **GitHub CLI (`gh`)** (for AI tool access)

### 2. Installation & Setup

First, clone the repository:
```bash
git clone https://github.com/rohman123/script-agent-ai-hermes.git
cd script-agent-ai-hermes
```

Run the automated setup script:
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Running the System

#### A. Start the WhatsApp Bridge (Authentication Required)
When you run this command, the terminal will display a **QR Code**. 
**You must scan this QR code with your own WhatsApp mobile app** (linked devices) to authenticate your session.

```bash
# This will prompt for QR Code scan on first run
node bridge.js --port 3000 --session ./whatsapp_session
```

#### B. Start the Hermes Gateway (The AI Brain)
Ensure your environment variables are set.
```bash
# From the hermes-agent directory
PYTHONPATH=. python3 -m gateway.run
```

#### C. Start the Telegram Controller (Optional)
To use Telegram as a remote terminal, set your credentials as environment variables first:
```bash
export TELEGRAM_TOKEN='your_bot_token_here'
export TELEGRAM_CHAT_ID='your_chat_id_here'
python3 telegram_controller.py
```

---

## 🛠️ Configuration (Environment Variables)

### For WhatsApp AI Agent
Set these in your Hermes environment:
```bash
export WHATSAPP_BRIDGE_PORT=3000
export WHATSAPP_BRIDGE_SCRIPT=/absolute/path/to/bridge.js
export WHATSAPP_SESSION_PATH=/absolute/path/to/whatsapp_session
export WHATSAPP_DM_POLICY=open
export WHATSAPP_GROUP_POLICY=open
```

### For Telegram Controller
```bash
export TELEGRAM_TOKEN='your_bot_token_here'
export TELEGRAM_CHAT_ID='your_chat_id_here'
```

---

*Developed with ❤️ by [Rohman Nur Haqiqi](https://github.com/rohman123)*