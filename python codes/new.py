from graphviz import Digraph

# Create a flowchart using Graphviz
flowchart = Digraph("PastaCooking", format="png")
flowchart.attr(rankdir="TB", size="8,8")

# Define nodes
flowchart.node("Start", "Start")
flowchart.node("BoilWater", "Boil Water")
flowchart.node("CookPasta", "Cook Pasta")
flowchart.node("CheckPasta", "Is Pasta Done?")
flowchart.node("Repeat", "Cook More")
flowchart.node("Done", "Drain Pasta and Serve")
flowchart.node("End", "End")

# Add edges
flowchart.edge("Start", "BoilWater")
flowchart.edge("BoilWater", "CookPasta")
flowchart.edge("CookPasta", "CheckPasta")
flowchart.edge("CheckPasta", "Done", label="Yes")
flowchart.edge("CheckPasta", "Repeat", label="No")
flowchart.edge("Repeat", "CheckPasta")
flowchart.edge("Done", "End")

# Render the flowchart
file_path = "/mnt/data/Pasta_Cooking_Flowchart"
flowchart.render(file_path, view=False)

file_path + ".png"
