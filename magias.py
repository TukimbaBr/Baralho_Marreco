baralho = ["as_copas", "dois_copas", "tres_copas", "quatro_copas", "cinco_copas", "seis_copas",
"sete_copas","oito_copas","nove_copas","dez_copas", 'onze_copas', "dama_copas", "valete_copas", "reis_copas",

"as_ouros", "dois_ouros", "tres_ouros", "quatro_ouros", "cinco_ouros", "seis_ouros",
"sete_ouros", "oito_ouros","nove_ouros","dez_ouros", 'onze_ouros', "dama_ouros", "valete_ouros", "reis_ouros",

"as_paus", "dois_paus", "tres_paus", "quatro_paus", "cinco_paus", "seis_paus", "sete_paus",
"oito_paus", "nove_paus","dez_paus", 'onze_paus', "dama_paus", "valete_paus", "reis_paus",

"as_espada", "dois_espada", "tres_espada", "quatro_espada", "cinco_espada", "seis_espada",
"sete_espada", "oito_espada", "nove_espada", "dez_espada", 'onze_espada', "dama_espada", "valete_espada",
"reis_espada"]

copas = ["as_copas", "dois_copas", "tres_copas", "quatro_copas", "cinco_copas", "seis_copas",
"sete_copas","oito_copas","nove_copas","dez_copas", 'onze_copas', "dama_copas", "valete_copas", "reis_copas",]

ouros = ["as_ouros", "dois_ouros", "tres_ouros", "quatro_ouros", "cinco_ouros", "seis_ouros",
"sete_ouros", "oito_ouros","nove_ouros","dez_ouros", 'onze_ouros', "dama_ouros", "valete_ouros", "reis_ouros",]

paus = ["as_paus", "dois_paus", "tres_paus", "quatro_paus", "cinco_paus", "seis_paus", "sete_paus",
"oito_paus", "nove_paus","dez_paus", 'onze_paus', "dama_paus", "valete_paus", "reis_paus",]

espada = ["as_espada", "dois_espada", "tres_espada", "quatro_espada", "cinco_espada", "seis_espada",
"sete_espada", "oito_espada", "nove_espada", "dez_espada", 'onze_espada', "dama_espada", "valete_espada",
"reis_espada"]

coringa = ['CORINGA']

arcanosmen = [{'carta':'as_copas','nome':' Feridas em Massa',
'magia':'''evocação 5       1 ação    18 metros      V, S        instantânea     

Uma onda de energia curativa emerge de um ponto, à sua escolha, dentro do alcance.
Escolha até seis criaturas numa esfera de 9 metros de raio, centrada nesse ponto.
Cada alvo recupera uma quantidade de pontos de vida igual a 3d8 + seu modificador de habilidade de conjuração.
A magia não afeta mortos-vivos ou constructos.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 6° nível ou superior, a cura aumenta em 1d8 para cada nível do espaço acima do 5°.'''},
              
{'carta':'dois_copas','nome':'Curar Feridas',
'magia':'''evocação 1       1 ação       toque       V, S        instantânea     

Uma criatura que você tocar recupera uma quantidade de pontos de vida igual a 1d8 + seu modificador de habilidade de conjuração.
Essa magia não produz efeito em mortos-vivos ou constructos.

Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 2° nível ou superior, a cura aumenta em 1d8 para cada nível do espaço acima do 1°.''',},

{'carta':'tres_copas','nome':'Armadura de Agathys',
'magia':'''abjuração 1      1 ação       pessoal     V, S, M     1 hora      

Material: um copo de água.

Uma força magica protetora envolve você, manifestando- se como um frio espectral que cobre você e seu equipamento.
Você ganha 5 pontos de vida temporários pela duração.
Se uma criatura atingir você com um ataque corpo-a-corpo enquanto estiver com esses pontos de vida, a criatura sofrerá 5 de dano de frio.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, tanto os pontos de vida temporários quanto o dano de frio aumentam em 5 para cada nível do espaço acima do 1°.
''',},

{'carta':'quatro_copas','nome':'Abençoar',
 'magia':'''encantamento 1      1 ação     9 metros        V, S, M     até 1 minuto     
 
 Material: um borrifo de água benta.

Você abençoa até três criaturas, à sua escolha, dentro do alcance.
Sempre que um alvo realizar uma jogada de ataque ou teste de resistência antes da magia acabar, o alvo pode jogar um d4 e adicionar o valor jogado ao ataque ou teste de resistência.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, você pode afetar uma criatura adicional para cada nível do espaço acima do 1°.''',},

{'carta':'cinco_copas','nome':'Área escorregadia',
'magia':'''conjuração 1     1 ação       18 metros       V, S, M     1 minuto     

Material: um pouco de pele de porco ou manteiga.

Graxa escorregadia cobre o solo em um quadrado de 3 metros centrado em um ponto, dentro do alcance, tornando essa área em terreno difícil pela duração.

Quando a graxa aparece, cada criatura de pé na área deve ser bem sucedida num teste de resistência de Destreza ou cairá no chão.
Uma criatura que entre na área ou termine seu turno nela, deve ser bem sucedido num teste de resistência de Destreza ou cairá no chão.''',},

{'carta':'seis_copas','nome':'Raio de Gelo',
 'magia':'''evocação 0      1 ação      18 metros       V, S        instantânea
 
Um raio frigido de luz azul clara parte em direção de uma criatura, dentro do alcance.
Realize um ataque à distância com magia contra o alvo. Se atingir, ele sofre 1d8 de dano de frio e seu deslocamento é reduzido em 3 metros até o começo do seu próximo turno.

O dano da magia aumenta em 1d8 quando você alcança o 5° nível (2d8), 11° nível (3d8) e 17° nível (4d8).''',},

{'carta':'sete_copas','nome':'Raio Guiador',
'magia':'''evocação 1        1 ação       36 metros       V, S        1 rodada

Um lampejo de luz se lança em direção de uma criatura, à sua escolha, dentro do alcance.
Realize um ataque à distância com magia contra o alvo.
Se atingir, o alvo sofre 4d6 de dano 1te e, a próxima jogada de ataque contra esse alvo, antes do final do seu próximo turno, terá vantagem, graças a penumbra mística cintilando no alvo, até então.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1°.''',},

{'carta':'oito_copas','nome':'Oração de Cura',
'magia':'''evocação 2       10 minutos      9 metros    V   instantânea
Até seis criaturas, à sua escolha, que você possa ver, dentro do alcance, recuperam uma quantidade de pontos de vida igual a 2d8 + seu modificador de habilidade de conjuração, cada uma.
Essa magia não afeta mortos-vivos ou constructos.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 3° nível ou superior, a cura aumenta em 1d8 para cada nível do espaço acima do 2°.''',},

{'carta':'nove_copas','nome':'Vínculo Protetor',
'magia':'''abjuração 2      1 ação      toque       V, S, M     1 hora

Material: um par de anéis de platina valendo, no mínimo, 50 po cada, que você e o alvo devem usar pela duração.

Essa magia protege uma criatura voluntária que você tocar e cria uma conexão mística entre você e o alvo até a magia acabar.
Enquanto o alvo estiver a até 18 metros de você, ele recebe +1 de bônus na CA, nos testes de resistência e terá resistência a todos os danos. No entanto, a cada vez que ele sofrer dano, você sofrerá a mesma quantidade de dano.

A magia acaba se você cair a 0 pontos de vida ou se você e o alvo ficarem separados a mais de 18 metros. Ela também termina se a magia for conjurada novamente em quaisquer das criaturas conectadas. Você também pode dissipar a magia com uma ação.''',},

{'carta':'dez_copas','nome':'Cegueira/Surdez',
'magia':'''necromancia 2        1 ação  9 metros        V       1 minuto
Você pode cegar ou ensurdecer um oponente. Escolha uma criatura que você possa ver dentro do alcance para fazer um teste de resistência de Constituição. Se ela falhar, ficará ou cega ou surda (à sua escolha) pela duração.
No final de cada um dos turnos dele, o alvo pode realizar um teste de resistência de Constituição. Se obtiver sucesso, a magia termina.

Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 3° nível ou superior, você pode afetar uma criatura adicional para cada nível de espaço acima do 2°.''',},

{'carta':'onze_copas','nome':'Maremoto',
'magia':'''Conjuração 3     1 ação      35m      V, S, M        Instantâneo

Material: uma gota de água

Você evoca uma onda de água que cai em uma área dentro do alcance.
A área pode ter até 30 pés de comprimento, até 10 pés de largura e até 10 pés de altura.
Cada criatura naquela área deve fazer um teste de resistência de Destreza.
Em uma falha, uma criatura sofre 4d8 de dano de concussão e é derrubada.
Em um sucesso, uma criatura recebe metade do dano e não é derrubada.
A água então se espalha pelo chão em todas as direções, extinguindo chamas desprotegidas em sua área e a até 9 metros dela.''',},

{'carta':'dama_copas','nome':'revivicar',
'magia':'''Necromancia 3        1 ação       toque       V, S, M     instantânea

Material: um diamante no valor de 300 po, consumido pela magia.

Você toca uma criatura que tenha morrido dentro do último minuto.
Essa criatura volta a vida com 1 ponto de vida. Essa magia não pode trazer de volta a vida criaturas que tenham morrido de velhice nem pode restaurar quaisquer partes do corpo perdidas.''',},

{'carta':'valete_copas','nome':'Tempestade de Gelo',
'magia':'''Evocação 4       1 ação       90 metros       V, S, M     instantânea

Material: um pouco de poeira e algumas gotas de água.

Uma rajada de pedras de gelo batem no chão em um cilindro de 6 metros de raio por 12 metros de altura, centrado num ponto dentro do alcance.
Cada criatura no cilindro deve realizar um teste de resistência de Destreza.
Uma criatura sofre 2d8 de dano de concussão e 4d6 de dano de frio se falhar na resistência ou metade desse dano se obtiver sucesso.
O granizo torna a área da tempestade em terreno difícil até o final do seu próximo turno.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 5° nível ou superior, o dano de concussão aumenta em 1d8 para cada nível do espaço acima do 4°.''',},

{'carta':'reis_copas','nome':'Proteção Contra a Morte',
'magia':'''abjuração 4      1 ação      toque       V, S    8 horas
Você toca uma criatura e concede a ela uma certa proteção contra a morte.
A primeira vez que o alvo cair a 0 pontos de vida, como resultado de ter sofrido dano, o alvo, ao invés disso, cai a 1 ponto de vida e a magia termina.

Se a magia ainda estiver funcionando quando o alvo for afetado por um efeito que poderia mata-lo instantaneamente sem causar dano, o efeito, ao invés disso, não funciona no alvo e a magia termina.''',},


#Magias de Ouros
{'carta':'as_ouros','nome':'Praga de insetos',
 'magia':'''conjuração 5        1 ação      90 metros   V, S, M     até 10 minutos

Material: alguns grãos de açúcar, alguns miolos de grão e uma mancha de gordura.

Um enxame voraz de gafanhotos preenche uma esfera de 6 metros de raio, centrada no ponto que você escolher, dentro do alcance.
A esfera se espalha dobrando esquinas.
A esfera permanece pela duração e sua área é de escuridão leve.
A área da esfera é de terreno difícil.
Quando a área aparece, cada criatura dentro dela deve realizar um teste de resistência de Constituição.
Uma criatura sofre 4d10 de dano perfurante se falhar na resistência ou metade desse dano se passar.
Uma criatura deve, também, realizar um teste de resistência quando entrar na área da magia pela primeira vez num turno ou terminar seu turno nela.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 6° nível ou superior, o dano aumenta em 1d10 para cada nível do espaço acima do 5°.''',},

{'carta':'dois_ouros','nome':'Infligir Ferimentos',
 'magia':'''necromancia 1       1 ação      toque       V, S        instantânea
 
Faça um ataque corpo-a-corpo com magia contra uma criatura dentro do alcance.
Se atingir, o alvo sofre 3d10 de dano necrótico.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d10 para cada nível acima do 1°.''',},

{'carta':'tres_ouros','nome':'Absorver Elementos',
'magia':'''Abjuração 1      Reação       pessoal        S      1 rodada

O feitiço captura parte da energia recebida, diminuindo seu efeito sobre você e armazenando-a para seu próximo ataque corpo a corpo.
Você tem resistência ao tipo de dano desencadeante até o início do seu próximo turno.
Além disso, na primeira vez que você acertar um ataque corpo a corpo no seu próximo turno, o alvo sofre 1d6 de dano extra do tipo desencadeante e a magia termina.

Em Níveis Superiores.  Quando você conjura esta magia usando um espaço de magia de 2º nível ou superior, o dano extra aumenta em 1d6 para cada nível do espaço acima do 1º.
''',},

{'carta':'quatro_ouros','nome':'Fogo das Fadas',
'magia':'''evocação 1       1 ação      18 metros       V       até 1 minuto

Cada objeto num cubo de 6 metros dentro do alcance fica delineado com luz azul, verde ou violeta (à sua escolha).
Qualquer criatura na área, quando a magia é conjurada, também fica delineada com luz, se falhar num teste de resistência de Destreza.
Pela duração, os objetos e criaturas afetadas emitem penumbra num raio de 3 metros.

Qualquer jogada de ataque contra uma criatura afetada ou objeto tem vantagem, se o atacante puder ver o alvo e, a criatura afetada ou objeto não recebe benefício por estar invisível.''',},

{'carta':'cinco_ouros','nome':'Emaranhar',
'magia':'''Conjuração 1     1 Ação      27m     V,S              Concentração 1 minuto

Ervas daninhas e trepadeiras brotam do chão em um quadrado de 20 pés a partir de um ponto dentro do alcance.
Durante a duração, essas plantas transformam o solo da área em terreno difícil.
Uma criatura na área quando você conjurar a magia deve ser bem sucedida em um teste de resistência de Força ou será impedida pelas plantas emaranhadas até que a magia termine.
Uma criatura impedida pelas plantas pode usar sua ação para fazer um teste de Força contra a CD de sua magia.
Em um sucesso, ele se liberta.
Quando o feitiço termina, as plantas conjuradas murcham.''',},

{'carta':'seis_ouros','nome':'Armas de Hadar',
'magia':'''Conjuração 1     1 ação       pessoal     V, S        instantânea     
Você invoca o poder de Hadar, o Faminto Sombrio.
Tentáculos de energia negra brotam de você e golpeiam todas as criaturas a até 3 metros de você.
Cada criatura na área deve realizar um teste de resistência de Força.
Se falhar, o alvo sofre 2d6 de dano necrótico e não pode fazer reações até o próximo turno dela.
Em um sucesso, uma criatura sofre metade do dano e não sofre qualquer outro efeito.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1°.''',},

{'carta':'sete_ouros','nome':'Ataque Arrebatador',
'magia':'''conjuração 1     1 ação bônus    pessoal     V       Concentração, até 1 minuto

A próxima vez que você acertar uma criatura com um ataque de arma antes que esta magia termine, uma massa contorcida de vinhas espinhosas aparece no ponto de impacto.
O alvo deve ser bem sucedido em um teste de resistência de Força ou será impedido pelas vinhas mágicas até que a magia termine.
Uma criatura Grande ou maior tem vantagem neste teste de resistência.
Se o alvo for bem sucedido no teste, as vinhas murcham.
Enquanto impedido por esta magia, o alvo sofre 1d6 de dano perfurante no início de cada um de seus turnos.
Uma criatura impedida pelas vinhas ou uma que possa tocar a criatura pode usar sua ação para fazer um teste de Força contra a CD de sua magia.
Em um sucesso, o alvo é libertado.

Em Níveis Superiores. Se você conjurar esta magia usando um espaço de magia de 2º nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1º.''',},

{'carta':'oito_ouros','nome':'Garra Terrestre Maximilian',
'magia':'''Transmutação 2       1 Ação      9m      V,S,M             1 minuto

Você escolhe um espaço desocupado de 1,5 metro quadrado no chão que você possa ver dentro do alcance.
Uma mão Média feita de solo compactado sobe até lá e alcança uma criatura que você pode ver a até 1,5 metro dela.
O alvo deve fazer um teste de resistência de Força.
Se falhar na resistência, o alvo sofre 2d6 de dano de concussão e fica impedido pela duração da magia.
Com uma ação, você pode fazer com que a mão esmague o alvo impedido , que deve fazer um teste de resistência de Força.
Ele sofre 2d6 de dano de concussão se falhar na resistência, ou metade desse dano se obtiver sucesso.
Para escapar, o alvo impedido pode usar sua ação para fazer um teste de Força contra a CD de sua magia.
Em um sucesso, o alvo escapa e não é mais contido pela mão.
Com uma ação, você pode fazer com que a mão alcance uma criatura diferente ou se mova para um espaço desocupado diferente dentro do alcance.
A mão libera um alvo impedido se você fizer qualquer um dos dois.''',},

{'carta':'nove_ouros','nome':'Segurar Pessoa',
'magia':''' Encantamento 2      1 Ação      18m      V,S,M      1 minuto

Escolha um humanóide que você possa ver dentro do alcance.
O alvo deve ser bem sucedido em um teste de resistência de Sabedoria ou ficará paralisado pela duração.
No final de cada um de seus turnos, o alvo pode fazer outro teste de resistência de Sabedoria.
Em um sucesso, a magia termina no alvo.

Em Níveis Superiores. Quando você conjura esta magia usando um espaço de magia de 3º nível ou superior, você pode escolher um humanóide adicional para cada nível de espaço acima do 2º.
Os humanóides devem estar a até 9 metros um do outro quando você os alvejar.''',},

{'carta':'dez_ouros','nome':'Passo Nebuloso',
'magia':'''conjuração 2     1 ação bônus    pessoal     V       instantânea

Brevemente envolto por uma neblina prateada, você se teletransporta a até 9 metros para um espaço desocupado que você possa ver.''',},

{'carta':'onze_ouros','nome':'Toque Vampírico',
'magia':'''necromancia 3        1 ação Bônus     Toque     V, S        1 hora

Você toca 1 arma e a imbui com uma aura de sifão de vida.
Quando uma criatura atinge com um ataque corpo a corpo usando a arma afetada, ela causa 1d8 de dano necrótico adicional e é curada pela metade do dano necrótico causado.

Esta magia causa 1d8 de dano adicional para cada 2 espaços de magia acima do 3º.''',},

{'carta':'dama_ouros','nome':'Transferência de Vida',
'magia':'''Necromancia 3        1 ação      9m      V, S        Instantâneo

Você sacrifica um pouco de sua saúde para curar os ferimentos de outra criatura.
Você sofre 4d8 de dano necrótico, que não pode ser reduzido de forma alguma, e uma criatura à sua escolha que você possa ver dentro do alcance recupera um número de pontos de vida igual ao dobro do dano necrótico que você sofre.

Em Níveis Superiores: Quando você lança esta magia usando um espaço de magia de 4º nível ou superior, o dano aumenta em 1d8 para cada nível de espaço acima do 3º.''',},

{'carta':'valete_ouros','nome':'Praga',
'magia':'''necromancia 5        1 ação      toque       V, S        7 dias

Seu toque inflige uma doença. Faça um ataque de magia corpo-a-corpo contra uma criatura ao seu alcance.
Se atingir, você aflige a criatura com uma doença, de sua escolha, entre qualquer um das descritas abaixo.
No final de cada turno do alvo, ele deve realizar um teste de resistência de Constituição.
Após obter três falhas nesses testes de resistência, o efeito da doença permanece pela duração e a criatura para de fazer testes de resistência.
Após obter três sucessos nesses testes de resistência, a criatura se recupera da doença e a magia termina.
Já que essa magia induz uma doença natural no alvo, qualquer efeito que remova uma doença, ou de outra forma, melhore os efeitos de uma doença, se aplicam a ela.

Ardência Mental: A mente da criatura fica febril.
A criatura tem desvantagem em testes de Inteligência, testes de resistência de Inteligência e a criatura age como se estivesse sob efeito da magia confusão durante um combate.

Enjoo Cegante: A dor se agarra a mente da criatura e seus olhos ficam branco-leitosos.
A criatura tem desvantagem em testes de Sabedoria e testes de resistência de Sabedoria e está cega.

Febre do Esgoto: Uma febre voraz se espalha pelo corpo da criatura.
A criatura tem desvantagem em testes de Força, testes de resistência de Força e jogadas de ataque que usem Força.

Necrose da Carne: A carne da criatura se decompõe.
A criatura tem desvantagem em testes de Carisma e vulnerabilidade a todos os danos.

Perdição Pegajosa: A criatura começa a sangrar incontrolavelmente.
A criatura tem desvantagem em testes de Constituição e testes de resistência de Constituição. Além disso, sempre que a criatura sofrer dano, ela ficará atordoada até o fim do seu próximo turno.

Tremedeira: A criatura é acometida por espasmos.
A criatura tem desvantagem em testes de Destreza, testes de resistência de Destreza e jogadas de ataque que usem Destreza.''',},

{'carta':'reis_ouros','nome':'Aura da Vida',
'magia':''' 4      1 ação     (raio de 9m)        V       Concentração, até 10 minutos

A energia que preserva a vida irradia de você em uma aura com um raio de 9 metros.
Até que a magia termine, a aura se move com você, centrada em você.
Cada criatura não hostil na aura (incluindo você) tem resistência a dano necrótico e seu máximo de pontos de vida não pode ser reduzido.
Além disso, uma criatura viva não hostil recupera 1 ponto de vida quando começa seu turno na aura com 0 pontos de vida.''',},


#Magias de Paus
{'carta':'as_paus','nome':'Imolação',
'magia':'''Evocação 5       1 Ação      27m     V       Concentração, 1 minuto

Chamas envolvem uma criatura que você pode ver dentro do alcance.
O alvo deve fazer um teste de resistência de Destreza.
Ele sofre 8d6 de dano de fogo se falhar na resistência, ou metade desse dano se obtiver sucesso.
Em uma falha na resistência, o alvo também queima pela duração do feitiço.
O alvo em chamas emite luz brilhante em um raio de 9 metros e penumbra por mais 9 metros.
No final de cada um de seus turnos, o alvo repete o teste de resistência.
Ele sofre 4d6 de dano de fogo se falhar na resistência, e a magia termina com sucesso.
Essas chamas mágicas não podem ser extintas por meios não mágicos.
Se o dano desta magia matar um alvo, o alvo é transformado em cinzas.''',},

{'carta':'dois_paus','nome':'Orbe Cromático',
'magia':'''evocação 1       1 ação      27 metros       V, S, M     instantânea

Material: um diamante valendo, no mínimo, 50 po.

Você arremessa uma esfera de energia de 12 centímetros de diâmetro numa criatura que você possa ver dentro do alcance.
Você escolhe ácido, frio, fogo, elétrico, veneno ou trovejante para o tipo de orbe que você cria e, então, realiza um ataque à distância com magia.
Se o ataque atingir, a criatura sofre 3d8 de dano do tipo escolhido.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d8 para cada nível do espaço acima do 1°.''',},

{'carta':'tres_paus','nome':'Armadura de Mago',
'magia':'''abjuração 1      1 ação      toque       V, S, M     8 horas

Material: um pedaço de couro curado.

Você toca uma criatura voluntária que não esteja vestindo armadura e uma energia mágica protetora a envolve até a magia acabar.
A CA base do alvo se torna 13 + o modificador de Destreza dele.
A magia acaba se o alvo colocar uma armadura ou se você dissipa-la usando uma ação.''',},

{'carta':'quatro_paus','nome':'Maldito',
'magia':'''Encantamento 1       1 Ação      9m      V, S, M         Cocentração, 1 minuto

Até três criaturas de sua escolha que você possa ver dentro do alcance devem fazer testes de resistência de Carisma.
Sempre que um alvo que falhar neste teste de resistência fizer uma jogada de ataque ou teste de resistência antes que a magia termine, o alvo deve rolar um d4 e subtrair o número rolado da jogada de ataque ou teste de resistência.

Em Níveis Superiores. Quando você conjura esta magia usando um espaço de magia de 2º nível ou superior, você pode mirar uma criatura adicional para cada nível de espaço acima do 1º.''',},

{'carta':'cinco_paus','nome':'Spray de Cor',
'magia':'''Ilusão 1     1 Ação      Próprio(4,5m)       V, S, M        1 rodada

Material:   uma pitada de pó ou areia de cor vermelha, amarela e azul

Uma deslumbrante variedade de luzes coloridas e piscantes brota de sua mão.
Jogue 6d10; o total é quantos pontos de vida de criaturas esta magia pode afetar.
Criaturas em um cone de 15 pés originado de você são afetados em ordem crescente de seus pontos de vida atuais (ignorando criaturas inconscientes e criaturas que não podem ver).

Começando com a criatura que tem os pontos de vida atuais mais baixos, cada criatura afetada por esta magia fica cega até o final do seu próximo turno.
Subtraia os pontos de vida de cada criatura do total antes de passar para a criatura com os próximos pontos de vida mais baixos. Os pontos de vida de uma criatura devem ser iguais ou menores que o total restante para que aquela criatura seja afetada.

Em Níveis Superiores. Quando você conjurar esta magia usando um espaço de magia de 2º nível ou superior, role 2d10 adicionais para cada nível do espaço acima do 1º.''',},

{'carta':'seis_paus','nome':'Mãos Ardentes',
'magia':'''evocação 1       1 ação      pessoal     V, S        instantânea

Enquanto você mantiver suas mãos com os polegares juntos e os dedos abertos, uma fino leque de chamas emerge das pontas dos seus dedos erguidos.
Cada criatura num cone de 4,5 metros deve realizar um teste de resistência de Destreza. Uma criatura sofre 3d6 de dano de fogo se falhar no teste, ou metade desse dano se obtiver sucesso.

O fogo incendeia qualquer objeto inflamável na área que não esteja sendo vestido ou carregado.

Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1°.''',},

{'carta':'sete_paus','nome':'Míssil Mágico',
'magia':'''evocação 1       1 ação      36 metros       V, S        instantânea

Você cria três dardos brilhantes de energia mística. Cada dardo atinge uma criatura, à sua escolha, que você possa ver, dentro do alcance.
Um dardo causa 1d4 + 1 de dano de energia ao alvo. Todos os dardos atingem simultaneamente e você pode direciona-los para atingir uma criatura ou várias.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, a magia cria um dardo adicional para cada nível do espaço acima do 1°.''',},

{'carta':'oito_paus','nome':'Queimador de Agnazzar',
'magia':'''Evocação 2       1 Ação      9m      V, S, M     Instantâneo

Materia: escama de um dragão vermelho

Uma linha de chamas rugindo de 9 metros de comprimento e 1,5 metros de largura emana de você na direção que você escolher.
Cada criatura na linha deve fazer um teste de resistência de Destreza.
Uma criatura sofre 3d8 de dano de fogo se falhar na resistência, ou metade desse dano se obtiver sucesso.

Em Níveis Superiores. Quando você conjura esta magia usando um espaço de magia de 3º nível ou superior, o dano aumenta em 1d8 para cada nível do espaço acima do 2º.''',},

{'carta':'nove_paus','nome':'Imagem Espelhada',
'magia':'''ilusão 2     1 ação      pessoal     V, S        1 minuto

Três duplicatas ilusórias de você aparecem no seu espaço.
Até a magia acabar, as duplicatas se movem com você e copiam as suas ações, trocando de posição, tornando impossível rastrear qual imagem é real.
Você pode usar sua ação para dissipar as duplicatas ilusórias.
Cada vez que uma criatura mirar você com um ataque enquanto a magia durar, role um d20 para determinar se o ataque, em vez de você, mira uma das suas duplicatas.

Se você tiver três duplicatas, você deve rolar um 6 ou maior para mudar o alvo do ataque para uma duplicata.
Com duas duplicatas, você deve rolar um 8 ou maior.
Com uma duplicata, você deve rolar um 11 ou maior.

A CA de uma duplicata é igual a 10 + seu modificador de Destreza.
Se um ataque atingir uma duplicata, ela é destruída.
Uma duplicata só pode ser destruída por um ataque que a atinja.
Ela ignora todos os outros danos e efeitos.
A magia acaba quando todas as três duplicatas forem destruídas.

Uma criatura não pode ser afetada por essa magia se não puder enxergar, se ela contar com outros sentidos além da visão, como percepção às cegas, ou se ela puder perceber ilusões como falsas, como com visão verdadeira.''',},

{'carta':'dez_paus','nome':'Ampliar/Reduzir',
'magia':'''transmutação 2       1 ação      9 metros        V, S, M     até 1 minuto

Material: um pouco de pó de ferro.

Você faz com que uma criatura ou um objeto que você possa ver dentro do alcance, fique maior ou menor, pela duração.
Escolha entre uma criatura ou um objeto que não esteja sendo carregado nem vestido.
Se o alvo for involuntário, ele deve realizar um teste de resistência de Constituição.
Se for bem sucedido, a magia não surte efeito.

Se o alvo for uma criatura, tudo que ele esteja vestindo ou carregando muda e tamanho com ela.
Qualquer item largado por uma criatura afetada, retorna ao seu tamanho natural.

Aumentar: O tamanho do alvo dobra em todas as dimensões e seu peso é multiplicado por oito.
Esse aumento eleva seu tamanho em uma categoria – de Médio para Grande, por exemplo.
Se não houver espaço suficiente para que o alvo dobre de tamanho, a criatura ou objeto alcança o tamanho máximo possível no espaço disponível.
Até o fim da magia, o alvo também tem vantagem em testes de Força e testes de resistência de Força.
O tamanho das armas do alvo crescem para se adequar ao seu novo tamanho.
Quando essas armas são ampliadas, os ataques do alvo com elas causam 1d4 de dano extra.

Reduzir: O tamanho do alvo é reduzido à metade em todas as dimensões e seu peso é reduzido a um oitavo do normal.
Essa redução diminui o tamanho do alvo em uma categoria – de Médio para Pequeno, por exemplo.
Até o fim da magia, o alvo tem desvantagem em testes de Força e testes de resistência de Força.
O tamanho das armas do alvo diminuem para se adequar ao seu novo tamanho.
Quando essas armas são reduzidas, os ataques do alvo com elas causam 1d4 de dano a menos (isso não pode reduzir o dano a menos de 1).''',},

{'carta':'onze_paus','nome':'Bola de Fogo',
'magia':'''evocação 3       1 ação      45 metros       V, S, M     instantânea

Material: uma minúscula bola de guano de morcego e enxofre.

Um veio brilhante lampeja na ponta do seu dedo em direção a um ponto que você escolher, dentro do alcance, e então eclode com um estampido baixo, explodindo em chamas.
Cada criatura em uma esfera de 6 metros de raio, centrada no ponto, deve realizar um teste de resistência de Destreza.
Um alvo sofre 8d6 de dano de fogo se falhar na resistência, ou metade desse dano se obtiver sucesso.
O fogo se espalha, dobrando esquinas.
Ele incendeia objetos inflamáveis na área que não estejam sendo vestidos ou carregados.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 4° nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 3°.''',},

{'carta':'dama_paus','nome':'Muralha de Fogo',
'magia':'''evocação 4       1 ação      36 metros       V, S, M     até 1 minuto

Material: um pequeno pedaço de fósforo.

Você cria uma muralha de fogo numa superfície sólida dentro do alcance.
Você pode fazer uma muralha de até 18 metros de comprimento, 6 metros de altura e 30 centímetros de espessura ou uma muralha anelar de até 6 metros de diâmetro, 6 metros de altura e 30 centímetros de espessura.
A muralha é opaca e permanece pela duração.
Quando a muralha aparece, cada criatura dentro da área dela deve realizar um teste de resistência de Destreza.
Se falhar na resistência, uma criatura sofrerá 5d8 de dano, ou metade desse dano se passar na resistência.

Um lado da muralha, escolhido por você no momento da conjuração da magia, causa 5d8 de dano de fogo a cada criatura que terminar o turno dela a até 3 metros desse lado ou dentro da muralha.
Uma criatura sofre o mesmo dano quando entra na muralha pela primeira vez num turno ou termina seu turno nela.
O outro lado da muralha não causa dano algum.

Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 5° nível ou superior, o dano aumenta em 1d8 para cada nível do espaço acima do 4°.''',},

{'carta':'valete_paus','nome':'Velocidade',
'magia':'''transmutação 3       1 ação      18 metros       V, S, M     até 1 minuto

Material: uma raspa de raiz de alcaçuz.

Escolha uma criatura voluntária que você possa ver, dentro do alcance.
Até a magia acabar, o deslocamento do alvo é dobrado, ele ganha +2 de bônus na CA, ele tem vantagem em testes de resistência de Destreza e ganha uma ação adicional em cada um dos turnos dele.
A ação pode ser usada apenas para realizar as ações de Atacar (um ataque com arma, apenas), Disparada, Desengajar, Esconder ou Usar um Objeto.

Quando a magia acabar, o alvo não poderá se mover ou realizar ações até depois do seu próximo turno, à medida que uma onda de letargia toma conta dele.''',},

{'carta':'reis_paus','nome':'Cão Fiel',
'magia':'''Conjuração 4       1 ação      9 metros       V, S, M     8h

Material:  Um pequeno apito de prata, um pedaço de osso e um fio

Você conjura um cão de guarda fantasma em um espaço desocupado que você possa ver dentro do alcance, onde ele permanece pela duração, até você dispensá-lo como uma ação, ou até você se afastar mais de 30 metros dele.

O cão é invisível para todas as criaturas exceto você e não pode ser ferido.
Quando uma criatura pequena ou maior chega a 9 metros dela sem primeiro falar a senha que você especificou quando conjurou esta magia, o cão começa a latir alto.
O cão vê criaturas invisíveis e pode ver o Plano Etéreo.
Ignora as ilusões.

No início de cada um de seus turnos, o cão tenta morder uma criatura a até 1,5 metro dele que seja hostil a você. O bônus de ataque do cão é igual ao seu modificador de habilidade de conjuração + seu bônus de proficiência. Em um acerto, causa 4d8 de dano perfurante.''',},


#Magias de Espada
{'carta':'as_espada','nome':'Golpe de Vento de Aço',
 'magia':'''Conjuração 5  1 ação        9 metros    S, M Instantâneo
 
Material: uma arma corpo a corpo valendo pelo menos 1 pp

Você floresce a arma usada no lançamento e depois desaparece para atacar como o vento.
Escolha até cinco criaturas que você possa ver dentro do alcance.
Faça um ataque mágico corpo a corpo contra cada alvo.
Em um acerto, o alvo sofre 6d10 de dano de força.

Você pode então se teletransportar para um espaço desocupado que você possa ver a até 1,5 metro de um dos alvos que você acertou ou errou.
 ''',},

{'carta':'dois_espada','nome':'Golpe Trovejante',
'magia':'''evocação 1       1 ação bônus        pessoal     V       até 1 minuto

Da primeira vez que você atingir um ataque corpo-a-corpo com arma enquanto essa magia durar,
sua arma é rodeada por trovões que são audíveis a até 90 metros de você e o ataque causa 2d6 de dano trovejante extra no alvo.
Além disso, se o alvo for uma criatura, ele deve ser bem sucedido num teste de resistência de Força ou será empurrado 3 metros para longe de você e cairá no chão.''',},

{'carta':'tres_espada','nome':'Escudo Arcano',
'magia':'''Abjuração 1      1 reação        pessoal     V, S        1 rodada
Reação que você faz quando é atingido por um ataque ou alvo da magia mísseis mágicos.

Uma barreira de energia invisível aparece e protege você.
Até o início do seu próximo turno, você recebe +5 de bônus na CA, incluindo contra o ataque que desencadeou a magia, e você não sofre dano de mísseis mágicos.''',},

{'carta':'quatro_espada','nome':'Favor Divino',
'magia':'''evocação 1       1 ação bônus        pessoal     V, S        até 1 minuto

Sua oração fortalece você com radiação divina.
Até o fim da magia, seus ataques com arma causam 1d4 de dano radiante extra ao atingirem.
''',},

{'carta':'cinco_espada','nome':'Nuvem de Névoa',
'magia':'''conjuração 1     1 ação      36 metros       V, S        até 1 hora

Você cria uma esfera de 6 metros de raio de névoa, centrada num ponto, dentro do alcance.
A esfera se espalha, dobrando esquinas, e a área dela é de escuridão densa.
Ela permanece pela duração ou até um vento moderado ou mais rápido (pelo menos 15 quilômetros por hora) dispersa-la.

Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o raio da névoa aumenta em 6 metros para cada nível do espaço acima do 1°.''',},

{'carta':'seis_espada','nome':'Onda de Trovão',
'magia':'''evocação 1       1 ação      pessoal     V, S        instantânea

Uma onda de força trovejante varre tudo a partir de você.
Cada criatura num cubo de 4,5 metros originado em você, deve realizar um teste de resistência de Constituição.
Se falhar na resistência, uma criatura sofrerá 2d8 de dano trovejante e será empurrada 3 metros para longe de você.
Se obtive sucesso na resistência, a criatura sofrerá metade desse dano e não será empurrada.
Além disso, objetos soltos que estiverem completamente dentro da área de efeito serão automaticamente empurrados 3 metros para longe de você pelo efeito da magia e a magia emitirá um ressonante barulho de trovão audível a até 90 metros.

Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d8 para cada nível acima do 1°.''',},

{'carta':'sete_espada','nome':'Raio de Bruxa',
'magia':'''evocação 1       1 ação      9 metros        V, S, M     até 1 minuto
Material: um galho de uma árvore que tenha sido atingida por um relâmpago.

Um raio crepitante de energia azul é arremessado em uma criatura dentro do alcance, formando um arco elétrico contínuo entre você e o alvo.
Faça um ataque à distância com magia contra a criatura.
Se atingir, o alvo sofrerá 1d12 de dano elétrico e, em cada um dos seus turnos, pela duração, você pode usar sua ação para causar 1d12 de dano elétrico ao alvo, automaticamente.
A magia acaba se você usar sua ação para fazer qualquer outra coisa.
A magia também acaba se o alvo estiver fora do alcance da magia ou se você tiver cobertura total para ele.

Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano inicial aumenta em 1d12 para cada nível do espaço acima do 1°.''',},

{'carta':'oito_espada','nome':'Despedaçar',
'magia':'''evocação 2       1 ação      18 metros       V, S, M     instantânea

Material: uma lasca de mica.

Um alto som estridente, dolorosamente intenso, emerge de um ponto, à sua escolha, dentro do alcance.
Cada criatura, numa esfera de 3 metros de raio, centrada no ponto deve fazer um teste de resistência de Constituição.
Uma criatura sofre 3d8 de dano trovejante se falhar na resistência ou metade desse dano se obtiver sucesso.
Uma criatura feita de material inorgânico como pedra, cristal ou metal, tem desvantagem nesse teste de resistência.
Um objeto não-mágico que não esteja sendo vestido ou carregado, também sofre o dano, se estiver na área da magia.

Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de magia de 3° nível ou superior, o dano aumenta em 1d8 para cada nível do espaço acima do 2°.''',},

{'carta':'nove_espada','nome':'Borrão',
'magia':'''Ilusão 2     1 Ação      Pessoal     V       Concentração 1 minuto

Seu corpo fica borrado, mudando e oscilando para todos que podem vê-lo.
Pela duração, qualquer criatura tem desvantagem nas jogadas de ataque contra você.
Um atacante é imune a este efeito se não confiar na visão, como na visão às cegas , ou pode ver através de ilusões, como na visão da verdade .''',},

{'carta':'dez_espada','nome':'Vento Protetor',
'magia':'''Evocação 2       1 Ação       Próprio (6m)        V   Concentração 10 minutos

Um vento forte (32 quilômetros por hora) sopra ao seu redor em um raio de 3 metros e se move com você, permanecendo centrado em você.
O vento dura pela duração do feitiço.

O vento tem os seguintes efeitos:
Ele ensurdece você e outras criaturas em sua área.
Extingue chamas desprotegidas em sua área que sejam do tamanho de uma tocha ou menores.
Ele protege o vapor, gás e neblina que podem ser dispersos pelo vento forte.
A área é um terreno difícil para outras criaturas além de você.
As jogadas de ataque de armas de longo alcance têm desvantagem se os ataques passarem pelo vento ou contra o vento.''',},

{'carta':'onze_espada','nome':'Relâmpago',
'magia':'''evocação 3       1 ação      pessoal     V, S, M     instantânea

Material: um pouco de pelo e uma haste de âmbar, cristal ou vidro.

Um relâmpago forma uma linha de 30 metros de comprimento e 1,5 metro de largura que é disparado por você em uma direção, à sua escolha.
Cada criatura na linha deve realizar um teste de resistência de Destreza.
Uma criatura sofre 8d6 de dano elétrico se falhar na resistência ou metade desse dano se obtiver sucesso.
O relâmpago incendeia objetos inflamáveis na área que não estejam sendo vestidos ou carregados.

Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de magia de 4° nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 3°.''',},

{'carta':'dama_espada','nome':'Passo do Trovão',
'magia':'''Conjuração 3     1 ação      27m     V       Instantâneo

Você se teletransporta para um espaço desocupado que você possa ver dentro do alcance.
Imediatamente após você desaparecer, um estrondo trovejante soa, e cada criatura a até 3 metros do espaço que você deixou deve fazer um teste de resistência de Constituição, sofrendo 3d10 de dano trovejante se falhar na resistência, ou metade desse dano se obtiver sucesso.
O trovão pode ser ouvido a até 300 metros de distância.
Você pode trazer objetos desde que o peso deles não exceda o que você pode carregar.
Você também pode teletransportar uma criatura voluntária do seu tamanho ou menor que esteja carregando equipamentos até sua capacidade de carga.
A criatura deve estar a até 1,5 metro de você quando você conjurar esta magia, e deve haver um espaço desocupado a até 1,5 metro do seu espaço de destino para a criatura aparecer; caso contrário, a criatura é deixada para trás.

Em Níveis Superiores: Quando você conjura esta magia usando um espaço de magia de 4º nível ou superior, o dano aumenta em 1d10 para cada nível de espaço acima do 3º.
''',},

{'carta':'valete_espada','nome':'Golpe Atordoante',
'magia':'''evocação 4       1 ação bônus        pessoal     V       Concentração, até 1 minuto

A próxima vez que você atingir uma criatura com um ataque corpo a corpo com arma durante a duração desta magia, sua arma perfurará o corpo e a mente, e o ataque causará 4d6 de dano psíquico extra ao alvo.
O alvo deve fazer um teste de resistência de Sabedoria.
Em uma falha na resistência, ele tem desvantagem nas jogadas de ataque e testes de habilidade, e não pode realizar reações, até o final de seu próximo turno.''',},

{'carta':'reis_espada','nome':'Esfera da Tempestade',
'magia':'''Evocação 4       1 Ação      45m     V, S          Concentração 1 minuto
Uma esfera de 6 metros de raio de ar rodopiante surge centrada em um ponto que você escolher dentro do alcance.
A esfera permanece pela duração do feitiço.
Cada criatura na esfera quando ela aparecer ou que terminar seu turno lá deve ser bem sucedida em um teste de resistência de Força ou sofrerá 2d6 de dano de concussão.
O espaço da esfera é um terreno difícil.
Até que a magia termine, você pode usar uma ação bônus em cada um de seus turnos para fazer com que um raio salte do centro da esfera em direção a uma criatura à sua escolha a até 18 metros do centro.
Faça um ataque de magia à distância.
Você tem vantagem na jogada de ataque se o alvo estiver na esfera.
Em um acerto, o alvo sofre 4d6 de dano de raio.
Criaturas a até 9 metros da esfera têm desvantagem em testes de Sabedoria ( Percepção ) feitos para ouvir.

Em Níveis Superiores: Quando você conjura esta magia usando um espaço de magia de 5º nível ou superior, o dano aumenta para cada um de seus efeitos em 1d6 para cada nível de espaço acima do 4º.''',},]

def magia(carta):
    for p, c in enumerate(arcanosmen):
        if carta in c['carta']:
            if carta in copas[:]:
                print('\n')
                print(f'\033[1;36m[{arcanosmen[p]["nome"]}]\033[0;0m',end='     ')
                print(f'\033[1;36m[{arcanosmen[p]["carta"]}]\033[0;0m')
                print('\n')
                print(f'\033[1;36m[{arcanosmen[p]["magia"]}]\033[0;0m',end=' ')
            
            if carta in espada[:]:
                print('\n')
                print(f'\033[1;32m[{arcanosmen[p]["nome"]}]\033[0;0m',end='     ')
                print(f'\033[1;32m[{arcanosmen[p]["carta"]}]\033[0;0m')
                print('\n')
                print(f'\033[1;32m[{arcanosmen[p]["magia"]}]\033[0;0m',end=' ')
            
            if carta in ouros[:]:
                print('\n')
                print(f'\033[1;35m[{arcanosmen[p]["nome"]}]\033[0;0m',end='     ')
                print(f'\033[1;35m[{arcanosmen[p]["carta"]}]\033[0;0m')
                print('\n')
                print(f'\033[1;35m[{arcanosmen[p]["magia"]}]\033[0;0m',end=' ')
            
            if carta in paus[:]:
                print('\n')
                print(f'\033[1;31m[{arcanosmen[p]["nome"]}]\033[0;0m',end='     ')
                print(f'\033[1;31m[{arcanosmen[p]["carta"]}]\033[0;0m') 
                print('\n')
                print(f'\033[1;31m[{arcanosmen[p]["magia"]}]\033[0;0m',end=' ')     
           

