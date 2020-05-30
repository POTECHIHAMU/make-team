import discord
import asyncio
import datetime
import random
from time import sleep
import os


#discordクライアント起動
client = discord.Client()
#鯖トークン
TOKEN = "NzE1OTAxMjMxNjIwNTU0Nzc0.XtJPJg.EmSg7Ph_qWjZSy4wrXt8LR1vtm4"
print("initialize...")
login_who = "none"
#global宣言
#ログインイベント
@client.event
async def on_ready():
    print('Bot Launched')

    print('------')

#メッセージ反応イベント
@client.event


@client.event
async def on_raw_reaction_add(payload):
    '''
    payload.~~
     message_id
     user_id
     channel_id
     guild_id
     emoji
    '''
    print("Add role by reaction :",end="")
    channel = client.get_channel(payload.channel_id)

    rankCh_id = 716286300898197554

    rank_bronze_id  = "<:bronze_rank:716284646501122139>" 
    rank_silver_id  = "<:silver_rank:716284702549606440>"
    rank_gold_id    = "<:gold_rank:716284774947225670>"
    rank_platinum_id= "<:platinum_rank:716284843750850572>"
    rank_diamond_id = "<:diamond_rank:716288384619774004>"
    rank_master_id  = "<:master_rank:716284890882244681>"
    rank_predator_id= "<:Predator:714901686346448948>"
    
    role_bronze_id  = 714882526207934464
    role_silver_id  = 714882517483651142
    role_gold_id    = 714882513239277569
    role_platinum_id= 714881605629378602
    role_diamond_id = 714881602940960809
    role_master_id  = 714881594451820596
    role_predator_id= 714881587182960680

    if channel.id == rankCh_id:
        if str(payload.emoji)   == rank_bronze_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_bronze_id          # Role: B
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        elif str(payload.emoji) == rank_silver_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_silver_id          # Role: S
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        elif str(payload.emoji) == rank_gold_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_gold_id         # Role: g
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        elif str(payload.emoji) == rank_platinum_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_platinum_id      # Role: B
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        elif str(payload.emoji) == rank_diamond_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_diamond_id         # Role: B
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        elif str(payload.emoji) == rank_master_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_master_id         # Role: B
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        elif str(payload.emoji) == rank_predator_id:
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            member_id = role_predator_id          # Role: B
            role = guild.get_role(member_id)    #付与役職を指定
            await member.add_roles(role)        #役職を付与
        

client.run(TOKEN)
