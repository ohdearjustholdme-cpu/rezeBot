import os
import disnake
from disnake.ext import commands

# Activar intents
intents = disnake.Intents.default()
intents.message_content = True
# Crear el bot
bot = commands.InteractionBot(intents=intents) 

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=disnake.Activity(
            type=disnake.ActivityType.playing,
            name="bleeeh"
        ),
        status=disnake.Status.online
    )
    print(f"{bot.user} listo!")

# Comando /love
@bot.slash_command()
async def love(inter):
    """Envía un mensaje yeii."""
    await inter.response.send_message("i luv uuu* 💗")


#comando /hug
hugs_gifs = [
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2NqeHhyZGV5eTE5eW1qOGNnYjR4azNrMjY4Y2J5YXllZTN2aW1xayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kvKFM3UWg2P04/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXdkNXhsdjZwMDV1ZDV2ZW43cncxZW00ZWR3bjB1enRpZjkwdHVlcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Y8wCpaKI9PUBO/giphy.gif",
]
@bot.slash_command(description="dar un gran abrazo yupi")
async def hug(
    inter: disnake.ApplicationCommandInteraction,
    usuario: disnake.Member = commands.Param(
        description="A quien quieres abrazar? ><"
    )
):
    import random
    gif = random.choice(hugs_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} le da un gran abrazo a {usuario.display_name}! yeiii",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

    #comando GrabBoobs equisde

grabboobs_gifs = [
    "https://media.discordapp.net/attachments/1319870731877875782/1319883617413107792/Animated_GIFs_Hentai___Ecchi_GIF_1.gif?ex=692335a8&is=6921e428&hm=f1967248285e1ec4034c2f507e7496c636c8a010b0148599be9b9d5942b68111&"
]
@bot.slash_command(description="agarrar las ttas de alguien")
async def grabboobs(  
      inter: disnake.ApplicationCommandInteraction,
      
        usuario: disnake.Member = commands.Param(
            description="De quien quieres agarrar las boobies? dskjasd"
        )
):
    import random
    gif = random.choice(grabboobs_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} agarra las boobies de {usuario.display_name}! ( T///T )",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)


# Comando makescum
makescum_gifs = [
    "https://nekocdn.com/images/X5gvPSzB.gif"
]
@bot.slash_command(name="makecum", description=" Hace que alguien se corra (∩˃ω˂∩)")
async def makescum(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description="A quien quieres hacer correr? <3"
        )
):
    import random
    gif = random.choice(makescum_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} hace que {usuario.display_name} se corra! ( • ᴗ - ) ✧",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

# comando cuminside

@bot.slash_command(name="cuminside", description= " te corres dentro de alguien (⁄⁄>⁄⁄<⁄⁄)")
async def cuminside(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description="Dentro de quien quieres correrte? <3"
        )
):
    import random
    gif = random.choice(makescum_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} se corre dentro de {usuario.display_name}! ( • ᴗ - ) ✧",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

# comando fuck
fuck_gifs = [
    "https://images-ext-1.discordapp.net/external/p_nTKSYkNoZnLxKmvIgecfsjFQjwxM_ZuWVbNbOOup0/https/nekocdn.com/images/dS2pUoBP.gif?width=625&height=351",
    "https://images-ext-1.discordapp.net/external/oibA5nnONylDe9iZ3pFLbTpVlB08upBjdJSLB7xBWJs/https/nekocdn.com/images/M7_yn-xn.gif?width=500&height=281",
    "https://images-ext-1.discordapp.net/external/-ioxb3-puWB8odGKlWHmYTJ9tMSgBf8lomsgO_W-rZ4/https/nekocdn.com/images/mtjefHdP.gif?width=675&height=380",
    "https://images-ext-1.discordapp.net/external/oZH2juD8q7Q4KePyhWLnNKYi0CNW4yk0r5gWSUBnTGU/https/nekocdn.com/images/wV5IfNks.gif?width=625&height=416",
    "https://images-ext-1.discordapp.net/external/SuaNFqnQtvbXGncH4bJpkwaP-oMCa9XjkYSv7JAHLdE/https/images-ext-2.discordapp.net/external/ncMN0Rec9RzYppAeg2WlkHg3i5r-JGYZud2JdYnws5w/https/nekocdn.com/images/0w68NtPM.gif?width=675&height=379",
    "https://images-ext-1.discordapp.net/external/XTpXldWT6Lb4y7SZs9o3zaIkiq3Nf_EubY4m2e-9CRE/https/images-ext-2.discordapp.net/external/sVs9_els9xjTpnnPYszdwBeAUv8_hbMd-RGhlthtotE/https/nekocdn.com/images/4yR6Omkp.gif?width=500&height=281",
    "https://images-ext-1.discordapp.net/external/2kwKYkDTnr3QASK7uv_MM2ueUHLEB3R0AaMs6RkjhBM/https/images-ext-2.discordapp.net/external/niimGx0TfuIA2L_OCbqtI_PV0Wb5rszLhN33r2fpFX4/https/nekocdn.com/images/AQXdegXA.gif?width=880&height=495",
    "https://images-ext-1.discordapp.net/external/WcUIYRfRUyrVVtLpokINH4QOEhCYbHaMjQljGyXHztA/https/nekocdn.com/images/ZCcFXAJz.gif?width=675&height=375",
    "https://images-ext-1.discordapp.net/external/-rdpg5iOMfIkMtcaP2vQ-eMu_UNu7n-jeV9P0OEpdPs/https/nekocdn.com/images/__hUU0In.gif?width=260&height=375",
    "https://images-ext-1.discordapp.net/external/EmMtG5LczI4lO4GuyJlit0mUZxkUgVdi6rJJO1tv0tQ/https/images-ext-2.discordapp.net/external/qpsPUItWb2PTYDTq2UhJQJQiTj67lbkcQmcoD5hDgSg/https/nekocdn.com/images/ZnGI2uzp.gif?width=1000&height=669",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307738809008138/asutora-Anime-Art-artist-hentai-gif-8996115.gif?ex=6924f541&is=6923a3c1&hm=53341b4edf19dc963012440fc96ba36506b6503356d2ee9fdcc21c980dcd2da5&=&width=523&height=930",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307797726400664/Meat-Eat-Girl-porn-vn-hentai-Censored-Hentai-8684976.gif?ex=6924f54f&is=6923a3cf&hm=b72781213272e19af66fff9e26beb8ffe97def084282ec2526f6e60e4998fb05&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308183241654408/Mai-Friend-porn-vn-hentai-Anime-VN-8684175.gif?ex=6924f5ab&is=6923a42b&hm=812a1593e73d2e7a594eaa0f48c8a4db0d683eed2f83b17076818147fa4d37e9&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308198114660444/Mai-Friend-porn-vn-hentai-Anime-VN-8684178.gif?ex=6924f5af&is=6923a42f&hm=8c641328bed64f3e841c240d0d1b5cbd6ea1f85c7b935bc51e7b84c218cc92d4&=&width=1014&height=570"
]
@bot.slash_command(name="fuck", description="folla a alguien (>⩊<)")
async def fuck(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" A quien quieres follar? <3"
        )
):
    import random
    gif = random.choice(fuck_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} folla a {usuario.display_name} ₊˚⊹♡",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

#comando anal
anal_gifs = [
    "https://images-ext-1.discordapp.net/external/hx1qEMolzhK35RvovwsmUghnZ3WM3qVpkryygt-neK4/https/images-ext-2.discordapp.net/external/749hpRoPAovsjZClIZexJGGCreNOBdE0jehp5ooQHH8/https/nekocdn.com/images/HQmsg98K.gif?width=935&height=701",
    "https://images-ext-1.discordapp.net/external/pBEbp1ipjS11M5Ipl6C9n6BwV7g3RyiyegduI7X0QwE/https/images-ext-2.discordapp.net/external/WAig0yih6lzk5GVXRwlfNIHeHeKuOeNsLhbzvRxsox4/https/nekocdn.com/images/88lWRl34.gif?width=750&height=423",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307680411582616/aseiusx-artist-porn-vn-hentai-8703477.gif?ex=6924f533&is=6923a3b3&hm=6eeb21ecd69c0bcf5b50e0da8a0c5af0e6515bd5e88972ba7ab5f4a310730c04&=&width=1000&height=563",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307834598658240/Mai-Friend-porn-vn-hentai-Anime-VN-8684131.gif?ex=6924f558&is=6923a3d8&hm=98450d31f144599ed8aa37e9923bbfd6ffea71a1c7d2f0ba8f4ec78c97104727&=&width=1014&height=570"
]
@bot.slash_command(name="anal", description="hazle un anal a alguien")
async def anal(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a quien le daras por detras?"
        )
):
    import random
    gif = random.choice(anal_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} le rompe el trasero a {usuario.display_name} (╥ ω ╥)",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

#comando bentfuck
bentfuck_gifs = [
    "https://images-ext-1.discordapp.net/external/t9YkG27VZGyVATISvc2MVaNm7NEaEeYSG9C-q0PjjGk/https/nekocdn.com/images/SYfiUFNl.gif?width=625&height=469",
    "https://images-ext-1.discordapp.net/external/HLfR-FiqNFo-yyHMVS8kTDHkJ8MfIM2Wu1vB_jrzJoM/https/nekocdn.com/images/6owdyfZO.gif?width=774&height=820",
    "https://images-ext-1.discordapp.net/external/ga-NT2qMb-_NU0R_AErkhZdfff0mdxP8iprhG6NK39Q/https/images-ext-2.discordapp.net/external/0nZdNbr3_y1cSYrAP4926YwR1SNwxiynL7RlkLEjXnQ/https/nekocdn.com/images/tEjM8ryQ.gif?width=611&height=750",
    "https://images-ext-1.discordapp.net/external/ZXjkqKia3iErerNUB2DB1QxwR2NTfsZwTnewCgsLiCk/https/images-ext-2.discordapp.net/external/kYEL2R7ayvmwiqKVZsOJ38SH9od2nGcAX0vblRn0DIo/https/nekocdn.com/images/E56hkcu9.gif?width=625&height=351",
    "https://images-ext-1.discordapp.net/external/YZu6c4dzHcxFWxPqi8mxD1j_rNDvHYRO3a1bdQzoSKA/https/nekocdn.com/images/d9fBq1Td.gif?width=675&height=379",
    "https://images-ext-1.discordapp.net/external/hEAzH40ZwnZYlQEIhibZ2SSPYMG9NFrbicKxfvt4aFg/https/nekocdn.com/images/n4kKrue8.gif?width=625&height=353",
    "https://images-ext-1.discordapp.net/external/lJ4pG-l82nLEJxZUt4bMTR03pPjVtWicmm20omdc8pc/https/images-ext-2.discordapp.net/external/1j7BpebUwD5i7Pxi24FeUbXdISo2hA7S3GKT1OZywZk/https/nekocdn.com/images/QC0IJLsx.gif?width=625&height=351",
    "https://images-ext-1.discordapp.net/external/nJh0hSpPz5j8oxhXt0wyRWBTnHsrNLP0ge7mRh0tHSk/https/images-ext-2.discordapp.net/external/Vku2Rr8-JLbvjCjd852YWVTZiT1PkHYb2tpeqcezhhs/https/nekocdn.com/images/zc6VIv-n.gif?width=675&height=379",
    "https://media.discordapp.net/attachments/1371018932084801586/1442212335778398442/680eab66392d4424767572.gif?ex=69249c67&is=69234ae7&hm=5674aa048b2eef978bba1cbf0b2e3cb9f6ece70db6bee36c651725fa54caf7b3&=&width=1200&height=675",
    "https://media.discordapp.net/attachments/1371018932084801586/1442212336160215121/kuro-no-kyoushitsu-2-scaled.webp?ex=69249c67&is=69234ae7&hm=71d1a6c5ca881848f3fae481934a4a80ef5e042fa40a9f88d1927630013a42a4&=&animated=true&width=625&height=351",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307773437313194/Mai-Friend-porn-vn-hentai-Anime-VN-8684145.gif?ex=6924f549&is=6923a3c9&hm=a2957c2409398de9244798db32db7565fd3e1c418cc08ae3df5142c71019b1b9&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308070788038798/Mai-Friend-porn-vn-hentai-Anime-VN-8684165.gif?ex=6924f590&is=6923a410&hm=ddc632c021b6e22f23d3008581c1c87b1f37ad73ebd7a661d6bd0c736ccc21ac&=&width=1014&height=570"

]
@bot.slash_command(name="bentfuck", description="folla a alguien por detras")
async def bentfuck(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a quien follaras por detras?"
        )
):
    import random
    gif = random.choice(bentfuck_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} folla a {usuario.display_name} por detras Σ(°ロ°)",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

#comando ride
ride_gifs = [
    "https://images-ext-1.discordapp.net/external/hx1qEMolzhK35RvovwsmUghnZ3WM3qVpkryygt-neK4/https/images-ext-2.discordapp.net/external/749hpRoPAovsjZClIZexJGGCreNOBdE0jehp5ooQHH8/https/nekocdn.com/images/HQmsg98K.gif?width=935&height=701",
    "https://images-ext-1.discordapp.net/external/BYfaVjZV0XKVczrNp1eNsfk_G0C3_FjYzHZyjZjJQ4Q/https/nekocdn.com/images/BWvAQd58.gif?width=500&height=375",
    "https://images-ext-1.discordapp.net/external/7NpinbmiF9iyH0C_a_f7TLf2Vsc_QK229VSbbnYtqj4/https/nekocdn.com/images/xbaR0gha.gif?width=935&height=784",
    "https://images-ext-1.discordapp.net/external/QVqhS9nIuysbcH74xnqlAwc5e1T4JBInpV1mTSAX5zM/https/images-ext-2.discordapp.net/external/MzCUiawVK6WrpYH3NDrhYxa1VpfT1v7iqB-oTeq-DyM/https/nekocdn.com/images/MXjoubgt.gif?width=611&height=820",
    "https://images-ext-1.discordapp.net/external/HczrG7W1OK4XfE8P2LYvlup-ir_28W1SGwQQRnh0ykY/https/images-ext-2.discordapp.net/external/x23lVZJxZ0P1y92v6JmEeCjIGOJmpIvhcvedoCMF9gs/https/nekocdn.com/images/DAXT0yUw.gif?width=675&height=380",
    "https://images-ext-1.discordapp.net/external/_PPMU_3lDe9zBfcfPygqfh7ENNooMMm12bAvSxp_ZB4/https/nekocdn.com/images/QguqlzYk.gif?width=625&height=351",
    "https://images-ext-1.discordapp.net/external/w0mXPNH5NDkBQJFpkH5CUvSCH5iESj3J3uDJMOYhwro/https/images-ext-2.discordapp.net/external/eHPw2SaHpRCxtXVTXsE-ROmA-kT6e4LxcDHa1fG56a4/https/nekocdn.com/images/NVlyyf3_.gif?width=500&height=334",
    "https://images-ext-1.discordapp.net/external/vD-2le7UF9hgBjrvE1XxCJLqttxw9MaZFlN_r85KBks/https/nekocdn.com/images/hkKxXYXm.gif?width=750&height=563",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307991595389111/bubble-de-house-de-marumarumaru-porn-vn-hentai-Censored-Hentai-8643747.gif?ex=6924f57d&is=6923a3fd&hm=855da897bc317290bf78da0f46aea9ea0f4b090108793223708a03ea7aded770&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308023010725959/Mai-Friend-porn-vn-hentai-Anime-VN-8684156.gif?ex=6924f585&is=6923a405&hm=ad98f8f72c2b628a0c3f8be55180ad75f9d70180005a9c3a6f6fa395e682cccf&=&width=1014&height=570"
]
@bot.slash_command(name="ride", description="Monta a alguien")
async def ride(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a Quien vas a montar?"
        )
):
    import random
    gif = random.choice(ride_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} Monta a {usuario.display_name} (>\\<)",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

#getsin4
getsin4_gifs = [
    "https://cdn.discordapp.com/attachments/827215645887954974/1292022036293615687/36e53c89f105cc4391a371dd83fafede.gif?ex=69235d0a&is=69220b8a&hm=84f2b17e3cf9b11ccab6d7cb614a0f54a2863c0f0c962951279f3167e91c343c",
    "https://images-ext-1.discordapp.net/external/y8gEA0QP2HnmKJ11FVztqevStuGoPCIRl_3IEzTnUW4/https/78.media.tumblr.com/5f7c1100b7803ba5b7008833ad128c70/tumblr_pd2xub3ZIn1w48222o7_500.gif?width=625&height=433"
]

class Getsin4View(disnake.ui.View):
    def __init__(self, author, target):
        super().__init__(timeout=None)
        self.author = author
        self.target = target

    @disnake.ui.button(label="follar por detras 🦭", style=disnake.ButtonStyle.primary)
    async def getsin4_back(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):

        
        if inter.author.id != self.target.id:
            return await inter.response.send_message(
                "woopm woopm este boton no es para ti", ephemeral=True
            )
        
        import random
        gif = random.choice(bentfuck_gifs)

        embed = disnake.Embed(
            title=f"{inter.author.display_name} folla por detras a {self.author}!",
            color=0xFFC0CB
        )
        embed.set_image(url=gif)

        await inter.response.send_message(embed=embed)



@bot.slash_command(name="getsin4", description="Te pones en 4")
async def getsin4(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" por quien te pondras en 4?"
        )
):
    import random
    gif = random.choice(getsin4_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} se pone en 4 para {usuario.display_name} (>\\<)",
        color=disnake.Color.from_rgb(255, 105, 180)  
    )
    embed.set_image(url=gif)

    view = Getsin4View(author=inter.author.display_name, target=usuario)

    await inter.response.send_message(embed=embed, view=view)

# show boobs
showboobs_gifs = [
    "https://media.discordapp.net/attachments/1305741665679704105/1409324831001809046/52472c460de68fe499ba7bb567c600e4.gif?ex=69239e87&is=69224d07&hm=7f122a13ec9e35bcf89de26109577e1f95cc37379c04304a7e45680594c584a2&=&width=1250&height=703",
    "https://media.discordapp.net/attachments/1328152649454845972/1330620676188405813/IMG_6415.gif?ex=69236112&is=69220f92&hm=4d6d918ec4d8405de4f3508859dc5df3093c156b159e260cab962bba533b9c18&=&width=1000&height=744"
]

class ShowBoobsView(disnake.ui.View):
    def __init__(self, author, target):
        super().__init__(timeout=None)
        self.author = author
        self.target = target

    @disnake.ui.button(label="suck", style=disnake.ButtonStyle.primary)
    async def ShowBoobs_back(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):

        
        if inter.author.id != self.target.id:
            return await inter.response.send_message(
                "woopm woopm este boton no es para ti", ephemeral=True
            )
        
        import random
        gif = random.choice(suckboobs_gifs)

        embed = disnake.Embed(
            title=f"{inter.author.display_name} le xupa las tetas a {self.author}!",
            color=0xFFC0CB
        )
        embed.set_image(url=gif)

        await inter.response.send_message(embed=embed)

    @disnake.ui.button(label="grab", style=disnake.ButtonStyle.secondary)
    async def ShowBoobs2_back(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):

        
        if inter.author.id != self.target.id:
            return await inter.response.send_message(
                "woopm woopm este boton no es para ti", ephemeral=True
            )
        
        import random
        gif = random.choice(grabboobs_gifs)

        embed = disnake.Embed(
            title=f"{inter.author.display_name} agrra las boobies de {self.author}!",
            color=0xFFC0CB
        )
        embed.set_image(url=gif)

        await inter.response.send_message(embed=embed) 

# ----- Comando -----
@bot.slash_command(name="showboobs", description="muestra tus tetas a alguien")
async def showboobs(inter: disnake.ApplicationCommandInteraction, user: disnake.User):
    import random
    gif = random.choice(showboobs_gifs)

    embed = disnake.Embed(
        title=f"**{inter.author.display_name}** le muestra las tetas a **{user.display_name}** 💞",
        color=0xFFC0CB
    )
    embed.set_image(url=gif)

    view = ShowBoobsView(inter.author, user)

    await inter.response.send_message(embed=embed, view=view)


# comando suck
suckboobs_gifs = [
    "https://media.discordapp.net/attachments/827215645887954974/1292083487582584903/76tLLzm.gif?ex=69239645&is=692244c5&hm=3d6aa16c7c0a61d94211447ebf02d998eec0b5d361e4965702b4ad4c57c27b6f&=&width=625&height=824"
]
@bot.slash_command(name="suckboobs", description=" chupa las boobies de alguien :3")
async def suckboobs(  
      inter: disnake.ApplicationCommandInteraction,
      usuario: disnake.Member = commands.Param(
            description=" a quien le xhuparas las tetas?"
        )
):
    import random
    gif = random.choice(suckboobs_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} le chupa las boobies a {usuario.display_name} (>\\<)",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

# comando handjob
handjob_gifs = [
    "https://media.discordapp.net/attachments/1371018932084801586/1442307757716799600/Mai-Friend-porn-vn-hentai-Anime-VN-8684143.gif?ex=6924f546&is=6923a3c6&hm=f49e15536d5a53169c1e8d0df641f4e3d4eb5dc03a7e9d93d3e51f26066113c9&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307847734956174/Mai-Friend-porn-vn-hentai-Anime-VN-8684133.gif?ex=6924f55b&is=6923a3db&hm=d7f6b662d5e89bdab54a95510f9082bb20383478b33a6b4b16a4db98b003f119&=&width=1014&height=570"
]
@bot.slash_command(name="handjob", description="darle ayuda manual a alguien")
async def handjob(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a quien se lo haras?"
        )
):
    import random
    gif = random.choice(handjob_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} le da una ayuda manual a {usuario.display_name} (ㅅ •᷄ ₃•᷅ )",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

# comando boobjob
boobjob_gifs = [
    "https://media.discordapp.net/attachments/1371018932084801586/1442212336877441167/hentai-scaled.webp?ex=69249c68&is=69234ae8&hm=b3240fa5e813efb7ae13184dfdc72d96a6d1352d8a3c472c72c63f8b68873765&=&animated=true&width=750&height=421",
    "https://media.discordapp.net/attachments/1379373514758557706/1385520021979005049/GIF_20250620_032102_990.gif?ex=69240792&is=6922b612&hm=47339e472241a5f0c5d2087c0bb0c488807f7b25931b6846cf5d23745959a269&=&width=808&height=605",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308037502173265/Mai-Friend-porn-vn-hentai-Anime-VN-8684163.gif?ex=6924f588&is=6923a408&hm=6fccb8d2057800d77c663425fa1c2bd8832e1fafafd2e3598789236f333f2a92&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442307980472352870/bubble-de-house-de-marumarumaru-porn-vn-hentai-Censored-Hentai-8643746.gif?ex=6924f57b&is=6923a3fb&hm=492f7acc748b865a377c2161183f6d980316cdaeba7f1fa95426145d351f2778&=&width=1014&height=570"
]
@bot.slash_command(name="boobjob", description="ayuda con tus pechos")
async def boobjob(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a quien se lo haras?"
        )
):
    import random
    gif = random.choice(boobjob_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} ayuda a {usuario.display_name} con sus boobies(๑>؂•̀๑)",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)

# comando suck
blowjob_gifs = [
    "https://media.discordapp.net/attachments/1371018932084801586/1442307670743842908/bubble-de-house-de-marumarumaru-porn-vn-hentai-Censored-Hentai-8643743.gif?ex=6924f531&is=6923a3b1&hm=2e1cfaefba6af30e42450a2533794e6d2e1b8c30bdb388cae641c269e0009a50&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308008351891628/Mai-Friend-porn-vn-hentai-Anime-VN-8684152.gif?ex=6924f581&is=6923a401&hm=854825fd71664ead1291f190bdc5cef0075a96fd8aed400b01cbfeecb988a777&=&width=1014&height=570"
]
cum_gifs = ["https://media.discordapp.net/attachments/1379373514758557706/1385520292268343417/6e88cd9c77e0f839af8fc973369206c1.gif?ex=6924b093&is=69235f13&hm=7abe3114be7a29cd47386624526aa4de4410a54d0519cd040d0ad7b43ac8d14c&=&width=281&height=375"
]
class BlowJobView(disnake.ui.View):
    def __init__(self, author, target):
        super().__init__(timeout=None)
        self.author = author
        self.target = target

    @disnake.ui.button(label="Correrse 🌸", style=disnake.ButtonStyle.primary)
    async def suck_back(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):

        
        if inter.author.id != self.target.id:
            return await inter.response.send_message(
                "woopm woopm este boton no es para ti", ephemeral=True
            )
        
        import random
        gif = random.choice(cum_gifs)

        embed = disnake.Embed(
            title=f"{inter.author.display_name} se corre en la boca de {self.author}!",
            color=0xFFC0CB
        )
        embed.set_image(url=gif)

        await inter.response.send_message(embed=embed)



@bot.slash_command(name="suck", description="Se la xupas a alguien")
async def suck(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a quien se la xupas?"
        )
):
    import random
    gif = random.choice(blowjob_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} se la xupa a {usuario.display_name} (๑>؂•̀๑)",
        color=disnake.Color.from_rgb(255, 105, 180)  
    )
    embed.set_image(url=gif)

    view = BlowJobView(author=inter.author.display_name, target=usuario)

    await inter.response.send_message(embed=embed, view=view)

# comando kuni

kuni_gifs = [
    "https://media.discordapp.net/attachments/1371018932084801586/1442308172495851632/Mai-Friend-porn-vn-hentai-Anime-VN-8684173.gif?ex=6924f5a9&is=6923a429&hm=b4132c8eef6470660562a4c29863422c44ce82322f1d63a48b83b6e8357d0df1&=&width=1014&height=570",
    "https://media.discordapp.net/attachments/1371018932084801586/1442308240783441940/Mai-Friend-porn-vn-hentai-Anime-VN-8684135.gif?ex=6924f5b9&is=6923a439&hm=5452d414f6a9160777d51e7d2095d03a82dd1799767254e2eecf62e326d8ee48&=&width=1014&height=570"
]
@bot.slash_command(name="kuni", description="lame a alguien")
async def kuni(  
      inter: disnake.ApplicationCommandInteraction,
        usuario: disnake.Member = commands.Param(
            description=" a quien lames?"
        )
):
    import random
    gif = random.choice(kuni_gifs)

    embed = disnake.Embed(
        title=f"{inter.author.display_name} le da placer a  {usuario.display_name} con su lengua                     o( ˶^▾^˶ )o",
        color=disnake.Color.from_rgb(255, 105, 180)  # #FF69B4 (hot pink)
    )
    embed.set_image(url=gif)
    await inter.response.send_message(embed=embed)
    
# Ejecutar bot
bot.run("OTQ4MDQzNDg2ODk1MTY1NDUw.Gu7NJ0.sZ_B8y4Pnk9X6RikskV1GmlIivASV9KrGeZwM0")