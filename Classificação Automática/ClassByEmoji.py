import emot

positive_emojis = set('😀 😁 😂 🤣 😃 😄 😅 😆 😉 😊 😋 😎 😍 😘 😗 😙 😚 ☺️ 🙂 🤗 🤩 :) :-) :D =)'.split())
negative_emojis = set('☹️ 🙁 😖 😞 😟 😤 😢 😭 😦 😧 😨 😩 🤯 😬 😰 😱 🤢 🤮 😈 👿 👹 👺 💩 😡 😠 🤬 :( :-('.split())
neutral_emojis = set('🤔 😐 😑 😶 😒 😓')

def classByEmoji(text):
	global positive_emojis
	global negative_emojis
	global neutral_emojis

	emojis = emot.emoji(text)
	emoticons = emot.emoticons(text)
	emots = set()
	for map_emoji in emojis:
		emots.add(map_emoji['value'])
	for map_emoji in emoticons:
		emots.add(map_emoji['value'])

	positive_inter = emots.intersection(positive_emojis)
	negative_inter = emots.intersection(negative_emojis)
	neutral_inter = emots.intersection(neutral_emojis)

	if positive_inter:
		if len(negative_inter) == 0 and len(neutral_inter) == 0:
			return 1
	elif negative_inter:
		if len(neutral_inter) == 0:
			return -1
	elif neutral_inter:
		return 0

	return ''

def main():
	print(classByEmoji('Oi, gente! :)'))
	print(classByEmoji('Oi, gente! :('))
	print(classByEmoji('Oi, gente! 😀'))
	print(classByEmoji('Oi, gente! 😐'))
	print(classByEmoji('Oi, gente! 🙁'))
	print(classByEmoji('Oi, gente! 😀😐'))
	print(classByEmoji('Oi, gente! 🙁😐'))
	print(classByEmoji('Oi, gente! 🙁😀'))

if __name__ == '__main__':
	main()