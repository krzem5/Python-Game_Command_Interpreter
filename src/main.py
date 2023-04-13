sayings={'xp amout':'Your Expirience Points:\t','coords':'%s:\tx=%s, y=%s, z=%s'}
errors={'short error':'Number must be smaller than 100001 and greater than -100001','integrer error':'%s must be integrer','no cmd':"Command %s don't exists",'len error':'Invalid lenght of %slist','invalid string':'String %sis invalid','bolean error':'%s is not true or false'}
help_={'xp':'/xp {add/delete} [amout]','help':'/help   OR   /help [cmd]','tp':'/tp [player] [x] [y] [z]','exit':'/exit','calculator':'/calculator','gamerule':'/gamerule [rule] [status]','effect':'/effect [effect] OR /effect [effect] [amplifier] [strenght]'}
commands=('xp','tp','help','exit','calculator','gamerule','effect')
gamerules={'chatOutput':True,'cheats':False,'characterLine':True}
#PLAYER INPUT(cmd)
#   |
#   |
#   +------ not starting-Y------ chat shows input string
#            with "/"
#                |
#+---------------N
#+/xp add/delete [short] adds or deletes expirience points @
#+/tp [player] [x] [y] [z] teleports the player to x,y,z @
#+/help OR /help [cmd] show help chat @
#+/exit exits program @
#+/calculator opens calculator @
#+/gamerule [rule] [status] changes gamerules
#+/effect [effect] OR /effect [effect] [amplifier] [strenght]
#+
#+
#+
#+

def interpret_command(cmd,user='krzem'):
	output='\n'
	global EXP
	global coords

	if cmd[1:3]=='xp':
		if cmd[4:7]=='add':
			exp_=cmd[8:]
			if exp_.isnumeric():
				if 100001>int(exp_)>-100001:
					EXP+=int(exp_)
					if EXP<0:
						EXP=0
					output+=sayings['xp amout']+str(EXP)

				else:
					output+=errors['short error']+'\n'
					output+='Usage:\t'+help_['xp']
			else:
			   output+=errors['integrer error']%('Number')+'\n'
			   output+='Usage:\t'+help_['xp']
		elif cmd[4:10]=='delete':
			exp_=cmd[11:]
			if exp_.isnumeric():
				exp_='-'+exp_
				if 100001>int(exp_)>-100001:
					EXP+=int(exp_)
					if EXP<0:
						EXP=0
					output+=sayings['xp amout']+str(EXP)
				else:
					output+=errors['short error']+'\n'
					output+='Usage:\t'+help_['xp']
			else:
			   output+=errors['integrer error']%('Number')+'\n'
			   output+='Usage:\t'+help_['xp']
		else:
			output+=errors['invalid string']%('')+'\n'
			output+='Usage:\t'+help_['xp']
	elif cmd[1:3]=='tp':
		list_tp=cmd[4:].split(' ')
		cnt=1
		exit_=False
		if len(list_tp)==4:
			for coord in list_tp:
				if not cnt==1:
					if not coord.isnumeric():
						output+=errors['integrer error']%('Coord')+'\n'
						output+='Usage:\t',+help_['tp']
						exit_=True
						break
				cnt+=1

			if not exit_:
				coords[list_tp[0]]['x']=list_tp[1]
				coords[list_tp[0]]['y']=list_tp[2]
				coords[list_tp[0]]['z']=list_tp[3]
				output+=sayings['coords']%('krzem',coords['krzem']['x'],coords['krzem']['y'],coords['krzem']['z'])

		else:
			output+=errors['len error']%("coordinater's ")+'\n'
			output+='Usage:\t'+help_['tp']

	elif cmd[1:5]=='help':
		if cmd[5]==' 'and cmd[6:].isalpha():
			if cmd[6:] in commands:
				output+='Usage:\t'+help_[cmd[6:]]
			else:
				output+=errors['no cmd']%(cmd[6:])
		else:
			output+='Commands:'
			for cmd_ in help_.keys():
				output+='\n'+help_[cmd_]
	elif cmd[1:5]=='exit':
		exit()

	elif cmd[1:]=='calculator':
		import calculator

	elif cmd[1:9]=='gamerule':
		if cmd[10:20]=='chatOutput':
			if cmd[21:]=='false':
				gamerules['chatOutput']=False
			elif cmd[21:]=='true':
				gamerules['chatOutput']=True
			else:
				output+=errors['bolean error']%(cmd[21:])+'\n'
				output+='Usage:\t'+help_['gamerule']
		if cmd[10:16]=='cheats':
			if cmd[17:]=='false':
				gamerules['cheats']=False
			elif cmd[17:]=='true':
				gamerules['cheats']=True
			else:
				output+=errors['bolean error']%(cmd[21:])+'\n'
				output+='Usage:\t'+help_['gamerule']
		if cmd[10:23]=='characterLine':
			if cmd[24:]=='false':
				gamerules['ccharacterLine']=False
			elif cmd[24:]=='true':
				gamerules['characterLine']=True
			else:
				output+=errors['bolean error']%(cmd[21:])+'\n'
				output+='Usage:\t'+help_['gamerule']
	elif cmd[1:7]=='effect':
		if cmd[8:16]=='strenght':
			output+='strenght'
			if cmd[16]==' ':
				if cmd[17:20].isnumeric():
					output+=' '+int(cmd[17:20])
				else:
					output+=errors['intiger error']%('Number')+'\n'
					output+='Usage:\t'+help_['effect']
			else:
				output+=errors['intiger error']%('Number')+'\n'
				output+='Usage:\t'+help_['effect']
	else:
		output+='<%s> '%(user)
		output+=cmd[0:]
	return output

coords={'krzem':{'x':1,'y':1,'z':1}}
EXP=100
for gamerule in gamerules.keys():
	print(gamerule)
while True:
	print(interpret_command(input('>>>')))
	print()

