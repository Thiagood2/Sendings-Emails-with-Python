import smtplib
import ssl

def Main():
    smtp_port, smpt_server = PuertoServidor()
    email_r, m = Mensaje()
    Servidor(email_r,m,smtp_port,smpt_server)
    
    
    
def PuertoServidor():
    smtp_port = 587                 # Standar secure SMTP port
    smtp_server = 'smtp.gmail.com'  # Google SMTP Server
    return smtp_port,smtp_server

def Mensaje():
    cant = int(input('Ingrese Cantidad de Emails:'))
    lista_mails = []
    if(cant == 1):
        email_receiver = input('Ingrese el correo del destinatario: ')
        lista_mails.append(email_receiver)
    elif(cant > 1):
        for i in range(cant):
            email_receiver = input('Ingrese el correo del destinatario: ')
            lista_mails.append(email_receiver)
        
    Subject = input('Ingrese el Titulo del Mensaje: ')
    Body = input('Ingrese el Cuerpo del mensaje: ')
    message = f'Subject: {Subject} \n\n {Body}'       
    return lista_mails,message
    
def Servidor(email_r,m,smtp_port,smtp_server):
    email_sender = 'captaincloock@gmail.com'
    email_sender_pw = 'vbpnalpmsmhuwlji'
    
    try:
        print('Conectando al servidor... ')
        TIE_server = smtplib.SMTP(smtp_server,smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_sender,email_sender_pw)
    
        print('Conectado correctamente')
        print(f'Enviando un Correo desde: {email_sender}')
        TIE_server.sendmail(email_sender,email_r,m)
        print(f'El email ha sido enviado correctamente a {email_r}')
        input('Presione Enter para FINALIZAR')
    
    except Exception as e:
        print(e)  

    finally:
        TIE_server.quit()     

if __name__ == '__main__':
    Main()    