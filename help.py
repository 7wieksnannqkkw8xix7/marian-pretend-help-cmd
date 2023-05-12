    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @blacklist()
    async def help(self, ctx):
        embeds = []
        embeds.append(discord.Embed(color=self.bot.color, title="pretend",description=f"> **To see the commands use the button's below**").set_footer(text="2.20.1 pretend rewrite version").set_author(name="pretend", icon_url=self.bot.user.avatar.url).set_thumbnail(url=self.bot.user.display_avatar.url).add_field(name="** **", value="> ** If you wanna join in the support server click [here](https://discord.gg/whA2tm9yVb)**"))
        embeds.append(discord.Embed(color=self.bot.color, title="info commands",description=f"> ` ping | botinfo | help`").set_author(name="pretend", icon_url=self.bot.user.avatar.url).set_thumbnail(url=self.bot.user.display_avatar.url))
        embeds.append(discord.Embed(color=self.bot.color, title="utility commands",description=f"> ` channelinfo | roleinfo | donate | serverinfo | spotify | permissions | ascii | sicon | splash | sbanner | bio`").set_author(name="pretend", icon_url=self.bot.user.avatar.url).set_thumbnail(url=self.bot.user.display_avatar.url))
        embeds.append(discord.Embed(color=self.bot.color, title="config commands",description=f"> ` autopost`").set_author(name="pretend", icon_url=self.bot.user.avatar.url).set_thumbnail(url=self.bot.user.display_avatar.url))
        paginator = pg.Paginator(self.bot, embeds, ctx, invoker=ctx.author.id)
        paginator.add_button('prev', emoji=':left:  ')
        paginator.add_button('delete', emoji=':nosee:', style=discord.ButtonStyle.danger)
        paginator.add_button('next', emoji=':right:') 
        await paginator.start()

