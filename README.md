# EbookReader
Repositório referenciado no TCC "Atribuição de Falas a Personagens e Geração de Diferentes Vozes para Leitura de Ebooks Utilizando Aprendizado Estruturado Profundo"

## Referências

Foram utilizados os códigos disponibilizados nos seguintes repositórios:

1. [r9y9/Deepvoice 3](https://github.com/r9y9/deepvoice3_pytorch): Deepvoice3_pytorch.
2. [schmrlng/RNN Quote Attribution](https://github.com/schmrlng/RNNQuoteAttribution): Quote attribution through recurrent neural networks.

## Pré-Requisitos

- Placa de vídeo Nvidia com suporte a Cuda 8+
- Distro Linux com Bash (Testado com Arch Linux)
- Driver proprietário Nvdia e Cuda 8+ instalados
- Pacote Anaconda instalado
- Pacote Wget instalado

## Instalação

- Clone esse repositório para uma pasta local:
```
git clone https://github.com/chapykiller/EbookReader.git
```
- Abra a pasta criada e rode o shell script de setup:
```
cd EbookReader
sh setup.sh
```
Durante a execução do script de setup todos os pacotes necessários serão baixados, os ambientes virtuais necessários serão criados utilizando o Anaconda e os arquivos necessários para execução também serão baixados. Isso pode demorar bastante tempo dependendo da velocidade da internet.


## Execução

- Configure as falas utilizadas como entrada
- Execute o shell script de run:
```
sh run.sh
```
