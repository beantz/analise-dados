import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

# Dados reorganizados
data_filmes_mais_venderam_bem = {
    'Title': [
        'Avatar', 'Avengers: Endgame', 'Avatar: The Way of Water', 
        'Star Wars: Episode VII - The Force Awakens', 'Avengers: Infinity War', 
        'Spider-Man: No Way Home', 'Jurassic World', 'The Lion King', 
        'The Avengers', 'Furious 7', 'Top Gun: Maverick', 'Frozen II', 
        'Barbie', 'Avengers: Age of Ultron', 'The Super Mario Bros. Movie',
        'Harry Potter and the Deathly Hallows: Part 2', 'Black Panther',
        'Star Wars: Episode VIII - The Last Jedi', 'Frozen', 
        'Jurassic World: Fallen Kingdom'
    ],
    'Gross worldwide': [
        2923706026, 2799439100, 2320250281, 2071310218, 2052415039, 
        1921847111, 1671537444, 1663075401, 1520538536, 1515341399, 
        1495696292, 1453683476, 1441791846, 1405018048, 1361976691, 
        1356841356, 1349926083, 1334407706, 1334291571, 1310466296
    ]
}

# Dados dos filmes que menos venderam globalmente
data_venderamMenos = {
    'Title': [
        'Sniper. The White Raven', 'About Cherry', 'We Are the Flesh', 
        'YPF', 'Barefoot', 'Red', 'London', 
        'Poultrygeist: Night of the Chicken Dead', 'A Secret Promise', 'CBGB'
    ],
    'Gross worldwide': [
        6105.0, 8315.0, 8438.0, 14459.0, 15071.0, 
        15617.0, 20361.0, 22623.0, 39493.0, 40400.0
    ]
}

# Dados dos orçamentos dos filmes
data_budget = {
    'Title': [
        'Alienoid', 'The Great Battle', 'The Host', 'Train to Busan', 
        'The Handmaiden', 'The Tale of The Princess Kaguya', 'Lady Vengeance', 
        'Brahmastra Part One: Shiva', 'RRR', 'Baahubali 2: The Conclusion', 
        'Laal Singh Chaddha', 'Bajirao Mastani', 'Student of the Year 2', 
        'Dangal', 'Red Cliff'
    ],
    'Budget': [
        30000000000.00, 15000000000.00, 12215500000.00, 10000000000.00, 
        10000000000.00, 5000000000.00, 4200000000.00, 4100000000.00, 
        3500000000.00, 2500000000.00, 1800000000.00, 1250000000.00, 
        800000000.00, 700000000.00, 553632000.00
    ]
}

# Dados dos filmes com durações
dados_duracao = {
    'Title': [
        'Gods and Generals', 'Killers of the Flower Moon', 'The Lord of the Rings: The Return of the King',
        'Avatar: The Way of Water', 'Grindhouse', 'Petite Maman', '9 Songs', 'The Secret of Kells',
        "Pooh's Heffalump Movie", 'Winnie the Pooh'
    ],
    'Runtime': ['3h 39m', '3h 26m', '3h 21m', '3h 12m', '3h 11m', '1h 13m', '1h 11m', '1h 11m', '1h 8m', '1h 3m']
}

# Dados dos filmes com melhores avaliações
data_melhores_avaliacoes = {
    'Title': [
        'The Dark Knight', 'The Lord of the Rings', 'Joker', 
        'Avengers: Infinity War', 'The Dark Knight Rises', 
        'Avengers: Endgame', 'Top Gun: Maverick', 'Toy Story 3', 
        'Spider-Man: No Way Home', 'Harry Potter'
    ],
    'Rating': [9.0, 9.0, 8.4, 8.4, 8.4, 8.4, 8.3, 8.3, 8.2, 8.1]
}

# Dados dos filmes com piores avaliações entre os mais bem vendidos
data_piores_avaliacoes = {
    'Title': [
        'Jurassic World Dominion', 'Transformers',
        'Jurassic World', 'Transformers: Dark',
        'Despicable Me 3', 'Star Wars: Episode IX',
        'Minions', 'Alice in Wonderland', 'The Fate of the Furious',
        'Pirates of the Caribbean', 'The Lion King',
        'Frozen II', 'Aquaman', 'Captain Marvel', 'Jurassic World',
        'Star Wars: Episode VIII - The Last Jedi', 'Aladdin', 'Barbie',
        'The Super Mario Bros. Movie', 'Iron Man 3', 'Beauty and the Beast',
        'Furious 7', 'Finding Dory'
    ],
    'Rating': [
        5.6, 5.6, 6.1, 6.2, 6.2, 6.4, 6.4, 6.4, 6.6, 6.6, 6.8, 6.8, 6.8,
        6.8, 6.9, 6.9, 6.9, 7.0, 7.1, 7.1, 7.1, 7.1, 7.2
    ],
    'Gross Worldwide': [
        800000000, 1000000000, 900000000, 1200000000, 950000000,
        750000000, 1100000000, 600000000, 850000000, 950000000,
        1150000000, 700000000, 850000000, 1050000000, 1250000000,
        950000000, 820000000, 900000000, 800000000, 850000000,
        1100000000, 1050000000, 1150000000
    ]
}

data = {
    'Title': [
        'The Dark Knight', 'The Lord of the Rings: The Return of the King',
        'Joker', 'Avengers: Infinity War', 'The Dark Knight Rises',
        'Avengers: Endgame', 'Top Gun: Maverick', 'Toy Story 3',
        'Spider-Man: No Way Home', 'Harry Potter and the Deathly Hallows: Part 2',
        'Zootopia', 'The Avengers', 'Avatar', 'Rogue One: A Star Wars Story',
        'The Hobbit: An Unexpected Journey'
    ],
    'Gross in US & Canada': [
        534987076, 379427292, 335477657, 678815482, 448149584,
        858373000, 718732821, 415004880, 814115070, 381447587,
        341268248, 623357910, 785221649, 533539991, 303030651
    ]
}

# Dados dos gêneros de filmes e suas contagens
generos = ['Drama', 'Comedy', 'Action', 'Adventure', 'Crime']
contagens = [1359, 1012, 937, 738, 505]

# Criar DataFrame para os dados dos gêneros
df_generos = pd.DataFrame({
    'Gênero': generos,
    'Contagem': contagens
})

# Dados dos diretores e a contagem de filmes que eles lançaram
dataDirector = {
    'Director': [
        'Steven Spielberg', 'Ridley Scott', 'Clint Eastwood', 'Antoine Fuqua', 
        'Steven Soderbergh', 'Michael Bay', 'Shawn Levy', 'Guy Ritchie', 
        'Tim Burton', 'M. Night Shyamalan', 'Marc Forster', 'James Wan', 
        'Christopher Nolan', 'James Mangold', 'Woody Allen'
    ],
    'Movies': [
        16, 16, 13, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 9, 9
    ]
}

# Criando o DataFrame
df_directors = pd.DataFrame(dataDirector)

# Criar o gráfico de pizza com Plotly
fig_pizza = px.pie(
    df_generos,
    names='Gênero',
    values='Contagem',
    title='Gêneros que Mais se Repetem',
    color_discrete_sequence=['gold', 'lightcoral', 'skyblue', 'lightgreen', 'lightskyblue']
)

# Configuração do gráfico de pizza
fig_pizza.update_traces(
    textinfo='label+percent',
    hole=0.3  # Faz um gráfico de pizza com um buraco no meio, similar a um gráfico de anel
)

fig_pizza.update_layout(
    title_text='Gêneros que Mais se Repetem',
    annotations=[dict(text='Gêneros', x=0.5, y=0.5, font_size=20, showarrow=False)],
    autosize=True,
    margin=dict(t=50, b=0, l=0, r=0)
)

# Criando um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Ordenando os filmes pelo faturamento em US & Canada (do maior para o menor)
df_sorted = df.sort_values(by='Gross in US & Canada', ascending=True).head(10)

# Convertendo o faturamento para milhões e ajustando o tipo de dados
df_sorted['Gross in US & Canada (Millions $)'] = df_sorted['Gross in US & Canada'] / 1_000_000
df_sorted['Gross in US & Canada (Formatted)'] = df_sorted['Gross in US & Canada (Millions $)'].apply(lambda x: f'${x:.2f}M')

# Criando DataFrames
df_mais_venderam_bem = pd.DataFrame(data_filmes_mais_venderam_bem)
df_venderamMenos = pd.DataFrame(data_venderamMenos)
df_budget = pd.DataFrame(data_budget)
df_duracao = pd.DataFrame(dados_duracao)
df_melhores_avaliacoes = pd.DataFrame(data_melhores_avaliacoes)
df_piores_avaliacoes = pd.DataFrame(data_piores_avaliacoes).head(10)

# Calcular a média dos valores de vendas globais
media_vendas = df_mais_venderam_bem['Gross worldwide'].mean()

# Função para formatar valores em bilhões (B)
def format_value(val):
    return f'{val/1e9:.2f}B'

# Aplicando a formatação ao DataFrame
df_mais_venderam_bem['Formatted Gross worldwide'] = df_mais_venderam_bem['Gross worldwide'].apply(format_value)
df_budget['Formatted Budget'] = df_budget['Budget'].apply(format_value)

# Função para converter 'Runtime' para minutos
def convert_to_minutes(runtime):
    parts = runtime.split()
    hours = int(parts[0][:-1]) * 60  # Remove o 'h' e converte para minutos
    minutes = int(parts[1][:-1]) if len(parts) > 1 else 0  # Remove o 'm' e converte para minutos
    return hours + minutes

# Aplicando a função de conversão
df_duracao['Runtime (minutes)'] = df_duracao['Runtime'].apply(convert_to_minutes)

# Ordenando os filmes pelo tempo de execução
df_sorted_duracao = df_duracao.sort_values(by='Runtime (minutes)', ascending=False)

# Selecionando os 5 filmes mais longos e os 5 filmes mais curtos
longest_movies = df_sorted_duracao.head(5)
shortest_movies = df_sorted_duracao.tail(5)

# Combinando os dados
combined_movies = pd.concat([longest_movies, shortest_movies])

# Criando o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Análise de Vendas Globais dos Filmes'),

    html.Div([
        html.H2('Top 15 Filmes que Mais Venderam Bem no Século 21'),
        dcc.Graph(
            id='line-plot',
            figure=px.line(
                df_mais_venderam_bem.head(15), x='Title', y='Gross worldwide',
                title='Top 15 Filmes que Mais Venderam Bem no Século 21',
                markers=True,
                text='Formatted Gross worldwide'
            ).update_traces(textposition='top center').update_layout(
                xaxis_tickangle=-45,
                yaxis_title='Arrecadação Global ($)',
                xaxis_title='Filme',
                height=800
            )
        )
    ]),

    html.Div([
        html.H2('Média de Vendas Globais dos Filmes que Mais Venderam'),
        dcc.Graph(
            id='bar-plot',
            figure=px.bar(
                df_mais_venderam_bem, x='Title', y='Gross worldwide', 
                title='Média de Vendas Globais dos Filmes que Mais Venderam',
                labels={'Gross worldwide': 'Vendas Globais ($)', 'Title': 'Filmes'}
            ).update_layout(
                shapes=[{
                    'type': 'line',
                    'x0': -0.5, 'x1': len(df_mais_venderam_bem)-0.5, 
                    'y0': media_vendas, 'y1': media_vendas,
                    'line': {'color': 'red', 'dash': 'dash'}
                }],
                annotations=[{
                    'x': len(df_mais_venderam_bem)-0.5, 'y': media_vendas * 1.15,
                    'xref': 'x', 'yref': 'y',
                    'text': f'Média: ${media_vendas:,.2f}',
                    'showarrow': False,
                    'align': 'right'
                }],
                xaxis_tickangle=-45
            )
        )
    ]),

    html.Div([
        html.H2('Os 10 Filmes que Menos Venderam Globalmente no Século 21'),
        dcc.Graph(
            id='bar-plot-menos',
            figure=px.bar(
                df_venderamMenos, x='Title', y='Gross worldwide',
                title='Os 10 Filmes que Menos Venderam Globalmente no Século 21',
                labels={'Gross worldwide': 'Vendas Globais ($)', 'Title': 'Filmes'}
            ).update_traces(texttemplate='%{y:,.2f}', textposition='outside').update_layout(
                xaxis_tickangle=-45,
                yaxis_title='Vendas Globais ($)',
                xaxis_title='Filme',
                height=600,
                showlegend=False
            )
        )
    ]),

    html.Div([
       html.H2('Orçamento de Filmes'),
       dcc.Graph(
           id='budget-plot',
           figure=px.bar(
               df_budget, x='Title', y='Budget',
               title='Filmes que tiveram o orçamento mais alto',
               text='Formatted Budget'
           ).update_traces(textposition='outside').update_layout(
               xaxis_tickangle=-45,
               yaxis_title='Orçamento ($)',
               xaxis_title='Filme',
               height=600
           )
       )
    ]),

    html.Div([
       html.H2('Top 5 Filmes com Menor e Maior Duração'),
       dcc.Graph(
           id='duration-plot',
           figure=px.bar(
               combined_movies, y='Title', x='Runtime (minutes)',
               orientation='h',
               title='Top 5 Filmes com Menor e Maior Duração',
               labels={'Runtime (minutes)': 'Duração (minutos)', 'Title': 'Filmes'}
           ).update_traces(texttemplate='%{x} min', textposition='outside').update_layout(
               xaxis_title='Duração (minutos)',
               yaxis_title='Título do Filme',
               height=600,
               showlegend=False
           )
       )
    ]),

    html.Div([
       html.H2('Melhores Avaliações Dentre os Filmes Mais Caros'),
       dcc.Graph(
           id='rating-plot',
           figure=px.scatter(
               df_melhores_avaliacoes, x='Title', y='Rating',
               title='Melhores Avaliações Dentre os Filmes Mais Caros',
               labels={'Rating': 'Avaliação', 'Title': 'Filmes'},
               hover_name='Title',  # Nome do filme exibido no hover
               hover_data={'Rating': True}  # Avaliação exibida no hover
           ).update_traces(marker=dict(size=12, color='blue'), mode='markers+text', text=df_melhores_avaliacoes['Rating'],
                           textposition='top center').update_layout(
               xaxis_tickangle=-45,
               yaxis_title='Avaliação',
               xaxis_title='Filme',
               height=600,
               showlegend=False
            )
        )
    ]),

    html.Div([
        html.H2('Piores Avaliações Dentre os Filmes Mais Bem Vendidos'),
        dcc.Graph(
            id='scatter-plot-piores-avaliacoes',
            figure={
                'data': [
                    go.Scatter(
                        x=df_piores_avaliacoes['Title'],
                        y=df_piores_avaliacoes['Gross Worldwide'],
                        mode='markers',
                        marker=dict(
                            size=12,
                            color=df_piores_avaliacoes['Rating'],  # Cor das bolinhas baseada na avaliação
                            colorscale='Viridis',  # Escala de cores para a avaliação
                            colorbar=dict(title='Avaliação'),  # Título da barra de cores
                            line=dict(width=1, color='DarkSlateGrey')
                        ),
                        text=df_piores_avaliacoes['Rating'],  # Texto exibido ao passar o mouse sobre as bolinhas
                        hoverinfo='text+y',  # Informação exibida no hover
                    )
                ],
                'layout': go.Layout(
                    title='Piores Avaliações Dentre os Filmes Mais Bem Vendidos',
                    xaxis=dict(title='Filmes', tickangle=-45,
                    title_standoff=20),
                    yaxis=dict(title='Arrecadação Global ($)'),
                    height=800,
                     margin=dict(l=100, b=150),
                    showlegend=False,
                    hovermode='closest'
                )
            }
        )
    ]),

    html.Div([
        html.H2('Filmes com Maior Faturamento em US & Canada'),
        dcc.Graph(
            id='bar-plot-faturamento-us-canada',
            figure={
                'data': [
                    go.Bar(
                        x=df_sorted['Gross in US & Canada (Millions $)'],
                        y=df_sorted['Title'],
                        orientation='h',
                        marker=dict(color='skyblue'),  # Cor das barras
                        text=df_sorted['Gross in US & Canada (Formatted)'],  # Texto formatado
                        textposition='outside',  # Posição do texto
                    )
                ],
                'layout': go.Layout(
                    title='Filmes com Maior Faturamento em US & Canada',
                    xaxis=dict(title='Faturamento em US & Canada (Milhões $)'),
                    yaxis=dict(title='Filmes', title_standoff=40 ),
                    height=800,
                    margin=dict(l=250),
                    showlegend=False,
                    hovermode='closest'
                )
            }
        )
    ]),


    html.Div([
        html.H2('Distribuição dos Gêneros de Filmes'),
        dcc.Graph(
            id='pie-chart',
            figure=fig_pizza
        )
    ]),

    html.Div([
        html.H2('Top 15 Diretores que Mais Lançaram Filmes no Século 21'),
        dcc.Graph(
            id='scatter-plot-directors',
            figure=px.scatter(
                df_directors, x='Movies', y='Director',
                title='Top 15 Diretores que Mais Lançaram Filmes no Século 21',
                labels={'Movies': 'Número de Filmes', 'Director': 'Diretores'},
                text='Movies'
            ).update_traces(
                marker=dict(size=15, color='blue', line=dict(width=2, color='DarkSlateGrey')),
                textposition='middle right'
            ).update_layout(
                xaxis_title='Número de Filmes',
                yaxis_title='Diretores',
                height=600,
                showlegend=False,
                hovermode='closest'
            )
        )
    ])

])

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
