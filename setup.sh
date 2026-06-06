#!/bin/bash
# Auto-setup script for Hermes WhatsApp Integration

echo "🚀 Starting Hermes WhatsApp Integration Setup..."

# 1. Install Node dependencies
echo "📦 Installing Node.js dependencies..."
npm install @whiskeysockets/baileys express pino qrcode-terminal

# 2. Create session directory
echo "📁 Creating session directory..."
mkdir -p ./whatsapp_session

echo "✅ Setup complete!"
echo "👉 To start the Bridge, run: node bridge.js --port 3000 --session ./whatsapp_session"
echo "👉 To start the Gateway, run the gateway command with the exported variables."
