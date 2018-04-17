def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

answer = shut_down("yes")
print(answer)

answer = shut_down("no")
print(answer)

answer = shut_down("maybe")
print(answer)