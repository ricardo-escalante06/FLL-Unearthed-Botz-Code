from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3" , "4" , "5" , "6", "7","0")

# Based on the selection, run a program.
if selected == "1":
    import Mission_5_6_7_NEW
elif selected == "2":
    import Mission_9_10_new
elif selected == "3":
    import Mission_8
elif selected == "4":
    import mission11
elif selected == "5":
    import Mission_12
elif selected == "6":
    import Mission_1
elif selected == "7":
    import Mission_2
elif selected == "0":
    import test
