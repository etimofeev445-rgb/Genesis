from __future__ import annotations

import json
from pathlib import Path

from .core import Blockchain


def save_chain(chain: Blockchain, path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(chain.to_dict(), indent=2), encoding="utf-8")
    temporary.replace(target)


def load_chain(path: str | Path) -> Blockchain:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return Blockchain.from_dict(data)
