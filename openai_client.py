from __future__ import annotations

import json
import urllib.request
import urllib.error
from typing import Any, Dict


class OpenAIRequestError(RuntimeError):
    pass


def _post_json(url: str, headers: Dict[str, str], payload: Dict[str, Any], timeout: int) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
        raise OpenAIRequestError(f"OpenAI HTTPError {e.code}: {body}") from e
    except Exception as e:
        raise OpenAIRequestError(f"OpenAI request failed: {e}") from e


def chat(*, api_key: str, model: str, system: str, user: str, timeout_seconds: int) -> str:
    url = "https://api.openai.com/v1/responses"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Keep it simple: single-turn with context included in user message.
    payload = {
        "model": model,
        "input": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }

    resp = _post_json(url, headers, payload, timeout_seconds)

    chunks = []
    for item in resp.get("output", []) or []:
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text" and "text" in content:
                chunks.append(content["text"])
    text = "\n".join(c.strip() for c in chunks if c and c.strip()).strip()
    if not text:
        text = (resp.get("output_text") or "").strip()
    if not text:
        raise OpenAIRequestError("No text returned from OpenAI response.")
    return text
