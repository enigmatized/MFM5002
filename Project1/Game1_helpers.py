from anytree import Node, RenderTree


def show_tree_game1():
    # Create the nodes for the game
    root = Node("Start")
    flip1_tails = Node("Play Game1", parent=root)
    flip1_heads = Node("Flip Again", parent=root)
    flip2_tails = Node("Play Game1", parent=flip1_heads)
    flip2_heads = Node("Lose $100", parent=flip1_heads)

    # Render the tree structure
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")