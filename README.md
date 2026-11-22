# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/verlianmr/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/verlianmr/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,067 bytes of Python (packed with the official make.fun `compress` from the readable 8,182-byte source). Final build of the v10–v17 iteration campaign, certified on the kit practice gauntlet (trial-0, two independent runs, byte-identical): **Elo 2112 (the practice cap), 6 wins / 0 draws / 0 losses, all checkmate, spare_plies 753**; trial-1 cross-check: Elo 1809, 5W / 1D / 0L, spare_plies 433. 0x88 board, copy-make, incremental Zobrist hashing; PVS alpha-beta with transposition table, quiescence search (captures, promotions, check replies), null-move pruning, late-move reductions with re-search, check extensions, history heuristic (reset at the start of every game), in-search repetition detection; full PeSTO tapered piece-square tables, passed-pawn bonus, endgame mop-up term; per-scenario node budgets (deterministic, no wall clock); 14-entry CRC32 opening book. Fully deterministic: fixed node counts per move, no clock. Speaks the make.fun environment protocol: it polls MAKEFUN_ENV_URL for games and answers with UCI moves.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8917 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=cw40tr4n&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
