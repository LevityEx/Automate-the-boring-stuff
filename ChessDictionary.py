def isValidChessBoard(board):
    # get list of all board item
    kings = 0
    pawns = 0
    vnum = '12345678'
    vchar = 'abcdefghijklmnopqrstuvwxyz'
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    # for each item
    for k, v in board.items():

        # check that key len < 2
        if(len(k) > 2):
            return False

        # check that key[0] is a number between 1 - 8
        # check that key[1] is a letter between 1 - h
        if(k[0] not in vnum or k[1] not in vchar):
            return False
        
        # check that value[0] is b or w 
        # add count for each w and b
        if(v[0] not in 'wb'):
            return False

        # check that value[1:strlen] is a correct piece
        if(v[1:len(v)] not in pieces):
            return False
        
        # count number of king and pawns there are
        if('king' in v[1:len(v)]):
            kings += 1
        if('pawn' in v[1:len(v)]):
            pawns += 1
    
    #check correct amount of kings and pawns
    if(kings != 2 or pawns > 8):
        return False

    #valid board
    return True

correctBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

if(isValidChessBoard(correctBoard)):
    print('this is valid board')
else:
    print('not a valid board')