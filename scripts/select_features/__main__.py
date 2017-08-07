import pandas as pd
import os
from datetime import date


dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(dir_path + '/raw.csv')


def calculaIdade(floatDate):
    if not floatDate > 0:
        return 0
    strDate = str(floatDate)
    dateObject = date(year=int(strDate[0:4]),
                      month=int(strDate[4:6]),
                      day=int(strDate[6:8]))
    return date.today().year - dateObject.year


variaveis_extrair = [
    # contratos.csv
    'faturado',
    'valor_entrada',
    'qtd_parcelas',
    'valor_financiado',
    'valor_parcela',
    'mda',
    'qtd_consultas_ate15dias',
    'qtd_consultas_ate60dias',
    'qtd_registros',
    'qtd_contratos_quitados_cliente',
    'qtd_contratos_abertos_cliente',
    'media_atraso_cliente',
    # clientes.csv
    'sexo',
    'data_nascimento',
    'tel_fixo',
    'estado_civil',
    'dependentes',
    'veiculo',
    'veiculo_financiado',
    'moradia',
    'anos_residencia',
    'ocupacao',
    'telefone_comercial',
    'data_admissao',
    'salario',
    'mda.1'
    ]

df = df[variaveis_extrair]
df['data_nascimento'] = df['data_nascimento'].apply(calculaIdade)
df['data_admissao'] = df['data_admissao'].apply(calculaIdade)
df = df.rename(index=str, columns={'mda.1': 'mda_cliente',
                                   'data_admissao': 'anos_empresa',
                                   'data_nascimento': 'idade'})

df.to_csv(path_or_buf='data/out.csv',
          sep=';')
