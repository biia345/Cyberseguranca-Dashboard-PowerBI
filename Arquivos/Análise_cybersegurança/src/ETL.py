import os
import pandas as pd

# 1. Extração
dados = pd.read_csv("../database/Global_Cybersecurity_Threats_2015-2024.csv")
print("[INFO] Arquivo carregado com sucesso.")

# 2. Transformação

# Renomear colunas pra português
dados.columns = [
    "país", "ano", "tipo_ataque", "setor_alvo",
    "perda_financeira_usd", "usuarios_afetados", "origem_ataque",
    "tipo_vulnerabilidade", "mecanismo_defesa", "tempo_resolucao_horas"
]
print("[INFO] Colunas padronizadas e traduzidas pra português.")

# Dicionários de tradução
mapa_ataques = {
    "phishing": "fraude por e-mail",
    "ransomware": "sequestro de dados",
    "man-in-the-middle": "interceptação",
    "ddos": "ataque de negação de serviço",
    "sql injection": "injeção de SQL",
    "zero-day": "exploração de vulnerabilidade desconhecida"
}

mapa_setores = {
    "education": "educação",
    "retail": "varejo",
    "it": "tecnologia da informação",
    "telecommunications": "telecomunicações",
    "finance": "finanças",
    "healthcare": "saúde"
}

mapa_origem = {
    "hacker group": "grupo hacker",
    "nation-state": "estado-nação",
    "insider": "agente interno",
    "individual": "indivíduo"
}

mapa_vulnerabilidades = {
    "unpatched software": "software desatualizado",
    "weak passwords": "senhas fracas",
    "social engineering": "engenharia social",
    "misconfigured systems": "sistemas mal configurados"
}

mapa_defesa = {
    "vpn": "rede privada virtual",
    "firewall": "firewall",
    "ai-based detection": "detecção baseada em IA",
    "multi-factor authentication": "autenticação multifator"
}

mapa_paises = {
    "china": "china",
    "india": "índia",
    "uk": "reino unido",
    "germany": "alemanha",
    "france": "frança",
    "australia": "austrália",
    "russia": "rússia",
    "united states": "estados unidos",
    "brazil": "brasil"
}

# Agrupar todos os mapeamentos
MAPAS = {
    "tipo_ataque": mapa_ataques,
    "setor_alvo": mapa_setores,
    "origem_ataque": mapa_origem,
    "tipo_vulnerabilidade": mapa_vulnerabilidades,
    "mecanismo_defesa": mapa_defesa,
    "país": mapa_paises
}

# Funções auxiliares
def limpar_texto(valor):
    """Remove espaços e coloca em minúsculo"""
    if isinstance(valor, str):
        return valor.strip().lower()
    return valor

def traduzir(dados: pd.DataFrame):
    """Aplica limpeza + tradução usando os dicionários"""
    for coluna, dicionario in MAPAS.items():
        dados[coluna] = dados[coluna].apply(limpar_texto).map(dicionario)
    return dados

def tratar_dados(dados: pd.DataFrame):
    """Remove duplicatas e valores nulos"""
    dados.drop_duplicates(inplace=True)
    dados.dropna(inplace=True)
    return dados

# Aplicar funções
dados = traduzir(dados)
print("[INFO] Dados categóricos traduzidos pra português.")

dados = tratar_dados(dados)
print("[INFO] Duplicatas e valores nulos removidos.")

# 3. Carga
os.makedirs("data/processed", exist_ok=True)
dados.to_csv("data/processed/Ameacas_Ciberseguranca_2015-2024_limpo.csv", index=False)
print("[INFO] Arquivo limpo salvo com sucesso em data/processed/Ameacas_Ciberseguranca_2015-2024_limpo.csv")
