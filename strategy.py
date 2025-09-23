#!/usr/bin/env python3
"""
Tit-for-Tat Player - Dynamic Game Platform
"""

import requests
import json
import os
import sys

# Configuration
PLAYER_NAME = "tit-for-tat"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "test-token-456")
SERVER_URL = "https://dynamic-game-platform-914970891924.us-central1.run.app"

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

def main():
    """Get state, run strategy, post action"""
    # Get game state
    state = requests.get(f"{SERVER_URL}/state", timeout=10).json()
    print(f"📊 Turn {state.get('turn_id', 0)}: {state.get('state', {})}")
    
    # Run strategy and submit
    action = strategy(state)
    print(f"🤔 Action: {action}")
    
    response = requests.post(f"{SERVER_URL}/action", 
                           # headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
                           json={"strategy": {"action": action}, "player_name": PLAYER_NAME})
    
    if response.status_code == 200:
        print(f"✅ {response.json()}")
    else:
        print(f"❌ {response.status_code}: {response.text}")

if __name__ == "__main__":
    main()