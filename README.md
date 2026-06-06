# Script Agent AI Hermes: WhatsApp Integration Components

This repository contains the core technical components required to deploy a professional, AI-powered WhatsApp Agent using the Hermes Agent architecture.

## 🤖 Overview

This integration transforms WhatsApp from a simple "Remote Terminal" into a highly intelligent AI Agent. By using the **Bridge-Adapter-Gateway** pattern, the agent can understand natural language and execute complex tasks (like GitHub operations) directly from a chat interface.

---

## 🛠️ Architecture & Components

The integration consists of three key parts:

| Component | File | Role |
| :--- | :--- | :--- |
| **WhatsApp Bridge** | `bridge.js` | **The Hands:** A Node.js process (using Baileys) that maintains the WhatsApp connection and exposes an HTTP API. |
| **WhatsApp Adapter** | `whatsapp_adapter.py` | **The Translator:** A Python adapter that polls the bridge and converts WhatsApp events into Hermes-compatible messages. |
| **Hermes Gateway** | (Core Process) | **The Brain:** The main Hermes Agent engine that performs reasoning, tool use, and decision-making. |

---

## 🚀 Step-by-Step Transformation Guide

If you are upgrading a standard shell-bridge bot to this AI-powered version, follow this evolution:

### Step 1: The Baseline (Traditional Bot)
A standard bot typically uses a simple Python script with `subprocess.run()` to execute raw Linux commands. 
*   **Limitation:** It cannot understand natural language and lacks access to the AI's toolset or environment.

### Step 2: Preparing the Environment
To make the bot "intelligent," we must ensure the Gateway can communicate with the WhatsApp Bridge. You need to set the following environment variables for the **Hermes Gateway**:

```bash
export WHATSAPP_BRIDGE_PORT=3000
export WHATSAPP_BRIDGE_SCRIPT=/path/to/your/bridge.js
export WHATSAPP_SESSION_PATH=/path/to/your/whatsapp/session
export WHATSAPP_DM_POLICY=open
export WHATSAPP_GROUP_POLICY=open
```

### Step 3: Launching the Gateway
Instead of running a standalone script, you launch the **Hermes Gateway**. This process automatically loads the `whatsapp.py` adapter and begins polling the bridge.

**Execution Command:**
```bash
cd /path/to/hermes-agent
PYTHONPATH=. python3 -m gateway.run
```

### Step 4: Result (AI Agent)
The transformation is complete. The user can now send natural language messages:
*   **User:** *"Show me my GitHub repos"*
*   **Agent:** *[Performs gh repo list via tool and responds conversationally]*

---

## 📦 Installation & Quick Start

### 1. Prerequisites
- **Node.js** (for the Bridge)
- **Python 3.x** (for the Gateway & Adapter)

### 2. Setup
Clone this repository and run the automated setup script:
```bash
# Clone the repo
git clone https://github.com/rohman123/script-agent-ai-hermes.git
cd script-agent-ai-hermes

# Run automatic setup
chmod +x setup.sh
./setup.sh
```

### 3. Running the System
**A. Start the WhatsApp Bridge:**
```bash
node bridge.js --port 3000 --session ./whatsapp_session
```

**B. Start the Hermes Gateway:**
(Ensure you have set the environment variables listed in the Step 2 section above)
```bash
python3 -m gateway.run
```

---
*Developed by Rohman Nur Haqiqi*
