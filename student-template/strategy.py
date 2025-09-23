#!/usr/bin/env python3
"""
Dynamic Game Strategy Template
Edit the main function to implement your strategy
"""

import requests
import json
import os
import sys

# Add parent directory to path to import config_manager
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from config_manager import get_current_server

# ==================== CONFIGURATION ====================
# CHANGE THESE TO YOUR INFO
PLAYER_NAME = "your-name"  # Your display name
GITHUB_TOKEN = "your-github-token"  # Get from GitHub Settings > Developer settings > Personal access tokens
SERVER_URL = get_current_server()  # Dynamic Game Platform Server (auto-configured)

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
            print(f"Action submitted: {result}")
            return True
        else:
            print(f"Error submitting action: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Error submitting action: {e}")
        return False

def strategy(state):
    """
    Your strategy function!
    
    Args:
        state: Dict with game state
            - state['turn_id']: Current turn number
            - state['state']: Dict of all players' action histories
                Example: {"player1": ["action1", "action2"], "player2": ["action1"]}
    
    Returns:
        str: Valid action for the current game (check game_rules.py for valid actions)
    """
    
    # ==================== YOUR STRATEGY HERE ====================
    # Example strategies:
    
    # 1. Always choose first action
    return "cooperate"
    
    # 2. Always choose second action
    # return "defect"
    
    # 3. Tit-for-tat (copy opponent's last move)
    # game_state = state.get('state', {})
    # my_player_id = f"github-{PLAYER_NAME}-{PLAYER_NAME}"
    # my_history = game_state.get(my_player_id, [])
    # 
    # if len(my_history) == 0:
    #     return "cooperate"  # First move: choose first action
    # else:
    #     # Find an opponent and copy their last move
    #     for player_id, history in game_state.items():
    #         if player_id != my_player_id and len(history) > 0:
    #             return history[-1]
    #     return "cooperate"  # Default if no opponent found
    
    # 4. Random strategy
    # import random
    # return random.choice(["cooperate", "defect"])
    
    # 5. Choose first action for first 3 turns, then second action
    # turn_number = state.get('turn_id', 0)
    # if turn_number < 3:
    #     return "cooperate"
    # else:
    #     return "defect"

def main():
    """Main function - gets game state and submits your strategy"""
    
    # Get current game state
    try:
        response = requests.get(f"{SERVER_URL}/state", timeout=10)
        if response.status_code != 200:
            print(f"Error getting game state: {response.status_code}")
            return
        game_state = response.json()
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return
    
    print(f"📊 Current turn: {game_state.get('turn_id', 0)}")
    print(f"🎯 Game state: {game_state.get('state', {})}")
    
    # Get your action from strategy
    action = strategy(game_state)
    print(f"🤔 Chosen action: {action}")
    
    # Submit action
    submit_action(action)

if __name__ == "__main__":
    main()
