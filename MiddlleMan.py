def getImage():
    print("Image")
    return [0,"image"]
def getPieces():
    print("Pieces")
    return [1,"Pieces"]
def getPiece():
    print("Piece")
    return [2,"Piece"]
def getArm():
    print("Arm")
    return [3,"Arm"]
def getBoard():
    print("Board")
    return [4,"Board"]
#this is a function map, takes a key value which is the command and calls the required function
function_map = {"image": getImage(), "board":getBoard(), "arm": getArm(), "piece": getPiece(),
        "pieces": getPieces()
        }
def getCommand(command = ""):
    result = "Hi"#function_map[command]()
    return result
