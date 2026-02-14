from __future__ import annotations

import base64
import os
import re
from dataclasses import dataclass
from typing import List, Tuple, Optional

from aqt import mw

try:
    from anki.utils import stripHTML  # type: ignore
except Exception:
    stripHTML = None  # type: ignore


_IMG_SRC_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
_MEDIA_PREFIX = re.compile(r"^(?:./)?_?media/")  # be permissive


@dataclass
class CardContext:
    deck: str
    note_type: str
    fields: List[Tuple[str, str]]
    question_text: str
    answer_text: str
    images: List[Tuple[str, str]]  # (filename, base64)


def _html_to_text(html: str) -> str:
    if stripHTML is not None:
        try:
            return stripHTML(html)
        except Exception:
            pass
    # fallback: very rough tag strip
    return re.sub(r"<[^>]+>", " ", html).replace("&nbsp;", " ").strip()


def _extract_img_filenames(html: str) -> List[str]:
    out: List[str] = []
    for m in _IMG_SRC_RE.finditer(html or ""):
        src = m.group(1).strip()
        if not src:
            continue
        # src might be e.g. "foo.png" or "_media/foo.png"
        src = _MEDIA_PREFIX.sub("", src)
        # ignore remote URLs
        if src.startswith("http://") or src.startswith("https://") or src.startswith("data:"):
            continue
        out.append(src)
    # de-dupe preserve order
    seen = set()
    dedup = []
    for x in out:
        if x not in seen:
            seen.add(x)
            dedup.append(x)
    return dedup


def _load_images_b64(filenames: List[str], max_images: int, max_bytes: int) -> List[Tuple[str, str]]:
    media_dir = mw.col.media.dir()
    images: List[Tuple[str, str]] = []
    for fn in filenames:
        if len(images) >= max_images:
            break
        path = os.path.join(media_dir, fn)
        if not os.path.exists(path):
            continue
        try:
            size = os.path.getsize(path)
            if size > max_bytes:
                continue
            with open(path, "rb") as f:
                b = f.read()
            b64 = base64.b64encode(b).decode("ascii")
            images.append((fn, b64))
        except Exception:
            continue
    return images


def current_card_context(*, max_images: int, max_image_bytes: int) -> Optional[CardContext]:
    # Works from the reviewer (doing cards). If no card is active, return None.
    reviewer = getattr(mw, "reviewer", None)
    card = getattr(reviewer, "card", None) if reviewer else None
    if card is None:
        return None

    note = card.note()
    deck = mw.col.decks.name(card.did) if hasattr(card, "did") else ""
    note_type = note.note_type()["name"] if hasattr(note, "note_type") else ""

    fields = [(name, note[name]) for name in note.keys()]

    q_html = card.question()
    a_html = card.answer()

    # Include both rendered Q/A text AND raw fields (often useful when templates rearrange).
    q_text = _html_to_text(q_html)
    a_text = _html_to_text(a_html)

    img_files = _extract_img_filenames(q_html) + _extract_img_filenames(a_html)
    # de-dupe again
    seen = set()
    img_files2 = []
    for x in img_files:
        if x not in seen:
            seen.add(x)
            img_files2.append(x)

    images = _load_images_b64(img_files2, max_images=max_images, max_bytes=max_image_bytes)

    return CardContext(
        deck=deck,
        note_type=note_type,
        fields=fields,
        question_text=q_text,
        answer_text=a_text,
        images=images,
    )
