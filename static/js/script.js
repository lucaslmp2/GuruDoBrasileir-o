function normalizeText(text) {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');
}
async function processarResposta2(resposta) {
  if (resposta.error) {
    addMessage('Guru', `Erro: ${resposta.error}`);
  } else {
    // Sort times array based on the number of titulos in ascending order
    const sortedTimes = resposta.times.sort((a, b) => b.titulos - a.titulos);
    // Display information for each time
    sortedTimes.forEach((time, index) => {
      const message = `${index + 1}. O time: ${time.nome}, foi campeão nos anos ${time.anos.join(', ')}, tendo hoje um total de ${time.titulos} títulos.`;
      addMessage('Guru', message);
    });
  }
}
function processarResposta(resposta) {
  if (resposta.error) {
    addMessage('Guru', `Erro: ${resposta.error}`);
  } else {
    // Find the team with the maximum number of titulos
    const timeComMaisTitulos = resposta.times.reduce((maxTime, currentTime) => {
      return currentTime.titulos > maxTime.titulos ? currentTime : maxTime;
    }, resposta.times[0]);

    // Display information for the team with the most titles
    const message = `O time com mais títulos é o ${timeComMaisTitulos.nome}, os anos dos titúlos do ${timeComMaisTitulos.nome} foram, ${timeComMaisTitulos.anos.join(', ')}, dando um total de ${timeComMaisTitulos.titulos} titúlos`;
    addMessage('Guru', message);
  }
}
// Função para buscar os dados do maior campeão
async function carregarDadosMaiorCampeao() {
  try {
      const response = await fetch('/get_maior_campeao');
      const data = await response.json();
      console.log("Data from carregarDadosMaiorCampeao:", data);
      return data;
  } catch (error) {
      console.error('Error in carregarDadosMaiorCampeao:', error);
      throw new Error('Erro na solicitação');
  }
}
// Função para adicionar mensagem com imagem em uma tabela
async function addMessageFoto(sender, imageUrl) {
  const tableBody = document.getElementById('message-table');
  const tableRow = document.createElement('tr');
  // Adiciona a imagem à célula
  const imageCell = document.createElement('td');
  const imageElement = document.createElement('img');
  imageElement.src = imageUrl;
  imageElement.alt = 'Imagem do clube';
  imageCell.appendChild(imageElement);
  tableRow.appendChild(imageCell);
  // Adiciona a linha à tabela
  tableBody.appendChild(tableRow);
  // Aplica o efeito de digitação
  await typeMessage(sender, imageCell);
}
// Função para adicionar mensagem de forma segura
let isTyping = false;
function safeAddMessage(cell, content) {
  // Limpa o conteúdo existente e adiciona o novo conteúdo
  while (cell.firstChild) {
      cell.removeChild(cell.firstChild);
  }
  cell.appendChild(document.createTextNode(content));
}
async function typeMessage(message, element) {
  isTyping = true; // Indica que o efeito de digitação está em andamento
  const delay = 20; // ajuste esse valor conforme necessário
  for (const char of message) {
      element.appendChild(document.createTextNode(char));
      await sleep(delay);
  }
  isTyping = false; // Indica que o efeito de digitação foi concluído
}
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
function addMessage(sender, text, imageSrc, isUser = false) {
  const messageTable = document.getElementById('message-table');
  const newRow = document.createElement('tr');
  const senderCell = document.createElement('td');
  const messageCell = document.createElement('td');
  if (isUser) {
    messageCell.textContent = text;
    messageCell.classList.add('user-message');
    newRow.classList.add('user-message-row');
  } else {
    messageCell.classList.add('bot-message');
    newRow.classList.add('bot-message-row');
    if (text !== '' && text !== 'aqui3! Não consegui compreender sua mensagem, pode repetir?') {
      if (imageSrc) {
        // Se houver uma imagem, use innerHTML para incluir a tag da imagem
        messageCell.innerHTML += `<img src="${imageSrc}">`;
      }
      // Adicionando o texto com o efeito de digitação
      typeMessage(text, messageCell);
    } else {
      messageCell.textContent = 'aqui4! Não consegui compreender sua mensagem, pode repetir?';
    }
  }
  newRow.appendChild(messageCell);
  messageTable.appendChild(newRow);

  const messageContainer = document.querySelector('.message-container');
  messageContainer.scrollTop = messageContainer.scrollHeight;
}
document.addEventListener("DOMContentLoaded", function () {
  const userInput = document.getElementById('user-input');
  const btnSubmit = document.getElementById('btn-submit');
  let jogadorSolicitado = false;
  let clubeSolicitado = false;
  let titulos = false;
  let voltar = false;
  let maiorCampeao = false;
  let todosCampeoes = false;
  const handleUserInput = async function () {
    if (!isTyping) {
      const userMessage = userInput.value.trim();
      addMessage('Você', userMessage, null, true);
      // Normalizar o texto removendo acentos e convertendo para minúsculas
      const normalizedUserMessage = normalizeText(userMessage);
      switch (normalizedUserMessage) {
        case 'jogadores':
          todosCampeoes = false;
          maiorCampeao = false;
          titulos = false;
          clubeSolicitado = false;
          jogadorSolicitado = true;
          voltar = false;                  
          addMessage('Guru', 'Vai lá!!! 😃 é so digitar o nome do jogador seguido pelo nome do time. Por exemplo: ("Pedro Flamengo") que eu vou te mostrar se ele está por aqui kkkk!😅');
          userInput.value = '';
          break;
        case 'clubes':
          todosCampeoes = false;
          maiorCampeao = false;
          titulos = false;
          clubeSolicitado = true;
          jogadorSolicitado = false;
          voltar = false;
          addMessage('Guru', '😃 Por favor, digite o nome ou abreviação do nome do clube: ');
          userInput.value = '';
          break;
        case 'voltar':
          todosCampeoes = false;
          maiorCampeao = false;
          titulos = false;
          clubeSolicitado = false;
          jogadorSolicitado = false;
          voltar = true;
          addMessage('Guru','Oi, de novo kkk... 😅 Deseja realizar uma nova busca? Digite: "História do campeonato", "titulos", "clubes", "jogadores", "Maior campeão", "Maiores Artilheiros", "Campeões", "Curiosidades", "Clubes", "História do clubes desejado" "Técnico do clube desejado" ou "voltar"!!!')
          userInput.value = '';                  
          break;
        case 'titulos':
          todosCampeoes = false;
          maiorCampeao = false;
          titulos = true;
          clubeSolicitado = false;
          jogadorSolicitado = false;
          voltar = false;
          addMessage('Guru','Por favor digite o ano do campeonato. 😅')
          userInput.value = '';
          break;
        case 'maior campeao':
          todosCampeoes = false;
          maiorCampeao = true;
          titulos = false;
          clubeSolicitado = false;
          jogadorSolicitado = false;
          voltar = false;
          break;
        case 'campeoes':
          todosCampeoes = true;
          maiorCampeao = false;
          titulos = false;
          clubeSolicitado = false;
          jogadorSolicitado = false;
          voltar = false;
          normalizedUserMessage === '';
          break;
        default:
            if (jogadorSolicitado) {
              let clubes;
              let posicoes;
              // Carregue o arquivo JSON de clubes
              fetch('/static/clubes.json')
                  .then(response => response.json())
                  .then(data => {
                      clubes = data;
                  })
                  .catch(error => console.error('Erro ao carregar o arquivo JSON de clubes:', error))
              // Carregue o arquivo JSON de posições
              fetch('/static/posicoes.json')
                  .then(response => response.json())
                  .then(data => {
                      posicoes = data;
                  })
                  .catch(error => console.error('Erro ao carregar o arquivo JSON de posições:', error));
          
              const userInputParts = userInput.value.trim().split(' ');
          
              if (userInputParts.length >= 2) {
                  const nomeJogador = userInputParts[0].toLowerCase(); // Primeira parte é o nome do jogador
                  const nomeTime = userInputParts.slice(1).join(' ').toLowerCase(); // Restante é o nome do time
          
                  // Lógica para solicitar jogadores aqui
                  try {
                      const response = await fetch(`/pesquisar_atletas/${nomeJogador}`);
                      if (!response.ok) {
                          throw new Error('Erro na solicitação');
                      }
                      const data = await response.json();
                      const jogadoresEncontrados = data.filter(atleta => {
                          const clube = clubes[atleta.clube_id];
                          const clubeNome = clube ? clube.nome.toLowerCase() : 'desconhecido';
                          return clubeNome === nomeTime && atleta.apelido.toLowerCase() === nomeJogador;
                      });
                      if (jogadoresEncontrados.length > 0) {
                          jogadoresEncontrados.forEach(atleta => {
                              const clube = clubes[atleta.clube_id];
                              const clubeNome = clube ? clube.nome : 'Desconhecido';
                              const posicaoId = atleta.posicao_id;
                              const posicao = posicoes[posicaoId];
                              const posicaoNome = posicao ? posicao.nomep : 'Desconhecida';
                              const gols = atleta.scout.G ? atleta.scout.G : 0;
                              const assistencias = atleta.scout.A ? atleta.scout.A : 0;
                              const mensagemAtleta = `O atleta ${atleta.apelido}, jogador do ${clubeNome} que joga como ${posicaoNome} foi encontrado 🥳. Até o momento ele possui ${gols} gols ⚽ e ${assistencias} assistências 👟, no Campeonato Brasileiro 2023. Se quiser procurar outros jogadores, basta digitar "Jogadores" 🏃 ou se não quiser 🤷‍♂️ é só digitar "Voltar"!`;
                              addMessage('Guru', mensagemAtleta);
                          });
                      } else {
                          addMessage('Guru', `Nenhum jogador encontrado com o nome "${nomeJogador}" no time "${nomeTime}" 🤷‍♂️ Se quiser procurar outros jogadores 🏃, basta digitar "Jogadores" ou se não quiser é só digitar "Voltar"! 😃`);
                      }
                  } catch (error) {
                      console.error('Erro na solicitação:', error);
                      addMessage('Guru', 'Ops algo inesperado aconteceu!!! 🤔 tenta digitar "Voltar"');
                  }
                  userInput.value = '';
                  jogadorSolicitado = false;
              } else {
                  addMessage('Guru', '🤔 Por favor, forneça o nome do jogador seguido pelo nome do time. Exemplo: ("Pedro Flamengo")');
              }
          }
            else // Lógica para tratar a solicitação de clube
            if (clubeSolicitado) {
              fetch('/static/clubes.json')
                .then(response => response.json())
                .then(data => {
                  const nomeClube = userMessage.toLowerCase().trim();
                  const clubeData = Object.values(data).find(clube =>
                    clube.nome.toLowerCase().includes(nomeClube) ||
                    clube.apelido.toLowerCase().includes(nomeClube) ||
                    clube.abreviacao.toLowerCase().includes(nomeClube)
                  );
                  if (clubeData) {
                    const mensagemClube = `O clube ${clubeData.nome} com abreviação ${clubeData.abreviacao} foi encontrado, mas também é conhecido popularmente como ${clubeData.apelido} 😃.`;
                    addMessage('Guru', mensagemClube);
            
                    const mensagemFoto = `${clubeData.escudos["60x60"]}`;
                    addMessageFoto('', mensagemFoto);
            
                    userInput.value = '';
                    clubeSolicitado = false;
            
                    const mensagemNovaSolicitacao2 = `Deseja realizar uma nova busca? Digite: "Clubes" ou "Voltar"!!!`;
                    addMessage('Guru', mensagemNovaSolicitacao2);
                  } else {
                    // Caso nenhum clube seja encontrado
                    const mensagemNenhumClube = `Desculpe, não foi possível encontrar o clube "${nomeClube}". Por favor, tente novamente. Digite: "Clubes" ou "Voltar"!!!`;
                    addMessage('Guru', mensagemNenhumClube);
                    userInput.value = '';
                    clubeSolicitado = false;
                  }
                })
                .catch(error => console.error('Erro ao carregar o arquivo JSON:', error));
            }
            else if (titulos) {
              let ano = userInput.value;
              const isValidYear = /^\d{4}$/.test(ano); // Verifica se o ano é um número de 4 dígitos
              if (isValidYear) {
                  // Faz uma solicitação para obter os campeões do ano especificado
                  fetch(`/get_campeoes/${ano}`)
                      .then(response => {
                          if (!response.ok) {
                              throw new Error(`Erro na solicitação: ${response.status} - ${response.statusText}`);
                          }
                          return response.json();
                      })
                      .then(data => {
                          addMessage('Bot', `O campeão do ano ${ano} foi: ${data}`);
                          campeaoSolicitado = false;
                          const mensagemNovaSolicitacao2 = `Deseja realizar uma nova busca? Digite: "Títulos" ou "Voltar"!!!`;
                          addMessage('Guru', mensagemNovaSolicitacao2);
                          userInput.value = '';
                      })
                      .catch(error => {
                          console.error('Erro:', error);
                          addMessage('Bot', `Não é possível obter o campeão do ano ${ano}: Digite um ano válido!!!`);
                      });
              } else {
                  addMessage('Bot', 'Por favor, ano inválido (Formato deve ser: YYYY). Refaça a consulta!');
              }
          }
          else if (maiorCampeao) {
            try {
              const responseMaiorCampeao = await fetch('/get_maior_campeao');
              const dadosMaiorCampeao = await responseMaiorCampeao.json();
              processarResposta(dadosMaiorCampeao);
            } catch (error) {
              console.error('Erro ao obter o maior campeão:', error.message);
              addMessage('Guru', 'Ops, algo deu errado ao obter o maior campeão.');
            } 
        }else if(todosCampeoes){
          try {
            const responseTodosCampeoes = await fetch('/get_maior_campeao');
            const dadosTodosCampeoes = await responseTodosCampeoes.json();
            processarResposta2(dadosTodosCampeoes);
          } catch (error) {
            console.error('Erro ao obter todos os campeões:', error.message);
            addMessage('Guru', 'Ops, algo deu errado ao obter todos os campeões.');
          }
        todosCampeoes = false;
        const mensagemNovaSolicitacao2 = `Deseja realizar uma nova busca? Digite: "História do campeonato", "titulos", "clubes", "jogadores", "Maior campeão", "Maiores Artilheiros", "Campeões", "Curiosidades", "Clubes", "História do clubes desejado" "Técnico do clube desejado" ou "voltar"!!!`;
        addMessage('Guru', mensagemNovaSolicitacao2);
        userInput.value = '';
        }
        else
          {
            // Lógica para tratar outros casos ou fazer uma solicitação Ajax
            try {
                const response = await fetch(`/search/${userMessage}`);
                if (!response.ok) {
                  throw new Error('Erro na solicitação');
                }
                const data = await response.json();
                if (data.result) {
                  addMessage('Guru', data.result);
                } else {
                  addMessage('Guru', 'Não consegui compreender sua mensagem, pode repetir?');
                }
              } catch (error) {
                console.error('Erro na solicitação:', error);
                addMessage('Guru', 'Não consegui compreender sua mensagem. pode repetir?.');
              }
              userInput.value = '';
          }
          break;
        }
        userInput.value = '';
      } else {
        console.log('Aguarde o efeito de digitação terminar.');
      }
    };
    userInput.addEventListener('keypress', async function (event) {
      if (event.key === 'Enter') {
        event.preventDefault();
        handleUserInput();
      }
    });
    btnSubmit.addEventListener('click', function () {
      handleUserInput();
    });
  });