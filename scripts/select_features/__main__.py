import pandas as pd
import os
import datetime


dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(dir_path + '/raw.csv')

variaveis_extrair = [
    # contratos.csv
    'data_venda',
    'faturado',
    'valor_entrada',
    'qtd_parcelas',
    'primeiro_vencimento',
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
df = df.rename(index=str, columns={'mda.1': 'mda_cliente'})

df.to_csv(path_or_buf='data/out.csv',
          sep=';')
