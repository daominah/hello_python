def addAsterisk(s):
    lines = s.split('\n')
    newLines = []
    for line in lines:
        # print([line])
        line = line.replace('\t', '    ')
        newLine = " * " + line
        newLines.append(newLine)
    newS = '\n'.join(newLines)
    print(newS)


if __name__ == '__main__':
    addAsterisk("""{
    "error": "Error when call HTTP API: rpc error: code = 400 desc = PHONE_NUMBER_INVALID",
    "result": {
        "constructor": 0,
        "data2": null
    }
}""")
    print(0x3e0bdd8c)
