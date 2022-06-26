from redbot.core import commands
import discord

class AdventureZ(commands.Cog):
    """Extra adventure commands, like the good ol'Z commands and (not) grindsquad"""

    @commands.command(name="z")
    async def zCMD(self, ctx, *, msg):
        """Followed by a personality value it'll return it's multiplier"""
        if msg == "absolutely-brutal-looking":
            await ctx.send("Attack Resistance: 1.9\nPersuasion Resistance: 1.1")
        elif msg == "ancient":
            await ctx.send("Attack Resistance: 0.8\nPersuasion Resistance: 2")
        elif msg == "cunning":
            await ctx.send("Attack Resistance: 1.2\nPersuasion Resistance: 1.2")
        elif msg == "delirious":
            await ctx.send("Attack Resistance: 0.6\nPersuasion Resistance: 0.8")
        elif msg == "disgusting":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 0.7")
        elif msg == "dumb":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 0.8")
        elif msg == "enlightened":
            await ctx.send("Attack Resistance: 1.2\nPersuasion Resistance: 1.8")
        elif msg == "fairly-intelligent":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 1.2")
        elif msg == "fat":
            await ctx.send("Attack Resistance: 1.1\nPersuasion Resistance: 0.9")
        elif msg == "flustered":
            await ctx.send("Attack Resistance: 0.9\nPersuasion Resistance: 1.1")
        elif msg == "focused":
            await ctx.send("Attack Resistance: 1.2\nPersuasion Resistance: 1")
        elif msg == "gigantic":
            await ctx.send("Attack Resistance: 1.4\nPersuasion Resistance: 1")
        elif msg == "hideous":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 1")
        elif msg == "highly-scarred":
            await ctx.send("Attack Resistance: 1.4\nPersuasion Resistance: 1.1")
        elif msg == "humongous":
            await ctx.send("Attack Resistance: 2\nPersuasion Resistance: 0.8")
        elif msg == "immortal":
            await ctx.send("Attack Resistance: 100\nPersuasion Resistance: 1.1")
        elif msg == "lazy":
            await ctx.send("Attack Resistance: 0.4\nPersuasion Resistance: 0.9")
        elif msg == "minuscule":
            await ctx.send("Attack Resistance: 0.2\nPersuasion Resistance: 1.1")
        elif msg == "muscle-bound":
            await ctx.send("Attack Resistance: 1.2\nPersuasion Resistance: 0.7")
        elif msg == "old":
            await ctx.send("Attack Resistance: 0.8\nPersuasion Resistance: 1.5")
        elif msg == "ordinary":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 1")
        elif msg == "plagued":
            await ctx.send("Attack Resistance: 1.2\nPersuasion Resistance: 0.9")
        elif msg == "possessed":
            await ctx.send("Attack Resistance: 1.8\nPersuasion Resistance: 100")
        elif msg == "prodigious":
            await ctx.send("Attack Resistance: 1.6\nPersuasion Resistance: 0.8")
        elif msg == "sad-looking":
            await ctx.send("Attack Resistance: 0.9\nPersuasion Resistance: 0.8")
        elif msg == "savage":
            await ctx.send("Attack Resistance: 1.8\nPersuasion Resistance: 0.9")
        elif msg == "scheming":
            await ctx.send("Attack Resistance: 1.3\nPersuasion Resistance: 1")
        elif msg == "sick":
            await ctx.send("Attack Resistance: 0.3\nPersuasion Resistance: 0.9")
        elif msg == "small":
            await ctx.send("Attack Resistance: 0.8\nPersuasion Resistance: 1")
        elif msg == "staunch":
            await ctx.send("Attack Resistance: 1.15\nPersuasion Resistance: 1")
        elif msg == "stupid":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 0.5")
        elif msg == "terrifying":
            await ctx.send("Attack Resistance: 1\nPersuasion Resistance: 1.2")
        elif msg == "tiny":
            await ctx.send("Attack Resistance: 0.\nPersuasion Resistance: 1")
        elif msg == "weak":
            await ctx.send("Attack Resistance: 0.5\nPersuasion Resistance: 1")
        elif msg == "weary":
            await ctx.send("Attack Resistance: 0.6\nPersuasion Resistance: 0.9")
        else:
            await ctx.send("You just mentioned a non existent-personality\nFor personalities with spaces in them replace the spaces with a -")