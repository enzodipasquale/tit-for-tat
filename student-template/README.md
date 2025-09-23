# Dynamic Game Platform - Student Template

## 🎮 How to Play

This is an automated dynamic game platform where you submit strategies via GitHub Actions.

### Game Rules
- **Actions**: Check `game_rules.py` for valid actions and scoring
- **Strategy**: Write Python code that decides your action based on game history
- **Platform**: Dynamic game engine that can run any game defined in `game_rules.py`

## 🚀 Setup Instructions

### 1. Fork This Repository
Click "Fork" in the top-right corner of this repository.

### 2. Update Your Player Info
Edit `strategy.py`:
```python
# Change these to your info
PLAYER_NAME = "your-name"  # Your display name
GITHUB_TOKEN = "your-github-token"  # Get from GitHub Settings > Developer settings > Personal access tokens
SERVER_URL = "https://your-server-url.run.app"  # Get this from your instructor
```

### 3. Get GitHub Token
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (full control of private repositories)
4. Copy the token and paste it in `strategy.py`

### 4. Get Server URL
Ask your instructor for the game server URL (it will look like `https://something.run.app`)

### 5. Enable GitHub Actions
1. Go to your forked repository
2. Click "Actions" tab
3. Click "I understand my workflows, go ahead and enable them"
4. The game will run automatically every few minutes

## 🎯 Your Strategy

Edit the `strategy` function in `strategy.py`:

```python
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
    # Example: Always choose first action
    return "cooperate"
    
    # Example: Tit-for-tat (copy opponent's last move)
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
```

## 🧪 Test Your Setup

1. **Test locally** (optional):
   ```bash
   python strategy.py
   ```

2. **Check GitHub Actions**:
   - Go to Actions tab in your repository
   - Look for "Dynamic Game Bot" workflow
   - Check if it runs successfully

## 📊 Monitor Your Performance

- **Game State**: Check the server for current game status
- **Scores**: Your score updates after each turn
- **History**: See all players' action histories

## 🔧 Troubleshooting

- **"Invalid token"**: Check your GitHub token is correct
- **"Player not registered"**: Make sure registration is open
- **"Game not active"**: Wait for the game to start

## 🎮 Game Phases

1. **Registration Open**: You can register your player
2. **Registration Closed**: Registration period ended
3. **Game Started**: You can submit actions
4. **Game Ended**: Game is finished

Good luck! 🚀
