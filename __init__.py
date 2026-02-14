from __future__ import annotations

from aqt import mw
from aqt.qt import QAction, QKeySequence
from aqt.utils import showWarning

from .ui_sidebar import ChatDock


_dock: ChatDock | None = None


def _ensure_dock() -> ChatDock:
    global _dock
    if _dock is None:
        _dock = ChatDock(mw)
        mw.addDockWidget(_dock.default_area, _dock)
    return _dock


def toggle_sidebar() -> None:
    dock = _ensure_dock()
    dock.setVisible(not dock.isVisible())


def open_sidebar() -> None:
    dock = _ensure_dock()
    dock.setVisible(True)
    dock.raise_()

def open_settings() -> None:
    dock = _ensure_dock()
    dock.open_settings_dialog()


def _add_menu_items() -> None:
    # Avoid relying on Tools menu (not present in some builds).
    # View menu is consistently present.
    menu = getattr(mw.form, "menuView", None) or getattr(mw.form, "menuHelp", None)
    if menu is None:
        showWarning("Could not find a menu to attach ChatGPT Sidebar action.")
        return

    action = QAction("ChatGPT Sidebar (Ask about current card)", mw)
    action.setShortcut(QKeySequence("Ctrl+Shift+G"))
    action.triggered.connect(toggle_sidebar)
    mw.form.menuView.addAction(action)

    # Add Settings to Tools Menu (User requested explicit Tools menu item)
    tools_menu = getattr(mw.form, "menuTools", None)
    if tools_menu:
        action_settings = QAction("Ricardo Settings", mw)
        action_settings.triggered.connect(open_settings)
        tools_menu.addAction(action_settings)


_add_menu_items()
