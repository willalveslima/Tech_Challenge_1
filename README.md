
# Tech Challenge 1 - FIAP

Este projeto é a implementação do Tech Challenge do curso de pós-graduação da FIAP. O objetivo é a criação de uma API pública para consulta de dados do site da Embrapa nas seguintes abas:

- Produção
- Processamento
- Comercialização
- Importação
- Exportação

A API servirá para alimentar uma base de dados que futuramente será usada para um modelo de Machine Learning.

## Objetivos

- Criar uma Rest API em Python que faça a consulta no site da Embrapa.
- Documentar a API.
- (Opcional) Implementar um método de autenticação (por exemplo, JWT).
- Criar um plano para o deploy da API, desenhando a arquitetura do projeto desde a ingestão até a alimentação do modelo. Não é necessário elaborar um modelo de ML, mas é preciso escolher um cenário interessante em que a API possa ser utilizada.
- Fazer um MVP realizando o deploy com um link compartilhável e um repositório no GitHub.

## Desenvolvimento do Projeto

1. **API em Python**: API implementada utilizando o frameworks FastAPI.
2. **Documentação**: Utilizado a ferramenta Swagger embutida no framework Fastapi.
3. **Autenticação**: Implementada autenticação JWT.
4. **Plano de Deploy**: Desenho da arquitetura do projeto, incluindo serviços de cloud, CI/CD, etc.
5. **MVP**: Deploy da API com um link compartilhável  e repositório no GitHub.

## Documentação do API

A Documentação da API é disponiblilizada após a execução do projeto:
http://url_de_execução/docs

ex: <http://127.0.0.1:8000/docs>

## Executar Localmente

```bash
  git clone https://github.com/willalveslima/Tech_Challenge_1.git
```

## Acessar diretório do projeto

```bash
  cd Tech_Challenge_1
```

## Criar o ambiente virtural

```bash
  pythom -m venv .venv
  source .venv/bin/activate
```

## Instalar dependências

```bash
  pip install -r requirements.txt
```

## Como executar

```bash
   python .\main.py
```

A pagina de documentação estará disponível em <http://127.0.0.1:8000/docs>

## Exemplo de consumo da API

O script `consumidor_api.py` demonstra a forma de consumo da API.

## Como Contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato com [w.alves.lima@gmail.com].
