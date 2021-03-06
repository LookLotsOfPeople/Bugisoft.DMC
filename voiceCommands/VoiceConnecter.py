class VoiceConnector:
    voice = None

    @staticmethod
    async def join():
        from Leak import client, message
        VoiceConnector.voice = await client.join_voice_channel(message.author.voice_channel)
        from voiceCommands.MusicPlayer import MusicPlayer
        await MusicPlayer.init(VoiceConnector.voice)

    @staticmethod
    async def leave():
        if VoiceConnector.voice is not None:
            await VoiceConnector.voice.disconnect()
            VoiceConnector.voice = None
