# Importação das bibliotecas necessárias para a aplicação
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS  # Importação do middleware para permitir solicitações de origens diferentes
import re  # Importação do módulo de expressões regulares para manipulação de texto
from unidecode import unidecode  # Importação para remover acentos
from btree_node import Node, BTree  # Importação das classes Node e BTree do módulo btree_node
from flask import Flask, request, jsonify
import requests
import json
import os
# Criação de uma instância do aplicativo Flask
app = Flask(__name__)
CORS(app)  # Aplicação do middleware CORS para permitir solicitações de origens diferentes

# Criação de uma instância da árvore B com ordem 9
btree = BTree(order=99)
# Inserção de pares chave-valor na árvore B
btree.insert(1, "oi")
btree.insert(2, "ola")
btree.insert(3, "tudo bem")
btree.insert(4, "historia do campeonato")
btree.insert(5, "jogadores")
btree.insert(6, "maiores artilheiros")
btree.insert(7, "curiosidades")
btree.insert(8, "como vai")
btree.insert(9, "como vai voce")
btree.insert(10, "historia do america")
btree.insert(11, "historia do athletico paranaense")
btree.insert(12, "historia do athletico mineiro")
btree.insert(13, "historia do bahia")
btree.insert(14, "historia do corinthians")
btree.insert(15, "historia do coritiba")
btree.insert(16, "historia do flamengo")
btree.insert(17, "historia do fluminense")
btree.insert(18, "historia do fortaleza")
btree.insert(19, "historia do goias")
btree.insert(20, "historia do internacional")
btree.insert(21, "historia do palmeiras")
btree.insert(22, "historia do bragantino")
btree.insert(23, "historia do sao paulo")
btree.insert(24, "historia do vasco")
btree.insert(25, "tecnico do flamengo")
btree.insert(26, "tecnico do palmeiras")
btree.insert(27, "tecnico do botafogo")
btree.insert(28, "tecnico do bragantino")
btree.insert(29, "tecnico do fortaleza")
btree.insert(30, "tecnico do fluminense")
btree.insert(31, "tecnico do gremio")
btree.insert(32, "tecnico do sao paulo")
btree.insert(33, "tecnico do cuiaba")
btree.insert(34, "tecnico do atletico mineiro")
btree.insert(35, "tecnico do atletico paranaense")
btree.insert(36, "tecnico do goias")
btree.insert(37, "tecnico do coritiba")
btree.insert(38, "tecnico do vasco")
btree.insert(39, "tecnico do internacional")
btree.insert(40, "tecnico do america mineiro")
btree.insert(41, "tecnico do cruzeiro")
btree.insert(42, "tecnico do bahia")
btree.insert(43, "tecnico do santos")
btree.insert(44, "tecnico do corinthians")
btree.insert(45, "historia do cruzeiro")
btree.insert(46, "historia do cuiaba")
btree.insert(47, "historia do botafogo")
btree.insert(48, "historia")
btree.insert(49, "e ai")

# Dicionário que mapeia palavras-chave a respostas
responses = {
    "E ai": "E aí, eu sou o Guru do Campeonato Brasileiro. Manda lá o que quer saber que tá ali ó em cima no menu inicial ",
    "Oi": "Oi, eu sou o Guru do Campeonato Brasileiro. Digite de acordo o menu inicial o que quer saber",
    "Ola": "Oi, eu sou o Guru do Campeonato Brasileiro. Digite de acordo o menu inicial o que quer saber",
    "Tudo bem": "Oi, tudo sim e você? Eu sou o Guru do Campeonato Brasileiro... Digite de acordo o menu inicial o que quer saber",
    "Historia do campeonato": "Criada pela Confederação Brasileira de Desportos (CBD), atual CBF, em 1959, a Taça Brasil é considerada a primeira competição nacional entre clubes de futebol. A criação do torneio tinha o objetivo de substituir o Campeonato Brasileiro de Seleções Estaduais, que era uma competição disputada entre os melhores times dos estados do Brasil. A Taça Brasil reunia as equipes campeãs estaduais do país e dava ao campeão o direito de representá-lo na Copa dos Campeões da América (Copa Libertadores da América) que, naquela época, reunia os campeões de cada país da América do Sul. As primeiras edições da Taça Brasil foram disputadas com jogos de mata-mata, pois, devido às complicações de locomoção e transporte da época, era difícil organizar um torneio nacional mais integrado, em um país com dimensões tão grandes como o Brasil." "O primeiro campeonato teve a participação de 16 equipes campeãs estaduais, e os campeões do estado de São Paulo e do Distrito Federal — na época, a capital do Brasil era o Rio de Janeiro — entraram na fase final. A equipe do Bahia foi a primeira a conquistar o título da competição e a vaga para representar o Brasil na Copa dos Campeões da América de 1960, após vencer o Santos na final." "Em 1967, o Torneio Rio-São Paulo, que era uma competição interestadual disputada por times do Rio de Janeiro e de São Paulo, foi ampliado para âmbito nacional e recebeu o nome de Torneio Roberto Gomes Pedrosa, o “Robertão”, em homenagem ao goleiro Pedrosa, do São Paulo e da Seleção Brasileira da Copa 1934, que morreu em 1954 como presidente da Federação Paulista. O Robertão foi disputado paralelamente à Taça Brasil. A partir da segunda edição, o torneio Robertão passou a ser chamado de Taça de Prata. A competição acabou agradando os clubes e torcedores, já que foi a primeira a reunir os principais times do país com os melhores jogadores. Com isso, a média de público do campeonato aumentou, já que os jogos tinham um nível melhor, e a competição começou a ter mais credibilidade e uma cobertura intensa da mídia. A consequência foi que o torneio ficou mais lucrativo para as equipes participantes, que começaram a ter um interesse maior pela competição. O sucesso do Robertão fez com que a CBD decidisse, em 1971, transformar o torneio em um Campeonato Nacional de Clubes. A CBF pretendia enxugar ainda mais o torneio, e, com isso, muitos clubes menos expressivos deixaram de fazer parte do campeonato nacional. Para evitar suas extinções, a CBF criou uma competição secundária, a Copa do Brasil, que poderia reunir clubes de todos os estados. Evitando confusão entre os nomes dos torneios, a Copa Brasil passou a ser chamada Campeonato Brasileiro, em 1989. O sistema só durou uma temporada. Na primeira fase da competição, foi descoberto que um jogador do São Paulo estava registrado de forma irregular, e a CBF decidiu punir o clube anulando os jogos em que participou. Com isso, Internacional e Botafogo ganharam pontos que levaram o Gama ao rebaixamento. A equipe resolveu, então, processar a CBF, que não pôde organizar o torneio em 2000. Novamente, o Clube dos 13 voltou a organizar o campeonato, que, naquele ano, teve o nome de Copa João Havelange e contou com a participação de Fluminense e Bahia como convidados, já que ambos estavam na Série B. O campeonato foi dividido em quatro módulos (azul, amarelo, verde e branco), com a participação de 116 times. A final foi entre Vasco, do Módulo Azul, e São Caetano, do Módulo Amarelo, e o time do Rio de Janeiro foi o campeão em uma final tumultuada e marcada pelo desabamento do alambrado do estádio São Januário.",
    "Historia":"Criada pela Confederação Brasileira de Desportos (CBD), atual CBF, em 1959, a Taça Brasil é considerada a primeira competição nacional entre clubes de futebol. A criação do torneio tinha o objetivo de substituir o Campeonato Brasileiro de Seleções Estaduais, que era uma competição disputada entre os melhores times dos estados do Brasil. A Taça Brasil reunia as equipes campeãs estaduais do país e dava ao campeão o direito de representá-lo na Copa dos Campeões da América (Copa Libertadores da América) que, naquela época, reunia os campeões de cada país da América do Sul. As primeiras edições da Taça Brasil foram disputadas com jogos de mata-mata, pois, devido às complicações de locomoção e transporte da época, era difícil organizar um torneio nacional mais integrado, em um país com dimensões tão grandes como o Brasil." "O primeiro campeonato teve a participação de 16 equipes campeãs estaduais, e os campeões do estado de São Paulo e do Distrito Federal — na época, a capital do Brasil era o Rio de Janeiro — entraram na fase final. A equipe do Bahia foi a primeira a conquistar o título da competição e a vaga para representar o Brasil na Copa dos Campeões da América de 1960, após vencer o Santos na final." "Em 1967, o Torneio Rio-São Paulo, que era uma competição interestadual disputada por times do Rio de Janeiro e de São Paulo, foi ampliado para âmbito nacional e recebeu o nome de Torneio Roberto Gomes Pedrosa, o “Robertão”, em homenagem ao goleiro Pedrosa, do São Paulo e da Seleção Brasileira da Copa 1934, que morreu em 1954 como presidente da Federação Paulista. O Robertão foi disputado paralelamente à Taça Brasil. A partir da segunda edição, o torneio Robertão passou a ser chamado de Taça de Prata. A competição acabou agradando os clubes e torcedores, já que foi a primeira a reunir os principais times do país com os melhores jogadores. Com isso, a média de público do campeonato aumentou, já que os jogos tinham um nível melhor, e a competição começou a ter mais credibilidade e uma cobertura intensa da mídia. A consequência foi que o torneio ficou mais lucrativo para as equipes participantes, que começaram a ter um interesse maior pela competição. O sucesso do Robertão fez com que a CBD decidisse, em 1971, transformar o torneio em um Campeonato Nacional de Clubes. A CBF pretendia enxugar ainda mais o torneio, e, com isso, muitos clubes menos expressivos deixaram de fazer parte do campeonato nacional. Para evitar suas extinções, a CBF criou uma competição secundária, a Copa do Brasil, que poderia reunir clubes de todos os estados. Evitando confusão entre os nomes dos torneios, a Copa Brasil passou a ser chamada Campeonato Brasileiro, em 1989. O sistema só durou uma temporada. Na primeira fase da competição, foi descoberto que um jogador do São Paulo estava registrado de forma irregular, e a CBF decidiu punir o clube anulando os jogos em que participou. Com isso, Internacional e Botafogo ganharam pontos que levaram o Gama ao rebaixamento. A equipe resolveu, então, processar a CBF, que não pôde organizar o torneio em 2000. Novamente, o Clube dos 13 voltou a organizar o campeonato, que, naquele ano, teve o nome de Copa João Havelange e contou com a participação de Fluminense e Bahia como convidados, já que ambos estavam na Série B. O campeonato foi dividido em quatro módulos (azul, amarelo, verde e branco), com a participação de 116 times. A final foi entre Vasco, do Módulo Azul, e São Caetano, do Módulo Amarelo, e o time do Rio de Janeiro foi o campeão em uma final tumultuada e marcada pelo desabamento do alambrado do estádio São Januário.",
    "Maiores artilheiros": "Desde que o campeonato foi criado, em 1959, muitos jogadores destacaram-se como goleadores, mas quem mais marcou gols no torneio foi Roberto Dinamite, com 190 gols. Em seguida, vem Romário, com 154, e, com um gol a menos, Edmundo é o terceiro. Roberto Dinamite é o maior artilheiro da história do Campeonato Brasileiro. Na era dos pontos corridos, outros jogadores também destacaram-se no número de gols. Nessa fase, os artilheiros são o atacante Fred com mais de 150 gols, seguido pelo meia/lateral Paulo Baier (106 gols). Fred é o principal artilheiro do campeonato na era dos pontos corridos(158 gols). Em uma única edição do Brasileirão, após a definição dos pontos corridos, os principais artilheiros são Washington (34 gols, em 2004, pelo Atlético-PR), Dimba (31 gols, em 2003, pelo Goiás), Gabriel Barbosa (25 gols, em 2019, pelo Flamengo), Jonas (23 gols, em 2010, pelo Grêmio) e Borges (23 gols, em 2011, pelo Santos).",
    "Curiosidades": "Nomes do Campeonato Brasileiro:\n| 1959 a 1968: Taça Brasil\n| 1967 a 1970: Torneio Roberto Gomes Pedrosa (Robertão) ou Taça de Prata\n| 1971 a 1974: Campeonato Nacional de Clubes\n| 1975 a 1979: Copa Brasil\n| 1980: Taça de Ouro e Copa Brasil\n| 1987 e 1988: Copa União\n| 1989 a 1999: Campeonato Brasileiro\n| 2000: Copa João Havelange\n| 2001 e 2002: Campeonato Brasileiro\n| 2003 até hoje: Campeonato Brasileiro - Série A",
    "Como vai voce": "Oi, vou bem e você? Eu sou o Guru do Campeonato Brasileiro...",
    "Como vai": "Oi, vou bem e você? Eu sou o Guru do Campeonato Brasileiro...",
    "Historia do cruzeiro": "O Cruzeiro Esporte Clube nasceu através do esforço de desportistas da comunidade italiana em Belo Horizonte, com o nome de Societá Sportiva Palestra Itália, em 2 de janeiro de 1921. Após mais de 100 anos de história, o Clube se transformou em uma das maiores agremiações de futebol do mundo.",
    "Historia do america": "O América Futebol Clube, fundado em 1912 em Belo Horizonte, é um clube de tradição no futebol mineiro. Ao longo de sua história, conquistou títulos estaduais e nacionais, destacando-se na revelação de talentos. O Coelho viveu altos e baixos, mas sua resiliência e paixão da torcida o mantêm como protagonista no cenário esportivo.",
    "Historia do athletico paranaense": "O Club Athletico Paranaense, estabelecido em 1924 em Curitiba, consolidou-se como um dos principais clubes brasileiros. Conquistou a Copa do Brasil e a Sul-Americana, destacando-se pela gestão moderna e pelo estilo de jogo ofensivo. O Furacão é reconhecido não apenas por suas vitórias, mas também por seu compromisso com a inovação no futebol nacional." ,
    "Historia do atletico mineiro": "O Clube Atlético Mineiro, fundado em 1908, é uma potência do futebol brasileiro. Com sede em Belo Horizonte, o Galo possui uma rica história, marcada por conquistas como a Copa Libertadores. Sua torcida fervorosa e o estádio Mineirão são símbolos da paixão que o Atlético-MG desperta, sendo protagonista em competições nacionais e internacionais.",
    "Historia do bahia": "O Esporte Clube Bahia, nascido em 1931 em Salvador, é um dos clubes mais queridos do Nordeste. Além de suas glórias no futebol, o Tricolor de Aço é reconhecido por sua atuação social e cultural. Com uma torcida apaixonada, o Bahia destaca-se como representante da diversidade e da energia vibrante do futebol brasileiro.",
    "Historia do corinthians": "O Sport Club Corinthians Paulista, fundado em 1910, é uma potência do futebol brasileiro. Com uma base de fãs impressionante, o Timão conquistou numerosos títulos, incluindo a Copa Libertadores e o Mundial de Clubes. Sua identidade marcante e o estádio Arena Corinthians simbolizam a grandeza e a paixão que envolvem esse clube icônico.",
    "Historia do coritiba": "O Cuiabá Esporte Clube, fundado em 2001, ascendeu rapidamente no cenário futebolístico brasileiro. Originário da capital do Mato Grosso, o clube alcançou a elite do futebol nacional, demonstrando ambição e talento. O Dourado representa uma nova era para o futebol mato-grossense, conquistando corações com seu estilo vibrante e determinado.",
    "Historia do flamengo": "O Clube de Regatas do Flamengo, fundado em 1895, é um dos clubes mais populares e vitoriosos do Brasil. O Mengão conquistou inúmeros títulos, incluindo a Libertadores e o Brasileirão. Sua torcida, conhecida como Maior do Mundo, e o Maracanã como palco sagrado, tornam o Flamengo uma força inigualável no futebol brasileiro e internacional.",
    "Historia do fluminense": "O Fluminense Football Club, fundado em 1902, é uma instituição carioca de prestígio. O Time de Guerreiros tem uma trajetória marcada por conquistas, com títulos nacionais e internacionais. Sua torcida fervorosa, as Laranjeiras como berço e a superação de desafios conferem ao Fluminense uma identidade única, consolidando sua importância no futebol brasileiro.",
    "Historia do fortaleza": "O Fortaleza Esporte Clube, fundado em 1918, é um orgulho do Nordeste brasileiro. Com conquistas expressivas, incluindo títulos nacionais, o Leão do Pici representa a paixão e a determinação cearense. Sua torcida apaixonada, aliada ao moderno estádio Castelão, torna o Fortaleza um protagonista respeitado no futebol nacional.",
    "Historia do goias": "O Goiás Esporte Clube, fundado em 1943, é uma potência do Centro-Oeste brasileiro. Com uma história de superação e conquistas, o Esmeraldino destaca-se no cenário nacional. Sua torcida fervorosa e o estádio Serra Dourada são testemunhas da força e tradição que o Goiás carrega, representando com orgulho o futebol goiano.",
    "Historia do gremio": "O Grêmio Foot-Ball Porto Alegrense, fundado em 1903, é um gigante do futebol brasileiro. Com uma trajetória de títulos nacionais e internacionais, o Tricolor Gaúcho é conhecido pela raça e pela tradição. A torcida apaixonada e a Arena do Grêmio são símbolos da grandiosidade desse clube, que deixou sua marca na história do esporte.",
    "Historia do internacional": "O Sport Club Internacional, fundado em 1909, é um dos maiores clubes do sul do Brasil. Com uma rica história, o Colorado conquistou títulos nacionais e internacionais, incluindo a Libertadores e o Mundial. Seu estádio, o Beira-Rio, e a torcida apaixonada são elementos que reforçam a grandeza e o legado do Internacional no futebol brasileiro.",
    "Historia do palmeiras": "A Sociedade Esportiva Palmeiras, fundada em 1914, é uma potência do futebol brasileiro. O Verdão possui uma história de conquistas, incluindo a Copa Libertadores e o Mundial de 1951. Sua torcida vibrante e o Allianz Parque, um dos estádios mais modernos do país, refletem a tradição e a paixão que envolvem o Palmeiras, um dos clubes mais laureados do Brasil.",
    "Historia do bragantino": "O Red Bull Bragantino, fundado em 1928, representa uma fusão entre tradição e modernidade. Sob a gestão inovadora da Red Bull, o clube ascendeu no cenário brasileiro, conquistando destaque na elite do futebol. O Massa Bruta é sinônimo de renovação e ambição, evidenciando um novo capítulo emocionante em sua história.",
    "Historia do santos": "O Santos Futebol Clube, fundado em 1912, é uma potência do futebol mundial. Conhecido como o Peixe, o clube revelou ícones como Pelé. Com títulos nacionais e internacionais, incluindo a Copa Libertadores, o Santos mantém sua tradição de jogo ofensivo e técnico, conquistando corações com sua história rica e inigualável.",
    "Historia do sao Paulo": "O São Paulo Futebol Clube, fundado em 1930, é um dos clubes mais vitoriosos do Brasil. O Tricolor Paulista ostenta títulos nacionais e internacionais, incluindo três Copas Libertadores e três Mundiais. Sua base de fãs fiel e o Morumbi como fortaleza reforçam a grandeza e a tradição desse clube que marcou época no futebol brasileiro.",
    "Historia do botafogo": "O Botafogo foi fundado por um grupo de estudantes do Colegio Alfredo Gomes no dia 12 de agosto de 1904. A ideia era formar um clube com a garotada que morava no Largo dos Leoes e nas ruas Sao Clemente e Voluntarios da Patria. O nome original era Eletro Club, time com cores alvi-negras, mas sem a estrela solitaria. A mudanca do nome veio rapida, um mes depois, na segunda reuniao do time por influencia da avo de um dos fundadores - Flavio Ramos - que no meio da reuniao nao gostou do nome Eletro Club, virou e falou para os jovens: morando onde voces moram o clube de voces so pode ser chamado Botafogo. Dito e feito as historias pitorescas sobre o Botafogo Futebol Clube comecaram desde cedo.",
    "Historia do cuiaba": "Cuiabá Esporte Clube é uma SAF de futebol brasileiro sediado na cidade de Cuiabá. Foi fundado no dia 12 de dezembro de 2001 pelo ex-jogador Luís Carlos Tóffoli, mais conhecido como Gaúcho.[3] O Dourado é seu maior símbolo; Suas cores tradicionais são o amarelo e o verde. Em seu escudo encontra-se representado o obelisco do Centro Geodésico da América do Sul, símbolo também presente na bandeira da cidade.[4] Costuma mandar suas partidas na Arena Pantanal, um dos estádios da Copa do Mundo FIFA de 2014.[5] Tem como principais rivais esportivos o Mixto Esporte Clube, com o qual protagoniza o Dérbi Cuiabano, e o Luverdense Esporte Clube, com quem disputa o Clássico Ouro-Verde.",
    "Historia do vasco": "O Club de Regatas Vasco da Gama, fundado em 1898, é um dos clubes mais antigos e queridos do Brasil. O Gigante da Colina tem uma história rica, marcada por títulos estaduais e nacionais. Com uma torcida apaixonada, São Januário como casa e momentos históricos, o Vasco continua a ser um símbolo da diversidade e resiliência no futebol brasileiro.",
    "Tecnico do flamengo": "O técnico do Flamengo é o Tite",
    "Tecnico do palmeiras": "O técnico do Palmeiras é o Abel Ferreira",
    "Tecnico do botafogo": "O técnico do Botafogo é o Lúcio Flávio",
    "Tecnico do bragantino": "O técnico do Bragantino é o Pedro Caixinha",
    "Tecnico do fortaleza": "O técnico do Fortaleza é o Juan Pablo",
    "Tecnico do fluminense": "O técnico do Fluminense é o Fernando Diniz",
    "Tecnico do gremio": "O técnico do Grêmio é o Renato Gaúcho",
    "Tecnico do sao paulo": "O técnico do São Paulo é o Dorival Júnior",
    "Tecnico do cuiaba": "O técnico do Cuiabá é o Toni Oliveira",
    "Tecnico do atletico mineiro": "O técnico do Atlético Mineiro é o Felipe Scolari",
    "Tecnico do athletico paranaense": "O técnico do Athletico Paranaense é o Wesley Carvalho",
    "Tecnico do goias": "O técnico do Goiás é o Armando Evangelista",
    "Tecnico do coritiba": "O técnico do Coritiba é o Thiago Kosloski",
    "Tecnico do vasco": "O técnico do Vasco é o Ramón Díaz",
    "Tecnico do internacional": "O técnico do Internacional é o Eduardo Coudet",
    "Tecnico do america mineiro": "O técnico do America Mineiro é o Fabián Bustos",
    "Tecnico do cruzeiro": "O técnico do Cruzeiro é o Zé Ricardo",
    "Tecnico do bahia": "O técnico do Bahia é o Rogério Ceni",
    "Tecnico do santos": "O técnico do Santos é o Marcelo Fernandes",
    "Tecnico do corinthians": "O técnico do Corinthians é o Mano Menezes"
}
# Carrega os dados do arquivo JSON
with open('static/clubes.json', 'r') as file:
    clubes_data = json.load(file)

@app.route('/posicoes', methods=['GET'])
def get_posicoes():
    try:
        with open('posicoes.json', 'r') as file:
            posicoes = json.load(file)
        return jsonify(posicoes)
    except FileNotFoundError:
        return jsonify({'error': 'O arquivo posicoes.json não foi encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao processar a requisição: {str(e)}'}), 500
    
@app.route('/clubes', methods=['GET'])
def obter_clubes():
    return jsonify(clubes_data)
# Função para adaptar e inserir as respostas na árvore B
def adapt_and_insert_responses(btree, responses):
    for key, value in responses.items():
        # Conversão da chave para um formato adequado para a árvore B 
        # Neste exemplo simples, estamos usando apenas strings, então usaremos as próprias chaves como chaves na árvore B
        btree.insert(key, value)

# Criação de outra instância da árvore B com ordem 9 e inserção das respostas
btree = BTree(order=99)
adapt_and_insert_responses(btree, responses)
@app.route("/")
def index():
    # Adicionando a configuração de Content Security Policy
    response = app.response_class(
        response=render_template("index.html"),
        status=200,
        mimetype='text/html'
    )
    response.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-inline' 'unsafe-eval';"
    return response

with open('static/campeoes.json', 'r') as file:
    campeoes_data = json.load(file)
    
@app.route('/get_campeoes/<int:ano>', methods=['GET'])
def get_campeoes(ano):
    if str(ano) in campeoes_data:
        return jsonify(campeoes_data[str(ano)])
    else:
        return jsonify({"error": f"Nenhum campeão encontrado para o ano {ano}"}), 404
    
with open('static/maiorCampeao.json', 'r') as file:
    maiorCampeao_data = json.load(file)
    
@app.route('/get_maior_campeao', methods=['GET'])
def get_maiorCampeao():
    try:
        return jsonify(maiorCampeao_data)
    except Exception as e:
        return jsonify({"error": f"Falha na busca dos maiores campeões: {str(e)}"}), 500
    
@app.route("/load_clubes", methods=["GET"])
def load_clubes():
    try:
        root_directory = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(root_directory, "clubes.json")

        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}, 500)
    
    
@app.route("/obter_dados_api", methods=["GET"])
def obter_dados_api():
    try:
        # Faça uma solicitação à API externa
        url = 'https://api.cartola.globo.com/atletas/pontuados/33'
        response = requests.get(url)

        if response.status_code == 200:
            # A solicitação à API externa foi bem-sucedida
            data = response.json()
            return jsonify(data)
        else:
            # A solicitação à API externa falhou
            return jsonify({"error": "A solicitação à API falhou"}, 500)  # Resposta de erro com código 500
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer
        return jsonify({"error": str(e)}, 500)
   
@app.route("/pesquisar_atletas/<nome>", methods=["GET"])
def pesquisar_atletas(nome):
    try:
        # Faça uma solicitação à API externa para obter a lista de atletas
        url = 'https://api.cartola.globo.com/atletas/mercado'
        response = requests.get(url)

        if response.status_code == 200:
            # A solicitação à API externa foi bem-sucedida
            data = response.json()

            # Filtrar os atletas cujo nome contenha o valor fornecido
            atletas_encontrados = [atleta for atleta in data['atletas'] if nome.lower() in atleta['apelido'].lower()]

            return jsonify(atletas_encontrados)
        else:
            # A solicitação à API externa falhou
            return jsonify({"error": "A solicitação à API falhou"}, 500)  # Resposta de erro com código 500
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer
        return jsonify({"error": str(e)}, 500)


@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("user_message")

    # Remoção de pontuações e outros caracteres não alfabéticos da entrada do usuário
    user_message = re.sub(r'[^\w\s]', '', user_message)

    # Conversão da entrada do usuário para letras minúsculas
    user_message = user_message.lower()

    # Utilização da classe BTree para obter a resposta
    bot_response_key = btree.search(user_message)

    if bot_response_key is not None and bot_response_key in responses:
        bot_response = responses[bot_response_key]
    else:
        bot_response = "Desculpe! Não consegui compreender sua mensagem, pode repetir?"

    return jsonify({"bot_response": bot_response})
# Rota que lida com solicitações POST para inserir chaves e valores na árvore B
@app.route("/insert", methods=["POST"])
def insert():
    data = request.json
    key = data["key"]
    value = data["value"]
    btree.insert(key, value)
    return jsonify({"message": "Inserção realizada com sucesso"})

# Rota que lida com solicitações GET para pesquisar na árvore B com base em uma chave inteira
@app.route("/search/<int:key>", methods=["GET"])
def search(key):
    result = btree.search(key)
    if result is not None:
        return jsonify({"result": result})
    else:
        return jsonify({"message": "Chave não encontrada"})

# Rota que lida com solicitações GET para pesquisar na árvore B com base em uma mensagem do usuário
@app.route("/search/<string:user_message>", methods=["GET"])
def search_tree(user_message):
    # Conversão da mensagem do usuário para um tipo consistente (por exemplo, minúsculas e sem pontuações)
    user_message = re.sub(r'[^\w\s]', '', user_message)

    # Remoção de acentuação e conversão para minúsculas usando unidecode
    user_message = unidecode(user_message).lower()
    
    # Verificação se a entrada começa com uma letra maiúscula e, em seguida, conversão para minúsculas
    if user_message:
        user_message = user_message[0].capitalize() + user_message[1:].lower()

    # Realização da pesquisa na árvore B e retorno do resultado como JSON
    bot_response = btree.search(user_message)

    if bot_response:
        return jsonify({"result": bot_response})
    else:
        return jsonify({"message": "Desculpe, não foi possível encontrar uma resposta para a sua pergunta."})

# Rota inicial que retorna um template HTML
@app.route("/")
def home():
    return render_template("index.html")

# Rota para servir arquivos estáticos (por exemplo, CSS e JavaScript)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Execução do aplicativo se este arquivo for o ponto de entrada
if __name__ == "__main__":
    app.run(debug=True)