import client.clientpy3 as cl


def run(*commands):
	print(commands)

	print(str(commands))
	print(type(commands))
	cl.run('comegetme','123waterloo',str(commands))