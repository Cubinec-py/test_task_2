import telethon

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from bot_congig.connection import Connection as BotConnection


class JoinGroup(BotConnection):
    def __init__(self):
        super().__init__()

    async def join_group(
        self, channel: str | telethon.tl.types.InputChannel, private=False
    ):
        try:
            if not private:
                try:
                    await self.client(JoinChannelRequest(channel))
                except telethon.errors.rpcerrorlist.ChannelPrivateError:
                    print("Channel private or you were banned")
                    return False
            else:
                group_hash = channel.replace("+", "").split("/")[-1]
                await self.client(ImportChatInviteRequest(group_hash))
        except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
            print("Already joined group")
            return False
        return True
