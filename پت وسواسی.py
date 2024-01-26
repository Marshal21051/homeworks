st = input()

last = 0
while True:
    last = st.find('@', last + 1)
    i = st.find('#', last)
    if last == -1 or i == - 1:
        break
    if i + 1 == len(st):
        st = st[: i]
    elif i == 0:
        st = st[i + 1:]
    else:
        st = st[:i] + st[i + 1:]

st = " ".join(st.split())
st = st.replace("\\n", "\n")

print("Formatted Text:", st)
