import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="dark", rc=custom_params, palette='dark')

pastas = ['datasets/comuns', 'datasets/otimizadas']
linguagens = ['C', 'CPP', 'Rust', 'Rust-Sem-Debug', 'Rust-Sem-Checks', 'Java', 'Python', 'JavaScript']
ordenacoes = ['Aleatorio', 'Crescente', 'Decrescente']
tipos = ['', '-RangeMenor', '-RangeMaior', '-CEP', '-Iguais', '-Extremo']
tamanhos = [10000, 100000, 500000, 1000000]
i = 1

for ordenacao in ordenacoes:
    for tipo in tipos:
        dfTotal = pd.DataFrame()
        for linguagem in linguagens:
            df = pd.read_csv(
                f"datasets/comuns/tempoExecucao-{linguagem}.csv",
                skiprows=3,
                sep=',',
                nrows=4,
                usecols=[0, i],
                index_col=0,
                names=['Tamanho da Entrada', linguagem]
            )

            dfTotal = pd.concat([dfTotal, df], axis=1)
            print(dfTotal)

        plt.figure(figsize=(19.2, 10.8))
        plot = sns.lineplot(
            data=dfTotal,
            dashes=False,
            linewidth=3,
            markersize=10,
            
        )
        
        #plot.set_title(f'Performance do Radix Sort \n Vetores em ordem {ordenacao}{tipo}', fontsize=25, color='#E42328') 
        plot.set_xlabel('Tamanho da Entrada (n)', fontsize=25, color='white')
        plot.set_ylabel('Tempo de Execução (s)', fontsize=25, color='white')
        legend = plt.legend(
            title='Linguagem',
            loc='upper left',
            ncol=1,
            shadow=True,
            fancybox=True,
            fontsize=22,
            title_fontsize=22,
            facecolor='black',
            edgecolor='white',
            labelcolor='white'
        )

        legend.get_title().set_color('white')

        plot.tick_params(axis='y', labelsize=18)
        
        x_ticks = dfTotal.index.unique()
        plot.set_xticks(x_ticks)
        plot.set_xticklabels(x_ticks, fontsize=18)

        plot.figure.set_facecolor('black')
        plot.set_facecolor('black')

        plot.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    

        plt.savefig(f"datasets/graficos/grafico-{ordenacao}{tipo}.png")
        plt.close()
    
        i += 1


#ler os arquivos txt com números crescentes e gerar gráficos de dispersão de valores, (aparições x valor)

def leituraArquivo(vetor, nomeArquivo):
    with open(nomeArquivo, 'r') as file:
        linhasArquivo = file.readlines()
        linhaNumeros = linhasArquivo[-1].strip()

    for numero in linhaNumeros.split(", "):
        vetor.append(int(numero))

for tipo in tipos:
    vetor = []
    leituraArquivo(vetor, f"datasets/arquivosVetores/crescentes/1000000Crescente{tipo}.txt")
    vetor = sorted(vetor)

    df = pd.DataFrame(vetor, columns=['Valor'])
    df['Aparicoes'] = df.groupby('Valor')['Valor'].transform('count')
    df = df.drop_duplicates()

    plt.figure(figsize=(19.2, 10.8))
    plot = sns.scatterplot(
        data=df,
        x='Valor',
        y='Aparicoes',
        s=100,
        color='red',
        alpha=0.7
    )

    #plot.set_title(f'Dispersão de Valores\nVetor Crescente de 1.000.000{tipo} elementos', fontsize=25, color='#E42328')
    plot.set_xlabel('Valor', fontsize=25, color='white')
    plot.set_ylabel('Aparições', fontsize=25, color='white')

    plot.tick_params(axis='both', labelsize=18)

    plot.figure.set_facecolor('black')
    plot.set_facecolor('black')

    # usar apenas notação científica nos valores do eixo x
    plot.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    

    plot.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)

    plt.savefig(f"datasets/graficos/dispersao-1000000{tipo}.png")
    plt.close()
