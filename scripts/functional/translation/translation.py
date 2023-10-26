from gtts import gTTS
from googletrans import Translator

# возвращает перевод текста
def get_translate_text(id:int, text:str, lang='ru'):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    _create_audio(id, translation.text)
    return translation.text

# генерируем и сохраняет аудио
def _create_audio(id:int, text:str, lang='ru'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(f"scripts/functional/translation/audio_temp/{id}-output.mp3")