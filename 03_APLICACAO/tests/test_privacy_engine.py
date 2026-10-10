#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o motor do Local Network Privacy Guard.
"""

import unittest
import re
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from privacy_engine import PrivacyEngine

class TestPrivacyEngine(unittest.TestCase):
    def test_formato_mac_valido(self):
        mac = PrivacyEngine.gerar_mac_aleatorio()
        padrao = r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"
        self.assertRegex(mac, padrao)

    def test_mac_bit_locally_administered(self):
        # Verifica se o primeiro byte tem o bit locally administered ativo (segundo hex digit 2, 6, A, E)
        for _ in range(20):
            mac = PrivacyEngine.gerar_mac_aleatorio()
            primeiro_byte = mac.split(":")[0].lower()
            self.assertIn(primeiro_byte[1], ["2", "6", "a", "e"])

    def test_diagnostico_estrutura(self):
        diag = PrivacyEngine.diagnostico_privacidade()
        self.assertIn("mac_sugerido", diag)
        self.assertIn("dns_servidores", diag)
        self.assertIn("dns_criptografado", diag)

if __name__ == "__main__":
    unittest.main()
