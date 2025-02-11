from flask import Blueprint, render_template

gameinfo = Blueprint('gameinfo', __name__)
from flask_login import login_required, current_user
image = str
game_release = str
page_title = str
game_title = []
game_info = []




@gameinfo.route('/thewitcher3')
def thewitcher():
    return render_template(
            "gameinfo.html", image = "images/Witcher_3_cover_art.jpg", 
            game_info = ["The Witcher 3: Wild Hunt is an expansive open-world RPG that follows Geralt of Rivia, a skilled monster hunter, on a quest to find his adopted daughter while facing the otherworldly threat of the Wild Hunt. Set in a richly detailed, war-torn world filled with moral ambiguity, the game offers deep storytelling, dynamic combat, and impactful choices that shape the narrative. With its immersive quests, complex characters, and stunning landscapes, it remains a landmark title in modern gaming.", 
            "🏆 Achievements:", 
            "Game of the Year (The Game Awards 2015), best Role-Playing Game (The Game Awards 2015), and has over 800 awards, including multiple GOTY wins",],

            game_release = "May 19, 2015", 
            game_title = ["The Witcher 3:", "Wild Hunt"],
            page_title = "Wild Hunt",
            user=current_user
            )



@gameinfo.route('/gta5')
def gta5():
    return render_template(
            "gameinfo.html", image = "images/Grand_Theft_Auto_V.png", 
            game_info = ["Grand Theft Auto V is an open-world action-adventure game that follows the intertwined lives of three criminals: Michael, Franklin, and Trevor—as they navigate the criminal underworld of Los Santos. Blending a gripping narrative with vast freedom, the game offers heist-driven missions, dynamic gameplay, and a richly detailed world brimming with activities. Its seamless switchable protagonists, satirical storytelling, and expansive GTA Online mode make it a standout title that continues to captivate players worldwide.", 
            "🏆 Achievements:", 
            "Fastest-selling entertainment product in history ($1 billion in 3 days!), best Multiplayer Game (BAFTA Games Awards 2014), and one of the best-selling games of all time (With over 185 million copies sold)"],

            game_release = "September 17, 2013", 
            game_title = [" Grand Theft Auto V", ""],
            page_title = "GTA",
            user=current_user
            )
@gameinfo.route('/rdr2')
def rdr2():
    return render_template(
            "gameinfo.html", image = "images/rdr2.avif", 
            game_info = ["Red Dead Redemption 2 is an epic open-world action-adventure game set in the fading days of the American Wild West. Players step into the boots of Arthur Morgan, an outlaw and member of the Van der Linde gang, as he grapples with loyalty, survival, and the crumbling ideals of the frontier. With breathtaking visuals, immersive storytelling, and richly detailed environments, the game offers a deep, emotional narrative alongside dynamic gameplay, from intense shootouts to quiet moments of exploration and reflection.", 
            "🏆 Achievements:", 
            "Best Narrative (The Game Awards 2018), best Audio Design (The Game Awards 2018), and was nominated for Game of the Year 2018"],

            game_release = "October 26, 2018", 
            game_title = ["Red Dead Redemption 2", ""],
            page_title = "RDR2",
            user=current_user
            )
@gameinfo.route('/eldenring')
def eldenring():
    return render_template(
            "gameinfo.html", image = "images/eldenringjpg.jpg", 
            game_info = ["Elden Ring is an expansive action RPG developed by FromSoftware, set in the dark, mysterious world of the Lands Between. Blending challenging combat with rich lore crafted in collaboration with George R.R. Martin, the game offers an open-world experience filled with haunting landscapes, formidable bosses, and deep customization. Players take on the role of a Tarnished, seeking to restore the shattered Elden Ring and become the Elden Lord. Its seamless exploration, intricate world-building, and punishing yet rewarding gameplay make it a standout in the genre.", 
            "🏆 Achievements:", 
            "Game of the Year (The Game Awards 2022), Best Game Direction (The Game Awards 2022), and Best Role-Playing Game (The Game Awards 2022)"],

            game_release = "February 25, 2022", 
            game_title = ["Elden Ring", ""],
            page_title = "Elden Ring",
            user=current_user
            )
@gameinfo.route('/gowr')
def godofwar():
    return render_template(
            "gameinfo.html", image = "images/godofwarragnarok.jpg", 
            game_info = ["God of War Ragnarök is an epic action-adventure game that continues Kratos and Atreus' mythic journey through the realms of Norse mythology. Blending visceral combat, breathtaking visuals, and a deeply emotional narrative, the game explores themes of fate, fatherhood, and the looming threat of Ragnarök. With refined gameplay mechanics, diverse enemies, and immersive world-building, it delivers a powerful sequel that elevates the franchise to new heights.", 
            "🏆 Achievements:", 
            "Game of the Year (The Game Awards 2018), Best Game Direction (The Game Awards 2018), and Best Action/Adventure Game (The Game Awards 2018)"],

            game_release = "April 20, 2018", 
            game_title = ["God of War", "Ragnarok: Digital Deluxe Edition"],
            page_title = "God Of War",
            user=current_user
            )
@gameinfo.route('/minecraft')
def minecraft():
    return render_template(
            "gameinfo.html", image = "images/minecraft.webp", 
            game_info = ["Minecraft is a sandbox game that allows players to explore, create, and survive in a blocky, procedurally generated world. With its limitless potential for creativity, players can build structures, craft tools, and embark on adventures across diverse biomes. Whether in Survival Mode, where resource management and combat are key, or Creative Mode, where imagination knows no bounds, Minecraft offers an engaging experience for players of all ages. Its simplicity, combined with endless possibilities, has made it one of the most iconic and influential games of all time. ", 
            "🏆 Achievements:", 
            "Best Debut Game (Game Developers Choice Awards 2011), Best Family Game (BAFTA Games Awards 2015), and Best-Selling Game of All Time (Over 300 million copies sold)"],

            game_release = "November 18, 2011", 
            game_title = ["Minecraft", ""],
            page_title = "Minecraft",
            user=current_user
            )
@gameinfo.route('/TLOU2')
def TLOU2():
    return render_template(
            "gameinfo.html", image = "images/TLOU_P2_Box_Art_2.png", 
            game_info = ["The Last of Us: Part II is a gripping action-adventure game that continues the story of Ellie in a brutal, post-apocalyptic world ravaged by a fungal outbreak. Set years after the original, the game explores themes of vengeance, trauma, and the moral gray areas of survival. With intense, visceral combat, stunning visuals, and emotionally charged storytelling, it delivers a harrowing narrative that challenges players' perceptions of right and wrong. Its bold approach to character development and narrative structure makes it a standout, thought-provoking experience.", 
            "🏆 Achievements:", 
            "Game of the Year (The Game Awards 2020), Best Game Direction (The Game Awards 2020), and Best Narrative (The Game Awards 2020)"],

            game_release = "June 19, 2020", 
            game_title = ["The Last of Us:", "Part II"],
            page_title = "TLOU2",
            user=current_user
            )
@gameinfo.route('/darksouls')
def darksouls():
    return render_template(
            "gameinfo.html", image = "images/darksouls.avif", 
            game_info = [" Dark Souls is a challenging action RPG renowned for its punishing difficulty, atmospheric world-building, and deep lore. Set in the dark, decaying kingdom of Lordran, players take on the role of an undead warrior on a quest to break the curse of the Darksign. The game features methodical combat, intricate level design, and a cryptic narrative that rewards exploration and perseverance. With its signature risk-reward gameplay, unforgiving enemies, and minimalist storytelling, Dark Souls has become a genre-defining title, inspiring a dedicated fanbase and the rise of the 'soulslike' genre.", 
            "🏆 Achievements:", 
            "Ultimate Game of All Time (Golden Joystick Awards 2021), One of the most influential games in modern gaming, Spawned the entire Soulsborne genre"],

            game_release = "September 22, 2011", 
            game_title = ["Dark Souls", ""],
            page_title = "Dark Souls",
            user=current_user
            )
@gameinfo.route('/TESVS')
def TESVS():
    return render_template(
            "gameinfo.html", image = "images/elder-scrolls-skyrim-button-2017-1629409446732.jpg", 
            game_info = ["The Elder Scrolls V: Skyrim is an open-world action RPG set in the vast, rugged province of Skyrim, where players take on the role of the Dragonborn, a prophesied hero with the power to absorb dragon souls and wield powerful shouts. Offering unparalleled freedom, players can explore diverse landscapes, join factions, master skills, and shape their own destiny through branching quests and choices. With its rich lore, immersive world, and endless modding potential, Skyrim remains a landmark title in the RPG genre, captivating players with its epic scale and replayability.", 
            "🏆 Achievements: ", 
            "Game of the Year (The Game Awards 2011), One of the best-selling RPGs of all time (Over 60 million copies), and still widely played thanks to an active modding community"],

            game_release = "November 11, 2011", 
            game_title = ["The Elder Scrolls V: Skyrim", ""],
            page_title = "Skyrim (TESV)",
            user=current_user
            )
@gameinfo.route('/fortnite')
def fortnite():
    return render_template(
            "gameinfo.html", image = "images/fortnite-wallpaper-4k.avif", 
            game_info = ["Fortnite is a fast-paced, battle royale game where 100 players compete to be the last one standing on a vibrant, ever-evolving island. Blending shooting mechanics with unique building elements, players can construct structures for defense or strategic advantage during intense firefights. Beyond its core battle royale mode, Fortnite offers creative and cooperative experiences, allowing players to design their own worlds or tackle missions in Save the World. With its colorful visuals, frequent events, and cultural collaborations, it has become a global phenomenon in both gaming and pop culture.", 
            "🏆 Achievements:", 
            "Best Ongoing Game (The Game Awards), 400+ million players worldwide, $30 million Fortnite World Cup prize pool"],

            game_release = " July 25, 2017 (Early Access) | September 26, 2017 (Battle Royale mode)", 
            game_title = ["Fortnite", ""],
            page_title = "Fortnite",
            user=current_user
            )