default:
	@cat makefile

tokenizer_setup:
	python3 -m venv env && . ./env/bin/activate && ./env/bin/pip install --upgrade pip && ./env/bin/pip install -r requirements.txt

get_texts:
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	wget https://www.gutenberg.org/cache/epub/1063/pg1063.txt
	wget https://www.gutenberg.org/cache/epub/932/pg932.txt
	wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt
	wget https://www.gutenberg.org/cache/epub/21964/pg21964.txt
	wget https://www.gutenberg.org/cache/epub/15143/pg15143.txt
	wget https://www.gutenberg.org/cache/epub/8893/pg8893.txt
	wget https://www.gutenberg.org/cache/epub/30092/pg30092.txt
	wget https://www.gutenberg.org/cache/epub/50852/pg50852.txt
	wget https://www.gutenberg.org/cache/epub/32037/pg32037.txt
	wget https://www.gutenberg.org/cache/epub/10031/pg10031.txt
	wget https://www.gutenberg.org/cache/epub/14082/pg14082.txt

raven_line_count:
	cat pg17192.txt | wc -l

raven_word_count:
	cat pg17192.txt | wc -w

raven_counts:
	 (cat pg17192.txt | grep raven | wc -l); (cat pg17192.txt | grep Raven | wc -l); (cat pg17192.txt | grep -i raven | wc -l);

total_lines:
	wc -l *.txt

total_words:
	wc -w *.txt

test:
	. env/bin/activate; pytest -m "not integration"
