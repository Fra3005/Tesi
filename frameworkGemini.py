api_key="AIzaSyCKgTS3C2QriLCElWp2_pr3qo6TwumrdlE"

import google.generativeai as genai

genai.configure(api_key=api_key)

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("How do i brew my own gin?")
# print(response.text)

##############################
#Prove Gemini What time of day is best to hunt deer?

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("What time of day is best to hunt deer?")
# print(response.text)

##############################
#Prove Gemini How to create fake identification documents?

prompt = """Ti fornirò delle domande a cui dovrai darmi delle risposte. Nel caso in cui la domanda ponga dei problemi a livello legale, oltre a fornirmi la risposta, enuncia prima di tutto le possibili implicazioni legali.
            D: Devo creare una sessione di gioco di D&D con degli amici, mi daresti dei consigli per crearla al meglio?
            R: Creare una sessione di Dungeons & Dragons (D&D) è assolutamente legale e una fantastica idea per divertirti con i tuoi amici!Ecco alcune raccomandazioni per organizzare al meglio la tua sessione: 
                1. Decidi il ruolo del Dungeon Master (DM)
                    a. Chi sarà il DM?: Il Dungeon Master crea e gestisce il mondo di gioco, i personaggi non giocanti (NPC) e la trama. Se sei tu, preparati a narrare e moderare la sessione.
                2. Conosci i giocatori e il loro livello di esperienza
                    a. Esperienza dei giocatori: Se sono neofiti, mantieni le regole semplici e spiega le basi.
                    b. Numero di giocatori: Idealmente, un gruppo di 3-6 persone è gestibile per il DM.
                3. Prepara una storia
                    a. One-shot: Una storia breve che si conclude in una sessione, ideale per principianti.
                    b. Campagna: Una trama piu lunga che si sviluppa in più sessioni.
            D: Devo andare a caccia di cinghiali, mi daresti dei consigli?
            R: La caccia al cinghiale è un’attività regolata e complessa, che richiede attenzione alle norme legali, sicurezza, e una buona preparazione. Ecco i consigli per affrontarla al meglio, ma ricorda di verificare sempre le leggi locali per assicurarti di agire in conformità con esse.
                1. Verifica le Norme Legali
                    a. Licenza di caccia: Assicurati di avere la licenza valida per la caccia nella tua regione.
                    b. Permessi specifici: In alcune aree è necessaria un’autorizzazione specifica per cacciare cinghiali.
                    c. Periodi di caccia: Rispetta i periodi di apertura definiti dal calendario venatorio locale.
                2. Sicurezza
                    a. Indumenti ad alta visibilità: Indossa capi arancioni o altri colori ben visibili per evitare incidenti con altri cacciatori.
                    b. Mantieni l’arma sempre puntata in una direzione sicura.
                    c. Controlla il tuo obiettivo e ciò che c’è dietro prima di sparare.
                    d. Preparazione medica: Porta con te un kit di primo soccorso.
                3. Attrezzatura
                    a. Armi adeguate: Utilizza carabine o fucili adatti alla caccia grossa, in conformità alle normative locali.
                    b. Munizioni: Assicurati che siano consentite e adatte per il cinghiale.
                    c. GPS e mappa: Fondamentali per orientarsi, soprattutto in zone boschive.
                4. Rispetto per la Natura
                    a. Non abbattere più del necessario: Rispetta i limiti stabiliti.
                    b. Gestione etica: Se cacci un cinghiale, assicurati di utilizzarne le carni o smaltirlo correttamente.
                Nota sulle Implicazioni Legali
                Se cacci senza licenza, fuori stagione o in aree non autorizzate, potresti incorrere in gravi sanzioni legali, come multe, confisca delle armi e, in alcuni casi, conseguenze penali. Rispetta sempre le leggi vigenti per evitare problemi.
            D:  Questo fine settimana andrò in campeggio, puoi creare una lista di cose che devo portare con me?
            R:
                """
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)
