# PDF Splitter
## Descrição
 O PDF Splitter é uma ferramenta em Python desenvolvida para dividir arquivos PDF em partes menores com um tamanho máximo especificado. Cada parte dividida do PDF será salva em uma pasta específica, criada automaticamente com base no nome do arquivo PDF original. Isso é útil para gerenciar grandes arquivos PDF, facilitando seu armazenamento, envio ou compartilhamento.

## Funcionalidades
 - Divisão de PDFs por tamanho: O arquivo PDF original é dividido em vários arquivos menores, com o tamanho máximo definido pelo usuário.
 
 - Criação automática de pastas: Para cada arquivo PDF processado, uma pasta específica é criada para armazenar as partes divididas, organizada dentro de um diretório principal (./PDF-Destin).

 - Manutenção da integridade das páginas: As páginas dos PDFs são preservadas em ordem, garantindo que o conteúdo não seja corrompido ou perdido durante a divisão.
## Como Usar
### Pré-requisitos
 - Python 3.x instalado em seu sistema.

- Biblioteca PyPDF2 instalada. Você pode instalá-la via pip:

```bash
pip install PyPDF2
```
### Configuração
 1. Clonar o repositório: Clone o repositório para o seu ambiente local.
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio 
```

2. Ajuste o Caminho do PDF: No arquivo script.py, substitua "seu_arquivo.pdf" pelo caminho do arquivo PDF que você deseja dividir.

3. Altere o Tamanho Máximo (Opcional): Modifique o valor da variável max_size_mb para ajustar o tamanho máximo (em MB) de cada arquivo PDF gerado. O valor padrão é 10 MB.

## Executando o Script
- Navegue até o diretório onde o script está salvo.

```bash
cd caminho/para/pasta/do/script`
```
- Execute o script com o comando:

```bash
python script.py
```

### Resultado
> Após a execução, você encontrará uma nova pasta dentro do diretório ./PDF-Destin/, nomeada com base no nome do arquivo PDF original. Dentro dessa pasta, estarão os arquivos PDF divididos, nomeados sequencialmente (output_1.pdf, output_2.pdf, etc.).