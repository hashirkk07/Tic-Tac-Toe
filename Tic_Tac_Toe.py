def rotate90left(board): # function to rotate the board by 90 degree left, so that rows becomes columns and vice-versa.
	tranBoard=[ ['-','-','-'],
				['-','-','-'],
				['-','-','-']]
	for i in range(0,3):
		for j in range(0,3):
			tranBoard[i][j]=board[j][2-i]
	return tranBoard

def show_board_state(board): # function to print the board
	for i in range(0,3):
		for j in range(0,3):
			print(board[i][j], end=' ')
		print()
	print()

def state_game(board): # function to check the winner / game over / game continues

	#checking for winner in horizontal rows
	for row in board: # checking for winner - row wise (no return action if all element in the row are empty ie '-')
		win=set(row) # making the row into a set to intake the unique elements
		if (len(win) == 1): # unary set if and only if all the row elements are equal (all the row elements are equal)
			win=win.pop() # getting that element that caused the win
			if win=='X': # if it X, return  human player has won ie. X won
				return 'Xwon'
			if win=='O': # if it O, return  human player has won ie. X won
				return 'Owon'

	tranBoard=rotate90left(board) # rotated matrix having rows as columns of board and principle diagonal as secondary diagonal of board

	#checking for winner in vertical columns of board
	#rows in tranBoard are columns of board
	for row in tranBoard: # checking for winner - row wise (no return action if all element in the row are empty ie '-')
		win=set(row) # making the row into a set to intake the unique elements
		if (len(win) == 1): # unary set if and only if all the row elements are equal (all the row elements are equal)
			win=win.pop() #getting that element that caused the win
			if win=='X': # if it X, return  human player has won ie. X won
				return 'Xwon'
			if win=='O': # if it O, return  human player has won ie. X won
				return 'Owon'

	diag=set() # set to store the principle diagonal elements of board
	revdiag=set() # set to store the secondary diagonal elements of board
	for i in range(0,3):
		for j in range(0,3):
			if(i==j):
				diag.add(board[i][j]) # adding principle diagonal elements of board to set diag
				revdiag.add(tranBoard[i][j]) # adding principle diagonal elements of rotated board (ie. sec diag elements of board) 

	#checking for winner in principle diagonal
	if (len(diag) == 1): # unary set if and only if all the diagonal elements are equal
		win=diag.pop()
		if win=='X': # if it X, return  human player has won ie. X won
			return 'Xwon'
		if win=='O':  # if it O, return  human player has won ie. X won
			return 'Owon'

	#checking for winner in secondary diagonal
	if (len(revdiag) == 1): # unary set if and only if all the diagonal elements are equal
		win=revdiag.pop()
		if win=='X': # if it X, return  human player has won ie. X won
			return 'Xwon'
		if win=='O': # if it O, return  human player has won ie. X won
			return 'Owon'
	for i in range(0,3): # checking if any space left to play
		for j in range(0,3):
			if board[i][j]=='-': # if found any space as empty, return saying the game continues
				return('continue')

	return("tie") # tie if no wins and no space left to play
utility_value={"player":-1,"tie":0,"ai":1}
def minimax_algo(board,agent_turn): # function implementing minimax algorithm

	state=state_game(board) # checking the current state of the game. Any winner/ tie /continues?
	if state=='Xwon':
		return utility_value["player"] # if at the end human player wins, return its utility value, ie. -1
	if state=='Owon':
		return utility_value["ai"] # if at the end AI Agent wins, return its utility value, ie. 1
	if state=='tie':
		return utility_value["tie"] # if at the end it's a tie, return its utility value, ie. 0
	if state=='continue': # if game is not over,continue
		if(agent_turn): #maximizing agent part
			bestScore=utility_value["player"]-1 # since AI tries to maximise its score, the best score is initialised with a minimum possible(ie. less than the values any player can get)
			for i in range(0,3):
				for j in range(0,3):
					if board[i][j]=='-': # checking if any not taken positions
						board[i][j]='O'#  AI agent playing a random move
						aiScore=minimax_algo(board,False) # checking the score it can get out of that move by applying minimax algorithm
						bestScore=max(bestScore,aiScore) # choosing the maximum score as it needs to maximise it's score
						board[i][j]='-' # changing that random position taken back to untaken
			return bestScore
		else: #minimizing agent part
			bestScore=utility_value["ai"]+1 # since AI tries to minimise opponent's score, the best score is initialised with a maximum possible(ie. greater than the values any player can get)
			for i in range(0,3):
				for j in range(0,3):
					if board[i][j]=='-': # checking if any not taken positions
						board[i][j]='X' # AI agent guessing the human player playing a random move
						aiScore=minimax_algo(board,True) # checking the score it can get out of that move by applying minimax algorithm
						bestScore=min(bestScore,aiScore) # choosing the minimum score as it needs to minimise human player's score
						board[i][j]='-' # changing that random position taken back to untaken
			return bestScore

def next_move_AI(board): # function that return the coordinates of AI agent's next move
	bestScore=utility_value["player"]-1 # since AI tries to maximise its score, the best score is initialised with a minimum possible(ie. less than the values any player can get)
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j]=='-': # checking if any not taken positions
				board[i][j]='O' # AI agent playing a random move
				aiScore=minimax_algo(board,False) # checking the score it can get out of that move by applying minimax algorithm
				if(aiScore>bestScore): # if the score is the best(ie. maximum) store it and store those coordinates
					bestScore=aiScore
					x=i
					y=j
				board[i][j]='-' # changing that random position taken back to untaken
	return x,y # return the best move coordinates

def tic_tac_toe_game(board):
	while True: # repeating till the game ends in a player winning or a tie
		# HUMAN PLAYER"S MOVE
		x,y=input("Enter space-separated row and column location for a human player\n").split() # taking coordinates from human player
		x=int(x)
		y=int(y)	
		while (x not in range(0,3)) or (y not in range(0,3) or (board[x][y]!='-')): # if the input is out of the board/ already taken , asking to input again
			x,y=input("Invalid input\nEnter space-separated row and column location for a human player\n").split()
			x=int(x)
			y=int(y)
		
		board[x][y]='X' # making that move on the board
		print("\nAfter the human player move -")
		print("Current State of the board")
		show_board_state(board) # printing the current board
		result=state_game(board) # checking current state of the board for any win/tie/continue . If any win/tie stop the loop and print result
		if result=='Xwon':
			print("You won!")
			return
		if result=='Owon':
			print("AI won!")
			return
		if result=="tie":
			print("Tie !")
			return
		# AI AGENT'S MOVE
		x,y=next_move_AI(board) # getting coordinates of AI agent's best move after doing minimax algorithm
		board[x][y]='O' # making that move on the board
		print("After the AI agent move -")
		print("Current State of the board")
		show_board_state(board) #printing the current board
		result=state_game(board) # checking current state of the board for any win/tie/continue . If any win/tie stop the loop and print result
		if result=='Xwon':
			print("You won!")
			return
		if result=='Owon':
			print("AI won!")
			return
		if result=="tie":
			print("Tie !")
			return

board=[ ['-','-','-'], # initialising the board with empty spaces '-'
		['-','-','-'],
		['-','-','-']]
print("The initial state of the board")
show_board_state(board) # printing the initial empty board
tic_tac_toe_game(board) # start the tic tac toe game
