import random

o_louco = ['O Louco',
{'nome': 'Investidura do Vento',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min

Até o feitiço terminar, o vento gira ao seu redor e você ganha os seguintes benefícios:

Ataques de armas à distância feitos contra você têm desvantagem na jogada de ataque.

Você ganha um deslocamento de voo de 18 metros.
Se você ainda estiver voando quando o feitiço terminar, você cairá, a menos que possa impedi-lo de alguma forma.

Você pode usar sua ação para criar um cubo de 4,5 metros de vento giratório centrado em um ponto que você possa ver a até 18 metros de você.
Cada criatura naquela área deve fazer um teste de resistência de Constituição.
Uma criatura sofre 2d10 de dano de concussão em caso de falha na resistência, ou metade desse dano em caso de sucesso.
Se uma criatura Grande ou menor falhar no teste de resistência, essa criatura também é empurrada até 3 metros do centro do cubo.           
            
            '''},
           
           {'nome': ' Investidura da Chama',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min

Chamas percorrem seu corpo, irradiando luz plena em um raio de 9 metros e penumbra por mais 9 metros durante a duração da magia. As chamas não te machucam. Até o feitiço terminar, você ganha os seguintes benefícios:

Você é imune a dano de fogo e tem resistência a dano de frio.

Qualquer criatura que se mova a até 1,5 metro de você pela primeira vez em um turno ou termine seu turno nesse local recebe 1d10 de dano de fogo.

Você pode usar sua ação para criar uma linha de fogo de 4,5 metros de comprimento e 1,5 metro de largura estendendo-se de você na direção que você escolher.
Cada criatura na linha deve fazer um teste de resistência de Destreza.
Uma criatura sofre 4d8 de dano de fogo se falhar na resistência, ou metade desse dano se obtiver sucesso           
            
            '''},
           
           {'nome': ' Investidura do Gelo',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min

Até o feitiço terminar, o gelo envolve seu corpo e você ganha os seguintes benefícios:

Você é imune a dano de frio e tem resistência a dano de fogo.

Você pode se mover em terreno difícil criado por gelo ou neve sem gastar movimento extra.

O solo em um raio de 3 metros ao seu redor é gelado e é um terreno difícil para outras criaturas além de você. O raio se move com você.

Você pode usar sua ação para criar um cone de vento gelado de 4,5 metros que se estende de sua mão estendida na direção que você escolher.
Cada criatura no cone deve fazer um teste de resistência de Constituição.
Uma criatura sofre 4d6 de dano de frio se falhar na resistência, ou metade desse dano se obtiver sucesso.
Uma criatura que falhe em seu teste de resistência contra este efeito tem seu deslocamento reduzido pela metade até o início do seu próximo turno.           
            
            '''},
           
           {'nome': ' Investidura da Pedra',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min

Até o fim da magia, pedaços de rocha se espalham pelo seu corpo e você ganha os seguintes benefícios:

Você tem resistência a dano de concussão, perfuração e corte de ataques não mágicos.

Você pode usar sua ação para criar um pequeno terremoto no chão em um raio de 4,5 metros centrado em você.
Outras criaturas naquele terreno devem ser bem sucedidas em um teste de resistência de Destreza ou serão derrubadas .

Você pode se mover por terreno difícil feito de terra ou pedra sem gastar movimento extra.
Você pode se mover através de terra sólida ou pedra como se fosse ar e sem desestabilizá-la, mas não pode terminar seu movimento ali.
Se fizer isso, você será ejetado para o espaço desocupado mais próximo, este feitiço termina e você ficará atordoado até o final do seu próximo turno           
            
            '''}]

o_mago = [{'nome': ' Portão Arcano',
'magia':'''Conjuração 6       1 ação      150m         V,S     Concentração, até 10 minutos

Você cria portais de teletransporte vinculados que permanecem abertos pela duração.
Escolha dois pontos no solo que você possa ver, um ponto a até 3 metros de você e um ponto a até 150 metros de você.
Um portal circular, de 3 metros de diâmetro, se abre sobre cada ponto.
Se o portal for abrir no espaço ocupado por uma criatura, o feitiço falha e o lançamento é perdido.

Os portais são anéis brilhantes bidimensionais cheios de névoa, pairando a centímetros do solo e perpendiculares a ele nos pontos que você escolher.
Um anel é visível apenas de um lado (a sua escolha), que é o lado que funciona como um portal.

Qualquer criatura ou objeto que entra no portal sai do outro portal como se os dois fossem adjacentes um ao outro; passar por um portal pelo lado não-portal não tem efeito.
A névoa que preenche cada portal é opaca e bloqueia a visão através dele. No seu turno, você pode girar os anéis como uma ação bônus para que o lado ativo fique voltado para uma direção diferente.           
            
            '''},
          
        {'nome': ' Miragem Arcana',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
        {'nome': ' Campo Antimagia',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
        {'nome': ' Desejo',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_alta_sacerdotisa = [{'nome': ' Encontrar o caminho',
'magia':'''Adivinhação 6       1 minuto      Auto         V,S,M     1 Dia

Material: (um conjunto de ferramentas divinatórias - como ossos, bastões de marfim, cartas, dentes ou runas esculpidas - no valor de 100 po e um objeto do local que você deseja encontrar)

Este feitiço permite que você encontre a rota física mais curta e direta para um local fixo específico com o qual você esteja familiarizado no mesmo plano de existência.
Se você nomear um destino em outro plano de existência, um destino que se move (como uma fortaleza móvel) ou um destino que não é específico (como "o covil de um dragão verde"), a magia falha.

Pela duração, desde que você esteja no mesmo plano de existência do destino, você sabe a que distância ele está e em que direção ele está.
Enquanto você estiver viajando para lá, sempre que for apresentado a uma escolha de caminhos ao longo do caminho, você determinará automaticamente qual caminho é a rota mais curta e direta (mas não necessariamente a rota mais segura) para o destino.           
            
            '''},
                      
                      {'nome': ' projetar imagem',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
                      
                      {'nome':'telepatia',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
                      
                      {'nome': ' previsão',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_imperatríz = [{'nome': ' Conjure Fey',
'magia':'''Conjuração 6       1 ação      27m         V,S     1h

Você invoca uma criatura feérica de nível de desafio 6 ou inferior, ou um espírito feérico que assume a forma de uma besta de nível de desafio 6 ou inferior. Ele aparece em um espaço desocupado que você possa ver dentro do alcance. A criatura feérica desaparece quando chega a 0 pontos de vida ou quando a magia termina.

A criatura feérica é amigável com você e seus companheiros pela duração. Role a iniciativa para a criatura, que tem seus próprios turnos. Ele obedece a quaisquer comandos verbais que você emitir para ele (nenhuma ação exigida por você), contanto que eles não violem seu alinhamento. Se você não emitir nenhum comando para a criatura feérica, ela se defenderá de criaturas hostis, mas não realizará nenhuma ação.

Se sua concentração for quebrada, a criatura feérica não desaparece. Em vez disso, você perde o controle da criatura feérica, ela se torna hostil com você e seus companheiros e pode atacar. Uma criatura feérica descontrolada não pode ser dispensada por você e desaparece 1 hora após ser invocada.

O GM tem as estatísticas da criatura feérica. Alguns exemplos de criaturas estão listados abaixo.

Em Níveis Superiores. Quando você conjura esta magia usando um espaço de magia de 7º nível ou superior, o nível de desafio aumenta em 1 para cada nível de espaço acima do 6º.           
            
            '''},
                
                {'nome': ' Regenerate',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
                
                {'nome': ' Animal Shapes',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
                
                {'nome': ' Mass Polymorph',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_imperador = [{'nome': ' Sugestão em Massa',
'magia':'''Encantamento 6       1 ação      Pessoal         V,M     10 Dias

Material:  (língua de cobra e um pouco de favo de mel ou uma gota de óleo doce)

Você sugere um curso de atividade (limitado a uma frase ou duas) e influencia magicamente até doze criaturas de sua escolha que você pode ver dentro do alcance e que podem ouvir e entender você.
Criaturas que não podem ser enfeitiçadas são imunes a este efeito.
A sugestão deve ser formulada de forma a tornar o curso de ação razoável.
Pedir à criatura para se esfaquear, se jogar em uma lança, se imolar ou fazer algum outro ato obviamente prejudicial nega automaticamente o efeito do feitiço.

Cada alvo deve fazer um teste de resistência de Sabedoria.
Em uma falha no teste de resistência, ele segue o curso de ação que você descreveu da melhor maneira possível.
O curso de ação sugerido pode continuar por toda a duração.
Se a atividade sugerida puder ser concluída em um tempo menor, o feitiço termina quando o alvo terminar o que foi solicitado a fazer.

Você também pode especificar as condições que acionarão uma atividade especial durante a duração.
Por exemplo, você pode sugerir que um grupo de soldados dê todo o seu dinheiro ao primeiro mendigo que encontrarem.
Se a condição não for satisfeita antes do término da magia, a atividade não é executada.

Se você ou qualquer um de seus companheiros causar dano a uma criatura afetada por esta magia, a magia termina para aquela criatura.

Em Níveis Superiores.
Quando você conjura esta magia usando um espaço de magia de 7º nível, a duração é de 10 dias.
Quando você usa um espaço de magia de 8º nível, a duração é de 30 dias.
Quando você usa um espaço de magia de 9º nível, a duração é de um ano e um dia.           
            
            '''},
               
               {'nome': ' Dedo da Morte',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
               
               {'nome': ' Dominar Monstro',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
               
               {'nome': ' Invulnerabilidade',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_papa = [{'nome': 'Relâmpago em Cadeia',
'magia':'''Evocação 6       1 ação      45m         V,S,M*     Instantâneo

Você cria um raio que se move em direção a um alvo de sua escolha que você possa ver dentro do alcance.
Três setas então saltam desse alvo para até três outros alvos, cada um dos quais deve estar a 9 metros do primeiro alvo.
Um alvo pode ser uma criatura ou um objeto e pode ser alvo de apenas um dos dardos.

Um alvo deve fazer um teste de resistência de Destreza.
O alvo recebe 10d8 de dano elétrico em caso de falha na resistência, ou metade desse dano em caso de sucesso.

Em Níveis Superiores.
Quando você conjura esta magia usando um espaço de magia de 7º nível ou superior, um raio adicional salta do primeiro alvo para outro alvo para cada nível de espaço acima do 6º.           
            
            '''},
          
          {'nome': ' Etéreo',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
          {'nome': ' Aura Sagrada',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
          {'nome': ' Palavra de Poder Curar',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

os_amantes = [{'nome': ' Festa dos Heróis',
'magia':'''Transmutação 6       1 ação      36m         V,S     intantâneo

Você traz um grande banquete, incluindo comida e bebida magníficas.
O banquete leva 1 hora para ser consumido e desaparece ao final desse tempo, e os efeitos benéficos não se estabelecem até que essa hora termine.
Até doze criaturas podem participar do banquete.

Uma criatura que participa do banquete ganha vários benefícios.
A criatura é curada de todas as doenças e venenos, torna-se imune a venenos e ao medo , e faz todos os testes de resistência de Sabedoria com vantagem.
Seu máximo de pontos de vida também aumenta em 2d10 e ganha o mesmo número de pontos de vida. Esses benefícios duram 24 horas.           
            
            '''},
          
              {'nome': ' Conjurar Celestial',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
              {'nome': ' Clone',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
              {'nome':'Projeção Astral',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_carro_de_guerra = [{'nome': ' Ossos da Terra',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min

Você faz até seis pilares de pedra explodirem de lugares no chão que você possa ver dentro do alcance. Cada pilar é um cilindro com diâmetro de 1,5 metro e altura de até 9 metros. O chão onde um pilar aparece deve ser largo o suficiente para seu diâmetro, e você pode mirar no chão sob uma criatura se essa criatura for Média ou menor. Cada pilar tem CA 5 e 30 pontos de vida. Quando reduzido a 0 pontos de vida, um pilar se desfaz em escombros, o que cria uma área de terreno acidentado com um raio de 3 metros que dura até que os escombros sejam removidos. Cada porção de 1,5 m de diâmetro da área requer pelo menos 1 minuto para ser limpa manualmente.

Se um pilar for criado sob uma criatura, essa criatura deve passar em um teste de resistência de Destreza ou será levantada pelo pilar. Uma criatura pode optar por falhar no teste de resistência.

Se um pilar for impedido de atingir sua altura total por causa de um teto ou outro obstáculo, uma criatura no pilar sofre 6d6 de dano de concussão e é contida , presa entre o pilar e o obstáculo. A criatura impedida  pode usar uma ação para fazer um teste de Força ou Destreza (à escolha da criatura) contra a CD de resistência da magia. Em um sucesso, a criatura não está mais contida e deve se mover para fora do pilar ou cair dele.           
            
            '''},
          
                     {'nome': ' Teletransporte',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                     {'nome': ' Labirinto',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                     {'nome':' Portão',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_justiça = [{'nome': ' Transformação de Tenser',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S,M     Concentração até 10min

Material: (alguns fios de cabelo de um touro)
Você se dota de resistência e destreza marcial alimentada por magia. Até que o feitiço termine, você não pode lançar feitiços e ganha os seguintes benefícios:

Você ganha 50 pontos de vida temporários. Se algum deles permanecer quando o feitiço terminar, eles serão perdidos.
Você tem vantagem nas jogadas de ataque feitas com armas simples e marciais.
Quando você atinge um alvo com um ataque de arma, esse alvo recebe 2d12 de dano de força extra.
Você tem proficiência com todas as armaduras, escudos, armas simples e armas marciais.
Você tem proficiência em testes de resistência de Força e Constituição.
Você pode atacar duas vezes, em vez de uma vez, quando realizar a ação Atacar no seu turno.
Você ignora esse benefício se já tiver um recurso, como Ataque Extra, que oferece ataques extras.

Imediatamente após o término do feitiço, você deve ter sucesso em um teste de resistência de Constituição CD 15 ou sofrerá um nível de exaustão.           
            
            '''},
          
             {'nome': ' Espada de Mordenkainen',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
             {'nome': ' Palavra de Poder Stun',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
             {'nome': ' Mudança de Forma',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_eremita = [{'nome': ' Globo da Invulnerabilidade',
'magia':'''Abjuração 6       1 ação      Pessoal(3m)         V,S,M     10min

Material: (uma conta de vidro ou cristal que se estilhaça quando o feitiço termina)

Uma barreira imóvel e levemente cintilante surge em um raio de 3 metros ao seu redor e permanece pela duração.

Qualquer magia de 5º nível ou inferior lançada de fora da barreira não pode afetar criaturas ou objetos dentro dela, mesmo que a magia seja lançada usando um espaço de magia de nível superior.
Tal feitiço pode atingir criaturas e objetos dentro da barreira, mas o feitiço não tem efeito sobre eles.
Da mesma forma, a área dentro da barreira é excluída das áreas afetadas por tais feitiços.

Em Níveis Superiores.
Quando você conjura esta magia usando um espaço de magia de 7º nível ou superior, a barreira bloqueia magias de um nível superior para cada nível de espaço acima do 6º.           
            
            '''},
          
             {'nome': ' Seqüestro',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
             {'nome': ' Escuridão Enlouquecedora',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
             {'nome': ' Muralha Prismática',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_roda_da_fortuna = [{'nome': ' Dispersão',
'magia':'''Conjuração 6       1 ação      9m         V     Instantâneo           
            
            '''},
          
                     {'nome': ' Pulverização Prismática',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                     {'nome': ' Controle do Clima',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                     ' Qualquer feitiço de 9º nível']

a_forca = [{'nome': ' Visão Verdadeira',
'magia':'''Adivinhação 6       1 ação      Toque         V,S,M     10min

Material: (uma pomada para os olhos que custa 25 po; é feita de pó de cogumelo, açafrão e gordura; e é consumida pelo feitiço)

Esta magia dá à criatura voluntária que você toca a habilidade de ver as coisas como elas realmente são. Pela duração, a criatura tem visão verdadeira , percebe portas secretas escondidas por magia e pode ver dentro do Plano Etéreo, tudo em um alcance de 36 metros.           
            
            '''},
          
           {'nome': ' Tempestade de Fogo',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
           {'nome': ' Nuvem Incendiária',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
           {'nome': ' Polimorfo Verdadeiro',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_enforcado = [{'nome': ' Carne para Pedra',
'magia':'''Transmutação 6       1 ação      18m         V,S,M     Concentração até 1min

Material: (uma pitada de cal, água e terra)

Você tenta transformar uma criatura que você pode ver dentro do alcance em pedra.
Se o corpo do alvo for feito de carne, a criatura deve fazer um teste de resistência de Constituição. Em uma falha na resistência, ele é contido quando sua carne começa a endurecer.
Em um teste de resistência bem-sucedido, a criatura não é afetada.

Uma criatura impedida por este feitiço deve fazer outro teste de resistência de Constituição no final de cada um de seus turnos.
Se ele resistir com sucesso contra este feitiço três vezes, o feitiço termina. Se falhar três vezes no teste de resistência, ele se transforma em pedra e fica petrificado enquanto durar.
Os sucessos e fracassos não precisam ser consecutivos; mantenha o controle de ambos até que o alvo colete três de um tipo.

Se a criatura for fisicamente quebrada enquanto petrificada , ela sofrerá deformidades semelhantes se voltar ao seu estado original.

Se você mantiver sua concentração neste feitiço por toda a duração possível, a criatura se transformará em pedra até que o efeito seja removido.           
            
            '''},
          
               {'nome': ' Gravidade Reversa',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
               {'nome': ' Tsunami',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
               {'nome': ' Estranho',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_morte = [{'nome': ' Prejuízo',
'magia':'''Necromancia 6       1 ação      18m         V,S     Instantâneo

Você libera uma doença virulenta em uma criatura que você pode ver dentro do alcance.
O alvo deve fazer um teste de resistência de Constituição. Em uma falha no teste de resistência, sofre 14d6 de dano necrótico, ou metade desse dano em um teste de resistência bem-sucedido.
O dano não pode reduzir os pontos de vida do alvo abaixo de 1. Se o alvo falhar no teste de resistência, seu máximo de pontos de vida é reduzido por 1 hora em uma quantidade igual ao dano necrótico sofrido.
Qualquer efeito que remova uma doença permite que o máximo de pontos de vida de uma criatura volte ao normal antes que o tempo passe.           
            
            '''},
          
           {'nome':'Ressurreição',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
           {'nome': ' Horrível Murchamento de Abi-Dalzim',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
           {'nome': ' Verdadeira Ressurreição',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_temperança = [{'nome': ' Contingência',
'magia':'''Evocação 6       1 ação      Pessoal         V,S,M*     10 dias

Material: (uma estatueta sua esculpida em marfim e decorada com pedras preciosas no valor mínimo de 1.500 po)

Escolha uma magia de 5º nível ou inferior que você possa conjurar, que tenha tempo de conjuração de 1 ação e que tenha como alvo você.
Você lança aquela magia - chamada de magia contingente - como parte da conjuração de contingência , gastando espaços de magia para ambos, mas a magia contingente não entra em vigor.
Em vez disso, ele entra em vigor quando uma determinada circunstância ocorre. Você descreve essa circunstância quando lança os dois feitiços.
Por exemplo, um conjuração de contingência com respiração na água pode estipular que a respiração na água entra em vigor quando você é engolfado em água ou em um líquido similar.

O feitiço contingente entra em vigor imediatamente após a circunstância ser atendida pela primeira vez, quer você queira ou não, e então a contingência termina.

O feitiço contingente tem efeito apenas em você, mesmo que normalmente possa atingir outros.
Você pode usar apenas um feitiço de contingência por vez.

Se você lançar este feitiço novamente, o efeito de outro feitiço de contingência sobre você termina. Além disso, a contingência termina em você se seu componente material não estiver em sua pessoa.
          
            
            '''},
          
                {'nome': ' Palavra de Poder Dor',
'magia':'''

           
            
            '''},
          
                {'nome': ' Antipatia/Simpatia',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                {'nome': ' Parada do Tempo',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_diabo = [{'nome': ' Soul Cage',
'magia':'''Necromancia 6       Reação      18m         V,S,M     8h

Reação: você realiza quando um humanóide que você pode ver a até 18 metros de você morre.

Material: (uma minúscula gaiola de prata no valor de 100 po)

Este feitiço arrebata a alma de um humanóide quando ele morre e o prende dentro da pequena gaiola que você usa para o componente material.
Uma alma roubada permanece dentro da gaiola até que o feitiço termine ou até que você destrua a gaiola, o que encerra o feitiço.
Enquanto você tiver uma alma dentro da jaula, você pode explorá-la de qualquer uma das maneiras descritas abaixo. Você pode usar uma alma presa até seis vezes.
Depois de explorar uma alma pela sexta vez, ela é liberada e o feitiço termina. Enquanto uma alma está presa, o humanóide morto de onde veio não pode ser revivido.

Roubar Vida.
Você pode usar uma ação bônus para drenar o vigor da alma e recuperar 2d8 pontos de vida.

Consulta Alma.
Você faz uma pergunta à alma (nenhuma ação é necessária) e recebe uma breve resposta telepática, que você pode entender independentemente do idioma usado.
A alma sabe apenas o que sabia em vida, mas deve responder a você com sinceridade e com o melhor de sua capacidade.
A resposta não é mais do que uma frase ou duas e pode ser enigmática.

Empreste Experiência.
Você pode usar uma ação bônus para se fortalecer com a experiência de vida da alma, fazendo sua próxima jogada de ataque, teste de habilidade ou teste de resistência com vantagem.
Se você não usar esse benefício antes do início do seu próximo turno, ele será perdido.

Olhos dos Mortos.
Você pode usar uma ação para nomear um lugar que o humanóide viu em vida, o que cria um sensor invisível em algum lugar naquele lugar se estiver no plano de existência em que você está atualmente.
O sensor permanece enquanto você se concentrar, até 10 minutos (como se você estivesse se concentrando em um feitiço).
Você recebe informações visuais e auditivas do sensor como se estivesse em seu espaço usando seus sentidos.

Uma criatura que pode ver o sensor (como uma que usa ver invisibilidade ou visão verdadeira) vê uma imagem translúcida do humanóide atormentado cuja alma você enjaulou.           
            
            '''},
          
           {'nome': ' Forcecage',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
           {'nome': ' Semiplano',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
           {'nome': ' Prisão'}]

a_torre_fulminada = [{'nome': ' Desintegrar',
'magia':'''Transmutação 6       1 ação      18 m         V,S,M     Instantâneo

Material: (uma magnetita e uma pitada de pó)


Um fino raio verde brota de seu dedo apontado para um alvo que você pode ver dentro do alcance.
O alvo pode ser uma criatura, um objeto ou uma criação de força mágica, como a parede criada pela parede de força .

Uma criatura alvo deste feitiço deve fazer um teste de resistência de Destreza.
Se falhar, o alvo sofre 10d6 + 40 de dano de força.
O alvo é desintegrado se este dano o deixar com 0 pontos de vida.

Uma criatura desintegrada e tudo o que está vestindo e carregando, exceto itens mágicos, são reduzidos a uma pilha de pó cinza fino.
A criatura pode ser restaurada à vida apenas por meio de uma verdadeira ressurreição ou um  feitiço de desejo .

Este feitiço desintegra automaticamente um objeto não mágico Grande ou menor ou uma criação de força mágica.
Se o alvo for um objeto Enorme ou maior ou criação de força, esta magia desintegra uma porção de 3 metros cúbicos dele.
Um item mágico não é afetado por este feitiço.

Em Níveis Superiores.
Quando você conjura esta magia usando um espaço de magia de 7º nível ou superior, o dano aumenta em 3d6 para cada nível de espaço acima do 6º.           
            
            '''},
          
                     {'nome': ' Redemoinho',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                     {'nome':'Terremoto',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
                     {'nome': ' Tempestade de Vingança',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_estrela = [{'nome': ' Cura',
'magia':'''Evocação 6       1 ação      18m         V,S     Instantâneo

Escolha uma criatura que você possa ver dentro do alcance.
Uma onda de energia positiva passa pela criatura, fazendo-a recuperar 70 pontos de vida.
Este feitiço também acaba com a cegueira, surdez e quaisquer doenças que afetem o alvo.
Este feitiço não tem efeito em constructos ou mortos-vivos.

Em Níveis Superiores.
Quando você conjura esta magia usando um espaço de magia de 7º nível ou superior, a quantidade de cura aumenta em 10 para cada nível de espaço acima do 6º           
            
            '''},
          
             {'nome': ' Coroa de Estrelas',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
             {'nome': ' Dragão Ilusório',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
          
             {'nome': ' Cura em Massa',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

a_lua = [{'nome': ' Prisão mental',
'magia':'''Ilusão 6       1 ação      18m         S     Concentração até 1min

Você tenta prender uma criatura dentro de uma célula ilusória que apenas ela percebe.
Uma criatura que você possa ver dentro do alcance deve fazer um teste de resistência de Inteligência.
O alvo é bem-sucedido automaticamente se for imune a ser enfeitiçado.
Em um teste de resistência bem-sucedido, o alvo recebe 5d10 de dano psíquico e o feitiço termina.
Em uma falha na resistência, o alvo sofre 5d10 de dano psíquico e você faz com que a área imediatamente ao redor do espaço do alvo pareça perigosa para ele de alguma forma.
Você pode fazer com que o alvo se perceba cercado por fogo, navalhas flutuantes ou bocas horríveis cheias de dentes gotejantes. Qualquer que seja a forma que a ilusão assuma, o alvo não pode ver ou ouvir nada além dela e é impedido pela duração da magia.
Se o alvo for movido para fora da ilusão, fizer um ataque corpo a corpo através dele, ou atingir qualquer parte de seu corpo através dele,

           
            
            '''},
         
         {'nome': ' mudança de plano',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
         
         {'nome': ' mente em branco',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
         
         {'nome':'grito psíquico',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_sol = [{'nome': ' Raio de Sol',
'magia':'''Evoação 6       1 ação      18m         V,S,M     1min

Material: (uma lupa)

Um feixe de luz brilhante sai de sua mão em uma linha de 1,5 metro de largura por 18 metros de comprimento. Cada criatura na fila deve fazer um teste de resistência de Constituição. Se falhar na resistência, uma criatura sofre 6d8 de dano radiante e fica cega até o seu próximo turno. Em um teste de resistência bem-sucedido, ele sofre metade do dano e não fica cego por esta magia.
Mortos-vivos e limos têm desvantagem neste teste de resistência.

Você pode criar uma nova linha de radiância como sua ação em qualquer turno até que o feitiço termine.

Durante a duração, uma partícula de radiância brilhante brilha em sua mão.
Ele emite luz plena em um raio de 9 metros e penumbra por mais 9 metros.
Esta luz é a luz solar           
            
            '''},
        
         {'nome': ' Bola de Fogo Explosiva',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
         {'nome': ' Atrasada',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
         {'nome': ' Explosão Solar',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
         {'nome': ' Enxame de Meteoros',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_julgamento = [{'nome': ' Caminhada no Vento',
'magia':'''Transmutação 6       1 min      9m         V,S,M     8h

Material: (fogo e água benta)

Você e até dez criaturas voluntárias que você possa ver dentro do alcance assumem uma forma gasosa pela duração, aparecendo como tufos de nuvem.
Enquanto estiver nesta forma de nuvem, uma criatura tem um deslocamento de voo de 300 pés e tem resistência a dano de armas não mágicas.
As únicas ações que uma criatura pode realizar nesta forma são a ação Correr ou reverter para sua forma normal.
A reversão leva 1 minuto, durante o qual a criatura fica incapacitada e não pode se mover.
Até o feitiço terminar, uma criatura pode reverter para a forma de nuvem, o que também requer a transformação de 1 minuto.

Se uma criatura estiver na forma de nuvem e voando quando o efeito terminar, a criatura desce 18 metros por rodada por 1 minuto até aterrissar, o que ela faz com segurança.
Se não conseguir pousar após 1 minuto, a criatura cai a distância restante.           
            
            '''},
        
                {'nome': ' Simulacrum',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
                {'nome': ' Fraqueza',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
                {'nome': ' Palavra de Poder Matar',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''}]

o_mundo = [{'nome': ' Druid Grove',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
           {'nome': ' Magnificent Mansion de Mordenkainen',
'magia':'''Transmutação 6       1 ação      Pessoal         V,S     10min           
            
            '''},
        
           {'nome': ' Mighty Fortress',
'magia':'''Abjuração 6       10 min      Toque         V,S,M     24h

Material: (visco, que o feitiço consome, que foi colhido com uma foice dourada sob a luz da lua cheia)

Você invoca os espíritos da natureza para proteger uma área externa ou subterrânea.
A área pode ser tão pequena quanto um cubo de 30 pés ou tão grande quanto um cubo de 90 pés.
Edifícios e outras estruturas são excluídos da área afetada.
Se você conjurar esta magia na mesma área todos os dias durante um ano, a magia dura até ser dissipada.
O feitiço cria os seguintes efeitos dentro da área. Ao conjurar esta magia, você pode especificar criaturas como amigas que são imunes aos efeitos.
Você também pode especificar uma senha que, quando falada em voz alta, torna o locutor imune a esses efeitos. Toda a área protegida irradia magia.
Um dissipar magia lançado na área, se bem sucedido, remove apenas um dos seguintes efeitos, não toda a área. 
O lançador desse feitiço escolhe qual efeito terminar.
Somente quando todos os seus efeitos se forem é que este feitiço é dissipado.

Névoa Sólida.
Você pode preencher qualquer número de quadrados de 1,5 metros no chão com névoa espessa, tornando-os fortemente obscurecidos.
A névoa chega a 10 metros de altura. Além disso, cada metro de movimento através do nevoeiro custa 2 metros extras. Para uma criatura imune a este efeito, a névoa não obscurece nada e se parece com uma névoa suave, com partículas de luz verde flutuando no ar.

Agarrando a vegetação rasteira.
Você pode preencher qualquer número de quadrados de 1,5 metros no chão que não estejam cheios de névoa com ervas daninhas e trepadeiras, como se fossem afetados por um feitiço emaranhado.
Para uma criatura imune a este efeito, as ervas daninhas e trepadeiras parecem macias e se remodelam para servir como assentos ou camas temporárias.

Guardiões do Bosque.
Você pode animar até quatro árvores na área, fazendo com que elas se desenraizem do chão. Essas árvores têm as mesmas estatísticas de uma árvore desperta, que aparece no Manual dos Monstros, exceto que não podem falar e sua casca é coberta com símbolos druídicos.
Se qualquer criatura não imune a este efeito entrar na área protegida, os guardiões do bosque lutam até expulsar ou matar os intrusos.
Os guardiões do bosque também obedecem aos seus comandos falados (nenhuma ação exigida por você) que você emite enquanto estiver na área.
Se você não der comandos a eles e nenhum intruso estiver presente, os guardiões do bosque não farão nada.
Os guardiões do bosque não podem deixar a área protegida.
Quando o feitiço termina, a magia que os anima desaparece e as árvores criam raízes novamente, se possível.

Efeito de Feitiço Adicional.
Você pode escolher um dos seguintes efeitos mágicos dentro da área protegida:

Uma rajada constante de vento em dois locais à sua escolha
Aumente o crescimento em um local de sua escolha
Muro de vento em dois locais à sua escolha
Para uma criatura imune a este efeito, os ventos são uma brisa fragrante e suave, e a área de crescimento do espigão é inofensiva.           
            
            '''},
        
           'qualquer feitiço de 9º nível']



baralho_tarot = ['O Louco','O Mago', 'A Alta Sacerdotisa','A Imperatríz','O Imperador','O Papa',
'Os Amantes','O Carro de Guerra','A Justiça','O Eremita','A Roda da Fortuna','A Forca',
'O Enforcado','A Morte','A Temperança','O Diabo','A Torre Fulminada','A Estrela','A Lua',
'O Sol','O Julgamento','O Mundo']

baralho_tarot = random.sample(baralho_tarot, len(baralho_tarot))

baralho_tarot_v = [o_louco, o_mago, a_imperatríz, o_imperador,o_papa, os_amantes, o_carro_de_guerra,
a_justiça, o_eremita, a_roda_da_fortuna, a_forca, o_enforcado, a_morte, a_temperança, o_diabo,
a_torre_fulminada, a_estrela, a_lua, o_sol, o_julgamento, o_mundo]   

def sorte():
   random.shufle(baralho_tarot)
   diario = baralho_tarot[0:3]
   
   for c in baralho_tarot:
   
   escolha = str(input('Qual dessas 3 você quer?'))
   while escolha not in diario[:]:
      escolha = str(input('Digite o nome da carta corretamente!'))
         
   return escolha

sorte() 

   


