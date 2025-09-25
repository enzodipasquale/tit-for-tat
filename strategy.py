#!/usr/bin/env python3
"""
Tit-for-Tat Player - Dynamic Game Platform
"""

import requests
import json
import os
import sys

# Add parent directory to path for config_manager
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'ubx-dev'))
from config_manager import get_current_server

# ==================== CONFIGURATION ====================
PLAYER_NAME = "tit-for-tat"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "test-token-456")
SERVER_URL = get_current_server()

def strategy(state):
    """
    Tit-for-Tat Strategy: Copy opponent's last move
    
    Args:
        state: Dict with game state
            - state['turn_id']: Current turn number
            - state['state']: Dict of all players' action histories
    
    Returns:
        "cooperate" or "defect"
    """
    game_state = state.get('state', {})
    my_player_id = f"github-{PLAYER_NAME}-{PLAYER_NAME}"
    my_history = game_state.get(my_player_id, [])
    
    # First move: cooperate
    if len(my_history) == 0:
        return "cooperate"
    
    # Find an opponent and copy their last move
    for player_id, history in game_state.items():
        if player_id != my_player_id and len(history) > 0:
            return history[-1]
    
    # Default if no opponent found
    return "cooperate"

def submit_action(action):
    """Submit action to server"""
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GITHUB_TOKEN}"
        }
        data = {
            "strategy": {"action": action},
            "player_name": PLAYER_NAME
        }
        
        response = requests.post(f"{SERVER_URL}/action", 
                               headers=headers, 
                               json=data, 
                               timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Action submitted: {result}")
            return True
        else:
            print(f"❌ Error submitting action: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error submitting action: {e}")
        return False

def main():
    """Main function - gets game state and submits strategy"""
    print(f"🎮 {PLAYER_NAME} playing turn...")
    
    # Get current game state
    try:
        response = requests.get(f"{SERVER_URL}/state", timeout=10)
        if response.status_code != 200:
            print(f"❌ Error getting game state: {response.status_code}")
            return
        game_state = response.json()
    except Exception as e:
        print(f"❌ Error connecting to server: {e}")
        return
    
    print(f"📊 Turn {game_state.get('turn_id', 0)}: {game_state.get('state', {})}")
    
    # Get action from strategy
    action = strategy(game_state)
    print(f"🤔 Chosen action: {action}")
    
    # Submit action
    submit_action(action)

if __name__ == "__main__":
    main()
