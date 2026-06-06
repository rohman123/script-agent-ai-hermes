import requests
import subprocess
import time

TOKEN='7757268858:AAG0DPSH01pGDV8jPQeuXnyBFt3xQ3qyWUU'
CHAT_ID = '581816529'
API_URL = f'https://api.telegram.org/bot{TOKEN}'

def send_message(text):
    url = f'{API_URL}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f'Error sending message: {e}')

def execute_command(command):
    try:
        import os
        # Ambil environment saat ini (termasuk PATH, HOME, dll)
        current_env = os.environ.copy()
        # Tambahkan path config gh jika perlu
        current_env["HOME"] = "/home/ubuntu/.hermes/profiles/appdev/home"
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30, env=current_env)
        output = result.stdout + result.stderr
        if not output.strip():
            output = "[Command executed successfully with no output]"
        return output[:4000]
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 30 seconds."
    except Exception as e:
        return f"Error executing command: {str(e)}"

def main():
    print("Telegram Controller started...")
    send_message("🚀 Telegram Controller is ONLINE (Token Updated). Send me a command!")
    last_update_id = 0
    
    while True:
        try:
            url = f'{API_URL}/getUpdates'
            params = {'offset': last_update_id + 1, 'timeout': 30}
            response = requests.get(url, params=params)
            updates = response.json().get('result', [])
            
            for update in updates:
                last_update_id = update['update_id']
                if 'message' in update and 'text' in update['message']:
                    chat_id_msg = str(update['message']['chat']['id'])
                    
                    if chat_id_msg != CHAT_ID:
                        send_message("⚠️ Unauthorized user. Access denied.")
                        continue
                        
                    command = update['message']['text']
                    print(f"Received command: {command}")
                    
                    if command.lower() in ['/start', '/help']:
                        send_message("Available commands:\n- Any shell command (e.g., `ls`, `pwd`, `gh repo list`)\n- `/status` to check controller status")
                    elif command.lower() == '/status':
                        send_message("✅ Controller is running and listening.")
                    elif command.lower() == '/stop':
                        send_message("Stopping controller... Goodbye!")
                        return
                    else:
                        send_message(f"Executing: `{command}`\n\n{execute_command(command)}")
                        
            time.sleep(1)
        except Exception as e:
            print(f"Main loop error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()