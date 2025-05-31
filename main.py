
import discord, random, os

CHARACTERS = {
    "🌈 Mythic": ["Sorcerer (Gojo)", "KJ", "Crab Boss"],
    "🟣 Legendary": ["The Strongest Hero (Saitama)", "Wild Psychic", "Blade Master"],
    "🔵 Epic": ["Brutal Demon", "Hero Hunter", "Destructive Cyborg"],
    "🟢 Rare": ["Deadly Ninja", "Psychic User", "Street Fighter"],
    "⚪️ Common": ["Fighter A", "Fighter B", "Fighter C", "Fighter D"]
}
RARITY_POOL = [
    ("🌈 Mythic", 0.5), ("🟣 Legendary", 3),
    ("🔵 Epic", 10), ("🟢 Rare", 20), ("⚪️ Common", 66.5)
]
intents = discord.Intents.default()
client = discord.Client(intents=intents)

def spin_character():
    roll = random.uniform(0, 100)
    cumulative = 0
    for rarity, chance in RARITY_POOL:
        cumulative += chance
        if roll <= cumulative:
            character = random.choice(CHARACTERS[rarity])
            return f"🎰 You spun... {rarity}!\n✨ **{character}** is yours!"
    character = random.choice(CHARACTERS["⚪️ Common"])
    return f"🎰 You spun... ⚪️ Common!\n✨ **{character}** is yours!"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower().startswith("!spin"):
        await message.channel.send(spin_character())

client.run(os.getenv("DISCORD_TOKEN"))
