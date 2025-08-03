# Sistema de Pedidos - Prova Técnica

Prova técnica para vaga de Desenvolvedor Pleno.

## Tecnologias

- **FastAPI** para backend assíncrono com validação via Pydantic
- **MongoDB** como banco de dados NoSQL
- **Jinja2** para renderização server-side
- **HTMX** para dinamismo sem recarregamento de página
- **Bulma CSS** para estilização responsiva
- **Docker + Docker Compose** para ambiente isolado e fácil deploy

## Como rodar

1. Criar Ambiente Virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

2. Ativar Ambiente Virtual
```bash
source venv/bin/activate
```

3. Instalar Dependências

```bash
pip install -r requirements.txt
```

4. Configurar Variáveis de Ambiente

Copie o arquivo `.env.example` e renomeie para `.env`:

5. Rodar

```bash
uvicorn main:app --reload
```

Por padrão, ele sobe na porta 8000.

---

Via Docker

```bash
docker-compose up --build
```

## Arquitetura

Este projeto segue os princípios da **Clean Architecture**, com separação clara entre as responsabilidades de cada camada:

### 🔹 Camadas

- `routes/` – Controladores
- `usecases/` – Casos de uso que encapsulam as regras de negócio
- `repositories/` – Abstração e implementação do acesso ao banco de dados (MongoDB neste caso).
- `datasources/` – Configuração da fonte de dados (cliente MongoDB).