# Tit-for-Tat Player

## Strategy
This player implements the **Tit-for-Tat** strategy:
- **First move**: Cooperate
- **Subsequent moves**: Copy the opponent's last move

## How to Play

1. **Push to GitHub** - This strategy will automatically play every 2 minutes
2. **Watch the game** - See how Tit-for-Tat performs against other strategies!

## Your Strategy Function

Edit the `main()` function in `strategy.py`:

```python
def main(state):
    # state contains:
    # - my_history: Your previous actions
    # - opponent_history: Opponent's previous actions  
    # - my_score: Your current score
    # - opponent_score: Opponent's current score
    # - round: Current round number
    
    # Return 'cooperate' or 'defect'
    return 'cooperate'  # Change this!
```

## Example Strategies

- **Always Cooperate**: `return 'cooperate'`
- **Always Defect**: `return 'defect'`
- **Tit-for-Tat**: Copy opponent's last move
- **Random**: Randomly choose cooperate/defect

## Game Rules

- **Both Cooperate**: 3 points each
- **One Cooperates, One Defects**: 0 points (cooperator), 5 points (defector)
- **Both Defect**: 1 point each

That's it! Just edit the `main()` function and push to GitHub.
