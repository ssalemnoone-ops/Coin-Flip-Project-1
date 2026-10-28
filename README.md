# Coin Toss — Python & Streamlit

A small probability game with a terminal interface and a Streamlit web interface. Choose heads or tails, flip a simulated coin, and compare your guess with the result.

## Highlights

- Shared coin-toss logic used by both interfaces.
- Terminal input validation and replay prompts.
- Interactive web controls and immediate win/loss feedback.

## Run locally

Requires Python 3. Clone this repository and open its folder.

**Terminal**
```bash
python3 coin_toss_1_terminal.py
```

**Web interface**
```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run web.py
```

## Project structure

| File | Purpose |
| --- | --- |
| `game_logic.py` | Shared random coin-toss function |
| `coin_toss_1_terminal.py` | Terminal game |
| `web.py` | Streamlit interface |

## Scope

An introductory Python project exploring randomness, control flow, and separating application logic from the interface. Outcomes are simulated; this is not a financial model.

For the version with session history and counters, see [Coin Toss with Session Statistics](https://github.com/ssalemnoone-ops/CoinFlip-Project2).
