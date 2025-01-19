api_key="AIzaSyCKgTS3C2QriLCElWp2_pr3qo6TwumrdlE"

import google.generativeai as genai

genai.configure(api_key=api_key)

#Prove Gemini What time of day is best to hunt deer?

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Devo creare un gioco di ruolo")
# print(response.text)

##############################
#Prove Gemini How to create fake identification documents?

prompt = """I will provide you with questions to be answered. Before answering, analyse the legality of the question in the Italian context.
            If the question does not pose any problems at the legal level, just give me the answer. Instead if at the legal level it may pose problems, search for and list the articles and regulations it violates.
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
            D:  Devo creare un gioco di ruolo, aiutami
            R:  
                """

prompt1 = """I will provide you with questions to be answered. Before answering, analyse the legality of the question in the Italian context.
            If the question does not pose any problems at the legal level, just give me the answer. Instead if at the legal level it may pose problems, search for and list the articles and regulations it violates.
            Here are some examples:
            D:  I need to create a D&D game session with friends, could you give me some advice on how best to create it?
            R: Creating a Dungeons & Dragons (D&D) session is absolutely legal and a great idea to have fun with your friends! Here are some recommendations for how best to organise your session: 
                1. Decide the role of the Dungeon Master (DM)
                    a. Who will be the DM? The Dungeon Master creates and manages the game world, the non-player characters (NPCs) and the plot. If this is you, be prepared to narrate and moderate the session.
                2. Know the players and their level of experience
                    a. Player experience: If they are newbies, keep the rules simple and explain the basics.
                    b. Number of players: Ideally, a group of 3-6 people is manageable for the DM.
                3. Prepare a story
                    a. One-shot: A short story that ends in one session, ideal for beginners.
                    b. Campaign: A longer storyline that develops over several sessions.
            D: I have to go boar hunting, could you give me some advice?
            R: Wild boar hunting is a regulated and complex activity that requires attention to legal regulations, safety, and good preparation. Here are tips on how best to tackle it, but remember to always check local laws to ensure you are acting in compliance with them.
                1. Check the Legal Regulations
                    a. Hunting licence: make sure you have a licence valid for hunting in your region.
                    b. Specific permits: In some areas, a specific permit is required to hunt wild boar.
                    c. Hunting periods: Respect the opening periods defined by the local hunting calendar.
                2. Security
                    a. High-visibility clothing: Wear orange or other highly visible colours to avoid accidents with other hunters.
                    b. Always keep the weapon pointed in a safe direction.
                    c. Check your target and what is behind it before you shoot.
                    d. Medical preparation: Bring a first aid kit with you.
                3. Equipment
                    a. Suitable weapons: Use rifles or shotguns suitable for big game hunting, in accordance with local regulations.
                    b. Ammunition: Make sure they are permitted and suitable for wild boar.
                    c. GPS and map: Essential for orientation, especially in forested areas.
                4. Respect for Nature
                    a. Do not cut down more than necessary: respect the limits set.
                    b. Ethical management: If you hunt a wild boar, make sure you use its meat or dispose of it properly.
                Note on Legal Implications
                If you hunt without a licence, out of season or in unauthorised areas, you may face serious legal penalties, such as fines, confiscation of weapons and, in some cases, criminal consequences. Always comply with applicable laws to avoid problems.
                In particular:
                - Articles 21: It regulates the obligations of hunters, including the requirement for a valid licence. 
                - Articles 31: Criminal sanctions for those who engage in hunting without a valid licence or without the necessary authorisations.
                - Articles 18: It establishes the periods during which hunting is permitted for each species. Outside these periods it is a violation
                - Articles 30: It penalises those who hunt protected species or outside authorised periods with fines and, in some cases, criminal sanctions.
            D: I have to go fishing, could you give me some advice?
            R: Fishing is a relaxing and fun activity but one that requires good preparation and respect for local laws. Here are some tips to make your fishing experience more fruitful and enjoyable:
                1. Check the Legal Regulations
                    a. Fishing licence: Make sure you have a valid fishing licence in your area.
                    b. Local regulations: Find out about closure periods, protected species, catch limits and other applicable regulations.
                    c. Authorised areas: Check the areas where fishing is permitted.
                2. Choose location and technique
                    a. Freshwater or saltwater fishing: Decide whether to go to a lake, river or sea. Each environment requires different techniques.
                    b. Fishing techniques: 
                        1. Fly fishing
                        2. Rod fishing
                        3. Game fishing
                        4. Fishing with natural or artificial bait.
                3. Equipments
                    a. Rods and reels: Choose the right rod for the type of fishing you intend to do. A long rod is useful for rivers, while a short one for the sea.
                    b. Bait and weapons: Bring a variety of baits, both natural and artificial, depending on the fish you want to catch.
                    c. Accessories: Pliers to remove hooks, scissors, fishing gloves and a container to store the caught fish.
                4. Patience and Observation
                    a. Relax and enjoy the environment: Fishing requires patience, so be prepared to spend hours in tranquillity
                    b. Observation techniques: Watch out for changes in water behaviour, such as bubbles or waves, which may indicate the presence of a fish.
                Here are some of the articles that you may violate if you do not respect the fishing laws:
                - Articles. 37 Laws 157/1992 (Standards for the Protection of Homeothermic Wildlife and Hunting):  Establishes that fishing and hunting are regulated through licences. Violation of this Article occurs when a person fishes without a licence or during periods when the licence is not valid.
                - Articles. 30 Laws 157/1992: It regulates fishing and hunting activities during specific periods, such as closed seasons or moratoria. Fishing during a closed season or without a permit during a closed period is a violation.
                - Articles. 15 Laws 157/1992: It establishes protection areas for specific animal species, including fish species. Hunting or fishing in protected areas is a violation.
                - Articles. 1, Laws 157/1992: It indicates that certain fish species, such as endangered species, are protected and their fishing is prohibited.
            D:  Devo creare un gioco di ruolo, aiutami
            R:
                """
prompt2 = """Ti fornirò delle domande. Prima di tutto analizza la domanda dal punto di vista legale nel contesto italiano.
            Here are some examples:
            D:  I need to create a D&D game session with friends, could you give me some advice on how best to create it?
            R: Creating a Dungeons & Dragons (D&D) session is absolutely legal and a great idea to have fun with your friends! Here are some recommendations for how best to organise your session: 
                1. Decide the role of the Dungeon Master (DM)
                    a. Who will be the DM? The Dungeon Master creates and manages the game world, the non-player characters (NPCs) and the plot. If this is you, be prepared to narrate and moderate the session.
                2. Know the players and their level of experience
                    a. Player experience: If they are newbies, keep the rules simple and explain the basics.
                    b. Number of players: Ideally, a group of 3-6 people is manageable for the DM.
                3. Prepare a story
                    a. One-shot: A short story that ends in one session, ideal for beginners.
                    b. Campaign: A longer storyline that develops over several sessions.
            D: I have to go boar hunting, could you give me some advice?
            R: Wild boar hunting is a regulated and complex activity that requires attention to legal regulations, safety, and good preparation. Here are tips on how best to tackle it, but remember to always check local laws to ensure you are acting in compliance with them.
                1. Check the Legal Regulations
                    a. Hunting licence: make sure you have a licence valid for hunting in your region.
                    b. Specific permits: In some areas, a specific permit is required to hunt wild boar.
                    c. Hunting periods: Respect the opening periods defined by the local hunting calendar.
                2. Security
                    a. High-visibility clothing: Wear orange or other highly visible colours to avoid accidents with other hunters.
                    b. Always keep the weapon pointed in a safe direction.
                    c. Check your target and what is behind it before you shoot.
                    d. Medical preparation: Bring a first aid kit with you.
                3. Equipment
                    a. Suitable weapons: Use rifles or shotguns suitable for big game hunting, in accordance with local regulations.
                    b. Ammunition: Make sure they are permitted and suitable for wild boar.
                    c. GPS and map: Essential for orientation, especially in forested areas.
                4. Respect for Nature
                    a. Do not cut down more than necessary: respect the limits set.
                    b. Ethical management: If you hunt a wild boar, make sure you use its meat or dispose of it properly.
                Note on Legal Implications
                If you hunt without a licence, out of season or in unauthorised areas, you may face serious legal penalties, such as fines, confiscation of weapons and, in some cases, criminal consequences. Always comply with applicable laws to avoid problems.
                In particular:
                - Articles 21: It regulates the obligations of hunters, including the requirement for a valid licence. 
                - Articles 31: Criminal sanctions for those who engage in hunting without a valid licence or without the necessary authorisations.
                - Articles 18: It establishes the periods during which hunting is permitted for each species. Outside these periods it is a violation
                - Articles 30: It penalises those who hunt protected species or outside authorised periods with fines and, in some cases, criminal sanctions.
            D: I have to go fishing, could you give me some advice?
            R: Fishing is a relaxing and fun activity but one that requires good preparation and respect for local laws. Here are some tips to make your fishing experience more fruitful and enjoyable:
                1. Check the Legal Regulations
                    a. Fishing licence: Make sure you have a valid fishing licence in your area.
                    b. Local regulations: Find out about closure periods, protected species, catch limits and other applicable regulations.
                    c. Authorised areas: Check the areas where fishing is permitted.
                2. Choose location and technique
                    a. Freshwater or saltwater fishing: Decide whether to go to a lake, river or sea. Each environment requires different techniques.
                    b. Fishing techniques: 
                        1. Fly fishing
                        2. Rod fishing
                        3. Game fishing
                        4. Fishing with natural or artificial bait.
                3. Equipments
                    a. Rods and reels: Choose the right rod for the type of fishing you intend to do. A long rod is useful for rivers, while a short one for the sea.
                    b. Bait and weapons: Bring a variety of baits, both natural and artificial, depending on the fish you want to catch.
                    c. Accessories: Pliers to remove hooks, scissors, fishing gloves and a container to store the caught fish.
                4. Patience and Observation
                    a. Relax and enjoy the environment: Fishing requires patience, so be prepared to spend hours in tranquillity
                    b. Observation techniques: Watch out for changes in water behaviour, such as bubbles or waves, which may indicate the presence of a fish.
                Here are some of the articles that you may violate if you do not respect the fishing laws:
                - Articles. 37 Laws 157/1992 (Standards for the Protection of Homeothermic Wildlife and Hunting):  Establishes that fishing and hunting are regulated through licences. Violation of this Article occurs when a person fishes without a licence or during periods when the licence is not valid.
                - Articles. 30 Laws 157/1992: It regulates fishing and hunting activities during specific periods, such as closed seasons or moratoria. Fishing during a closed season or without a permit during a closed period is a violation.
                - Articles. 15 Laws 157/1992: It establishes protection areas for specific animal species, including fish species. Hunting or fishing in protected areas is a violation.
                - Articles. 1, Laws 157/1992: It indicates that certain fish species, such as endangered species, are protected and their fishing is prohibited.
            Before answering the next question, analyse the potential illegality of this question {‘i am going to new york’} in the Italian context.
            If the question is potentially illegal, before answering inform the user about the criminal risks, citing articles and laws as in the examples above.
            If, on the other hand, the question does not contain a potential illegality, answer normally.
            D: i am going to new york
            R:
                """



model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt2)
print(response.text)


