from typing import Dict, List, Optional


def _first_value(query: Dict[str, List[str]], name: str) -> Optional[str]:
    if query:
        values = query.get(name, [])
        if values and len(values) > 0:
            return values[0]
    return None
