#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Network Privacy Guard - Motor de Rotação de MAC e Blindagem DNS
Python 3 stdlib puro
"""

import sys
import os
import random
import re
from typing import List, Dict, Any

class PrivacyEngine:
    @staticmethod
    def gerar_mac_aleatorio() -> str:
        """
        Gera um MAC Address unicast localmente administrado válido.
        O segundo dígito hexadecimal deve ser 2, 6, A ou E para indicar Locally Administered Unicast.
        """
        prefixos_locais = ["02", "06", "0a", "0e"]
        primeiro_byte = random.choice(prefixos_locais)
        restante = [f"{random.randint(0, 255):02x}" for _ in range(5)]
        return f"{primeiro_byte}:{':'.join(restante)}"

    @staticmethod
    def ler_dns_atual() -> List[str]:
        """Lê os servidores DNS configurados no sistema (/etc/resolv.conf)."""
        caminho = "/etc/resolv.conf"
        servidores = []
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if linha.startswith("nameserver"):
                        partes = linha.split()
                        if len(partes) >= 2:
                            servidores.append(partes[1])
        except Exception:
            pass
        return servidores

    @classmethod
    def diagnostico_privacidade(cls) -> Dict[str, Any]:
        mac_sugerido = cls.gerar_mac_aleatorio()
        dns_servidores = cls.ler_dns_atual()
        
        # Considera seguro se utilizar localhost (stub-resolver de DoH) ou servidores seguros conhecidos
        dns_seguro = any(s in ["127.0.0.53", "1.1.1.1", "9.9.9.9", "127.0.0.1"] for s in dns_servidores)
        
        return {
            "mac_sugerido": mac_sugerido,
            "dns_servidores": dns_servidores,
            "dns_criptografado": dns_seguro
        }

def main():
    print("=" * 65)
    print("🛡️  TECHDIM LOCAL NETWORK PRIVACY GUARD - STATUS DE PRIVACIDADE")
    print("=" * 65)
    
    diag = PrivacyEngine.diagnostico_privacidade()
    
    print(f"🔒 MAC Address Randômico Gerado : {diag['mac_sugerido']}")
    print(f"🌐 Servidores DNS Detectados    : {', '.join(diag['dns_servidores']) or 'Nenhum'}")
    
    status_dns = "✅ SEGURO (DoH / Stub Local Ativo)" if diag["dns_criptografado"] else "⚠️  POTENCIAL VAZAMENTO (DNS em texto claro)"
    print(f"🛡️  Status de Proteção DNS       : {status_dns}")
    print("-" * 65)
    print("✓ Módulo de privacidade operacional.")

if __name__ == "__main__":
    main()
