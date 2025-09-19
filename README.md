<p align="center">
  <picture>
    <img src="encrypt.gif" width="25%">
  </picture>
</p>

## 📚 Sobre

Este repositório contém a implementação do projeto final para a disciplina de **Segurança Computacional (CIC0201)** da **Universidade de Brasília (UnB)**. O trabalho, desenvolvido durante meu 6º semestre em Ciência da Computação, foca na criação de ferramentas criptográficas e na exploração de seus princípios fundamentais.

O projeto é dividido em duas partes principais: uma para **criptografia simétrica** e outra para **criptografia assimétrica com assinatura digital**. Através da implementação dos algoritmos **AES** e **RSA**, pude aprofundar meu entendimento sobre como a teoria por trás da segurança de dados se aplica na prática, desde a cifração de blocos até a geração de chaves e verificação de assinaturas digitais.

Essa experiência foi crucial para solidificar o conhecimento sobre temas como modos de operação, integridade de dados e autenticação, demonstrando o poder dessas ferramentas para proteger informações em um ambiente digital.

## 📌 Funcionalidades

### Criptografia Simétrica (AES-CTR/GCM)

- **Cifra de Bloco AES:** Implementação da cifra de bloco AES com chave e bloco de 128 bits.
- **Modo de Operação CTR:** Utilização do modo `Counter (CTR)` para cifrar e decifrar arquivos de qualquer tamanho.
- **Modo GCM Autenticado:** Implementação extra do modo `Galois/Counter Mode (GCM)` para garantir a autenticidade e integridade dos dados.
- **Testes Visuais:** Cifração de uma imagem (`selfie.jpg`) com diferentes números de rodadas do AES para demonstrar o efeito do algoritmo.

### Criptografia Assimétrica e Assinatura Digital (RSA)

- **Geração de Chaves RSA:** Criação de chaves públicas e privadas com primos de 1024 bits ou mais.
- **Cifração/Decifração RSA:** Implementação dos processos assimétricos de cifração e decifração.
- **Assinatura Digital:** Cálculo de `hash (SHA-3)` e criação de uma assinatura digital para um documento.
- **Verificação de Assinatura:** Processo de verificação de documentos assinados para autenticidade.

## 🛠 Feito Com

<p align="left">
  <img src="https://skillicons.dev/icons?i=py,aes,rsa,sha" />
</p>

- **Linguagem:** Python
- **Algoritmos:** AES, RSA, SHA-3
- **Bibliotecas:** `hashlib`, `PIL (Pillow)`

## 👨‍💻 Como Rodar

### Pré-requisitos

Certifique-se de que você tem o **Python 3** instalado.

### Instalação de Dependências

Instale as bibliotecas necessárias usando `pip`:

```bash
pip install Pillow
````

```bash
pip install cryptography
```

*(As bibliotecas `hashlib` e `os` já vêm instaladas com o Python padrão.)*

### Instruções de Uso

Os scripts são modulares e podem ser executados separadamente. Os arquivos necessários para os testes estão nas pastas `AES/arquivos/` e `RSA/arquivos/`.

Exemplo de execução dos scripts de testes:

```bash
python AES/aes_test.py
```

```bash
python RSA/rsa_test.py
```

## 👥 Autor

Este projeto foi desenvolvido por:

  - **Daniel Luz** — [GitHub](https://github.com/dancpluz)

## 🤝 Contribuições / Agradecimentos

Este projeto foi realizado para a disciplina de **Segurança Computacional** no Departamento de Ciência da Computação da **Universidade de Brasília (UnB)**.

  - **Relatório Técnico:** O relatório completo do trabalho, com toda a fundamentação teórica e detalhes da implementação, pode ser acessado em: [https://www.overleaf.com/read/bfchdyydqrmv\#dbb63d](https://www.overleaf.com/read/bfchdyydqrmv#dbb63d).

## ⚠ Status

Este trabalho está completo para fins acadêmicos.

<details>
<summary>Clique para ver a lista</summary>

  - [x] Implementação da cifra AES (128 bits).
  - [x] Implementação do modo de operação CTR.
  - [x] Implementação da cifra assimétrica RSA (1024+ bits).
  - [x] Implementação de Assinaturas Digitais.
  - [x] Geração e verificação de hashes SHA-3.

</details>
