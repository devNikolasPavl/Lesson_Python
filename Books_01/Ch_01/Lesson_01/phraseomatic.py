# сообщаем Python о том, что собираемся использовать функции модуля random
import random

# создаем 3 списка: глаголы, прилагательные и существительные
verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced',
'24/7', 'Lean in', '30 000 foot']

adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siload', 'B-to-B',
'Oriented', 'Cloud-based', 'API-based']

nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page',
'Productivity', 'Process', 'Tipping Point', 'Paradigm']

# выбирыем по одному глаголу, прилагательному и существительному из каждого 
# списка
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# состовляем фразу, "суммируя" все 3 слова
phrase = verb + ' ' + adjective + ' ' + noun

# выводим готовуб фразу
print(phrase)
