import asyncio
import edge_tts

TEXT = "வணக்கம்! இது தமிழ் குரல் சோதனை."

VOICE = "ta-IN-PallaviNeural"

async def main():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save("output.mp3")

asyncio.run(main())

print("Voice created successfully!")