from transformers import pipeline

translator = pipeline('translation_ru_to_en', 'Helsinki-NLP/opus-mt-ru-en')

print(translator('Меня зовут Максим, и я студент УрФУ'))
