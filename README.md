<h1 align="center">C Remédios</h1>

<p align="center">
	<a href="#sobre">Sobre</a> &nbsp;|&nbsp;
	<a href="#porque">Por Que</a> &nbsp;|&nbsp;
	<a href="#tecnologias">Tecnologias</a> &nbsp;|&nbsp;
	<a href="#funcionalidades">Funcionalidades</a> &nbsp;|&nbsp;
	<a href="#instalando">Instalando</a> &nbsp;|&nbsp;
	<a href="#rodando">Rodando</a> &nbsp;|&nbsp;
	<a href="#autor">Autor</a> &nbsp;|&nbsp;
	<a href="#license">Licença</a>
</p>

<h6 align="center"> 
	Se você quiser visualizar as imagens do aplicativo, clique <a href="github/images/README.md">aqui</a>.
</h6>

<h3 id="sobre">:information_source: Sobre</h3>

> Este projeto foi desenvolvido utilizando o Django como framework back-end e o Materialize como framework front-end. 

A ideia é:

_"Criar um Sistema de Remédios onde o mesmo tenha um design simples e belo, com intuito de promover o aprendizado e gerar um projeto completo utilizando o Django framework."_

--------------------------------------------------------------------------------------

<h3 id="porque">:question: Por Que</h3>

Este projeto faz parte do meu portfólio pessoal, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer funcionalidade&melhoria que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

<h3 id="tecnologias">:rocket: Tecnologias</h3>

As seguintes ferramentas foram usadas na construção do projeto:

- [Django Framework](https://www.djangoproject.com/)
- [Boostrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

--------------------------------------------------------------------------------------

<h3 id="funcionalidades">:sparkles: Funcionalidades</h3>

:construction: - As Funcionalidades serão construída em breve...

--------------------------------------------------------------------------------------

<h3 id="instalando">:computer: Instalando o Projeto</h3>

**Clonando o Repositório**

```
git clone git@github.com:LucasSantus/c-remedios.git

cd c-remedios
```

#### Preparando o Projeto

Com o terminal aberto, digite no terminal:

**Windows**

> **Observação:** Foi utilizado o Windows(versão 10), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!
 
```
make install-windows
```

**Linux**

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

```
make install-linux
```

**Iniciando Ambiente Virtual**

<h3 id="rodando">:zap: Rodando</h3>

Inicie a virtual env:

**Windows**

```
env\Scripts\activate;
```

**Linux**

```
source env/bin/activate
```

**Rodar script's**
```
python manage.py shell

exec(open('apps/scripts/main.py').read())

exit()
```
**Rodando o Projeto**

```
python manage.py runserver
```

**Criando Super Usuário**

```
python manage.py createsuperuser
```
**Acessando o Projeto**

para visualizar o projeto: http://127.0.0.1:8000/


**Acessando o Admin**

Com o projeto rodando, adicione o 'admin/' dps da URL:

http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------------

<h3 id="autor">:bust_in_silhouette: Autor(es)</h3>

<table>
	<tr>
		<td>
			<div> 
				<a href="https://github.com/LucasSantus">
					<img style="border-radius: 50%;" src="https://github.com/LucasSantus.png" width="100px;" alt=""/>
					<br />
					Lucas Santus
				</a>
			</div>
		</td>
		<td>
			<div> 
				<a href="https://github.com/michel110299">
					<img style="border-radius: 50%;" src="https://github.com/michel110299.png" width="100px;" alt=""/>
					<br />
					Michel Lemes
				</a>
			</div>
		</td>
	</tr>
</table>
<br />
Feito com ❤️ por Lucas Santus!<br />
Obrigado por visitar e boa codificação!<br />

--------------------------------------------------------------------------------------

<h3 id="license">:memo: License</h3>

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/c-remedios/blob/master/LICENSE) para melhores detalhes.
