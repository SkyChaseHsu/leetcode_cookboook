from jinja2 import Environment, FileSystemLoader
import os

def get_problems():
	problems = dict()
	with open("array.txt", "r") as f:
		for line in f.readlines():
			no, title = tuple(line.split("/"))
			problems[no] = title.strip()
	
	return problems

def get_finished(dirpath="./solutions"):
	finished = dict()
	for _, _dirs, _ in os.walk(dirpath):
		for _dir in _dirs:
			no, title = tuple(_dir.split("_"))
			finished[no.zfill(4)] = title
	
	return finished

def get_md():
	with open("array.md", "w", encoding="utf-8") as f:
		env = Environment(loader=FileSystemLoader("template"))
		md_template = env.get_template("array.md")
		context = md_template.render({"problems": get_problems(), "finished": get_finished()})
		f.write(context)

if __name__ == "__main__":
	get_md()