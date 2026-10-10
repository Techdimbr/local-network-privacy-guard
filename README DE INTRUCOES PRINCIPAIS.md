# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Local Network Privacy Guard

**Repositório Oficial:** `https://github.com/Techdimbr/local-network-privacy-guard`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Local Network Privacy Guard
- **Identificador (Slug):** `local-network-privacy-guard`
- **Categoria:** Segurança Operacional & Privacidade de Rede
- **Stack Tecnológica:** Python 3 (stdlib puro), NetworkManager (`nmcli`), `iproute2`, `systemd-resolved`, DoH/DoT
- **Objetivo Central:** Automatizar a proteção contra vigilância de rede local para endpoints corporativos, aplicando rotação determinística de endereços físicos (MAC), encriptação de requisições DNS e bloqueio de vazamentos.

### Casos de Uso Reais
1. **Proteção em Viagens e Aeroportos:** Ativação instantânea do modo sigilo antes de associar a redes Wi-Fi abertas.
2. **Prevenção contra Perfilamento de Dispositivo:** Alteração diária do MAC Address em estações corporativas.
3. **Teste de DNS Leak Automatizado:** Diagnóstico contínuo para garantir que nenhuma consulta DNS escape em texto claro na porta 53.

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── privacy_engine.py                  # Motor central de geração de MAC e verificação de rede
├── mac_rotator.py                     # Wrapper para manipulação via nmcli e ip link
├── dns_guardian.py                    # Gerenciador de perfis DoH para systemd-resolved
└── killswitch.py                      # Regras iptables/nftables para contenção de tráfego em caso de falha
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS RECURSOS DE PRIVACIDADE -->
- [x] Gerador de MAC com bit locally administered (`02:...`) para evitar colisões;
- [x] Detector de servidores DNS ativos no resolv.conf;
- [ ] Integração com daemon systemd em background para monitoramento de troca de SSID;
- [ ] Interface CLI com atalhos rápidos (`privacy-guard --stealth-on` / `--stealth-off`).
