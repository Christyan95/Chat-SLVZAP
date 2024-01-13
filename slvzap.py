# Framework
    # # Django
    # # Flask
    # # Flet
        # # pip install flet

# PASSO A PASSO
    # # Titulo SLVZAP
    # # Botao de iniciar o chat
    # # Popup
        # # Bem vindo ao SVZAP
        # # Escreva seu nome
        # # Entrar no chat
    # # Chat
        # # Christyan entrou no chat
        # # Mensagens do usuario
    # # Campo para enviar mensagem
    # # Botao de enviar



import flet as ft

def main(pagina) : 
    titulo = ft.Text("SLV ZAP")
    
    nome_usuario = ft.TextField(label="Escreva seu nome")

    msg = ft.TextField(label="Escreva sua mensagem")

    chat = ft.Column()



    # #
    def enviar_msg_tunel(informacoes) :
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    pagina.pubsub.subscribe(enviar_msg_tunel)



    # #
    def enviar_msg(evento) :
        # Colocar o nome do usuario na msg
        texto_msg = f"{nome_usuario.value} : {msg.value}"

        pagina.pubsub.send_all(texto_msg)
 
        # Limpar o campo msg
        msg.value = ""
        pagina.update()
    bt_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg)



    # #
    def entrar_chat(evento) :
        # Feche o popup
        popup.open = False

        # Tire o botao iniciar chat da tela
        pagina.remove(bt_iniciar)

        # Adicionar o nosso chat
        pagina.add(chat)

        # Criar o campo de enviar msg e o botao enviar msg
        linha_msg = ft.Row(
            [msg, bt_enviar]
        )
        pagina.add(linha_msg)

        texto = f"{nome_usuario.value} entrou no chat"

        pagina.pubsub.send_all(texto)
        
        # Atualizar pagina
        pagina.update()
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem Vindo ao SLVZAP"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )



    # #
    def iniciar_chat(evento) :
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    bt_iniciar = ft.ElevatedButton("Iniciar o chat", on_click=iniciar_chat)
    
    pagina.add(titulo)
    pagina.add(bt_iniciar)
    


# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)