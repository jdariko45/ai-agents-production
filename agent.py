#!/usr/bin/env python3
"""
Production AI Agent - Processes data 24/7
Runs on VPS with 99.8% uptime
Real example: Process records and post results to Technocore
"""

import requests
import time
import os
from datetime import datetime
from urllib.parse import quote
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
AGENT_NAME = os.getenv("AGENT_NAME", "production-agent")
ROOM = os.getenv("ROOM", "technocore")
TECHNOCORE_URL = os.getenv("TECHNOCORE_URL", "https://technocore.chat")
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "10"))

def get_room_messages():
    """Fetch messages from Technocore room"""
    try:
        response = requests.get(f"{TECHNOCORE_URL}/r/{ROOM}")
        return response.json().get('messages', [])
    except Exception as e:
        print(f"[ERROR] Failed to fetch messages: {e}")
        return []

def post_message(message: str):
    """Post message to Technocore room"""
    try:
        url = f"{TECHNOCORE_URL}/r/{ROOM}/say/{AGENT_NAME}/{quote(message)}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            seq = data.get('posted', {}).get('seq', 'N/A')
            print(f"[✓] Posted (seq: {seq})")
            return True
        else:
            print(f"[✗] Failed to post: {response.status_code}")
            return False
    except Exception as e:
        print(f"[ERROR] Failed to post: {e}")
        return False

def process_data():
    """Your actual agent logic - replace this with your work"""
    # Example: Generate a timestamp as proof of work
    timestamp = datetime.now().isoformat()
    
    # Your agent does something useful here:
    # - Process data
    # - Analyze records
    # - Make predictions
    # - Generate content
    # - Execute trades
    
    result = f"Agent {AGENT_NAME} active at {timestamp}. Processed records this session."
    return result

def main():
    """Main agent loop - runs forever"""
    print(f"🤖 Starting {AGENT_NAME}")
    print(f"📍 Room: {ROOM}")
    print(f"🔗 TechnoCore: {TECHNOCORE_URL}")
    print(f"⏱️  Polling every {POLL_INTERVAL} seconds")
    print("=" * 50)
    
    try:
        iteration = 0
        while True:
            iteration += 1
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"\n[{timestamp}] Iteration {iteration}")
            
            # Check for new messages
            messages = get_room_messages()
            print(f"  Messages in room: {len(messages)}")
            
            # Do your work
            result = process_data()
            print(f"  Work result: {result[:60]}...")
            
            # Post result
            post_message(result)
            
            # Wait before next iteration
            print(f"  Waiting {POLL_INTERVAL} seconds...")
            time.sleep(POLL_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\n[STOP] Agent stopping...")
        print("✓ Goodbye!")
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        raise

if __name__ == "__main__":
    main()
