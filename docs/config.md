# config.md

## Descrição:
Instruções para preparação do ambiente de desenvolvimento a ser utilizado neste _workshop_.

## Antes de começar:
Existem três casos possíveis para configuração:
1. Você já possui o Python instalado e também possui um editor de texto sem formatação ou IDE para Python
2. Você possui o Python instalado, mas não possui o editor de texto sem formatação
3. Você não possui nem o Python e nem o editor de texto sem formatação instalados

Caso você se encaixe no caso 1 você está pronto para rodar o _workshop_.

Caso você se encaixe no caso 2 você precisa de um editor de texto sem formatação (vale lembrar que o Bloco de Notas do Windows não serve para esse propósito). No Windows o instalador do Python inclui o IDLE, que é um editor simples mas apropriado para isso, então pode ser utilizado caso não queiras realizar qualquer instalação a mais.

Caso você se encaixe no caso 3 é necessária a instalação do Python. Por praticidade, essa instalação será feita com o uso do Anaconda, que é uma plataforma de _data science_ para Python que inclui diversos pacotes extras utéis em diversas aplicações, incluindo o Jupyter Notebook, que é onde foi feita a estrutura do curso. Se possível, recomendo a preparação do ambiente considerando esse cenário, mesmo que você se encaixe nos casos anteriores (a instalação do Anaconda não interfere em qualquer instalação anterior do Python no sistema).

Em todos os cenários recomendo a instalção de uma IDE para a edição do texto que seja compatível com o Python. A sugestão é o Visual Studio Code, por isso a instalação dele também será abordada aqui.

Todas as intruções assumem que seu sistema operacional é o Windows.

## Obtendo os itens necessários:
### Anaconda:
O Anaconda pode ser baixado [nesse link](https://www.anaconda.com/distribution/#windows). Certifique-se de baixar a versão para Python 3 ou superior, de acordo o seu tipo de máquina (se é 64-bit ou 32-bit. Você pode saber como verificar isso [aqui](https://www.lifewire.com/am-i-running-a-32-bit-or-64-bit-version-of-windows-2624475)). Instruções para instalação podem ser encontradas [aqui](https://docs.anaconda.com/anaconda/install/windows/). **Leia todo o texto das instruções de instalação antes de começar de fato a instalar.** Itens opcionais ou recomendados não são necessários, então execute-os apenas se você souber o que está fazendo. Se a instalação for bem sucedida o Anaconda Navigator está disponível no Iniciar do Windows. Abra-o para confirmar que a instalação foi concluída com sucesso.

Uma das vantagens ao usar o Anaconda é a possibilidade da criação de ambientes (_environments_), que funcionam como instalações separadas do Python, o que permite instalar um conjunto de pacotes sem interferir em outras instalações. Apesar de não ser necessário para esse _workshop_, é recomendada a criação de um ambiente próprio para ele. As instruções para criação do ambiente podem ser lidas na sessão _Managing Environments_ [aqui](https://docs.anaconda.com/anaconda/navigator/getting-started/#managing-environments).

### Visual Studio Code:
O instalador do Visual Studio Code pode ser baixado [aqui](https://code.visualstudio.com/#alt-downloads). Novamente, atente para a versão do seu sistema operacional (32 ou 64 bit). Tanto o _User Installer_ quanto o _System Installer_ são válidos. Instruções para instalação podem ser encontradas na sessão _Installation_ [aqui](https://code.visualstudio.com/docs/setup/windows#_installation).

Após instalar o Visual Studio Code é necessário instalar a extensão para compatibilidade com Python. Abra o Visual Studio Code e siga as intruções contidas na sessão _Browse for extensions_ [aqui](https://code.visualstudio.com/docs/editor/extension-gallery#_browse-for-extensions) para procurar a extensão _Python_ (provavelmente será a primeira, como no site).
