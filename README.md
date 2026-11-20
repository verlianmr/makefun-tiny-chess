# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/verlianmr/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/verlianmr/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,073 bytes of Python. 0x88 board, negamax alpha-beta with a transposition table, quiescence search (captures), MVV-LVA and TT-move ordering, and piece-square-table evaluation (Michniewski-style pawn and knight tables). Fully deterministic: fixed 100,000-node search per move, no clock. Speaks the make.fun environment protocol: it polls MAKEFUN_ENV_URL for games and answers with UCI moves.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8917 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=REFERRAL_CODE_HERE&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
