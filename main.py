import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

""" ---------------------------------------------------------------------------------------------"""

# Não mudar função DEF. - A função printa os dados informados no formulário diretamente no terminal

def salvar_dados():
    Aceito = aceitar_var.get()
    
    if Aceito =="Aceito":

        # Informação de usuario - imprimir
        numero_nfiscal = dados_entrada_nf.get()
        numero_nserie = dados_entrada_serie.get()

        if numero_nfiscal and numero_nserie:

            entrada_saida = entrada_saida_combobox.get()
            quantidade_itens_nf = quantidade_itens_spinbox.get()
            tipo_servico_nf = tipo_servico_combobox.get()

            # Informação de Cursos - imprimir
            status_registro = registro_status_var.get()
            selecao_frete_nf = selecao_frete_spinbox.get()
            valor_nf_total = dados_valor_nf.get()

            print("-------------COLETA DE DADOS FORMULARIO-------------")
            print()
            print("Numero NF: ", numero_nfiscal, "Numero Série: ", numero_nserie)
            print("Entrada ou saída: ", entrada_saida, "Quantidade de itens: ", quantidade_itens_nf, "Tipo de serviço: ", tipo_servico_nf)
            print("Frete: ", selecao_frete_nf, "Valor total da NF: ", valor_nf_total)
            print("Staus do registro: ", status_registro)
            print()
            print("----------------------------------------------------")
        
        # Criar tabela SQL
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Dados_nota_fiscal 
                    (numero_nfiscal TEXT, numero_nserie TEXT, entrada_saida TEXT, quantidade_itens_nf INT, tipo_servico_nf TEXT, 
                    status_registro TEXT, selecao_frete_nf INT, valor_nf_total TEXT)
            '''
            conn.execute(table_create_query)

        # inserir dados
            data_insert_query = '''INSERT INTO Dados_nota_fiscal (numero_nfiscal, numero_nserie, entrada_saida, 
            quantidade_itens_nf, tipo_servico_nf, status_registro, selecao_frete_nf, valor_nf_total) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (numero_nfiscal, numero_nserie, entrada_saida,
                                  quantidade_itens_nf, tipo_servico_nf, status_registro, selecao_frete_nf, valor_nf_total)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            tkinter.messagebox.showwarning(title = 'Error', message ='É necessário informar Numero e Série')

    else:
        tkinter.messagebox.showwarning(title = 'Error', message ='Favor revisar seu lançamento')

""" ----------------------------------------------------------------------------------------------"""

janela = tkinter.Tk()
janela.title('Sistema de lançamento de Notas Fiscais')

cabecalho = tkinter.Frame(janela)
cabecalho.grid() # Compactando o arquivo de acordo com as informações na janela. 

# Input de informações da NF
cabecalho_informacao_NF = tkinter.LabelFrame(cabecalho, text = 'Informação da Nota Fiscal')
cabecalho_informacao_NF.grid(row = 0, column = 0, padx = 20, pady = 10)

numero_nf = tkinter.Label(cabecalho_informacao_NF, text = 'Numero NF')
numero_nf.grid(row = 0, column= 0)
serie_nf = tkinter.Label(cabecalho_informacao_NF, text = 'Série')
serie_nf.grid(row = 0, column = 1)

dados_entrada_nf = tkinter.Entry(cabecalho_informacao_NF)
dados_entrada_serie = tkinter.Entry(cabecalho_informacao_NF)

dados_entrada_nf.grid(row = 1, column = 0)
dados_entrada_serie.grid(row = 1, column= 1)

entrada_saida = tkinter.Label(cabecalho_informacao_NF, text = 'Entrada ou Saída')
entrada_saida_combobox = ttk.Combobox(cabecalho_informacao_NF, values = ["Entrada", "Saída"])
entrada_saida.grid(row = 0, column = 2)
entrada_saida_combobox.grid(row = 1, column = 2)

quantidade_itens = tkinter.Label(cabecalho_informacao_NF, text = 'Quantidade item')
quantidade_itens_spinbox = tkinter.Spinbox(cabecalho_informacao_NF, from_=1, to=100)
quantidade_itens.grid(row = 2, column = 0)
quantidade_itens_spinbox.grid(row = 3, column = 0)

tipo_servico = tkinter.Label(cabecalho_informacao_NF, text = 'Serviço')
tipo_servico_combobox = ttk.Combobox(cabecalho_informacao_NF, values = ["Manutenção","Limpeza","Financeiro","Entregas"])
tipo_servico.grid(row = 2 , column = 1)
tipo_servico_combobox.grid(row = 3, column = 1)

for widget in cabecalho_informacao_NF.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# Salvar quantidade de cursos realizados

cabecalho_fiscal_sn_frete_valor = tkinter.LabelFrame(janela)
cabecalho_fiscal_sn_frete_valor.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

status_simples_nacional = tkinter.Label(cabecalho_fiscal_sn_frete_valor, text = 'Status registro Simples Nacional')

# Criando um botão clicavel e atribuindo responsividade pela informação
registro_status_var = tkinter.StringVar(value = 'Não Registrado no S/N')
check_registro = tkinter.Checkbutton(cabecalho_fiscal_sn_frete_valor, text = "Atualmente inscrito", 
                                    variable = registro_status_var, onvalue = "Registrado no S/N", offvalue ="Não Registrado no S/N")

status_simples_nacional.grid(row = 0, column = 0)
check_registro.grid(row = 1, column = 0)

selecao_frete_cabecalho = tkinter.Label(cabecalho_fiscal_sn_frete_valor, text = '1 - Com Frete / 2 - Sem Frete')
selecao_frete_spinbox = tkinter.Spinbox(cabecalho_fiscal_sn_frete_valor, from_= 1, to = 2)
selecao_frete_cabecalho.grid(row = 0, column = 1)
selecao_frete_spinbox.grid(row = 1, column = 1)

valor_nota_fiscal = tkinter.Label(cabecalho_fiscal_sn_frete_valor, text = 'Valor NF')
dados_valor_nf = tkinter.Entry(cabecalho_fiscal_sn_frete_valor)
valor_nota_fiscal.grid(row = 0, column = 2)
dados_valor_nf.grid(row = 1, column = 2)

for widget in cabecalho_fiscal_sn_frete_valor.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)


# Aceite dos Termos


termos_cabecalho = tkinter.LabelFrame(janela, text = 'Revisão de lançamento')
termos_cabecalho.grid(row = 2, column = 0, sticky='news', padx=20, pady=10)

aceitar_var = tkinter.StringVar(value = "Não Aceito")
check_termos = tkinter.Checkbutton(termos_cabecalho, text = 'Estou ciente que os dados acima foram revisados antes do lançamento',
                                    variable = aceitar_var, onvalue = "Aceito", offvalue="Não aceito")

check_termos.grid(row = 0, column=0)

# Botão

button = tkinter.Button(janela, text = 'Salvar Dados', command = salvar_dados)
button.grid(row = 3, column = 0, sticky='news', padx = 20 , pady = 10)

janela.mainloop()