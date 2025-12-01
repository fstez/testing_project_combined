"""Pytest konfigureerija, mis lisab projekti juure sys.path'i."""

import sys
from pathlib import Path

PROJEKTI_JUUR = Path(__file__).resolve().parent
if str(PROJEKTI_JUUR) not in sys.path:
    sys.path.insert(0, str(PROJEKTI_JUUR))

