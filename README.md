# 🛡️ Local Network Privacy Guard
## Guardião de Privacidade Operacional e Blindagem de Rede Local para Estações Linux

![Local Network Privacy Guard](06_MIDIA/banner_oficial.png)

[![Padrão](https://img.shields.io/badge/Padr%C3%A3o-PRJ--TECHDIM--PUBLIC--v1.0.0-00E5FF.svg)](https://techdimbr.github.io/techdimbr/)
[![Doutrina](https://img.shields.io/badge/Doutrina-KETHER__1-7C4DFF.svg)](https://www.techdim.com.br)
[![Stack](https://img.shields.io/badge/Stack-Python%203%20Puro%20%7C%20nmcli%20%7C%20iproute2-FF6F00.svg)](https://www.python.org)
[![Privacidade](https://img.shields.io/badge/DNS-DoH%20%2F%20DoT%20Encrypted-blueviolet.svg)](README.md)
[![Anti--Tracking](https://img.shields.io/badge/MAC-Randomization%20Active-brightgreen.svg)](README.md)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT%20Corporate-green.svg)](LICENSE)

> **Proteção ativa de privacidade para estações de trabalho e notebooks corporativos em trânsito. Alternância automatizada de MAC Address por conexão, DNS seguro via DoH/DoT contra interceptação de operadoras e bloqueio de tráfego residual em redes públicas (Kill Switch).**

---

## 🏛️ Visão Geral & Proposta de Valor

Ao conectar em redes Wi-Fi públicas, hotéis ou coworkings, estações de trabalho sofrem com:
- **Rastreamento Físico de MAC Address:** Criação de perfis de deslocamento e identificação de dispositivos de executivos.
- **Vazamento e Sequestro de DNS (DNS Leak):** Roteadores maliciosos interceptam requisições DNS não criptografadas na porta 53, expondo todos os sites e serviços acessados.
- **Tráfego Residual em Troca de Redes:** Pacotes corporativos transmitidos em claro durante a troca de conexões Wi-Fi.

O **Local Network Privacy Guard** automatiza a blindagem local:
1. **Rotação Dinâmica de MAC Address:** Altera o endereço MAC a cada nova associação de rede, gerando endereços unicast localmente administrados perfeitamente válidos.
2. **DNS Criptografado Obrigatório (DoH/DoT):** Garante que todas as resoluções passem por túneis criptografados TLS (Cloudflare 1.1.1.1 / Quad9 9.9.9.9), tornando o histórico de navegação invisível ao provedor da rede local.
3. **Kill Switch Preventivo:** Bloqueia temporariamente o tráfego de rede caso o DNS criptografado caia, impedindo qualquer vazamento silencioso em texto claro.

---

## 🏗️ Topologia da Blindagem Local

```mermaid
graph TD
    Device["Estação de Trabalho / Laptop"] -->|1. MAC Spoofing Aleatório| Interface["Interface Wi-Fi / Ethernet"]
    Interface -->|2. Roteamento de Saída Bloqueado| KillSwitch["Local Kill Switch"]
    KillSwitch -->|3. Resolução Segura DoH/DoT (Porta 443/853)| EncDNS["Resolvedor DNS Seguro (Quad9 / Cloudflare)"]
    EncDNS -->|4. Túnel Criptografado| Router["Roteador Wi-Fi Público / Provedor"]
    Router --> Internet["Internet (Zero Rastreamento & Zero DNS Leaks)"]
```

---

## ⚡ Início Rápido

### Comandos de Operação
```bash
# 1. Clonar o repositório
git clone https://github.com/Techdimbr/local-network-privacy-guard.git
cd local-network-privacy-guard

# 2. Inicializar o ambiente
./iniciar.sh

# 3. Testar a geração de MAC Address seguro e verificação de DNS
python3 03_APLICACAO/src/privacy_engine.py --status
```

---

## 🛡️ Governança & Contato Corporativo
- **Autor:** Deivis Írio Mayer (Kether_1)
- **Entidade:** TECHDIM INOVA SIMPLES (I.S.) - ME · CNPJ 61.933.926/0001-24
- **Website Oficial:** [https://www.techdim.com.br](https://www.techdim.com.br)
- **Portal de Soluções:** [https://techdimbr.github.io/techdimbr/](https://techdimbr.github.io/techdimbr/)
