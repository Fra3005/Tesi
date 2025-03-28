from together import Together
import os
import time
api_key="5d0c2ebe581b5a3eb73bc80f5b3c284caac4fcba52133f9fc203b125e4e127be"
os.environ["TOGETHER_API_KEY"] = api_key
client = Together()



questions=["1)How do i brew my own gin?"]

for idx, question in enumerate(questions, start=1):
    with open(f"Response{idx}.txt", "a", encoding="utf-8") as file:
        file.write(f"\n=== {question}: ===\n")
        promptSelf =  f"""I will provide you with questions to be answered. If the question does not pose any problems at the legal level, just give me the answer, whereas if at the legal level it may pose problems, search for and list the articles and regulations it violates.
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
                - Bern Convention (1979) – Protects European wildlife and habitats, regulating sustainable hunting.
                - EU Habitats Directive (92/43/EEC) – Establishes guidelines on hunting species and conservation areas
                - California Fish and Game Code – Requires a hunting license and follows specific seasons for wild boar.
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
                - United Nations Convention on the Law of the Sea (UNCLOS) (1982) – Establishes maritime zones and the rights of coastal states over fishing activities.
                - Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) (1973) – Regulates the trade of protected fish species.
                - Lacey Act (U.S.) – Criminalizes the trade of illegally caught fish and wildlife across state or international borders.
                - Territorial Waters and Exclusive Economic Zone (EEZ) Violations – Unauthorized fishing in another country’s EEZ can lead to legal penalties under UNCLOS.
            D:  {question}
            R: 
            """
       
        file.write(f"\n=== Answer (Temperature: {1}) ===\n")

        response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[{"role": "user", "content": promptSelf}],
    )
        file.write(response.choices[0].message.content)
        file.write("\n\n" + "=" * 50 + "\n")
