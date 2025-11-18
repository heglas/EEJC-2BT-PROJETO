# Tutorial para Acessar o Branch do Projeto no GitHub

Este tutorial irá ajudar cada aluno a encontrar e acessar seu branch específico no repositório GitHub do projeto "EEJC-2BT-PROJETO".

## Passo 1: Clonar o Repositório

1. Abra o terminal no seu computador.
2. Execute o comando para clonar o repositório:

```
git clone https://github.com/heglas/EEJC-2BT-PROJETO.git
```

3. Navegue até a pasta do projeto:

```
cd EEJC-2BT-PROJETO
```

## Passo 2: Listar os Branches Disponíveis

Para ver todos os branches existentes no repositório remoto, execute:

```
git branch -r
```

Você verá uma lista com os branches, incluindo o seu.

## Passo 3: Acessar o Branch do Seu Grupo

Para mudar para o branch do seu grupo, use o seguinte comando, substituindo `<nome-do-branch>` pelo nome do seu branch:

```
git checkout <nome-do-branch>
```

Exemplo para o grupo de cadastro de livros:

```
git checkout modulo-cadastro-remocao-livros
```

## Passo 4: Trabalhar no Branch

Agora você está no branch correto e pode adicionar, editar, e commitar seus arquivos normalmente.

## Passo 5: Enviar Alterações para o Repositório Remoto

Depois de fazer suas alterações, envie-as com:

```
git add .
git commit -m "Mensagem descritiva das alterações"
git push origin <nome-do-branch>
```

## Passo 6: Enviar Pull Request

Para integrar suas alterações na branch principal, abra o GitHub e crie um pull request do seu branch para o branch `main`.

---

Se precisar de ajuda, entre em contato com o responsável do projeto.
